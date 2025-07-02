# Python Code Evaluator

A tool for evaluating Python code submissions using Google's Gemini AI API. This application helps judges assess multiple Python solutions for coding competitions, providing structured feedback and rankings.

## Features

- Load problem descriptions from text/markdown files
- Import multiple Python solution files from a directory or zip file
- Optional solution code template support
- AI-powered evaluation using Google's Gemini API
- Markdown-formatted output with syntax highlighting
- Copy results to clipboard or save as markdown
- Light and dark theme support
- Configurable API key management

## Installation

1. Clone this repository
2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Get a Google Gemini API key from https://makersuite.google.com/app/apikey
4. Copy `.env.example` to `.env` and add your API key (optional)
5. Run the application:
   ```
   python judge2.py
   ```

## Usage

1. Enter your Gemini API key in the settings
2. Load a problem description (or use the sample)
3. Load team solutions (or use the sample)
4. Optionally load a solution code template
5. Click "Evaluate Solutions" to start the evaluation
6. View, copy, or save the generated report

## Sample Data

The `sample_data` directory contains example problems and solutions to help you get started:

- `minion_game.txt` - A sample problem description
- `team1_brutal_loops.py` - A solution using a brute force approach
- `team2_optimized.py` - An optimized solution to the same problem
- `solution_template.py` - A template file for the expected solution structure

## Dependencies

- google.generativeai
- customtkinter
- CTkMessagebox
- tkinter

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Google's Gemini API for AI-powered code evaluation
- CustomTkinter for the modern UI components
