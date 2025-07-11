# Imports
from flask import Flask, render_template, redirect, request
from flask_scss import Scss
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
# My app
app = Flask(__name__)
Scss(app)

# Configuring database
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATION"] = False
db = SQLAlchemy(app)

# Kinda like a data class ~ row of data
class MyTask(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Master key allows to add or delete
    content = db.Column(db.String(100), nullable=False)
    complete = db.Column(db.Integer, default=0) # default no not complete
    created = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    def __repr__(self):
        return f"Task {self.id}"

### create new database via context manager 
with app.app_context():
        db.create_all()
# Homepage
@app.route("/",methods=["POST","GET"])
def index():
    # 1. Add a Task
    if request.method == "POST":
        current_task = request.form['content'] ## form on index.html content is that id
        new_task = MyTask(content=current_task)
        
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print("ERROR:{e}")
            return f"ERROR:{e}"
    
    # 2. See all current tasks 
    else: ### GET request
        tasks = MyTask.query.order_by(MyTask.created).all()
        

        return render_template("index.html",tasks=tasks)


# Delete an item
@app.route("/delete/<int:id>")
def delete(id: int):
    delete_task = MyTask.query.get_or_404(id)
    try:
        db.session.delete(delete_task)
        db.session.commit()
        return redirect("/")
    except Exception as e:
        print("ERROR: Delete{e}")
        return f"ERROR: Delete{e}"

# Edit an item
@app.route("/edit/<int:id>", methods=["GET","POST"])
def edit(id:int):
    task = MyTask.query.get_or_404(id)
    if request.method == "POST":
        task.content = request.form['content']
        try:
            db.session.commit()
            return redirect("/")
        except Exception as e:
            print("ERROR: Delete{e}")
            return f"ERROR: Delete{e}"
    else:
        return render_template('edit.html',task=task)
    
    
if __name__ in "__main__":
    
        
    app.run(debug=True)