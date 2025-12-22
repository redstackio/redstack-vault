---
id: 16d2a5da-cacd-4de5-b17e-bdbda45313ac
name: CSRF-Attack-to-Set-User-Role-to-Admin-via-JSON-POST
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:55:55.528736+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Drive-by Compromise|T1189 - Drive-by Compromise]]'
sub_techniques: []
tags:
  - csrf
  - web-attack
  - role-escalation
  - json-post
  - cross-site-request-forgery
commands: []
platforms:
  - Web
tools: []
validated: true
---

# CSRF-Attack-to-Set-User-Role-to-Admin-via-JSON-POST

## Summary

This procedure outlines a Cross-Site Request Forgery (CSRF) attack that tricks a logged-in user into setting their own account role to 'admin' via a malicious JSON POST request. By hosting a crafted webpage, the attacker exploits the victim's active session to send unauthorized requests to the target application's API endpoint, potentially granting administrative privileges without direct authentication.

## Description

In a CSRF attack, the attacker leverages the victim's authenticated session on a trusted site by inducing them to visit a malicious page that automatically submits a forged request. Here, the target is a web application with an API endpoint (e.g., /api/setrole) that accepts JSON payloads to update user roles without proper CSRF protection. The procedure uses an HTML page with JavaScript to perform a POST request with Content-Type set to text/plain (to bypass simple request restrictions for JSON), sending {"role":"admin"}. This works if the application parses the payload despite the content type mismatch. The attack assumes the victim is logged in and the endpoint lacks CSRF tokens or same-site cookie enforcement. Success leads to role escalation, enabling further unauthorized actions like data access or system control.

## Requirements

1. Victim must be authenticated (logged in) to the target web application with an active session cookie.
2. Attacker must identify the API endpoint for role updates (e.g., via reconnaissance or source code review).
3. Attacker needs to host the malicious webpage on a controllable domain or use social engineering to deliver it (e.g., phishing link).
4. Target application must accept text/plain or similar content types for JSON parsing without strict validation.
5. No CSRF tokens or SameSite=Strict/Lax cookie attributes enforced on the session.

## Defense

- Implement CSRF tokens in all state-changing forms and API endpoints, validating them server-side.
- Set HttpOnly and Secure flags on session cookies, and use SameSite=Strict or Lax to prevent cross-site requests.
- Enforce strict Content-Type validation (e.g., reject text/plain for JSON endpoints) and use anti-CSRF headers like Origin or Referer checks.
- Apply role-based access controls (RBAC) to prevent self-escalation and log all role changes for auditing.
- Educate users on phishing risks and use Content Security Policy (CSP) to restrict script execution.

## Objectives

1. Trick the victim into executing a forged request that changes their user role to 'admin'.
2. Achieve privilege escalation on the victim's account without direct credentials.
3. Gain administrative access to the application, enabling further exploitation like data exfiltration or lateral movement.

## Instructions

### Step 1: Identify the Target API Endpoint

**Context**: Determine the exact URL and parameters for the role-update endpoint to ensure the payload targets the correct resource. This can be done via manual testing, proxy interception, or reviewing application documentation/source code.

Inspect network traffic while performing a legitimate role change (if possible) using browser developer tools or a proxy like Burp Suite to capture the POST request details, including URL, headers, and payload format.

**Expected Output**: Confirmation of the endpoint (e.g., POST /api/setrole) and required payload structure (e.g., {"role":"admin"}).

### Step 2: Craft the Malicious Webpage

**Context**: Create an HTML file containing JavaScript that automatically sends the forged POST request upon page load, exploiting the victim's session.

Use the following code snippet as the basis for your malicious page. Save it as an HTML file and host it on a server under your control.

**Code** ([[codes/HTML-CSRF-Script-for-Role-Change-to-Admin]]):

```html
<script>
var xhr = new XMLHttpRequest();
xhr.open("POST", "http://www.example.com/api/setrole");
//application/json is not allowed in a simple request. text/plain is the default
xhr.setRequestHeader("Content-Type", "text/plain");
//You will probably want to also try one or both of these
//xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");
//xhr.setRequestHeader("Content-Type", "multipart/form-data");
xhr.send('{"role":admin}');
</script>
```

> This script initializes an XMLHttpRequest, sets the method to POST targeting the role endpoint, overrides the Content-Type to text/plain (bypassing CORS preflight for JSON), and sends the payload {"role":admin}. If the server parses it as JSON, the role updates using the victim's session.

**Expected Output**: The page loads silently, and the request is sent in the background.

### Step 3: Deliver the Malicious Page to the Victim

**Context**: Use social engineering to lure the victim to visit the hosted page while logged into the target site, ensuring their session cookie is included in the request.

Host the HTML file on a domain you control (e.g., via GitHub Pages or a simple web server). Send a phishing email or link disguised as a legitimate resource (e.g., "Check this update on your account"). Monitor network traffic on your end or use webhooks to confirm request submission.

**Expected Output**: Victim visits the page, triggering the request; server responds with success (e.g., 200 OK) if the role change succeeds, verifiable by checking the victim's account status.

### Step 4: Verify Role Escalation

**Context**: Confirm the attack's success by accessing the victim's account or observing application behavior.

After delivery, have the victim (or use another method to check) log in and verify their role has changed to 'admin' in the user profile or by attempting admin-only actions.

**Expected Output**: User interface shows 'admin' role, or API queries return elevated permissions.

### Step 5: Clean Up and Iterate

**Context**: If the initial content type fails, test alternatives like application/x-www-form-urlencoded by uncommenting the relevant lines in the script and redeploying.

Adjust the payload based on server responses (e.g., via error logs if accessible) and retest delivery.

**Expected Output**: Successful role change without errors.
