from flask import Flask, jsonify
from flask_cors import CORS
import os
from dotenv import load_dotenv
from bakong_khqr import KHQR
import qrcode
from io import BytesIO
import base64

app = Flask(__name__)
# Enable CORS for requests from localhost
CORS(app, resources={r"/api/*": {"origins": ["http://localhost:8000", "http://localhost:5000"], "methods": ["GET", "POST"]}})

# Load environment variables from the .env file
load_dotenv()

# Get the Bakong Developer Token from the environment
bakong_dev_token = os.getenv('BAKONG_DEV_TOKEN')

# Initialize KHQR with the developer token
khqr = KHQR(bakong_dev_token)

@app.route('/api/qr-code')
def qr_code():
    qr_data = khqr.create_qr(
        bank_account='name@trmc',
        merchant_name='Name',
        merchant_city='Phnom Penh',
        amount=4000,
        currency='KHR',
        store_label='Gavin Shop',
        phone_number='855123456789',
        bill_number='TRX019283775',
        terminal_label='Cashier-01',
        static=False
    )
    
    qr_img = qrcode.make(qr_data)
    buffered = BytesIO()
    qr_img.save(buffered, format="PNG")
    buffered.seek(0)

    qr_code_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    return jsonify({'image': qr_code_base64})

if __name__ == '__main__':
    app.run(debug=True)
