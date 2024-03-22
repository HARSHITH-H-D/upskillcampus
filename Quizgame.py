import tkinter as tk
import cProfile
import matplotlib.pyplot as plt
import time
start_time = time.time()
class QuizApp:
    def __init__(self, root, questions, answers):

        self.root = root
        self.questions = questions
        self.answers = answers
        self.score = 0
        self.current_question = 0
        self.correct_answers = []
        self.incorrect_answers = []

        self.label_question = tk.Label(root, text="")
        self.label_question.pack()

        self.radio_var = tk.StringVar()
        self.radio_var.set(None)

        self.radio_buttons = []
        for i in range(3):
            radio_btn = tk.Radiobutton(root, text="", variable=self.radio_var, value=i+1)
            self.radio_buttons.append(radio_btn)
            radio_btn.pack()

        self.next_button = tk.Button(root, text="Next", command=self.next_question)
        self.next_button.pack()
        # Label to display the score
        self.score_label = tk.Label(root, text="Score: 0")
        self.score_label.pack()


        self.load_question()

    def load_question(self):
        if self.current_question < len(self.questions):
            question_text, options = self.questions[self.current_question]
            self.label_question.config(text=question_text)
            for i, option in enumerate(options):
                self.radio_buttons[i].config(text=option)  # Use option as the text for radio buttons
            self.radio_var.set(None)
        else:
            self.show_result()


    def next_question(self):
        if self.radio_var.get() is not None:
            answer_index = int(self.radio_var.get()) - 1
            user_answer = self.questions[self.current_question][1][answer_index].strip()  # Strip whitespace
            correct_answer = self.answers[self.current_question].strip()  # Strip whitespace
            if user_answer == correct_answer:
                self.score += 1
                self.correct_answers.append(self.current_question)
            else:
                self.incorrect_answers.append(self.current_question)
        # Update the score label
            self.score_label.config(text=f"Score: {self.score}")
        self.current_question += 1
        if self.current_question < len(self.questions):  # Check if there are more questions
            self.load_question()
        else:
            self.show_result()

    def show_result(self):
        self.root.destroy()
        total_questions = len(self.questions)
        print("Total Score:", self.score)
        print("Correct Answers:", self.correct_answers)
        print("Incorrect Answers:", self.incorrect_answers)
        self.plot_graph()

    def plot_graph(self):
        labels = ['Correct', 'Incorrect']
        values = [len(self.correct_answers), len(self.incorrect_answers)]
        plt.bar(labels, values)
        plt.xlabel('Answers')
        plt.ylabel('Count')
        plt.title('Correct vs Incorrect Answers')
        plt.show()

def read_questions(filename):
    questions = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for i in range(0, len(lines), 4):
            question_text = lines[i].strip()
            options = [opt.strip() for opt in lines[i+1:i+4]]
            print("Question:", question_text)
            print("Options:", options)
            questions.append((question_text, options))
    return questions

def read_answers(filename):
    with open(filename, 'r') as file:
        answers = file.readlines()
        # Strip newline characters and split by '.' to extract only the answer part
        answers = [answer.strip().split('.')[1].strip() for answer in answers]
    return answers

# Example usage:
answers = read_answers("answers.txt")
print(answers)  # Check if the answers are correctly read from the CSV file



# Define a function to run your program
def run_program():


    questions = read_questions("example.txt")
    answers = read_answers("answers.txt")

    root = tk.Tk()
    root.title("Quiz App")
    app = QuizApp(root, questions, answers)
    root.mainloop()
cProfile.run('run_program()', filename='profile_results.txt')
# Profile the program execution


end_time = time.time()
# Total execution time
execution_time = end_time - start_time
print("Total execution time:", execution_time, "seconds")

