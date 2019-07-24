from flask import Flask, request, jsonify


app = Flask(__name__)


my_store = [
        { 'name': "welcome store",
            'items': { ['name': "chair",
                        'price': 7.99
                        ]
                }

                }


        ]


#POST used to receive data
#GET used to send back data

#POST /store data: {name:}
@app.route("/my_store",method=["POST"])
def store_home():
    request_data = request.get_json()
    new_store = { 'name' : request_data['name'],
                'item' : { []
                    }
            }
    my_store.append(new_store)
    return jsonify(my_store)

#GET /my_store dikhaye
@app.route("/my_store",method=["GET"])
def show_my_store():
    return jsonify({'stores': my_store})

#GET /my_store/<string:name> searched store dikhaye
@app.route("/my_store/<string:name>",method="GET")
def show_entered_store():
    request_data = request.get_json()
    if request_data['name'] == my_store["name"]:
        

#POST /my_store/<string:name>/item
#GET /my_store/<string:name>/item





app.run()
