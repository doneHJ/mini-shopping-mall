from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
#client = MongoClient('localhost', 27017)
client = MongoClient('mongodb://test:test@localhost', 27017)
db = client.dbsparta

## HTML을 주는 부분
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/order', methods=['POST'])
def s_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    phone_receive = request.form['phone_give']

    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'phone': phone_receive
    }
    db.orders.insert_one(doc)
    return jsonify({'result':'success','msg': '주문해 주셔서 감사합니다'})

@app.route('/order', methods=['GET'])
def view():
    orders = list(db.orders.find({},{'_id':False}))
    return jsonify({'result' : 'success', 'orders': orders})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
