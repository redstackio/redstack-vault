---
type: procedure
description: >-
  Conduct a CSRF attack by hosting a malicious page and using a semicolon in the
  Referer header to bypass naive validation checks on the target website.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - >-
    [[techniques/Phishing Spearphishing Attachment|T1566.001 - Phishing:
    Spearphishing Attachment]]
sub_techniques: []
tags:
  - csrf
  - cross-site-request-forgery
  - referer-bypass
  - semicolon-payload
commands:
  - '[[commands/host-csrf-page-with-python]]'
  - '[[commands/curl-csrf-request-with-semicolon-referer]]'
platforms:
  - Web
tools: []
validated: true
---

# Perform CSRF Attack with Semicolon Referer Bypass

## Summary

This procedure outlines how to execute a Cross-Site Request Forgery (CSRF) attack against a web application that fails to properly validate the Referer header. By crafting a malicious HTML page that auto-submits a form to the target site and using a semicolon (;) in the Referer header (e.g., 'https://attacker.com/page;https://trusted.domain.com'), the attack bypasses simplistic checks that look for the presence of the trusted domain in the Referer string. This allows unauthorized actions, such as changing user settings, while the victim is authenticated to the target site.

## Description

CSRF attacks exploit the trust a site has in a user's browser by tricking the browser into sending authenticated requests to the target without user consent. In this variant, the target application performs inadequate Referer header validation—such as checking if the Referer contains the trusted domain substring—allowing the attacker to append ';https://trusted.domain.com' to their own URL in the Referer. This fools the validation while the actual origin remains the attacker's domain. The attack requires the victim to visit the attacker's hosted page while logged into the target site, typically via phishing. It targets web applications vulnerable to CSRF without tokens or with weak anti-CSRF measures. Success leads to actions like account takeover or data modification on the victim's behalf.

## Requirements

1. Control over a web server or domain (e.g., attacker.com) to host the malicious HTML page.
2. Knowledge of the target site's vulnerable endpoint (e.g., a POST action like /change-email without CSRF protection).
3. Victim must be authenticated to the target site (e.g., via an active session cookie).
4. Ability to deliver the malicious link to the victim (e.g., via email or social engineering).
5. Tools like Python for hosting and curl for testing the Referer bypass.

## Defense

- Implement CSRF tokens in all state-changing forms and validate them server-side.
- Enforce strict Referer header checks (e.g., exact match or same-origin policy) rather than substring presence.
- Use Content Security Policy (CSP) with 'referrer' directive to control Referer exposure.
- Educate users on phishing risks and enable browser protections like SameSite cookies.
- Monitor for anomalous requests from unexpected Referers.

## Objectives

1. Trick the victim into visiting the attacker's malicious page while authenticated to the target.
2. Forge a state-changing request (e.g., update user data) using the victim's session.
3. Bypass Referer validation to ensure the request is accepted by the target server.

## Instructions

### Step 1: Create and Host the Malicious CSRF Page

**Context**: Develop an HTML page that automatically submits a form to the target's vulnerable endpoint. This page will be hosted on your controlled domain. Use the provided code snippet to generate the page, customizing the form action and fields to match the target's endpoint (e.g., changing email or password).

**Code** ([[codes/csrf-auto-submit-html]]):

Embed the code here or save it as csrf.html on your server.

Host the page using a simple HTTP server.

**Command** ([[commands/host-csrf-page-with-python]]):
```bash
python3 -m http.server $_PORT --directory $_HOST_DIR
```

> This starts a local HTTP server to serve the CSRF HTML. Replace $_PORT with 80 (or 8080 if port 80 requires sudo) and $_HOST_DIR with the directory containing csrf.html. Access the page at http://attacker.com:$_PORT/csrf.html. Expected: Server logs show 'Serving HTTP on ...' and the page is accessible via browser.

### Step 2: Test the Semicolon Referer Bypass

**Context**: Before sending to the victim, verify the bypass works by simulating the request with curl. Craft the Referer header to include your domain followed by ';https://trusted.domain.com'. This exploits substring-based validation. Identify the exact POST data (e.g., from Burp or browser dev tools) needed for the action.

**Command** ([[commands/curl-csrf-request-with-semicolon-referer]]):
```bash
curl -X POST -H "Referer: $_ATTACKER_URL;$_TRUSTED_URL" -H "Cookie: $_VICTIM_COOKIE" -d "$_POST_DATA" $_TARGET_URL
```

> Simulate the CSRF POST from the victim's perspective. Replace $_ATTACKER_URL with 'https://attacker.com/csrf.html', $_TRUSTED_URL with 'https://trusted.domain.com', $_VICTIM_COOKIE with the target's session cookie (obtained via prior access or testing), $_POST_DATA with form parameters (e.g., 'new_email=attacker@evil.com'), and $_TARGET_URL with the vulnerable endpoint (e.g., 'https://trusted.domain.com/change-email'). Expected: Server responds with success (e.g., 200 OK or redirect) without Referer validation errors, confirming the action (e.g., email changed in user profile).

### Step 3: Deliver the Attack to the Victim

**Context**: Send the link to the hosted CSRF page via phishing (e.g., email attachment or link). When the victim clicks it while logged into the target, the auto-submit triggers the forged request with the crafted Referer (set by the browser to the attacker's URL). If the site uses substring validation, the ;trick bypasses it.

No specific command needed; use email tools or social engineering. Monitor the target for changes or use a callback in the HTML to confirm execution (e.g., img src to attacker logger).

**Expected Output**: Victim's browser loads the page invisibly (due to auto-submit), performs the POST, and the target processes the unauthorized action.

### Step 4: Verify Success

**Context**: Check the target's site (if accessible) or use notifications to confirm the action (e.g., new email received). If testing on a lab, inspect server logs for the request with the manipulated Referer.
