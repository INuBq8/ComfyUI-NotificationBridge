import requests

class DiscordNotifyNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "img": ("IMAGE",),
                "message": ("STRING", {"default": "✅ Workflow complete!"}),
                "webhook_url": ("STRING", {"default": "https://discord.com/api/webhooks/..."}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "notify"
    CATEGORY = "Notifications"

    def notify(self, img, message, webhook_url):
        try:
            payload = {"content": message.strip()}
            response = requests.post(webhook_url.strip(), json=payload)

            if response.status_code == 204:
                print("[💬 DiscordNotifyNode] ✅ Message sent to Discord.")
            else:
                print(f"❌ DiscordNotifyNode Error: HTTP {response.status_code} - {response.text}")
        except Exception as e:
            print("❌ DiscordNotifyNode Exception:", e)

        return (img,)
