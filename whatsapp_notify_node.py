class WhatsAppNotifyNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "img": ("IMAGE",),
                "message": ("STRING", {"default": "✅ Workflow completed!"}),
            }
        }

    RETURN_TYPES = ("IMAGE",)
    FUNCTION = "notify"
    CATEGORY = "Notifications"

    def notify(self, img, message: str):
        print(f"[📲 WhatsAppNotifyNode] Message to send: {message}")
        return (img,)  # Pass image forward so node isn't "useless"
