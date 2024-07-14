# Gmail Mails Access

This project provides a Python script to access and read unread emails from a Gmail account using the Gmail API.

## Features

- Authenticates with Gmail API using OAuth 2.0
- Retrieves unread messages from the inbox
- Displays the total number of unread messages
- Saves the unread messages data to a JSON file
- Prints message IDs and subjects of unread emails

## Prerequisites

- Python 3.x
- Google Cloud Project with Gmail API enabled
- OAuth 2.0 Client ID credentials

## Setup

1. Clone this repository
2. Install required packages:
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client
3. Place your `credentials.json` file in the project root directory

## Usage

Run the script using:
python readGmail.py

On first run, you'll be prompted to authorize the application. Follow the instructions in your browser to complete the OAuth flow.

## Output

- Displays the total number of unread messages in the console
- Saves unread messages data to `email_message.txt` in JSON format
- Prints message IDs and subjects of unread emails in the console

## Note

This script uses readonly access to your Gmail account. If you modify the SCOPES, remember to delete the `token.json` file to re-authenticate.

## License

[Add your chosen license here]
