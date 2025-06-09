from twilio.rest import Client

class WhatsAppNotifyNodeTwilio:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "img": ("IMAGE",),
                "message": ("STRING", {"default": "✅ Workflow completed!"}),
                "sid": ("STRING", {"default": "Your Twilio SID here"}),
                "token": ("STRING", {"default": "Your Twilio Auth Token"}),
                "from_number": ("STRING", {"default": "whatsapp:+14155238886"}),  # Twilio Sandbox
                "to_number": ("STRING", {"default": "whatsapp:+YOUR_PHONE_NUMBER"}),  # Your verified number
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "notify"
    CATEGORY = "Notifications"

    def notify(self, img, message, sid, token, from_number, to_number):
        try:
            # Basic validation
            required_fields = [sid, token, from_number, to_number]
            if any(v.strip() == "" or "Twilio" in v for v in required_fields):
                raise ValueError("One or more required fields are missing or still set to default.")

            client = Client(sid.strip(), token.strip())
            sent = client.messages.create(
                from_=from_number.strip(),
                body=message.strip(),
                to=to_number.strip()
            )
            print(f"[📲 WhatsAppNotifyNodeTwilio] ✅ WhatsApp message sent. SID: {sent.sid}")

        except Exception as e:
            print("❌ WhatsAppNotifyNodeTwilio Error: ", str(e).split('\n')[0])

        return (img,)

