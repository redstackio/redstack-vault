---
id: 035d9802-2fe6-4939-8c31-b823f91e7a4c
name: HTML-POST-CSRF-Attack
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.410589+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - >-
    [[techniques/Exploitation of Remote Services|T1210 - Exploitation of Remote
    Services]]
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - '[[tags/Cross-Site Request Forgery]]'
  - '[[tags/HTML POST - Requiring User Interaction]]'
  - '[[tags/Payloads]]'
  - csrf
  - web-attack
  - social-engineering
commands: []
platforms:
  - Web
tools: []
validated: true
---

# HTML-POST-CSRF-Attack

## Summary

The HTML POST CSRF attack tricks a victim into submitting a malicious HTML form that performs unauthorized actions on a target website using the victim's active session. This procedure outlines creating and delivering such a form to execute actions like changing user settings or initiating transactions without the victim's awareness.

## Description

Cross-Site Request Forgery (CSRF) exploits the trust a website has in a user's browser by leveraging the user's authenticated session. In this HTML POST variant, the attacker crafts a form that mimics a legitimate one and hosts it on a controlled site or embeds it in phishing content. When the victim interacts with it (e.g., clicks submit), the browser sends a POST request to the target site's endpoint, forging the action as if initiated by the victim. This requires user interaction but can be disguised effectively via social engineering, such as in spearphishing emails or malicious links. The attack targets sites lacking CSRF protections like tokens or SameSite cookies, potentially leading to account compromise, data alteration, or financial loss. It is effective against web applications where POST requests modify state without additional verification.

## Requirements

1. Access to a web server or hosting service to serve the malicious HTML form (e.g., attacker-controlled domain).
2. Knowledge of the target website's API endpoint and required form parameters (e.g., via reconnaissance or prior testing).
3. Victim must have an active, authenticated session with the target website (e.g., logged in via browser).
4. Basic HTML knowledge to customize the form payload.

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens in all state-changing forms to validate request origin.
- Enforce SameSite=Strict or SameSite=Lax cookies to block cross-site requests.
- Require multi-factor authentication (MFA) for sensitive actions to add an extra verification layer.
- Monitor for anomalous POST requests from unusual referers or user agents.
- Educate users on phishing risks and verifying links before interaction.

## Objectives

1. Perform unauthorized state-changing actions (e.g., update user profile, transfer funds) on the target website using the victim's session.
2. Demonstrate session hijacking without direct credential theft.
3. Exfiltrate session-based access to sensitive functions or data.

## Instructions

### Step 1: Reconnaissance of Target Endpoint

**Context**: Identify the target website's POST endpoint and required parameters to ensure the form submits correctly. This step involves inspecting the legitimate form via browser developer tools or proxy interception to replicate the structure.

Use browser tools or a proxy to capture a legitimate POST request. Note the action URL, method (POST), and fields like 'username'.

> No specific command is needed here; perform manual inspection. Expected: Full endpoint details, e.g., 'http://www.example.com/api/setusername' with fields {'username': 'value'}.

### Step 2: Create Malicious HTML Form

**Context**: Build the HTML form using the identified endpoint and parameters. Embed hidden fields with attacker-desired values to forge the action.

Reference the payload code [[codes/HTML-POST-CSRF-Form]] and customize it with the target URL and malicious values.

> Save the HTML to a file (e.g., csrf.html) and host it. Expected: A functional form that, when submitted, sends the POST to the target.

### Step 3: Host and Deliver the Form

**Context**: Serve the HTML on an attacker-controlled site and lure the victim to interact with it, ensuring their browser is authenticated to the target.

Upload the HTML to a web server (e.g., Apache, Nginx, or free hosting). Send the link via email, social media, or embed in a phishing page disguised as a legitimate update or survey.

> Example delivery: Email with "Click here to update your profile: http://attacker.com/csrf.html". Expected: Victim visits and submits the form, triggering the forged request.

### Step 4: Verify Attack Success

**Context**: Monitor the target site or victim's account for changes to confirm the action executed using the victim's session.

Check the target's API logs (if accessible) or observe account modifications (e.g., username changed to 'CSRFd'). If possible, use a proxy to intercept the submitted request.

> Expected: Confirmation of action, such as updated user data on the target site.
