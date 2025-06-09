class WhatsAppNotifyNode:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "message": ("STRING", {"default": "✅ Workflow complete!"}),
            }
        }

    RETURN_TYPES = ()  # No outputs
    FUNCTION = "notify"
    CATEGORY = "Notifications"

    def notify(self, message: str):
        print(f"[📲 WhatsAppNotifyNode] Message to send: {message}")
        return ()
