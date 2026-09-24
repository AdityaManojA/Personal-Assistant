from google_auth_oauthlib.flow import InstalledAppFlow

# Full access scope (adjust if you only need read or send permissions)
SCOPES = ['https://mail.google.com/']

flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
creds = flow.run_local_server(port=0)

# Save credentials (including refresh_token) to token.json
with open('token.json', 'w') as token_file:
    token_file.write(creds.to_json())

print("Refresh token saved successfully in token.json!")