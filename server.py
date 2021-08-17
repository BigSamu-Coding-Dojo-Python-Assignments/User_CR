from flask import Flask, render_template, request, redirect
# import the class from friend.py
from user import User
app = Flask(__name__)

@app.route('/users')
def index():
    users = User.get_all()
    return render_template("index.html", users_info = users)


@app.route('/users/new', methods=["GET","POST"])
def create_friend():

    if(request.method == "POST"):
        data = {
            "first_name": request.form["first_name"],
            "last_name" : request.form["last_name"],
            "email" : request.form["email"]
        }
        User.save(data)
        return redirect('/users')

    return render_template("new_user.html")
            
if __name__ == "__main__":
    app.run(debug=True)

