---
tags:
  - ear
  - response-modification
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:18.073Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2b658e2a-d1ed-4c18-a2a8-ac533369c104
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Redirect-Response-with-Burp-Suite

## Summary

This procedure intercepts a 302 redirect response using Burp Suite and modifies the HTTP status code to 200 OK, exposing the full admin panel HTML for unauthenticated access.

## Description

The EAR vulnerability stems from the server sending a redirect header but continuing to output the protected admin page content without halting execution. By altering the status code, attackers can force the browser to render this content, bypassing authentication. This affects PHP endpoints in the target DoD application, revealing S3 management interfaces.

## Requirements

1. Burp Suite installed and running as a proxy
2. Browser configured to use the proxy (e.g., 127.0.0.1:8080)
3. Access to the authentication redirect endpoint

## Defense

Defensive measures and detection strategies:

- Ensure redirects are followed by immediate script exit
- Use Content-Security-Policy to prevent unauthorized rendering
- Log and alert on modified HTTP statuses in proxy traffic

## Objectives

1. Intercept and alter the redirect response
2. Render the admin panel without authentication
3. Identify exposed admin functions

## Instructions

### Step 1: Intercept the Response

**Context**: Trigger the login redirect and enable interception in Burp Suite to capture the 302 response.

With Burp Suite's Intercept tab active, browse to `https://████████/████` and submit the login form.

**Expected Output**: Intercepted response showing Status: 302 Found and body with admin HTML (e.g., links to upload.php, delete.php).

### Step 2: Modify Status Code

**Context**: Change the status to 200 OK to load the content.

In the Burp interceptor, edit the response header from `HTTP/1.1 302 Found` to `HTTP/1.1 200 OK`, then forward the response.

**Expected Output**: Browser displays the full admin panel with functional links to S3 management tools.

### Step 3: Verify Access

**Context**: Interact with the panel to confirm no authentication is enforced.

Click on admin links like 'Upload File' and observe no session requirements.

**Expected Output**: Accessible forms for file operations.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ear]]
- [[response-modification]]
