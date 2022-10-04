'''
Rubber Duckies: Ivan Yeung, Jeffrey Zou, Raven (Ruiwen) Tang
SoftDev
K07 -- Teardown / Investigating Flask
2022-10-03
time spent: hrs
'''

from flask import Flask

app = Flask("bob") # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print("bob") # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
* Without changing the content of the given code, we immediately receive a ModuleNotFoundError: "No module named 'flask'"
QCC:
0. We've seen similar syntax in Java, especially with overloaded constructors and typecasting. Here, Flask would be the constructor name, and __name__ is the parameter it takes in.
1. We've seen '/' in file paths when we're working with directories in Terminal, and the character also shows up in URLs, similarly denoting a kind of path.
2. We think this line will print to the console, as that's where print statements have printed in our experience.
3. It'll print whatever __name__ is a placeholder for, perhaps the name of the app.
4. This will appear on the webpage whose local link is given to us when we run this Python file. We know because the address was hyperlinked, and we were able to open it in a web browser.
5. We've seen the dot and empty parentheses used in a lot of class methods in Java. We think that if we interpret line 11 to be a constructor, then perhaps line 18 is running a non-static (or static?) method of the Flask class, though we're not sure if characteristics like staticness translate from Java to Python.
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
'''