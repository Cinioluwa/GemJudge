# GemJudge – Python Code Evaluator

GemJudge is a desktop application that evaluates Python code submissions using Google's Gemini AI API. Designed for hackathons, coding competitions, and automated assessment systems, it provides structured feedback, performance insights, and rankings across multiple solutions.

---

## One-Click Download (No Setup Required)

If you simply want to use the application without installing Python or any dependencies:

**[Download the latest installer (.exe) from the Releases page](https://github.com/Cinioluwa/GemJudge/releases/latest)**

-   Windows-only
-   No setup required beyond installing the `.exe`
-   Make sure you have a valid Gemini API key and an an internet connection

For developers who wish to run or modify the application from source, continue reading below.

---

## Features

-   AI-powered evaluation using Google's Gemini API
-   Load problem descriptions from text or markdown files
-   Import multiple Python solution files from a directory or zip file
-   Optional solution code template support
-   Markdown-formatted output with syntax highlighting
-   Copy results to clipboard or save to a markdown file
-   Light and dark mode theme support
-   Configurable API key management
-   Streaming evaluation output and real-time feedback

---

## Developer Setup (Run from Source)

### Prerequisites

-   Python 3.8 or higher
-   A Google Gemini API key (available at [makersuite.google.com](https://makersuite.google.com/app/apikey))

### Installation

1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/GemJudge.git](https://github.com/your-username/GemJudge.git)
    cd GemJudge
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3.  (Optional) Set up environment variables:
    -   Copy `.env.example` to `.env`
    -   Add your Gemini API key to the `.env` file

4.  Run the application:
    ```bash
    python judge2.py
    ```

---

### Usage Guide

1.  Launch the app and enter your Gemini API key in the settings panel.
2.  Load a problem description from a text or markdown file.
3.  Load one or more Python solution files using the file dialog or drag-and-drop.
4.  Optionally load a code template for structured comparison.
5.  Click "Evaluate Solutions" to start the evaluation.
6.  View the generated markdown report in-app, copy it, or save it to a disk.

---

### Sample Data

The `sample_data` directory contains sample problems and solutions to get you started:

-   `minion_game.txt` – A sample problem description
-   `team1_brutal_loops.py` – A brute-force implementation
-   `team2_optimized.py` – A more efficient version
-   `solution_template.py` – Optional code structure guide for evaluation

---

### Packaging

This application can be compiled into a standalone `.exe` using `pyinstaller`. The provided release uses:

```bash
pyinstaller --noconfirm --onefile --windowed judge2.spec
```

You can modify the `.spec` file or icon as needed for your own builds.

### Dependencies

-   `google.generativeai`
-   `customtkinter`
-   `CTkMessagebox`
-   `tkinter`
-   `markdown`
-   `dotenv`
-   `os`, `json`, `threading`, `time` (standard library)

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

### Acknowledgments

-   Google for the Gemini API
-   The CustomTkinter team for modern GUI components
