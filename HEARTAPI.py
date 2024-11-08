from flask import Flask, jsonify, request

app = Flask(__name__)

heart = [
    {
        "Heart_id" : "1",
        "Date" : "Nov 8, 2024",
        "Heart_rate" : "96" 
    },
    {
        "Heart_id" : "2",
        "Date" : "Nov 8, 2024",
        "Heart_rate" : "91",
    }
    
]
@app.route('/heart', methods=['GET'])
def getHeart():
    return jsonify(heart)

@app.route('/heart', methods=['POST'])
def addHeart():
    hearts = request.get_json()
    heart.append(hearts)
    return {'Successful, id' : len(heart)}, 200

@app.route('/heart/<int:index>', methods=['PUT'])
def update_heart(index):
    hearts = request.get_json()
    heart[index] = hearts
    return jsonify(heart[index]), 200

@app.route('/heart/<int:index>', methods=['DELETE'])
def deleteHeart(index):
    heart.pop(index)
    return 'The heart has been deleted', 200

if __name__ == '__main__':
    app.run()
