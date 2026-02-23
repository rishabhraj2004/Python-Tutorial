# store following word meaning in py dict
# table : "a piece of furniture", "list of facts & figures"
# cat : "a small animal"

word_meaning = {
    "table": ["a piece of furniture", "list of facts & figures"], #two ya two se jada meaning store karne ke liye LIST AND STRING ka use karte hai, kyuki list mai hum multiple value store kar sakte hai, but tuple mai hum multiple value store nahi kar sakte hai, kyuki tuple immutable hota hai, but list mutable hota hai
    "cat": "a small animal"
}
print(word_meaning) #to print the whole dictionary
print(word_meaning["table"]) #to print meaning of table key
print(word_meaning["cat"]) #to print meaning of cat key