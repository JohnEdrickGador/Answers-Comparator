import os
import time
def clear():
    os.system('cls')
class AnswerSheet():
    def __init__(self,file_name):
        self.file_name = file_name
    def getAnswers(self):
        sheet = open(self.file_name)
        lines = sheet.readlines()
        answers = []
        for line in lines:
            line = line.rstrip()
            line = line.lower()
            answers.append(line)
        return answers

print("""Welcome to JEG's answer comparator v1.0
This program only supports 2 file comparisons multiple choice questions at the moment.
Thank you!""")

file1 = AnswerSheet(input("Enter file name of first answer sheet (e.g. answers.txt): "))
answers1 = file1.getAnswers()
clear()

file2 = AnswerSheet(input("Enter file name of second answer sheet (e.g. answers.txt): "))
answers2 = file2.getAnswers()
clear()
print("Comparing...")
time.sleep(3)
same = []
diff = []
if len(answers2) != len(answers1):
    print("The number of answers do not match. please recheck your files")
    exit()
else:
    for i in range(len(answers1)):
        if answers1[i] == answers2[i]:
            same.append(i+1)
        elif answers1 != answers2:
            diff.append(i+1)
clear()
new_file = open("results.txt","w+")

print(f"similar answers:",end = " ")
new_file.write("similar answers: ")
for i in range(len(same)):
    print(same[i],end = "-")
    new_file.write(f"{same[i]}-")

print("\n")
new_file.write("\n\n")

print(f"contradicting answers:", end = " ")
new_file.write("contradicting answers: ")
for i in range(len(diff)):
    print(diff[i],end = "-")
    new_file.write(f"{diff[i]}-")
new_file.close()


        


        