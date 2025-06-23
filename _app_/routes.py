#Has all the core, admin and auth routes#
from flask import Blueprint, render_template, request, flash, redirect, url_for
from . import db
from .models import User, Note
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user


#---------------------------------All Core/view routes---------------------------------#
#These are routes available to the user before they login/authorized/authenticated
core = Blueprint("core", __name__)

@core.route("/")
def landing_page():
    return render_template("landPage.html", user=current_user)


@core.route("/dashboard", methods=["GET","POST"])
@login_required
def dashboard():
    if(request.method =="POST"):
        note = request.form.get("note")
        if(len(note)<1):
            flash("Need to input text to save", category="error")
        else:
            flash("Note added", category="success")
            new_Note = Note()
            new_Note.data = note
            new_Note.user_id = current_user.id

            db.session.add(new_Note)
            db.session.commit()

            # Always redirect after POST to avoid duplication issues #
            return redirect(url_for("core.dashboard"))
    
    return render_template("dashboard.html", user=current_user)


@core.route("/test-button", methods=["GET", "POST"])
def test_button():
    return redirect(url_for("core.landing_page"))


    #Event/Trigger-only route function:
@core.route("/delete-note/<int:note_id>", methods=["POST"])
@login_required
def delete_note(note_id):
    note = Note.query.get(note_id)
    if note and note.user_id == current_user.id:
        db.session.delete(note)
        db.session.commit()
        flash("Note deleted.", category="success")

    return redirect(url_for("core.dashboard"))
#-----------------------------------------End-----------------------------------------#



#-----------------------------------All Authorized routes-----------------------------------#
auth = Blueprint("auth", __name__)

@auth.route("/signUp", methods=['GET','POST'])
def signup_page():
    if(request.method == "GET"):
        return render_template("signUp.html", user=current_user)
    
    elif(request.method == "POST"):
        #Collecting data from POSTed form:
        data = request.form
        print(data)

        email = request.form.get("email")
        name = request.form.get("firstName")
        p1 = request.form.get("password1")
        p2 = request.form.get("password2")  

        is_valid = check_data(email, name, p1, p2)
        if(is_valid):
            new_user = User()
            new_user.email = email
            new_user.first_name = name
            new_user.password = generate_password_hash(p1, method="pbkdf2:sha256")
            #Or:
            #new_user = User(email=email, first_name = name, password = generate_password_hash(p1, method="pbkdf2:sha256")

            db.session.add(new_user)
            db.session.commit()

            login_user(new_user)

            return redirect(url_for("core.dashboard"))
        else:
            return render_template("signUp.html", user=current_user) #WHY DO THIS HERE????
    
def check_data(e, n, p1, p2):
    user = User.query.filter_by(email=e).first()

    if(user):
        flash("User already exists", category="error")
        return False
    if(n=="" or p1=="" or p2==""):
        flash("Missing field(s)!", category="error")
        return False
    elif not (e.__contains__("gmail") or e.__contains__("yahoo") or e.__contains__("icloud")):
        flash("Add a valid email", category="info")
        return False
    elif(p1 != p2):
        flash("Passwords do not match", category="error")
        return False
    elif(len(p1) < 7):
        flash("Password length too small", category="error")
        return False

    flash("Account Made!", category="success")
    return True


@auth.route("/login", methods=['GET','POST'])
def login_page():
    if(request.method == "POST"):
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        #if(user==None):
            #Or:
        if(user):
            if(check_password_hash(user.password, password)):
                flash("Logged in successfully", category="success")

                login_user(user, remember=True)
                return redirect(url_for("core.dashboard"))  # Send user to /dashboard
            else: 
                flash("Incorrect password. Try again", category="error")
        else:
            flash("Email does not exist or password is incorrect", category="error")

    user = {"username": "user"}
    return render_template("login.html", user=user)
        #Or:
    #return render_template("login.html")
        #OR:
    #return redirect(url_for("dashboard"))  # Send user to /dashboard


@auth.route("/logout")
@login_required #Makes sure that user is logged in when accessing this route.
def logout():
    logout_user()
    flash("Has logged out of account", category="info")
    return redirect(url_for("auth.login_page"))
#----------------------------------------End----------------------------------------#



#To add in the future:
admin = Blueprint("admin", __name__)