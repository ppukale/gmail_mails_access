import os.path
import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]


def main():
  """Shows basic usage of the Gmail API.
  Lists the user's Gmail labels.
  """
  creds = None
  # The file token.json stores the user's access and refresh tokens, and is
  # created automatically when the authorization flow completes for the first
  # time.
  if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
  # If there are no (valid) credentials available, let the user log in.
  if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
      creds.refresh(Request())
    else:
      flow = InstalledAppFlow.from_client_secrets_file(
          "credentials.json", SCOPES
      )
      creds = flow.run_local_server(port=0)
    # Save the credentials for the next run
    with open("token.json", "w") as token:
      token.write(creds.to_json())

#   try:
#     # Call the Gmail API
#     user_id =  'me'
#     label_id_one = 'INBOX'
#     label_id_two = 'UNREAD'
#     service = build("gmail", "v1", credentials=creds)


#     results = service.users().labels().list(userId="me").execute()
#     labels = results.get("labels", [])

#     if not labels:
#       print("No labels found.")
#       return
#     print("Labels:")
#     for label in labels:
#       print(label["name"])

#   except HttpError as error:
    # T(developer) - Handle errors from gmail API.
    
    try:
      user_id =  'me'
      label_id_one = 'INBOX'
      label_id_two = 'UNREAD'
      service = build("gmail", "v1", credentials=creds)
      unread_msg = service.users().messages().list(userId=user_id,labelIds=[label_id_one,label_id_two]).execute()
      msg_list = unread_msg.get('messages',[])
      print("Total Unread messages", str(len(msg_list)))

        # Convert the message to a formatted JSON string
      message_str = json.dumps(unread_msg, indent=4)

      # Define the file path
      file_path = 'email_message.txt'

      # Write the message to a text file
      with open(file_path, 'w') as file:
          file.write(message_str)


      for msg in msg_list:
        msg_id = msg['id']
        print(msg_id)
        msg_data = service.users().messages().get(userId=user_id,id=msg_id).execute()
        payload = msg_data['payload']
        headers = payload['headers']
        body = payload['body']
        parts = body['parts']
        for header in headers:
          if header['name'] == 'Subject':
            subject = header['value']
            print(subject)
        print(msg_data)
        print("----------------------------------")


    except Exception as error:
      print(f"An error occurred: {error}")


if __name__ == "__main__":
  main()