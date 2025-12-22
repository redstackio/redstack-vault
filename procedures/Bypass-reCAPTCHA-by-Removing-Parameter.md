---
id: b526eced-c8a4-486d-8540-322f1abf1d66
name: Bypass-reCAPTCHA-by-Removing-Parameter
type: procedure
verified: true
submitted: true
created_at: '2020-08-17T16:27:31.645257+00:00'
updated_at: '2023-05-26T18:40:44.268396+00:00'
platforms:
  - Web
tags:
  - '[[tags/Bypass]]'
  - '[[tags/Captcha]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
commands:
  - '[[commands/curl-submit-form-without-captcha]]'
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-reCAPTCHA-by-Removing-Parameter

## Summary

This procedure demonstrates how to bypass a simple reCAPTCHA implementation on a web registration form by intercepting the submission request and removing the CAPTCHA validation parameter. This exploits applications that fail to enforce server-side CAPTCHA verification, allowing automated submissions without solving the challenge.

## Description

reCAPTCHA is commonly used to prevent bot-driven attacks on web applications, such as bulk registrations or spam submissions. However, if the server does not properly validate the CAPTCHA token (e.g., the 'g-recaptcha-response' parameter), an attacker can bypass it by omitting the parameter entirely during form submission. This technique relies on client-side enforcement only and is effective against poorly implemented defenses. It is typically used in scenarios involving automated account creation, spam injection, or denial-of-service via form flooding. The target environment is a web application with a registration form protected by reCAPTCHA v2 ("I'm not a robot" checkbox).

## Requirements

1. Access to a web browser with proxy capabilities or direct API access to the target form endpoint.
2. [[tools/Burp-Suite]] installed and configured as a proxy, or equivalent interception tool.
3. Knowledge of the form's POST endpoint and required parameters (e.g., username, email, password).
4. Network access to the target web application without restrictions.

## Defense

Defensive measures and detection strategies:

- Implement server-side CAPTCHA validation using secret keys and token verification against Google's reCAPTCHA API.
- Log and monitor form submissions for missing or invalid CAPTCHA tokens, implementing rate limiting or IP blocking.
- Use additional bot detection layers, such as behavioral analysis (e.g., mouse movements) or device fingerprinting.
- Enable web application firewall (WAF) rules to detect anomalous submission patterns.

## Objectives

1. Intercept and modify the form submission request to remove CAPTCHA validation.
2. Successfully submit the form without completing the CAPTCHA challenge.
3. Validate that the bypass allows unauthorized automated interactions with the application.
4. Expected outcome: Successful form submission (e.g., account creation) without CAPTCHA solving.

## Instructions

### Step 1: Configure Proxy and Access the Form

**Context**: Set up interception to capture the form submission request. This ensures you can inspect and modify parameters before they reach the server.

Use [[tools/Burp-Suite]] to configure your browser proxy (typically at 127.0.0.1:8080). Navigate to the target registration page and fill in the form fields (e.g., username, email, password) without completing the CAPTCHA.

> No specific command is needed here, as this is a manual browser action. Ensure Burp's Proxy tab is intercepting requests.

### Step 2: Trigger Form Submission and Intercept Request

**Context**: Submit the form to generate the request containing the CAPTCHA parameter, which you will then remove.

Click the "I'm not a robot" checkbox (even if not solved) and submit the form. In Burp Suite, the request will be intercepted in the Proxy > Intercept tab. Observe the POST request body for the 'g-recaptcha-response' parameter.

> Expected: The intercepted request shows form data including 'g-recaptcha-response' (a long token string if checkbox was clicked).

### Step 3: Remove CAPTCHA Parameter and Forward Request

**Context**: Modify the request to bypass validation by deleting the CAPTCHA token, exploiting the lack of server-side checks.

In the intercepted request, delete the entire 'g-recaptcha-response=...' line from the body. Forward the modified request to the server.

As an alternative to manual interception, test the bypass directly using [[commands/curl-submit-form-without-captcha]] to send a POST request omitting the parameter:

```bash
curl-submit-form-without-captcha
```

> This step confirms the vulnerability by submitting without the token. Expected: HTTP 200 or redirect response indicating successful submission.

### Step 4: Verify Successful Bypass

**Context**: Confirm the form was processed without CAPTCHA validation, such as by checking for a success message or new account creation.

Observe the server's response and the application's behavior (e.g., confirmation email or dashboard access). If successful, the form submits without errors related to CAPTCHA.

> Expected: Application confirms registration or submission without prompting for CAPTCHA resolution.
