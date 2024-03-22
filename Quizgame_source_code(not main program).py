import answers1 as a
import matplotlib.pyplot as plt

count=0
score=0
correct=0
incorrect=0
f=open("example1.txt","r+")
for i in range(41):
    if(count<10 and score<20):
        for j in range(4):
            print(f.readline())

        ans=input("Enter the answer:")

        if(ans == a.ans[count]):
            print("Answer is correct")
            score+=2
            count+=1
            correct+=1
        else:
            print("Answer is incorrect")
            print("Correct answer:",a.ans[count])
            count+=1
            incorrect+=1

f.close()
print("The Score:",score,"/20")
print("Correct values:",correct)
print("Incorrect values:",incorrect)
categories = ['Correct', 'Incorrect']
values = [correct, incorrect]

plt.bar(categories, values, color=['blue', 'red'])
plt.xlabel('Answers')
plt.ylabel('Total')
plt.title('Correct vs Incorrect Answers')
plt.show()
