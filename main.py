from flask import Flask, request, redirect
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),"templates")
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():

    template = jinja_env.get_template("hello_form.html")
    return template.render()

@app.route("/validate", methods=["POST"])
def hello():

    uname = request.form["user_name"]
    psw = request.form["password"]
    vpsw = request.form["vpassword"]
    mail = request.form["email"]

    err_name = ""
    err_pswd = ""
    err_vpswd = ""
    err_email = ""

    if len(uname) == 0:
        err_name = "Please enter the user name"
    if len(uname) >= 1 and len(uname) < 3:
        err_name = "Username has to be atleast 3 characters"   
    if len(uname) > 20:
        err_name = "Username has to be less than 20 characters"
    if (" " in uname) == True:
	    err_name = "Invalid Username"
     
 
    if len(psw) == 0:
        err_pswd = "Please enter the password"
    if len(psw) >= 1 and len(psw) < 3:
        err_pswd = "Password has to be atleast 3 characters"   
    if len(psw) > 20:
        err_pswd = "Password has to be less than 20 characters"
    if (" " in psw) == True:
	    err_pswd = "Invalid Password"

    if len(vpsw) == 0:
        err_vpswd = "Please enter the password"
    if vpsw != psw:
        err_vpswd = "Passwords don't match"

    if len(mail) == 0:
        err_email = ""
    else:    
        if len(mail) >= 1 and len(mail) < 3:
            err_email = "Email-id has to be atleast 3 characters"   
        if len(mail) > 20:
            err_email = "Email-id has to be less than 20 characters"
        if (" " in mail) == True:
	        err_email = "Invalid Email-id"
        if (mail.count("@")) == 0 or (mail.count("@")) > 1:    
            err_email = "Invalid Email-id"
        if (mail.count(".")) == 0 or (mail.count(".")) > 1:    
            err_email = "Invalid Email-id"
    

    if err_name == "" and err_pswd == "" and err_vpswd == "" and err_email == "":
        return redirect("/valid?name={0}".format(uname))
    else:

        template = jinja_env.get_template("hello_form.html")
        return template.render(usrname=uname, err_name=err_name, err_pswd=err_pswd, err_vpswd=err_vpswd, 
                emailid=mail, err_email=err_email)

@app.route("/valid")
def greet():
    
    name = request.args.get("name")
    template = jinja_env.get_template("hello_greetings.html")
    return template.render(uname=name)

app.run()

