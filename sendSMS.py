from twilio.rest import Client

import os

account_id=os.getenv("TWILIO_ACCOUNT_SID")
auth_token=os.getenv("TWILIO_AUTH_TOKEN")
twilio_number=+183040
recipient_number=+917411

client = Client(account_id, auth_token)

message = client.messages.create(
    body='Your trial account time is ended, the amount of $15 will be debited from your bank account in 2 days to upgrade your twilio account,\n Thank You',
    from_=twilio_number,
    to=recipient_number
    )

print(f"Message sent successfully, msg id: {message}")