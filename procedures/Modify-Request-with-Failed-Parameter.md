---
id: uuid-3
tags:
  - parameter-tampering
  - open-redirect
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite-Community-Edition]]'
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
updated_at: '2025-12-14T17:24:27.000Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify-Request-with-Failed-Parameter

## Summary

Edits the 'failed' parameter in the AMA POST request body to an arbitrary external URL, setting up the open redirect exploitation.

## Description

The 'failed' field in multipart/form-data is changed to a malicious or test URL (e.g., http://google.com), exploiting lack of validation in the redirect logic.

## Requirements

1. Request loaded in Burp Repeater
2. Knowledge of multipart/form-data structure

## Defense

Defensive measures and detection strategies:

- Validate and whitelist redirect URLs
- Sanitize Location header inputs

## Objectives

1. Insert external URL into 'failed' parameter
2. Maintain valid request syntax
3. Simulate form failure redirect

## Instructions

### Step 1: Edit POST Body

**Context**: Locate and alter the parameter.

In Repeater, switch to the request body view and find the 'failed' field in the multipart section.

### Step 2: Set Arbitrary URL

**Context**: Replace with test external site.

Change the value to `http://google.com` and ensure the Content-Disposition header is correct.

**Expected Output**: Updated body with 'failed' = http://google.com, no parsing errors in Burp.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Community-Edition]]

## Tags

- [[parameter-tampering]]
- [[open-redirect]]
- [[web]]
