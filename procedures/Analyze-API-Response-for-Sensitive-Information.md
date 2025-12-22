---
tags:
  - data-analysis
  - user-profile
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:12.860Z'
sub_techniques: []
id: c832c068-6930-4bd8-ae5b-7c07a5124a40
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Analyze-API-Response-for-Sensitive-Information

## Summary

This procedure parses the JSON response from the MTN API to extract disclosed user details, such as names and profile images, for use in further attacks.

## Description

After receiving the 200 OK response, attackers review the JSON for fields exposing personal data. This completes the disclosure chain in MTN's app, highlighting risks like social engineering. No additional tools beyond Burp; outcomes include actionable intel.

## Requirements

1. Successful API response from previous procedure
2. Basic JSON parsing knowledge
3. Burp Suite Response tab

## Defense

Defensive measures and detection strategies:

- Mask or pseudonymize sensitive fields in API responses
- Audit and remove unnecessary data from public endpoints
- Use data loss prevention (DLP) tools to scan API outputs

## Objectives

1. Identify and extract key user data fields
2. Assess impact of disclosure
3. Document for reconnaissance purposes

## Instructions

### Step 1: Inspect Response in Burp

**Context**: View the raw HTTP response containing the JSON payload.

In Burp Repeater, switch to the Response tab after sending.

> Look for HTTP 200 and JSON body.

### Step 2: Parse JSON Fields

**Context**: Extract specific sensitive information from the response.

Review keys: 'firstname', 'lastname', 'othername', 'customerType' (e.g., Prepaid), 'profileImg' (image URL). Copy or export the data.

> Expected: Full name (e.g., John Doe), type, and downloadable profile image.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[data-analysis]]
- [[user-profile]]
