import re

def restore_blank_lines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Ensure a blank line before each new question
    fixed_content = re.sub(r'(\nCorrect Answer: [A-D])\n(Q\d+\.)', r'\1\n\n\2', content)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

    print(f"Fixed file saved as: {output_file}")

restore_blank_lines("mcq.txt", "fixed_mcqs.txt")
