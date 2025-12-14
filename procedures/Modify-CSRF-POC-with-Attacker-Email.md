---
tags:
  - csrf
  - modification
  - poc
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
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.190Z'
sub_techniques: []
id: cdf9086f-b8b0-4cc9-b4b2-f9747e889ba3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Drive-by Compromise]]'
---
# Modify-CSRF-POC-with-Attacker-Email

## Summary

Edit the generated CSRF PoC HTML to replace the email address with an attacker-controlled one, while preserving the authenticity token for valid submission.

## Description

Modification targets the email_relay[address] parameter to redirect notifications or access to the attacker upon successful addition to the victim's account. The token remains unchanged to leverage the reuse vulnerability, ensuring the forged request authenticates under the victim's session.

## Requirements

1. Generated CSRF PoC HTML file
2. Text editor (e.g., VS Code, Notepad++)
3. Attacker email address

## Defense

Defensive measures and detection strategies:

- Audit email relay additions for anomalies
- Require confirmation for sensitive changes

## Objectives

1. Update email parameter to attacker value
2. Retain token and other params
3. Validate HTML syntax

## Instructions

### Step 1: Edit HTML File

**Context**: Change the target email without altering security params.

Open omise_csrf_poc.html and find <input name="email_relay[address]" value="testaccount1@gmail.com" />; change value to "attacker@gmail.com".

> Ensures form posts attacker's email on submission.

### Step 2: Save and Review

**Context**: Confirm no breakage.

Save as omise_modified_csrf.html and inspect source; token should still be present as <input name="authenticity_token" value="UoPkXa4u..." />.

> File ready for delivery.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[modification]]
