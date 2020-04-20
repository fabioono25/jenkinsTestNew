from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/customers")

def get_customers():
    customers = list_customers()    
    return jsonify(customers)

def list_customers():
    return [{ 'name': 'John', 'surname': 'Nash' }, 
            { 'name': 'Steve', 'surname': 'Wozniak' }]

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=80)