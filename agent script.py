import os

class Agent:
    def __init__(self, files):
        self.files = files
        self.knowledge = {}

    def load_files(self):
        for file_name in self.files:
            if file_name.endswith('.txt'):
                with open(file_name, 'r') as file:
                    content = file.read()
                    self.knowledge[file_name] = content

    def answer_question(self, question):
        for content in self.knowledge.values():
            lines = content.split("\n")
            for line in lines:
                if line.startswith("Question:") and question.lower() in line.lower():
                    answer_index = lines.index(line) + 1
                    return lines[answer_index].lstrip("Answer:").strip()

        return "I'm sorry, I don't have an answer for that."

def main():
    print("Welcome to the Agent Creation System!")

    # Agent creation
    files = []
    file_count = int(input("How many files would you like to upload? "))

    for i in range(file_count):
        file_name = input(f"Enter the name of file {i+1}: ")
        files.append(file_name)

    agent = Agent(files)
    agent.load_files()

    print("Agent created successfully!")

    # Interaction with the Agent
    while True:
        question = input("Ask a question to the Agent (or 'exit' to quit): ")

        if question.lower() == 'exit':
            break

        answer = agent.answer_question(question)
        print("Agent's answer: ", answer)

if __name__ == '__main__':
    main()

