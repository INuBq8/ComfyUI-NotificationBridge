from .notify_whatsapp_twilio import WhatsAppNotifyNodeTwilio
from .notify_discord import DiscordNotifyNode

NODE_CLASS_MAPPINGS = {
    "WhatsAppNotifyNodeTwilio": WhatsAppNotifyNodeTwilio,
    "DiscordNotifyNode": DiscordNotifyNode,

}

NODE_DISPLAY_NAME_MAPPINGS = {
    "WhatsAppNotifyNodeTwilio": "📲 WhatsApp (Twilio)",
    "DiscordNotifyNode": "💬 Discord Notify",

}