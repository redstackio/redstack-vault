---
id: proc-uuid-1
tags:
  - idor
  - web
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-access-edit-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.515Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Moneybird-Accountant-Company-Edit-Endpoint-via-IDOR

## Summary

This procedure exploits an IDOR vulnerability in the Moneybird web application to access the edit endpoint for accountant company details without proper authorization, allowing viewing of sensitive information.

## Description

In the Moneybird platform, the endpoint for editing accountant company details lacks sufficient permission checks on the referenced company object. By manipulating the company ID in the URL, an authenticated user can access edit forms for companies they do not own. This is a classic IDOR scenario in a web application, targeting the /user/accountant_company/edit path. The attack requires a valid session but no ownership verification, potentially exposing company names and other details. Expected outcomes include loading the edit form for unauthorized entities, rated as low severity due to limited impact on data modification.

## Requirements

1. Authenticated session in Moneybird (e.g., via login cookie)
2. Knowledge of a target accountant company ID (e.g., from API responses or enumeration)
3. Web browser or command-line tool like curl for HTTP requests
4. Network access to https://moneybird.com

## Defense

Defensive measures and detection strategies:

- Implement server-side permission checks verifying user ownership of the referenced object before loading edit forms
- Use indirect object references (e.g., hashed IDs) instead of sequential IDs
- Log and monitor access to edit endpoints for anomalies, such as cross-user ID manipulations
- Enable web application firewall (WAF) rules to detect IDOR patterns in requests

## Objectives

1. Gain unauthorized read access to accountant company edit details
2. Identify exploitable endpoints for further modification
3. Validate IDOR vulnerability presence

## Instructions

### Step 1: Prepare Session and Target ID

**Context**: Obtain a valid session cookie and identify the target company ID to reference in the request.

Log in to Moneybird via browser, extract the session cookie from developer tools, and note a target company ID (e.g., from your own company's URL or enumeration).

### Step 2: Access the Edit Endpoint

**Context**: Send a GET request to the edit endpoint with the manipulated company ID to bypass authorization.

**Command** ([[commands/curl-access-edit-endpoint]]):
```bash
curl -H "Cookie: session=your_session_cookie" https://moneybird.com/user/accountant_company/edit?company_id=TARGET_COMPANY_ID
```

> This command fetches the edit page for the specified company ID. Expected output includes HTML form with company details if successful, or a permission error if patched.

### Step 3: Verify Access

**Context**: Inspect the response to confirm unauthorized access.

Check for the presence of editable fields like company name in the HTML response.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-edit-endpoint]]

## Tools Used


## Tags

- idor
- web
- moneybird
