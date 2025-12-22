---
id: f6926594-a03a-4a94-be07-50580306e5fc
name: Password-Reset-Poisoning
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T17:26:11.571283+00:00'
updated_at: '2023-05-26T01:22:47.090957+00:00'
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Modify Authentication Process]]'
sub_techniques: []
tags:
  - broken authentication
  - Web Applications
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# Password-Reset-Poisoning

## Summary

Password reset poisoning is a technique that exploits misconfigurations in web application password reset mechanisms, particularly when the application trusts headers like X-Forwarded-Host to construct reset links. By intercepting and modifying the reset request, an attacker can redirect the reset link to a controlled server, allowing them to hijack the process and change the victim's password without direct access to their email or credentials.

## Description

In typical password reset flows, applications send a unique link to the user's email for password changes. If the application uses client-supplied headers (e.g., X-Forwarded-Host) to build the reset URL without proper validation, an attacker can poison this by altering the header to point to their own server. This enables the attacker to capture the reset token and complete the password change for the target account. This procedure assumes access to a legitimate user account on the target application and uses a proxy tool to intercept traffic. It is commonly seen in web applications with reverse proxies or load balancers that forward headers insecurely. Success grants the attacker control over the victim's account, potentially leading to full compromise.

## Requirements

1. Valid credentials for a non-privileged account on the target web application.
2. Access to the victim's username (e.g., 'carlos').
3. Burp Suite or similar proxy tool configured to intercept HTTP traffic from the browser.
4. Control over an exploit server or attacker-controlled domain to host the poisoned reset page.
5. Network access to the target application and email service for observing reset links.

## Defense

Defensive measures and detection strategies:

- Validate and sanitize all headers used in URL construction, ignoring X-Forwarded-* unless from trusted proxies.
- Use absolute URLs with hardcoded domains for reset links instead of relying on request headers.
- Implement rate limiting on password reset requests per IP or account.
- Monitor for anomalous reset link domains in email logs or application access logs.
- Enable web application firewall (WAF) rules to block suspicious header manipulations.

## Objectives

1. Intercept and modify the password reset request to poison the link destination.
2. Redirect the reset process to an attacker-controlled server.
3. Complete the password change for the victim's account using the captured token.
4. Gain unauthorized access to the victim's account.

## Instructions

### Step 1: Initiate Password Reset for Attacker Account

**Context**: Log in to the target application and trigger the password reset functionality to observe the request flow and confirm email delivery. This establishes the baseline for the poisoning attack.

Configure your browser to proxy traffic through Burp Suite. Log in using your valid credentials, navigate to the account or profile page, and locate the password reset option. Enter your own username and submit the reset request.

Observe the application response and check your email for the reset link to confirm the flow works as expected.

### Step 2: Intercept the Password Reset Request

**Context**: Use the proxy to capture the HTTP request sent during the reset initiation, allowing inspection of headers and parameters for manipulation opportunities.

In Burp Suite's Proxy history, identify the POST request to the forgot-password endpoint (typically something like /forgot-password or /reset). Right-click the request and send it to the Repeater tab for modification.

Examine the request body for the username parameter and headers for forwardable fields like X-Forwarded-Host.

### Step 3: Modify Request for Poisoning

**Context**: Alter the X-Forwarded-Host header to point to your controlled exploit server and change the username to the victim's to poison the reset link specifically for their account.

In Burp Repeater, add or modify the X-Forwarded-Host header to your exploit server's domain (e.g., X-Forwarded-Host: your-exploit-server.com). Update the username parameter in the request body to the victim's username (e.g., carlos). Forward the modified request to the server.

This causes the application to generate a reset link pointing to your server instead of the legitimate domain.

### Step 4: Access and Load the Poisoned Reset Link

**Context**: Retrieve the poisoned reset link from the victim's email (or simulate access in a lab) and load it via your exploit server to capture the token and complete the reset.

Check the victim's email for the new reset link, which should now reference your exploit server. Copy the full URL and load it in your browser (with Burp proxy active to intercept if needed).

The link should direct to a page on your server mimicking the password reset form, where the reset token is embedded in the URL or parameters.

### Step 5: Complete Password Change

**Context**: Use the poisoned link to submit a new password for the victim's account, verifying successful takeover.

On your exploit server's reset page, enter a new password of your choice and submit the form. This sends the reset token and new credentials back to the original application, changing the victim's password.

Attempt to log in to the victim's account with the new password to confirm access.

## Expected Output

- Successful interception shows the modified request accepted without errors (HTTP 200 or redirect to reset initiation).
- Victim's email contains a reset link with your domain (e.g., https://your-exploit-server.com/reset?token=abc123).
- Submitting the new password results in a success message from the application, and login with the new credentials works.

Success is confirmed when the victim's account password is changed and accessible to the attacker.
