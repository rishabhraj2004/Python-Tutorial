# create a new file "practice.txt" using py. Add the following data in try:
# hi everyone
# we are learning file I/O in java
# i like programming in java
# i am enjoying it

# WAF that replace all the occurances of "java" with "python" in the file "practice.txt". 

# search if the word "learning" exists in the file or not

with open("practice.txt", "w") as f:
    f.write("hi everyone\n")
    f.write("we are learning file I/O in java\n")
    f.write("i like programming in java\n")
    f.write("i am enjoying it\n")

#for replacing "java" with "python"
with open("practice.txt", "r") as f:
    data = f.read()

new_data = data.replace("java", "python")
print(new_data)

with open("practice.txt", "w") as f:
    f.write(new_data)

#for searching "learning" as simple way 
with open("practice.txt", "r") as f:
    data = f.read()
    if(data.find("learning") != -1): #yha pe direct learning kar diye hm cahhte to word="learning" krke find ke andr word dal dete to bhi output same atta.
        print("word found")
    else:        print("word not found")



    # found learning by function
    def check_word():
        word = "rishu"
        with open("practice.txt", "r") as f:
            data = f.read()
        if(data.find(word) != -1):
            print("word found")
        else:
            print("word not found")

    check_word()


#WAF to find in which line of the file doest the word "learning" occur first.
#print -1 if word not found
def check_for_line():
    word = "xlearning"
    data = True # data true isleiye kiye qki agar ye nhi krte to read hone ke baad data ka value false ho jata aur loop nhi chalta
    line_no = 1
    with open("practice.txt", "r") as f:
        while data :
            data = f.readline()
            if(word in data):
                print("word found at line no ", line_no)
                return
                line_no += 1
                

    return -1 # we use return instead of print because we want to exit the function after finding the word and if we use print then it will print -1 also after finding the word which is not correct.

check_for_line()# aise krenge to agar exist nhi krega to print -1 nhi hoga 
print(check_for_line()) # aise krenge to agar exist nhi krega to print -1 hoga
   

