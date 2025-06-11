# Python Code Evaluator
# A tool for evaluating Python code submissions using Google's Gemini AI API

import google.generativeai as genai
import sys
import re
import os
import json
import threading
import zipfile
import tempfile
import shutil
import customtkinter as ctk
from tkinter import filedialog # Standard tkinter for file dialogs
from CTkMessagebox import CTkMessagebox
from datetime import datetime

# Try to import dotenv for API key management
try:
    from dotenv import load_dotenv
    load_dotenv()  # Load API key from .env file if available
except ImportError:
    pass  # dotenv is optional

class PythonEvaluatorApp:
    CONFIG_FILE = "config.json"
    THEMES = {
        "dark": {
            "text": "#DCE4EE",
            "background": "#2B2B2B", # Main background for text areas
            "frame_bg": "#242424",   # Background for frames
            "accent": "#3A7EBF",
            "highlight": "#4CAF50",
            "error": "#F44336",
            "warning": "#FF9800",
            "code_bg": "#1E1E1E",   # Specific background for code blocks
            "code_text": "#DCE4EE",
            "border": "#333333",
        },
        "light": {
            "text": "#1E1E1E",
            "background": "#FFFFFF", # Main background for text areas
            "frame_bg": "#EFEFEF",   # Background for frames
            "accent": "#3A7EBF",
            "highlight": "#4CAF50",
            "error": "#F44336",
            "warning": "#FF9800",
            "code_bg": "#F5F5F5",   # Specific background for code blocks
            "code_text": "#1E1E1E",
            "border": "#CCCCCC",
        }
    }
    
    def __init__(self):
        """Initialize the application"""
        self.root = ctk.CTk()  # Use CTk for the root window
        self.root.title("Python Code Evaluator")
        self.root.geometry("800x600")
        self.root.resizable(True, True)
        
        # Set default theme
        self.set_theme("dark")
        
        # Load configuration
        self.load_config()
        
        # Initialize UI components
        self.init_ui()
        
        # Center the window on the screen
        self.center_window()
        
        # Bind events
        self.bind_events()
        
        # Start the main loop
        self.root.mainloop()
    
    def set_theme(self, theme_name):
        """Set the application theme"""
        theme = self.THEMES.get(theme_name, self.THEMES["dark"])
        ctk.set_appearance_mode(theme_name)  # "System" / "Dark" / "Light"
        ctk.set_default_color_theme("blue")  # "blue" / "green" / "dark-blue"
        
        # Update colors for all widgets
        for widget in self.root.winfo_children():
            self.apply_theme_to_widget(widget, theme)
    
    def apply_theme_to_widget(self, widget, theme):
        """Recursively apply theme colors to a widget and its children"""
        try:
            widget.configure(fg_color=theme["background"], text_color=theme["text"])
        except Exception as e:
            print(f"Error applying theme to widget {widget}: {e}")
        
        for child in widget.winfo_children():
            self.apply_theme_to_widget(child, theme)
    
    def load_config(self):
        """Load configuration from the config file"""
        if not os.path.exists(self.CONFIG_FILE):
            self.save_config()  # Create a new config file if it doesn't exist
        
        with open(self.CONFIG_FILE, "r") as f:
            config = json.load(f)
            self.theme = config.get("theme", "dark")
            # Load other configuration settings as needed
    
    def save_config(self):
        """Save configuration to the config file"""
        config = {
            "theme": self.theme,
            # Add other configuration settings as needed
        }
        
        with open(self.CONFIG_FILE, "w") as f:
            json.dump(config, f, indent=4)
    
    def init_ui(self):
        """Initialize the user interface components"""
        # Create and pack your UI components here
        self.text_area = ctk.CTkTextbox(self.root, wrap="word")
        self.text_area.pack(expand=True, fill="both")
        
        self.run_button = ctk.CTkButton(self.root, text="Run", command=self.run_code)
        self.run_button.pack(side="bottom")
        
        # Add menu bar
        self.menu_bar = ctk.CTkMenu(self.root)
        self.root.config(menu=self.menu_bar)
        
        # Add "File" menu
        self.file_menu = ctk.CTkMenu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Add "Edit" menu
        self.edit_menu = ctk.CTkMenu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Cut", command=self.cut)
        self.edit_menu.add_command(label="Copy", command=self.copy)
        self.edit_menu.add_command(label="Paste", command=self.paste)
        
        # Add "Theme" menu
        self.theme_menu = ctk.CTkMenu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Theme", menu=self.theme_menu)
        self.theme_menu.add_radiobutton(label="Dark", command=lambda: self.set_theme("dark"))
        self.theme_menu.add_radiobutton(label="Light", command=lambda: self.set_theme("light"))
        
        # Add status bar
        self.status_bar = ctk.CTkLabel(self.root, text="Welcome to Python Code Evaluator!", anchor="w")
        self.status_bar.pack(side="bottom", fill="x")
        
        # Add a frame for the code area
        self.code_frame = ctk.CTkFrame(self.root)
        self.code_frame.pack(expand=True, fill="both")
        
        # Add a scrollbar to the code area
        self.code_scrollbar = ctk.CTkScrollbar(self.code_frame, orientation="vertical", command=self.text_area.yview)
        self.code_scrollbar.pack(side="right", fill="y")
        
        # Configure the text area to use the scrollbar
        self.text_area.configure(yscrollcommand=self.code_scrollbar.set)
        
        # Add a menu for selecting language (Python, Java, etc.)
        self.language_menu = ctk.CTkOptionMenu(self.root, values=["Python", "Java", "JavaScript"], command=self.change_language)
        self.language_menu.pack(side="top", fill="x")
        
        # Add a button for submitting code
        self.submit_button = ctk.CTkButton(self.root, text="Submit Code", command=self.submit_code)
        self.submit_button.pack(side="top")
    
    def center_window(self):
        """Center the window on the screen"""
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = int((self.root.winfo_screenwidth() - width) / 2)
        y = int((self.root.winfo_screenheight() - height) / 2)
        self.root.geometry(f"{width}x{height}+{x}+{y}")
    
    def bind_events(self):
        """Bind events to handlers"""
        self.root.bind("<Control-n>", self.new_file)
        self.root.bind("<Control-o>", self.open_file)
        self.root.bind("<Control-s>", self.save_file)
        self.root.bind("<Control-q>", self.root.quit)
        self.root.bind("<Control-z>", self.undo)
        self.root.bind("<Control-y>", self.redo)
        self.root.bind("<Control-x>", self.cut)
        self.root.bind("<Control-c>", self.copy)
        self.root.bind("<Control-v>", self.paste)
        
        # Add other event bindings as needed
    
    def new_file(self, event=None):
        """Create a new file"""
        self.text_area.delete(1.0, "end")
        self.root.title("Untitled - Python Code Evaluator")
        self.status_bar.configure(text="New file created")
    
    def open_file(self, event=None):
        """Open a file"""
        file_path = filedialog.askopenfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as f:
                code = f.read()
                self.text_area.delete(1.0, "end")
                self.text_area.insert("end", code)
                self.root.title(f"{os.path.basename(file_path)} - Python Code Evaluator")
                self.status_bar.configure(text=f"Opened file: {file_path}")
    
    def save_file(self, event=None):
        """Save the current file"""
        file_path = filedialog.asksaveasfilename(defaultextension=".py", filetypes=[("Python Files", "*.py"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "w") as f:
                code = self.text_area.get(1.0, "end")
                f.write(code)
                self.root.title(f"{os.path.basename(file_path)} - Python Code Evaluator")
                self.status_bar.configure(text=f"Saved file: {file_path}")
    
    def run_code(self):
        """Run the Python code in the text area"""
        code = self.text_area.get(1.0, "end")
        try:
            # Use Google's Gemini AI API to evaluate the code
            response = genai.run_code(code=code, language="python")
            output = response.get("output", "")
            error = response.get("error", "")
            
            if output:
                self.show_output(output)
            if error:
                self.show_error(error)
        except Exception as e:
            self.show_error(str(e))
    
    def show_output(self, output):
        """Show the output of the code execution"""
        self.status_bar.configure(text=f"Output: {output}")
        CTkMessagebox.show_info("Output", output)
    
    def show_error(self, error):
        """Show the error message"""
        self.status_bar.configure(text=f"Error: {error}", text_color="red")
        CTkMessagebox.show_error("Error", error)
    
    def change_language(self, language):
        """Change the programming language"""
        # Update the language for code evaluation
        self.language = language.lower()
        self.status_bar.configure(text=f"Language set to: {language}")
    
    def undo(self, event=None):
        """Undo the last action"""
        try:
            self.text_area.edit_undo()
        except Exception as e:
            print(f"Undo error: {e}")
    
    def redo(self, event=None):
        """Redo the last undone action"""
        try:
            self.text_area.edit_redo()
        except Exception as e:
            print(f"Redo error: {e}")
    
    def cut(self, event=None):
        """Cut the selected text"""
        try:
            self.text_area.event_generate("<<Cut>>")
        except Exception as e:
            print(f"Cut error: {e}")
    
    def copy(self, event=None):
        """Copy the selected text"""
        try:
            self.text_area.event_generate("<<Copy>>")
        except Exception as e:
            print(f"Copy error: {e}")
    
    def paste(self, event=None):
        """Paste text from clipboard"""
        try:
            self.text_area.event_generate("<<Paste>>")
        except Exception as e:
            print(f"Paste error: {e}")


# Function to get the version
def get_version():
    return "1.0.0"

def main():
    """Entry point for the application"""
    # Check for environment variable API key
    if os.environ.get("GEMINI_API_KEY"):
        print("Found Gemini API key in environment variables")
    
    # Print version info
    print(f"Python Code Evaluator v{get_version()}")
    print("Starting application...")
    
    app = PythonEvaluatorApp()
    app.root.mainloop()


if __name__ == "__main__":
    main()
