---
id: proc-gratipay-email-intercept-001
tags:
  - input-validation
  - request-modification
  - web-exploit
type: procedure
tools:
  - '[[tools/Burp-Repeater]]'
  - '[[tools/Live-HTTP-Headers]]'
  - '[[tools/Tamper-Data]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:10.725Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-Email-Addition-Request

## Summary

This procedure exploits the lack of server-side input validation in Gratipay's email addition endpoint by intercepting a legitimate HTTP POST request, modifying the email parameter to an invalid or oversized value, and replaying it. It demonstrates how client-side checks can be circumvented, allowing storage of non-RFC compliant emails that may cause email delivery failures and bounce rate spikes when integrated services like Mandrill attempt to send notifications.

## Description

In the Gratipay web application, email addresses are managed via a POST request to /~username/emails/modify.json. Client-side JavaScript validates format and length before submission, but the server trusts the incoming 'address' parameter without re-validation. An attacker with an authenticated session can use proxy tools to tamper with requests, injecting invalid syntax (e.g., HTML tags) or exceeding the 255-character RFC limit. This leads to stored invalid data, potentially disrupting email workflows without granting unauthorized access. Prerequisites include a logged-in Gratipay account and a browser proxy setup. Expected outcomes: Invalid emails persist in user settings, verifiable by checking the account or monitoring bounce alerts from Mandrill.

## Requirements

1. Authenticated session in Gratipay (standard user account).
2. Browser with HTTP interception proxy enabled (e.g., Burp Suite at 127.0.0.1:8080).
3. Access to https://gratipay.com/~username/settings/ for the target account.

## Defense

Defensive measures and detection strategies:

- Implement server-side email validation using regex for format (RFC 5322) and length checks (<=255 chars).
- Use web application firewalls (WAF) to inspect and block anomalous POST parameters in /emails/modify.json.
- Monitor email service logs (e.g., Mandrill) for unusual bounce rates and correlate with user activity.
- Enable request logging to detect proxy-intercepted patterns like repeated submissions from the same IP.

## Objectives

1. Bypass client-side restrictions to store invalid email data on the server.
2. Validate the exploit by confirming persistence of malformed emails.
3. Assess impact through simulated email sends or bounce monitoring.

## Instructions

### Step 1: Setup Interception Tool

**Context**: Configure a tool like Burp Repeater to proxy traffic and capture requests from the Gratipay settings page.

No specific command; launch [[tools/Burp-Repeater]] and set browser proxy to intercept HTTPS traffic to gratipay.com.

> Ensure CA certificate is installed for HTTPS interception. Expected: All browser traffic routed through proxy.

### Step 2: Submit Valid Email for Capture

**Context**: Trigger a legitimate request to obtain a baseline for modification.

Enter 'mail01@gmail.com' in the email form at https://gratipay.com/~username/settings/ and submit. Intercept the POST to /~username/emails/modify.json with body 'action=add-email&address=mail01%40gmail.com'.

> The request should return 200 OK, adding the email. Drop the request if needed to avoid actual addition, or forward it first.

### Step 3: Modify and Replay for Invalid Email

**Context**: Tamper with the captured request to inject invalid data, exploiting the lack of server validation.

Edit the 'address' parameter to 'mymail%40gmail.com%22%3E%3Ch1%3E' (decoded: mymail@gmail.com"><h1>). Replay the POST request.

> Server accepts without error; refresh settings to see the invalid email stored. No client-side block since validation is bypassed.

### Step 4: Test Length Bypass

**Context**: Extend the procedure to violate size limits, confirming no length checks.

Modify 'address' to a 300+ character string, e.g., 'a' repeated 290 times + '@example.com', URL-encoded. Replay.

> Email saved intact; test by attempting to use it for notifications to trigger bounces.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Repeater]]
- [[tools/Live-HTTP-Headers]]
- [[tools/Tamper-Data]]

## Tags

- input-validation
- web-exploit
- email-bypass
