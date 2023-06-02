import PyPDF2

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def read_pdf_file(file_path):
    text = ''
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def find_answer(question, content):
    answers = []
    content = content.lower()
    question = question.lower()
    index = 0
    while index < len(content):
        index = content.find(question, index)
        if index == -1:
            break
        start_index = content.rfind("\n", 0, index) + 1
        end_index = content.find("\n", index)
        answer = content[start_index:end_index].strip()
        answers.append(answer)
        index += len(question)
    return answers

# Prompt the user to select a file
file_choice = input("Select a file (1 for text file, 2 for PDF file): ")

if file_choice == "1":
    text_file_path = input("Enter the path of the text file: ")
    try:
        text_content = read_text_file(text_file_path)
        pdf_content = ""
    except FileNotFoundError:
        print("Text file not found. Exiting.")
        exit()
elif file_choice == "2":
    pdf_file_path = input("Enter the path of the PDF file: ")
    try:
        text_content = ""
        pdf_content = read_pdf_file(pdf_file_path)
    except FileNotFoundError:
        print("PDF file not found. Exiting.")
        exit()
else:
    print("Invalid choice. Exiting.")
    exit()

# Ask a question and get the answer
question = input("Ask a question: ")

if file_choice == "1":
    answers = find_answer(question, text_content)
elif file_choice == "2":
    answers = find_answer(question, pdf_content)

if not answers:
    print("No answers found.")
else:
    print("Answers:")
    for answer in answers:
        print("- ", answer)
