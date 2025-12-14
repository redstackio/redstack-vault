---
tags:
  - dos
  - unicode
  - payload
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.792Z'
sub_techniques: []
id: 716fa268-7441-4665-87f6-0fe6bbf92022
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Send-Single-Large-Unicode-Payload

## Summary

This procedure crafts and sends a single POST request to the Django admin login with over 1 million invalid Unicode characters, triggering slow NFKC normalization.

## Description

Using Burp Suite, intercept the login request and modify the username field to include a massive payload of characters like '¾'. This exploits the fact that invalid values longer than max_length are still normalized on Windows, causing delays.

## Requirements

1. Running vulnerable Django server on Windows
2. Burp Suite configured as proxy
3. Browser or tool to access /admin/login/

## Defense

Defensive measures and detection strategies:

- Enforce strict input validation and length checks before normalization
- Use rate limiting on login endpoints
- Log and alert on large input sizes

## Objectives

1. Trigger normalization processing delay
2. Confirm single-request impact
3. Prepare for concurrent scaling

## Instructions

### Step 1: Intercept Login Request

**Context**: Navigate to admin login and proxy through Burp.

Access http://localhost:8000/admin/login/ in a proxied browser.

Submit a normal login to capture the POST request in Burp Repeater.

### Step 2: Craft and Send Payload

**Context**: Modify the username field with large Unicode input.

In Burp Repeater, edit the 'username' parameter to repeat '¾' over 1,000,000 times (e.g., using Burp's paste or script). Send the request.

> Expected output: Response after ~4.4 seconds, with validation error but delayed due to normalization.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos
- unicode
- payload
