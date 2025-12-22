---
id: e503ca4f-bb8c-425b-be1e-187b160a3c3d
name: Perform-CSRF-Attack-via-File-Upload
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:56.191107+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - file-upload
  - web-attack
  - user-interaction
  - payloads
commands: []
platforms:
  - Web
tools: []
validated: true
---

# Perform-CSRF-Attack-via-File-Upload

## Summary

This procedure demonstrates how to execute a Cross-Site Request Forgery (CSRF) attack by tricking an authenticated victim into uploading a malicious file via a hidden HTML form. The attack leverages user interaction to submit unauthorized requests to a vulnerable web application, allowing the attacker to perform actions on the victim's behalf, such as data modification or privilege escalation.

## Description

Cross-Site Request Forgery (CSRF) exploits the trust a web application has in a user's browser by inducing the victim to perform unintended actions. In this variant, the attack uses a file upload mechanism to embed and submit malicious payloads. The victim, already authenticated to the target site, is social-engineered into clicking a button on a malicious page, which programmatically populates and submits a form with dummy file content. This submits a POST request with multipart/form-data, mimicking a legitimate file upload but executing attacker-controlled actions. The procedure assumes the attacker knows the target's endpoint and the victim's session is active. It targets web applications lacking CSRF tokens or proper validation on file uploads. Success relies on the victim being logged in and the application processing the forged request without additional checks.

## Requirements

1. The target web application must be vulnerable to CSRF, lacking anti-CSRF tokens or same-origin policy enforcement on file uploads.
2. Knowledge of the victim's active session cookie and the exact URL endpoint for the file upload form (e.g., /upload).
3. Ability to host or deliver the malicious HTML page to the victim (e.g., via phishing email or malicious website).
4. The victim must be authenticated to the target application during the interaction.
5. Basic web development knowledge to customize the payload for the specific target form fields.

## Defense

Defensive measures and detection strategies:

- Implement and enforce anti-CSRF tokens in all forms to validate request origin and intent.
- Use Content Security Policy (CSP) headers to restrict script execution and inline form submissions from untrusted sources.
- Monitor web application logs for anomalous file uploads or POST requests from unexpected referers.
- Educate users on recognizing phishing attempts and avoiding clicks on suspicious links or buttons.
- Validate file uploads server-side with strict content-type checks and size limits to prevent abuse.

## Objectives

1. Trick the victim into submitting an unauthorized file upload request to the target application.
2. Perform actions on behalf of the victim, such as uploading malicious files or modifying account settings.
3. Potentially steal sensitive information or escalate privileges if the forged request succeeds.
4. Demonstrate the impact of missing CSRF protections in web applications.

## Instructions

### Step 1: Identify the Target Endpoint

**Context**: Determine the exact URL and form structure of the vulnerable file upload endpoint on the target web application. This ensures the forged request matches the expected format.

Inspect the legitimate upload form using browser developer tools to note the action URL, enctype (multipart/form-data), and any required fields beyond the file.

> Analyze network requests during a legitimate upload to capture the POST structure.

### Step 2: Prepare the Malicious HTML Payload

**Context**: Create or customize the HTML page containing the hidden form and JavaScript to automate the file population and submission. This payload will be hosted on an attacker-controlled site.

Use the [[codes/CSRF-File-Upload-HTML-Payload]] code snippet as the base. Replace the <target> placeholder with the actual upload endpoint URL (e.g., https://target.com/upload).

Embed additional form fields if needed to match the target's requirements (e.g., hidden inputs for session or metadata).

> Save the HTML as a file (e.g., csrf.html) and host it on a web server or use it in a phishing campaign.

### Step 3: Deliver the Payload to the Victim

**Context**: Social-engineer the victim to visit the malicious page while authenticated to the target site. The goal is to ensure the victim's browser includes the session cookie in the forged request.

Send the malicious link via email, SMS, or embed in a compromised site, disguising it as a legitimate action (e.g., "Upload your profile picture here").

Instruct the victim (via deception) to click the "Submit Request" button, which triggers the JavaScript to create a dummy file and submit the form.

> Monitor for the request on the target application or use a proxy like Burp Suite to intercept and verify.

### Step 4: Verify the Attack Success

**Context**: Confirm the forged request was processed by the target application, checking for the intended unauthorized action.

Review application logs, victim account changes, or any callbacks/alerts from the upload success. If the request included a malicious file payload, check for execution indicators.

> Look for server responses indicating successful upload (e.g., 200 OK with confirmation message) or changes in the victim's session/data.
