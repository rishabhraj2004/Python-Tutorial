#with use krenge to f close krne ka zaroorat nhi hai qki with file ko automatically close kar deta hai.
with open("D:\python (appna college)\lc.7 file input output\with read and write.txt") as f:
    data = f.read()
    print(data)
    
    f.seek(0) #seek() method ka use karke hum file ke cursor ko wapas start me le aate hai taki hum file ko dobara read kar sake.
    data = f.read()
    print(data)


#yha pe write mode use kiye hai isliye data overwrite ho mtlb kyuki jo pehle likhe the wo sab dlt ho jayega jo abhi likhenge sirf wahi rhega 
with open("D:\python (appna college)\lc.7 file input output\with read and write.txt", "w") as f:
    f.write("This is a demo file.\n")
    f.write("It is used for demonstrating file handling in Python.\n")
    f.write("This line is added using with statement.\n") #with statement me hum file ko read and write mode me open kar rahe hai aur usme kuch text add kar rahe hai. with statement me hum file ko automatically close kar dete hai isliye hume manually close karne ki zaroorat nhi hai. 
    