---
tags:
  - csrf
  - web
  - api
  - poc
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 0322bb8f-2840-4529-bded-6491ea5c5d8b
created_at: '2025-12-14T17:27:35.977Z'
updated_at: '2025-12-14T17:27:35.977Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Generate-and-Execute-CSFR-POC-for-Stripo-Project-Settings

## Summary

This procedure outlines the generation and execution of a Cross-Site Request Forgery (CSRF) proof-of-concept (POC) to exploit the Stripo Inc platform's PATCH endpoint for unauthorized modification of project settings, such as emails, contacts, and social networks, by forging requests that leverage the victim's authenticated session.

## Description

The Stripo Inc platform at https://my.stripo.email/cabinet/stripeapi/v1/projects/{Project_Id} lacks anti-CSRF tokens, allowing an attacker with knowledge of the project ID to craft an HTML page that submits malicious PATCH requests. The attack involves intercepting a legitimate request with Burp Suite, generating a CSRF POC, modifying it to use PATCH with altered JSON data, and triggering it in the victim's browser. This leads to critical impacts like data manipulation and potential account compromise. Prerequisites include the project ID and the victim's active session; no additional credentials are needed.

## Requirements

1. Burp Suite installed and configured as a proxy in the browser.
2. Access to the target's project ID.
3. Victim authenticated to Stripo Inc in the browser.
4. Ability to deliver the POC HTML (e.g., via email or malicious site).

## Defense

Defensive measures and detection strategies:

- Implement anti-CSRF tokens (e.g., synchronizer tokens) on all state-changing endpoints.
- Enforce same-site cookie attributes (Lax or Strict) and validate Origin/Referer headers.
- Monitor for anomalous PATCH requests from unexpected referrers using WAF rules.
- Educate users on phishing risks and disabling auto-submits in emails.

## Objectives

1. Forge and execute a CSRF request to modify project settings without authentication.
2. Demonstrate unauthorized changes to sensitive data like emails and contacts.
3. Validate the vulnerability's exploitability for reporting or remediation.

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Capture the structure of a valid project update to base the POC on.

Use Burp Suite Proxy to intercept a POST request while modifying settings in the app.

> Forward to Repeater for analysis; note the JSON payload and endpoint.

### Step 2: Generate CSRF POC

**Context**: Create an HTML template for cross-site submission.

In Repeater, use Engagement Tools > Generate CSRF POC to produce the HTML.

> Save as poc.html; the form will mimic the request without tokens.

### Step 3: Trigger and Intercept POC

**Context**: Test the basic forgery and prepare for modifications.

Open poc.html in the browser and submit; intercept with Burp Proxy.

> Confirm the request reaches the endpoint without CSRF blocks.

### Step 4: Modify Method to PATCH

**Context**: Match the API's update method.

Edit the intercepted request in Burp to change POST to PATCH.

> Verify syntax; forward to test if accepted.

### Step 5: Alter Payload Data

**Context**: Inject malicious changes to project info.

Copy JSON from original Repeater, paste into current body, edit fields (e.g., email).

> Ensure JSON validity; example change: {"email": "hacked@example.com"}.

### Step 6: Update Content-Type Header

**Context**: Ensure proper JSON parsing by the server.

Set header to Content-Type: application/json;charset=UTF-8 in Burp.

> This matches the legitimate request format.

### Step 7: Execute the Exploit

**Context**: Send the final forged request to apply changes.

Forward the modified PATCH request through Burp.

> Expect 200 OK; verify changes in the project settings.

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

- [[csrf]]
- [[web]]
- [[api]]
