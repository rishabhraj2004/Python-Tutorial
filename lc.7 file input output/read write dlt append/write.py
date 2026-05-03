f = open("D:\python (appna college)\lc.7 file input output\demo.txt", "w") 
f.write("This is a demo file.\n")
f.write("It is used for demonstrating file handling in Python.\n")
#yha pe humne demo.txt file ko write mode me open kiya hai aur usme kuch text likh diya hai. agar demo.txt file pehle se exist karti hai to uska content overwrite(erase old data ) ho jayega aur agar file exist nahi karti hai to wo file create ho jayegi aur usme text likh diya jayega.
f.close() #file ko close karna jaruri hai taki data properly save ho jaye aur file par koi bhi akke hamare file par kuch bhi kar sakta hai isliye close karna jrurui hai.


#agar write krne ke bd phir se write mode use krenge to pehle jo likhe hai wo dlt ho jayega aur abhi jo likhenge sirf wahi rhega
#agar append mode use krenge to pehle jo likhe hai wo rhega aur abhi jo likhenge wo uske baad add ho jayega

f = open("D:\python (appna college)\lc.7 file input output\demo.txt", "a")
f.write("This line is added using append mode.\n")
f.write("This is another line added using append mode.\n" "Append mode me humne demo.txt file ko open kiya hai aur usme kuch text add kiya hai. agar demo.txt file pehle se exist karti hai to uska content delete nahi hoga aur jo bhi text hum append mode me likhenge wo uske baad add ho jayega. agar file exist nahi karti hai to wo file create ho jayegi aur usme text likh diya jayega.")
f.close()


#agar write mode mai koi file open kiye or wo exist nhi karta hai to wo file create ho jata hai aur usme text likh diya jata hai. agar file exist karta hai to uska content overwrite(erase old data ) ho jata hai aur agar file exist nahi karta hai to wo file create ho jata hai aur usme text likh diya jata hai.