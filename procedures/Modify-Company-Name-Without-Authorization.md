---
id: proc-uuid-2
tags:
  - idor
  - web
  - modification
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-modify-company-name]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:29.504Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Modify-Company-Name-Without-Authorization

## Summary

This procedure leverages an IDOR vulnerability in Moneybird to submit unauthorized changes to an accountant company's name via the edit endpoint, altering sensitive information without permission checks.

## Description

Following access to the edit endpoint, this procedure submits a POST request with modified company details, exploiting the lack of ownership verification. The Moneybird application at https://moneybird.com/user/accountant_company/edit allows direct object manipulation, leading to unauthorized updates. This can compromise data integrity for accountant firms, though the reported impact was low (CVSS 3.8) as it did not enable broader access. Prerequisites include a valid session and the target ID; outcomes include successful name changes visible in the application.

## Requirements

1. Successful access to the edit endpoint from the prior procedure
2. Valid session cookie for authentication
3. Target company ID
4. Form data knowledge (e.g., from inspecting the edit page HTML)
5. Tool for sending POST requests (browser or curl)

## Defense

Defensive measures and detection strategies:

- Add explicit permission checks on POST submissions to verify user access to the company object
- Implement audit logs for all edit operations, flagging cross-entity modifications
- Use session-based access tokens tied to specific objects
- Rate-limit edit requests and monitor for unusual patterns

## Objectives

1. Perform unauthorized write access to company details
2. Alter sensitive information like company name
3. Confirm IDOR enables data modification

## Instructions

### Step 1: Inspect Form Fields

**Context**: Review the edit form from the access step to identify required parameters for submission.

Use browser dev tools or curl output to note fields like `company_name` and `company_id`.

### Step 2: Submit Modification

**Context**: Send a POST request with altered data to apply changes without authorization.

**Command** ([[commands/curl-modify-company-name]]):
```bash
curl -X POST -H "Cookie: session=your_session_cookie" -d "company_name=Modified Company Name&company_id=TARGET_COMPANY_ID" https://moneybird.com/user/accountant_company/edit
```

> This submits the form data. Expected output is a success redirect or confirmation; check the application to verify the name change.

### Step 3: Validate Changes

**Context**: Confirm the modification took effect.

Re-access the company details page to see the updated name.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-modify-company-name]]

## Tools Used


## Tags

- idor
- web
- moneybird
