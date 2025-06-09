# 🔔 ComfyUI Notification

A lightweight notification system for [ComfyUI](https://github.com/comfyanonymous/ComfyUI).  
Send alerts when a workflow completes — currently supports WhatsApp notifications via Twilio and Discord webhooks.

---

## ✅ Features

- 📲 **WhatsApp Notifications (Twilio Sandbox)**
- 💬 **Discord Channel Alerts (Webhook-based)**

---

## 📦 Usage

After installing, two new nodes will appear in the ComfyUI node menu under **Notifications**:

### 📲 WhatsApp (Twilio) & 💬 Discord Notify

These nodes are designed to **act as a bridge** between your image decoder and the final output step — such as `[Save Image]`.

For example:

```
[VAE Decode] → [💬 Discord Notify] → [Save Image]
[VAE Decode] → [📲 WhatsApp (Twilio)] → [Save Image]
```

---

### 💬 Discord Notify
Use this node to send a message to a Discord channel via webhook.

**Inputs:**
- `img`: connect it between `[VAE Decode]` and `[Save Image]`
- `message`: the text message to send
- `webhook_url`: Discord channel webhook URL

---

### 📲 WhatsApp (Twilio)
Use this node to send a WhatsApp message via Twilio's API.

**Inputs:**
- `img`: bridge image output to downstream nodes
- `message`: message text
- `sid`: Twilio Account SID
- `token`: Twilio Auth Token
- `from_number`: `whatsapp:+14155238886` (Twilio Sandbox)
- `to_number`: your WhatsApp number (must join sandbox)

---

## 🛠 Installation

Clone this repo into your ComfyUI `custom_nodes` folder:

```
git clone https://github.com/Waheed-Mousad/ComfyUI_Notification.git
```

If you're using WhatsApp (Twilio), install the required package:

```
pip install -r custom_nodes/ComfyUI_Notification/requirements.txt
```

---

## 🧪 Notes

This was my first custom node — built on the fly as a learning project.  
Apologies if parts seem unpolished. Feedback and improvements are welcome!

---

MIT Licensed – use freely, and improve it however you'd like.
