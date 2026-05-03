f = open("D:\\python (appna college)\\lc.7 file input output\\sample_file.txt", "r")
data = f.read()
print(data)
print(type(data))
f.close()   #agar hum file close nhi krenge to koi bhi akke  hamare file par kuch bhi kar sakta hai isliye close karna jrurui hai.



f = open("D:\\python (appna college)\\lc.7 file input output\\sample_file.txt", "r")
data = f.read(7)#agar hum read ke andar number denge to wo utne hi character read karega jitna number humne diya hai.
#yha pe output I am le tk hi ayega kyuki yha tak 7 character hai.
print(data)
print(type(data))
# f.close() agar yha pe file close kar dete hai to error ayega kyuki file close ho chuki hai aur hum uske baad usko read karne ki koshish kar rahe hai.


line1 = f.readline() #agar hum readline use krte hai to wo file ke first line ko read krta hai aur uske baad cursor next line pe chala jata hai.    
print(line1)
print(type(line1))



line2 = f.readline() #agar hum readline use krte hai to wo file ke first line ko read krta hai aur uske baad cursor next line pe chala jata hai.    
print(line2)
print(type(line2))

line3= f.readline()
print(line3)
#yha pe hamare txt file mai 3rd line hai to ek empty line print ho jayegi kyuki 3rd line blank hai. agar hamare txt file mai 3rd line blank nhi hoti to wo 3rd line print kar deta.
f.close()