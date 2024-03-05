{"filter":false,"title":"app.py","tooltip":"/app.py","undoManager":{"mark":8,"position":8,"stack":[[{"start":{"row":0,"column":0},"end":{"row":131,"column":52},"action":"insert","lines":["from flask import Flask, request","","app = Flask(__name__)","","import dynamodb_handler as dynamodb","","","@app.route('/')","def root_route():","    dynamodb.CreatATableBook()","    return 'Hello World'","","# TODO: GET all books route","","","","#  Add a book entry","#  Route: http://localhost:5000/book","#  Method : POST","@app.route('/book', methods=['POST'])","def addABook():","","    data = request.get_json()","    # id, title, author = 1001, 'Angels and Demons', 'Dan Brown'","","    response = dynamodb.addItemToBook(data['id'], data['title'], data['author'])    ","    ","    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):","        return {","            'msg': 'Added successfully',","        }","","    return {  ","        'msg': 'Some error occcured',","        'response': response","    }","","# TODO: DELETE all books route","","","#  Read a book entry","#  Route: http://localhost:5000/book/<id>","#  Method : GET","@app.route('/book/<int:id>', methods=['GET'])","def getBook(id):","    response = dynamodb.GetItemFromBook(id)","    ","    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):","        ","        if ('Item' in response):","            return { 'Item': response['Item'] }","","        return { 'msg' : 'Item not found!' }","","    return {","        'msg': 'Some error occured',","        'response': response","    }","","","#  Delete a book entry","#  Route: http://localhost:5000/book/<id>","#  Method : DELETE","@app.route('/book/<int:id>', methods=['DELETE'])","def DeleteABook(id):","","    response = dynamodb.DeleteAnItemFromBook(id)","","    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):","        return {","            'msg': 'Deleted successfully',","        }","","    return {  ","        'msg': 'Some error occcured',","        'response': response","    } ","","","#  Update a book entry","#  Route: http://localhost:5000/book/<id>","#  Method : PUT","@app.route('/book/<int:id>', methods=['PUT'])","def UpdateABook(id):","","    data = request.get_json()","","    # data = {","    #     'title': 'Angels And Demons',","    #     'author': 'Daniel Brown'","    # }","","    response = dynamodb.UpdateItemInBook(id, data)","","    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):","        return {","            'msg'                : 'Updated successfully',","            'ModifiedAttributes' : response['Attributes'],","            'response'           : response['ResponseMetadata']","        }","","    return {","        'msg'      : 'Some error occured',","        'response' : response","    }   ","","","# like a book - api","","#  Like a book","#  Route: http://localhost:5000/like/book/<id>","#  Method : POST","@app.route('/like/book/<int:id>', methods=['POST'])","def LikeBook(id):","","    response = dynamodb.LikeABook(id)","","    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):","        return {","            'msg'      : 'Likes the book successfully',","            'Likes'    : response['Attributes']['likes'],","            'response' : response['ResponseMetadata']","        }","","    return {","        'msg'      : 'Some error occured',","        'response' : response","    }","","","if __name__ == '__main__':","    app.run(host='127.0.0.1', port=5000, debug=True)"],"id":1}],[{"start":{"row":107,"column":0},"end":{"row":111,"column":16},"action":"remove","lines":["# like a book - api","","#  Like a book","#  Route: http://localhost:5000/like/book/<id>","#  Method : POST"],"id":2},{"start":{"row":106,"column":0},"end":{"row":107,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":87,"column":1},"end":{"row":90,"column":7},"action":"remove","lines":["   # data = {","    #     'title': 'Angels And Demons',","    #     'author': 'Daniel Brown'","    # }"],"id":3}],[{"start":{"row":79,"column":0},"end":{"row":81,"column":15},"action":"remove","lines":["#  Update a book entry","#  Route: http://localhost:5000/book/<id>","#  Method : PUT"],"id":4},{"start":{"row":78,"column":0},"end":{"row":79,"column":0},"action":"remove","lines":["",""]}],[{"start":{"row":58,"column":0},"end":{"row":62,"column":18},"action":"remove","lines":["","","#  Delete a book entry","#  Route: http://localhost:5000/book/<id>","#  Method : DELETE"],"id":5}],[{"start":{"row":37,"column":0},"end":{"row":42,"column":15},"action":"remove","lines":["# TODO: DELETE all books route","","","#  Read a book entry","#  Route: http://localhost:5000/book/<id>","#  Method : GET"],"id":6}],[{"start":{"row":12,"column":0},"end":{"row":18,"column":16},"action":"remove","lines":["# TODO: GET all books route","","","","#  Add a book entry","#  Route: http://localhost:5000/book","#  Method : POST"],"id":7}],[{"start":{"row":105,"column":18},"end":{"row":105,"column":27},"action":"remove","lines":["127.0.0.1"],"id":8},{"start":{"row":105,"column":18},"end":{"row":105,"column":19},"action":"insert","lines":["0"]},{"start":{"row":105,"column":19},"end":{"row":105,"column":20},"action":"insert","lines":["."]},{"start":{"row":105,"column":20},"end":{"row":105,"column":21},"action":"insert","lines":["0"]},{"start":{"row":105,"column":21},"end":{"row":105,"column":22},"action":"insert","lines":["."]},{"start":{"row":105,"column":22},"end":{"row":105,"column":23},"action":"insert","lines":["0"]},{"start":{"row":105,"column":23},"end":{"row":105,"column":24},"action":"insert","lines":["."]},{"start":{"row":105,"column":24},"end":{"row":105,"column":25},"action":"insert","lines":["0"]}],[{"start":{"row":17,"column":3},"end":{"row":17,"column":64},"action":"remove","lines":[" # id, title, author = 1001, 'Angels and Demons', 'Dan Brown'"],"id":9}]]},"ace":{"folds":[],"scrolltop":90,"scrollleft":0,"selection":{"start":{"row":32,"column":45},"end":{"row":32,"column":45},"isBackwards":false},"options":{"guessTabSize":true,"useWrapMode":false,"wrapToView":true},"firstLineState":{"row":5,"state":"start","mode":"ace/mode/python"}},"timestamp":1709666423118,"hash":"e3ece241a0a9a070c41daa24129fa491dd6dedb8"}