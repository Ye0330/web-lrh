from flask import Flask, render_template, request
import json
app = Flask(__name__)
# 功能未完成，无法记录用户信息， 以后试试用sql实现


@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "GET":
        return render_template('register.html')
    else:
        user = request.form.get("user")
        password = request.form.get("password")
        gender = request.form.get("gender")
        sexual_orientation = request.form.get("so")
        skill = request.form.getlist("skill")
        info = request.form.get("info")

        user_dict = {
            "user": user,
            "password": password,
            "gender": gender,
            "sexual_orientation": sexual_orientation,
            "skill": skill,
            "info": info
        }
        print(user_dict)
        with open("C:/Users/W2007/PycharmProjects/pythonProject/Web_2/user_info.txt", "a", encoding="UTF-8") as f:
            f.write(json.dumps(user_dict))
            # f.write('\n')
        return render_template('register_1.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    else:
        with open("C:/Users/W2007/PycharmProjects/pythonProject/Web_2/user_info.txt", "r", encoding="UTF-8") as f:
            for line in f:
                print(line)
                user_list_1 = list(line[::-2])
                print(user_list_1)
                for i in user_list_1:
                    if request.form.get("user") == i[0] and request.form.get("password") == i[1]:
                        return render_template("login_1.html")
                    else:
                        return render_template("login.html")


@app.route("/home", methods=["GET", "POST"])
def home_page():
    return render_template('home.html')


if __name__ == "__main__":
    app.run()
