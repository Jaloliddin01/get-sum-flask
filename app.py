from flask import Flask, request

app = Flask(__name__)


@app.route('/api/get-sum/', methods=['GET'])
def get_sum():
    
    return { "sum" : sum(map(int, request.args.values())) }


if __name__ == "__main__":
    app.run(debug=True)