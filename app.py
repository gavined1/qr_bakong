from flask import Flask, jsonify, send_from_directory
from flask_cors import CORS
import os
from dotenv import load_dotenv
from bakong_khqr import KHQR
import qrcode
from io import BytesIO
import base64

app = Flask(__name__, static_folder='.')  # Set static folder to the root
CORS(app, resources={r"/api/qr-code*": {"origins": ["https://spiffy-selkie-449161.netlify.app"], "methods": ["GET", "POST"]}})


# Load environment variables from the .env file
load_dotenv()

# Get the Bakong Developer Token from the environment
bakong_dev_token = os.getenv('BAKONG_DEV_TOKEN')

# Initialize KHQR with the developer token
khqr = KHQR(bakong_dev_token)

@app.route('/api/qr-code')
def qr_code():
    qr_data = khqr.create_qr(
        bank_account='tang_soklim1@trmc',
        merchant_name='Tang Soklim',
        merchant_city='Phnom Penh',
        amount=4000,
        currency='KHR',
        store_label='Gavin Shop',
        phone_number='85586873125',
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

@app.route('/')
def serve_index():
    return send_from_directory('.', 'index.html')  # Serve the HTML file

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
