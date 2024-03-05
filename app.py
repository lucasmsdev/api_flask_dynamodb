from flask import Flask, request

app = Flask(__name__)

import dynamodb_handler as dynamodb


@app.route('/')
def root_route():
    dynamodb.CreatATableBook()
    return 'Hello World'


@app.route('/book', methods=['POST'])
def addABook():

    data = request.get_json()
   

    response = dynamodb.addItemToBook(data['id'], data['title'], data['author'])    
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Added successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    }


@app.route('/book/<int:id>', methods=['GET'])
def getBook(id):
    response = dynamodb.GetItemFromBook(id)
    
    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        
        if ('Item' in response):
            return { 'Item': response['Item'] }

        return { 'msg' : 'Item not found!' }

    return {
        'msg': 'Some error occured',
        'response': response
    }

@app.route('/book/<int:id>', methods=['DELETE'])
def DeleteABook(id):

    response = dynamodb.DeleteAnItemFromBook(id)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg': 'Deleted successfully',
        }

    return {  
        'msg': 'Some error occcured',
        'response': response
    } 


@app.route('/book/<int:id>', methods=['PUT'])
def UpdateABook(id):

    data = request.get_json()

 

    response = dynamodb.UpdateItemInBook(id, data)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'                : 'Updated successfully',
            'ModifiedAttributes' : response['Attributes'],
            'response'           : response['ResponseMetadata']
        }

    return {
        'msg'      : 'Some error occured',
        'response' : response
    }   


@app.route('/like/book/<int:id>', methods=['POST'])
def LikeBook(id):

    response = dynamodb.LikeABook(id)

    if (response['ResponseMetadata']['HTTPStatusCode'] == 200):
        return {
            'msg'      : 'Likes the book successfully',
            'Likes'    : response['Attributes']['likes'],
            'response' : response['ResponseMetadata']
        }

    return {
        'msg'      : 'Some error occured',
        'response' : response
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)