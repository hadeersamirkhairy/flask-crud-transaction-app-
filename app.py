# Import libraries
from flask import Flask , request , url_for , redirect , render_template
# Instantiate Flask functionality
app = Flask(__name__)

# Sample data
# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions=transactions)

# Create operation
@app.route('/add' , methods= ['GET','POST'])
def add_transaction():
    if request.method == 'GET':
        return render_template("form.html")
    elif request.method =='POST':
        date_new = request.form['date']
        amount_new = float(request.form['amount'])
        transaction = {
            "id" : len(transactions)+1,
            "date" : date_new,
            "amount" : amount_new
        }
        transactions.append(transaction)
        return redirect(url_for('get_transactions'))

# Update operation
@app.route('/edit/<int:transaction_id>' , methods    = ['GET','POST'])
def edit_transaction(transaction_id):
    found_transaction = None
    for transaction in transactions :
        if transaction['id'] == transaction_id:
            found_transaction = transaction
            break
    if found_transaction is None :
        return {"message":"Transaction not found"},404
    if request.method == 'GET':
        return render_template("edit.html" , transaction = found_transaction)
    elif request.method == 'POST':
        date_new = request.form['date']
        amount_new = float(request.form['amount'])
        found_transaction['date'] = date_new
        found_transaction['amount'] = amount_new
        return redirect(url_for('get_transactions'))
# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    found_transaction = None
    for transaction in transactions :
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
    return redirect(url_for('get_transactions'))


# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)