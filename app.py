from flask import Flask, request, render_template, jsonify
from backendScraper import *
import threading
from flask_sqlalchemy import SQLAlchemy


#formatting for apy and ltv values
def removePRCNT(string):
    return float(string.replace("%", ""))

#set up for flask and SQL
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#setting nft class for database storage
class NFT(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nft_name = db.Column(db.Text)  
    nft_eth = db.Column(db.Text)
    nft_ltv = db.Column(db.Text)
    nft_apy = db.Column(db.Text)

    def __repr__(self):
        return f'<NFT {self.id}>'

with app.app_context():
    db.create_all()


# Route to serve the HTML form
@app.route('/')
def index():
    return render_template('index.html')


global min_apy 
global max_ltv 
global max_eth 
# Route to handle form submission
@app.route('/submit_form', methods=['GET'])
def submit_form():
    global min_apy 
    global max_ltv 
    global max_eth 
    
    #extracting inputted values from frontend
    min_apy = float(request.args.get('input1'))
    max_ltv = float(request.args.get('input2'))
    max_eth = float(request.args.get('input3'))
   
        

    #print statement for testing
    #print(f'Min APY: {min_apy}, Max LTV: {max_ltv}, Max Eth: {max_eth}')
        
    # Query NFT data from the database
    nfts = NFT.query.all()
    #filtering data to return to frontend based on user specified apy, ltv, and eth amount
    filtered_nfts = [{'id': nft.id, 'name': nft.nft_name, 'eth': nft.nft_eth, 'ltv': nft.nft_ltv, 'apy': nft.nft_apy} for nft in nfts if removePRCNT(nft.nft_apy) >= min_apy and removePRCNT(nft.nft_ltv) <= max_ltv and removePRCNT(nft.nft_eth) <= max_eth]

    # Return filtered data as JSON
    return jsonify({'nft_data': filtered_nfts})
        


#FOR TESTING
def print_database_data():
    with app.app_context():
        all_nfts = NFT.query.all()
        
        # Iterate through the results and print the data
        for nft in all_nfts:
            print(f'ID: {nft.id}')
            print(f'Name: {nft.nft_name}')
            print(f'ETH Asked: {nft.nft_eth}')
            print(f'LTV: {nft.nft_ltv}')
            print(f'APY: {nft.nft_apy}')
            print('-----')


def database_loop():
    global nftData
    while True:
        
        execute_loan_checker(0, 9999, 9999) #default values for this function to gather all open auction loans
         # Insert the serialized data into the database
        # Insert the new data
        with app.app_context():
            db.session.query(NFT).delete() # deleting previous data from database 
            db.session.commit()
            for nft in nftData:
                new_nft = NFT(
                    nft_name=nft[0],
                    nft_eth=nft[1],
                    nft_ltv=nft[2],
                    nft_apy=nft[3]
                )
                db.session.add(new_nft) # adding updated data to database
            db.session.commit()
        #print_database_data() #For testing database
        time.sleep(300) # updating loan data to database every 5min


if __name__ == '__main__':
    # Start app in seperate thread
    flask_thread = threading.Thread(target=app.run)
    flask_thread.start()

    # Start database loop in a separate thread
    loop_thread = threading.Thread(target=database_loop)
    loop_thread.daemon = True  # Make the thread a daemon thread (optional)
    loop_thread.start()

    


