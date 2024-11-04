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
git clone https://github.com/gavined1/qr_bakong.git
cd qr_bakong
