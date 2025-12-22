---
id: uuid-analyze-response
tags:
  - response-parsing
  - data-collection
  - email-enumeration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:28:59.254Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Analyze-Response-for-Billing-Admins

## Summary

Parse the JSON response from the Dashlane API to extract billing admin email addresses, confirming unauthorized access.

## Description

The response includes a 'billingAdmins' field with an array of user objects containing emails. This step collects the sensitive data exposed by the IDOR.

## Requirements

1. Successful API response (HTTP 200)
2. JSON viewing capability in Burp

## Defense

Defensive measures and detection strategies:

- Mask sensitive fields in responses for non-authorized users
- Encrypt or omit PII in API outputs
- Audit logs for data access patterns

## Objectives

1. Identify billingAdmins array
2. Extract email addresses
3. Document for impact assessment

## Instructions

### Step 1: View Response in Burp

**Context**: Inspect returned JSON.

**Instructions**: In Repeater, switch to Response tab and search for 'billingAdmins'.

> Example: {"billingAdmins": [{"login": "admin@team.com"}]}

### Step 2: Copy Emails

**Context**: Collect data.

**Instructions**: Manually copy or use Burp extensions to export emails from the array.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Local System]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- collection
- json
