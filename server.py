from flask import Flask, jsonify, request
import json
app = Flask(__name__)

# Student data
# items = [
#     {
#         "id": 1,
#         "name": "Rishi",
#         "marks": {
#             "Maths": 99,
#             "chem": 99,
#             "english": 99}
#     },
#     {
#         "id": 2,
#         "name": "Sanket",
#         "marks": {
#             "Maths": 99,
#             "chem": 99,
#             "english": 99
#         }
#     }
# ]


class student:
    Id = 0 
    Name = ""
    Marks = None
    Rank = 0
    
    def printMe(self):
        print("I am a student ID is: ",self.Id,self.Marks)
    def average(self):
        avg = 0
        for i in self.Marks:
            avg = avg + i 
        average = avg/len(self.Marks)
        return average
    def __init__(self,Id,Name,Marks):
        self.Id = Id
        self.Name = Name 
        self.Marks = Marks

items = []


@app.route('/', methods=['GET'])
def home():
   # return jsonify({"message": "Welcome to the NHCE student reports"})
    return "<html><i>Welcome to the <b>NHCE</b> student reports</i></html>"


@app.route('/stuList', methods=['GET'])
def stuList():
   # return jsonify({"message": "Welcome to the NHCE student reports"})
    return json.dumps(items.__dict__)

# curl -H 'Content-Type: application/json' -X "POST" \
# -d '{
#     "name": "Sanket",
#     "maths": 99,
#     "chem": 99,
#     "english": 99
# }' http://127.0.0.1:5000/newstu
    
@app.route('/newstu', methods=['POST'])
def create_item():
    data = request.get_json()
    # new_item = {
    #     "id": 1,
    #     "name": data.get("name"),
    #     "marks": {
    #         "Maths": data.get("maths"),
    #         "chem": data.get("chem"),
    #     }
    # }
    
    newItem = student(1, data.get("name"),[data.get("maths"), data.get("english"), 
                                           data.get("chem"), data.get("phy")])
    items.append(newItem)
    
    return json.dumps(newItem.__dict__), 201


if __name__ == '__main__':
    app.run(debug=True)
