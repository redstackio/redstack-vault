---
tags:
  - csrf
  - execution
  - account-creation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/Submit-User-Registration-POST]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:36.133Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: dbaf17e8-b3ed-4efb-b86e-e9dd39b91563
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-CSRF-PoC-for-Unauthorized-Account-Creation

## Summary

This procedure delivers and executes the CSRF PoC HTML in a victim's browser context to forge a user registration request, creating unauthorized accounts and triggering verification emails that can lead to DoS on email servers.

## Description

The PoC HTML, generated from the intercepted request, is loaded in a browser where the victim is authenticated to the target site (or cookies are sent). It automatically submits the hidden form via POST, mimicking a legitimate registration. In ASP.NET apps without CSRF protection, this succeeds, creating accounts with victim-supplied details and sending emails. Impacts include spam, resource exhaustion, and potential financial costs from excessive emails.

## Requirements

1. Generated CSRF PoC HTML file
2. Victim browser with cookies for the target domain
3. Method to deliver PoC (e.g., phishing link to hosted HTML)

## Defense

Defensive measures and detection strategies:

- Require user confirmation for state-changing actions
- Monitor email server logs for registration floods
- Implement rate limiting on registration endpoints

## Objectives

1. Forge and submit the registration request without user input
2. Confirm account creation via server response
3. Demonstrate cascading impact on email verification

## Instructions

### Step 1: Save and Host the PoC

**Context**: Prepare the HTML file for delivery to the victim.

Save the generated PoC as csrf-poc.html and host it on a server or local file system.

> Ensure the form action points to the target /███████ endpoint. Expected output: Accessible HTML file.

### Step 2: Trigger Execution in Victim Context

**Context**: Load the PoC while the victim is on the target site to ensure cookies are included.

Open the HTML in the victim's browser (e.g., via link: <img src="x" onerror="document.forms[0].submit()"> or direct load).

This executes the equivalent of [[commands/Submit-User-Registration-POST]]:

```http
POST /███████ HTTP/1.1
Host: ████████
Content-Type: application/x-www-form-urlencoded

[encoded form data with user details]
```

> Expected output: Redirect or message "Your account has been created, but before you can login you must first verify your email address. A message has been sent to the email address you specified."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/Submit-User-Registration-POST]]

## Tools Used


## Tags

- [[csrf]]
- [[Execution]]
