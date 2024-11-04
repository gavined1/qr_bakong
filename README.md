# Bakong QR Code Generator

This is a simple Flask application that generates QR codes for Bakong payments. It provides an API endpoint to fetch QR codes based on specific transaction data.

## Features

- Generates QR codes using the Bakong KHQR library.
- Provides a RESTful API to access generated QR codes.
- Supports Cross-Origin Resource Sharing (CORS) for frontend applications.

## Technologies Used

- Python 3.x
- Flask
- Flask-CORS
- qrcode
- dotenv for environment variable management
- bakong-khqr library for QR code generation

## Installation

### Prerequisites

- Python 3.6 or higher
- pip

### Clone the Repository

```bash
git clone https://github.com/your-username/bakong-qr-code-generator.git
cd bakong-qr-code-generator
```
### Set up a Virtual Environment

- Create a virtual environment:

This step will create an isolated environment for your project dependencies.
```bash
python -m venv .venv
```

- Activate the virtual environment:

On Windows:
```bash
.venv\Scripts\activate
```

On macOS/Linux:
```bash
source .venv/bin/activate
```

Once activated, your command prompt will change to indicate that you're now working inside the virtual environment.

### Install Dependencies
After activating your virtual environment, install the required packages:

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a .env file in the root directory of the project and add the following variable:
```
BAKONG_DEV_TOKEN=your_bakong_developer_token_here
```

### Run Your Flask Application: 
You can start your Flask application by using one of the following methods:

- Using the Flask CLI:

If you have set the FLASK_APP environment variable to point to your application file (for example, app.py), you can run:
```bash
flask run
```
If you haven't set it, you can do so by running:

On Windows:
```bash
set FLASK_APP=app.py
```
On macOS/Linux:
```bash
export FLASK_APP=app.py
```

- Running the Script Directly:

If you prefer or if your script has a main block, you can run it directly with Python:
```bash
python app.py
```

### Serve Your Frontend Files

Open another terminal window in a different directory (where your index.html is located).
Run the HTTP server on a different port (like 8000):

```bash
python -m http.server 8000
```

### Access Your Application
Open your web browser and navigate to:
```bash
http://localhost:8000/index.html
```




