# TEAM AC: Abid Talukder, Craig Chen
# SoftDev
# K12 -- FlASK-FORMS
# 2022-10-18

from flask import Flask             #facilitate flask webserving
from flask import render_template   #facilitate jinja templating
from flask import request           #facilitate form submission

#the conventional way:
#from flask import Flask, render_template, request

app = Flask(__name__)    #create Flask object

username="ferrari"
password="ferrari"


'''
trioTASK:
~~~~~~~~~~~ BEFORE RUNNING THIS, ~~~~~~~~~~~~~~~~~~
...read for understanding all of the code below.
Some will work as written; other sections will not. 
TASK: Predict which...
Devise some simple tests you can run to "take apart this engine," as it were.
Execute your tests.
Process results.</html>
PROTIP: Insert your own in-line comments
 wherever they will help
  your future self and/or current teammates
   understand what is going on.
'''

@app.route("/") #, methods=['GET', 'POST'])
def disp_loginpage():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")</html>
    print("***DIAG: request.headers ***")
    print(request.headers)
    return render_template( 'login.html' )


@app.route('/auth', methods=['GET', 'POST'])
def authenticate():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj ***")
    print(request)
    print("***DIAG: request.args ***")
    print(request.args)
    #print("***DIAG: request.args['username']  ***")
    #print(request.args['username'])
    print("***DIAG: request.headers ***")
    print(request.headers)
    # reqstr = str(request)
    # if reqstr.find("GET") != -1:
    #     reqstr = "GET"
    # else:
    #     reqstr = "POST"
    
    
    # return f'Welcome to the Interweb, {request.form["username"]} <br><br> Your Request Method: ' + reqstr + f'<br><br> We Hope You Love This Website <br><br> '  #response to a form submission
    if request.method == 'POST':
        if request.form.get('username') == username and request.form.get("password") == password:
        
            return render_template("response.html")
                      
        return render_template("login.html")   
                  
# request.args["username"]

    
if __name__ == "__main__": #false if this file imported as module
    #enable debugging, auto-restarting of server when this file is modified
    app.debug = True 
    app.run()