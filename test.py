print ("hello world!")

#variabless
name = "Nick"
last_name = "Greenfield"
age = 30
found = False
print (name)

#if / statement
if age < 100:
    print ("no worries you're not that old")
    print ("I'm using the indentation")
    print ("I'm in the if statement")
elif age == 100: #else if
    print ("wow you're a century")
else:
    print ("Seems that your really old")

#functions
def sayHello():
    print ("Hello world!")

def sayGoodbye(name):
    print ("bye " + str(name))

#call functions
sayHello()
sayGoodbye(2)

#arrays are called lists
color = ["red", "green", "blue", "yellow"]
print (color)
#add an element
color.append("pink")
print (color)
print (color[0])
color.remove("yellow")
print (color)

#for loop
for col in color:
    print (col)
#for (let i=0; limit>0; i++)
#elt temp = color[i]
#print temp

#dictionaries
me = {
    "name": "Nick",
    "last_name": "Greenfield",
    "age": 30
}
print(me["last_name"])
me["last_name"] = "Doe"
print(me)
me["color"] = "blue"
print(me)