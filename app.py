from flask import Flask,request,jsonify
app=Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

tasks=[
    {
        "id":1,
        "name":u"Raju",
        "contact":u"9987644456",
        "done":False
    },
    {
        
        "id":2,
        "name":u"Rahul",
        "contact":u"9876543222",
        "done":False
    }
]
@app.route("/add-data",methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message":"pls provide the data"
        })
    task={
        "id":tasks[-1]["id"]+1,
        "title":request.json["title"],
        "description":request.json.get("description",""),
        "done":False
    }    
    tasks.append(task)
    return jsonify({
        "status":"success",
        "message":"task added succesfully"
    })

@app.route("/get-data")
def get_task():
    return jsonify({
        "data":tasks
    })
if __name__ == "__main__":
    app.run(debug=True)