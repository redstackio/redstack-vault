---
id: proc-uuid-123
tags:
  - xss
  - stored-xss
  - meta-injection
  - web-exploit
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.543Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-Malicious-META-Tags-for-Stored-XSS-in-VK-Messages

## Summary

This procedure exploits a stored XSS vulnerability in VK.com's personal messages by injecting malicious JavaScript into META tags on a controlled webpage. When the URL is shared in a message, VK.com's preview generation pulls and executes the unsanitized META content in the victim's browser, enabling session hijacking or data theft.

## Description

The vulnerability stems from VK.com's instant messenger service failing to filter data from META tags when creating site previews for linked URLs in messages. An attacker crafts a webpage with a META tag containing executable JavaScript (e.g., via the 'content' attribute). Upon sending the link in a private message, the preview renders the META data without escaping, storing and executing the script when the recipient views the message. This was reported on HackerOne (Report #181823) on November 12, 2016, with medium severity due to its potential for client-side attacks like cookie theft in the victim's session.

## Requirements

1. Access to a VK.com account for sending messages
2. Control over a web server or hosting service to host the malicious webpage
3. A target victim who will receive and view the message
4. Basic knowledge of HTML and JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all third-party content like META tags in previews
- Use Content Security Policy (CSP) to restrict script execution from untrusted sources
- Monitor for anomalous JavaScript execution in browser logs or via web application firewall (WAF) rules targeting META tag payloads
- Educate users on avoiding suspicious links in messages

## Objectives

1. Inject and store malicious JavaScript via META tags in message previews
2. Execute the script in the victim's browser context for data exfiltration
3. Achieve session hijacking or other client-side impacts

## Instructions

### Step 1: Craft the Malicious Webpage

**Context**: Create an HTML file hosted on a server you control, embedding JavaScript in a META tag's content attribute to bypass filtering.

No specific command; use a text editor to create `malicious.html`:

```html
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="refresh" content="0; url='javascript:alert(document.cookie)'">
    <!-- Or more stealthy: <meta name="description" content="'; alert(document.cookie);//"> -->
</head>
<body>
    <h1>Preview Bait</h1>
</body>
</html>
```

> This embeds JavaScript that executes on page load or via refresh. Host this file on a public server (e.g., GitHub Pages or a VPS) to obtain a URL like `https://attacker.com/malicious.html`. Expected output: A publicly accessible webpage.

### Step 2: Send the Malicious Link in a VK.com Message

**Context**: Log into VK.com, navigate to personal messages, and send the URL to the victim to trigger preview generation.

No specific command; use the VK.com web interface:

1. Go to `https://vk.com/im`
2. Select or create a conversation with the victim
3. Paste the malicious URL into the message and send

> VK.com will fetch the page to generate a preview, pulling the META tags and storing the unsanitized content. Expected output: Message sent with a preview snippet containing the injected script.

### Step 3: Verify Execution on Victim Side

**Context**: Have the victim (or test account) view the message to confirm script execution.

No specific command; instruct the victim to open the messages page.

> When the victim loads `https://vk.com/im`, the preview renders, executing the JavaScript (e.g., alerting cookies). Expected output: Script runs in victim's browser, demonstrating XSS success.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[web]]
- [[session-hijacking]]
