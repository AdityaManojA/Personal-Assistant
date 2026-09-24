from google_auth_oauthlib.flow import InstalledAppFlow

flow = InstalledAppFlow.from_client_secrets_file(
    "credentials.json",  # Your existing OAuth credentials
    ["https://www.googleapis.com/auth/gmail.modify"]  # Adjust scope as needed
  )
credentials = flow.run_local_server(port=0)

print("\n=== COPY THIS REFRESH TOKEN ===")
print(credentials.refresh_token)
print("\nAdd to voice-assistant/config.yaml:")
print(f"  GMAIL_REFRESH_TOKEN: \"{credentials.refresh_token}\"")