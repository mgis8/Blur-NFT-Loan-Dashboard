from flask import Flask, request, render_template, redirect, url_for
from backendScraper import *

app = Flask(__name__)

# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('frontend.html')


global min_apy 
global max_ltv 
global max_eth 
global update_interval 
# Route to handle form submission
@app.route('/submit_form', methods=['post'])
def submit_form():
    global min_apy 
    global max_ltv 
    global max_eth 
    global update_interval
    if request.method == 'POST':
        # Retrieve form data
        min_apy = float(request.form.get('input1'))
        max_ltv = float(request.form.get('input2'))
        max_eth = float(request.form.get('input3'))
        update_interval = float(request.form.get('input4'))
       

        # Process the data (e.g., save to database, perform calculations, etc.)
        # Example: Print the values
        print(f'Min APY: {min_apy}, Max LTV: {max_ltv}, Max Eth: {max_eth}, Update Interval: {update_interval}')
        execute_loan_checker(min_apy, max_ltv, max_eth)
        # You can redirect or render another template here
        return redirect(url_for('index'))

    # Handle cases where method is not POST (optional)
    return 'Method Not Allowed', 405

if __name__ == '__main__':
    app.run(debug=True)
