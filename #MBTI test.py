#MBTI test

#Import time to use 'timesleep' statement
import time

#function to use 'timesleep'
def wait(second):
    time.sleep(second)

#MBTI Explanation
#While loop to repeat explanation
print("Welcome to SPT!")
wait(2)

while True:
    print("SPT stands for Short, Simple, and Scientific Personality Test.")
    wait(2)
    
    print("Our personality test will use MBTI to indicate users' personality.")
    wait(2)
    
    print("MBTI which stands for 'Myers Briggs Type Indicator' is a personality typology which is used to help individuals understand their own personality.")
    wait(3)

    reInstruct = input("Type 'repeat' to repeat the explanation, or type 'continue' to continue ")
    if reInstruct == "repeat":
        continue
    else:
        break

#Instruction
#While loop to repeat instruction

instructionList = ["Now we will explain how the test will go.", "We will give you two opposing statements.", "If you agree with the first statement type in '1', and if you agree with the second statement type in '2'."]

print(instructionList[0])
wait(2)
    
print(instructionList[1])
wait(2)
    
print(instructionList[2])
wait(3)
    
reInstruct = input("Type 'repeat' to repeat the instrucion, or type 'continue' to continue ")
while reInstruct == "repeat":
    print(instructionList[1])
    wait(2)

    print(instructionList[2])
    wait(2)

    reInstruct = input("Type 'repeat' to repeat the instrucion, or type 'continue' to continue ")



#test start
print("Now we will start the test.")
wait(2)

#Function to ask question and get a return value
def question(ques):
    while True:
        answ = input(ques)
        if answ == "1":
            break
        elif answ =="2":
            break
        else:
            print("Please type in your answer using '1' or '2' ")
            continue
    return(answ)

#Questions
#1E 2I
MBTI11 = question("I enjoy meeting and talking with other people VS I prefer to be alone and to listen to others' opinion ")
MBTI12 = question("I tend to take action before I think and proceed quickly VS I think a lot before taking action and proceed cautiously ")
MBTI13 = question("I think it is more important to learn diverse things VS I think it is more important to learn one thing deeply ")

#1S 2N
MBTI21 = question("I try to focus on the present VS I tend to imagine my future ")
MBTI22 = question("I smell or touch a flower when I receive it VS I think or talk about stories when I see a flower ")
MBTI23 = question("I am a person who likes procedural and repetitive work VS I am a person who likes to experience and learn new things ")

#1T 2F
MBTI31 = question("I like a cold-hearted person at work VS I like a warm-hearted person even if he or she is not good at work ")
MBTI32 = question("I am a person with a clear opinion and want to lead a group in the right direction VS I am a person who listens to everyone’s opinions ")
MBTI33 = question("I am a person who says that what is wrong is clearly wrong VS I am a person who encourages people to think it was a good idea without being offended by something wrong ")

#1J 2P
MBTI41 = question("I am planned and quick at making decisions VS I am improvised and slow at make decisions depending on the mood ")
MBTI42 = question("I try to control or manage a situation VS I usually am being dominated or managed by someone else ")
MBTI43 = question("My living space is organized and I am living a systematic life VS I am poorly organized and am more accessible than systematic ")

#Calculation
MBTI1 = int(MBTI11) + int(MBTI12) + int(MBTI13)
MBTI2 = int(MBTI21) + int(MBTI22) + int(MBTI23)
MBTI3 = int(MBTI31) + int(MBTI32) + int(MBTI33)
MBTI4 = int(MBTI41) + int(MBTI42) + int(MBTI43)

if MBTI1 > 4:
    first = "I"
else:
    first = "E"

if MBTI2 > 4:
    second = "N"
else:
    second = "S"

if MBTI3 > 4:
    third = "F"
else:
    third = "T"

if MBTI4 > 4:
    fourth = "P"
else:
    fourth = "J"

MBTI = first + second + third + fourth

print("According to your answers...")
wait(3)

print("Your MBTI is " + MBTI)
wait(4)

#explanation of conclusion
if first == "I":
    print("'I' stands for 'Introverts' ")
else:
    print("'E' stands for 'Extroverts' ")
wait(3)


if second == "N":
    print("'N' stands for 'iNtuitives' ")
else:
    print("'S' stands for 'Sensors' ")
wait(3)


if third == "F":
    print("'F' stands for 'Feelers' ")
else:
    print("'T' stands for 'Thinkers' ")
wait(3)


if fourth == "P":
    print("'P' stands for 'Perceivers' ")
else:
    print("'J' stands for 'Judgers' ")
wait(3)



if MBTI == "ISTJ":
    print("ISTJs are accurate and systematic. They are logical, careful, and responsible at handling work. ")

if MBTI == "ISFJ":
    print("ISFJs are quiet, calm, warm and friendly. They have strong responsibility and perseverance. ")

if MBTI == "INFJ":
    print("INFJs are patient, insightful, intuitive, and creative. They are less than '1%' of the world. ")

if MBTI == "INTJ":
    print("INTJs are active, systematic, and goal-oriented. Some of them are perfectionism. ")

if MBTI == "ISTP":
    print("ISTPs are sensitive to situational awareness and have excellent ability to handle tools. They speak little and observe life objectively and rationally. ")

if MBTI == "ISFP":
    print("ISFPs are friendly, gentle, kind to people, and remain quiet until they get to know the other person well. ")

if MBTI == "INFP":
    print("INFPs tend to run out of energy easily. They prefer to interact with a handful of people with whom they have a high degree of intimacy. ")

if MBTI == "INTP":
    print("INTPs are quiet and reticent. They enjoy solving problems with logic and analysis. They don't usually start a conversation first, but they talk a lot about areas that they are interested in. ")

if MBTI == "ESTP":
    print("ESTPs are realistic, generous, and open-minded. They have a strong sense of reality and excel at finding compromises and solving problems. ")

if MBTI == "ESFP":
    print("ESFPs are sociable, active, receptive, friendly and optimistic. They are adaptable to any realistic and practical situation. ")

if MBTI == "ENFP":
    print("ENFPs are passionate, lively and imaginative. They are warm-hearted and creative types who always find new possibilities and challenges. ")

if MBTI == "ENTP":
    print("ENTPs are versatile, discussion-loving, and always willing to work and change in different environments. ")

if MBTI == "ESTJ":
    print("ESTJs are realistic, concrete, factual, and have leadership in leading any activity. They are practical, realistic, and have the ability to organize, plan, and drive work. ")

if MBTI == "ESFJ":
    print("ESFJs are sympathetic and they care about others. As natural collaborators, they are friendly and active members of the team. ")

if MBTI == "ENFJ":
    print("ENFJs are gentle, active, responsible, sociable and sympathetic. They are quite altruistic, agile, and value humanity. ")

if MBTI == "ENTJ":
    print("ENTJs are zealous, self-assertive, resolute, and have leadership skills. They have a great desire and interest in knowledge. ")


#Closing statement
wait(3)
print("Thank you for using SPT!")
wait(1)

print("See you next time!")