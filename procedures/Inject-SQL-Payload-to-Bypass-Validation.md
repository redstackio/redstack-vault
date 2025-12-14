---
tags:
  - sqli
  - injection
  - bypass
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 85d64333-f8ed-4b25-bddf-703a370f20a2
created_at: '2025-12-14T03:46:20.631Z'
updated_at: '2025-12-14T03:46:20.631Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject SQL Payload to Bypass Validation

## Summary

This procedure exploits SQL injection in the partner ID field to manipulate the backend query, bypassing verification and allowing unauthorized account creation.

## Description

Targeting the Teavana sign-up form's partnerno field on Salesforce Commerce Cloud, this injects a tautology payload to make the SQL condition always true, evading partner ID checks. The root cause is unsanitized user input in SQL queries. A similar issue exists in the card addition AJAX endpoint (https://www.teavana.com/on/demandware.store/Sites-Teavana-Site/default/MyAccount-StarbucksCardAdd?format=ajax), where invalid inputs redirect without errors but add no card. Outcomes: Successful account creation; no data exfiltration observed.

## Requirements

1. Confirmed validation failure from prior test
2. Web browser with form access
3. Understanding of basic SQL injection payloads

## Defense

Defensive measures and detection strategies:

- Use prepared statements and parameterized queries to prevent injection
- Implement web application firewall (WAF) rules to block common SQL payloads
- Monitor for anomalous success rates after validation failures

## Objectives

1. Alter SQL query logic to bypass checks
2. Complete unauthorized account creation
3. Validate exploitation without data compromise

## Instructions

### Step 1: Modify Input with SQL Payload and Submit

**Context**: Replace the test input with a payload that forces the query to evaluate as true, tricking the validation.

**Action**:

Change the partnerno field to `'1234' OR 1=1` (omit outer quotes), keep other fields the same, and submit the form.

> Expected output: Sign-up succeeds without partner ID error; account is created and user may be redirected to login or dashboard. For the card addition variant, input similar payloads in card number/PIN fields to observe redirect to account-login without addition.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- sqli
- injection
- bypass
