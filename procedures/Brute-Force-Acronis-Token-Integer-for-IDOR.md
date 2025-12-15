---
id: proc-acronis-brute-token
tags:
  - brute-force
  - idor
  - enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-acronis-lead-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:29.037Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Brute Force]]'
  - '[[Account Discovery]]'
---
# Brute-Force Acronis Token Integer for IDOR

## Summary

This procedure involves systematically modifying the integer in the Acronis token to guess valid values, exploiting the IDOR to access unauthorized lead data despite a 60 requests/second rate limit.

## Description

The API at https://www.acronis.com/en-us/api/v1/lead/ lacks proper authorization, allowing token modifications to enumerate other users' leads. Starting from a known integer (e.g., 39235), attackers increment/decrement values to find matches, retrieving data for Cyber Cloud and other accounts.

## Requirements

1. Base token URL from analysis
2. Script or manual tool for requests (e.g., browser or curl)
3. Awareness of rate limit (60/sec) to avoid detection

## Defense

Defensive measures and detection strategies:

- Enforce server-side ownership checks for tokens and lead IDs
- Implement exponential backoff and IP-based rate limiting
- Monitor for high-volume token modifications

## Objectives

1. Enumerate valid token integers
2. Bypass IDOR to access foreign leads
3. Identify targets for data extraction

## Instructions

### Step 1: Prepare Token Modifications

**Context**: Select a range around known integers for brute-forcing.

Based on analysis, target 5-digit values like 39235 ± increments (e.g., 39200-39300).

> Plan ~1000 guesses within rate limits.

### Step 2: Submit Modified Requests

**Context**: Replace the integer and query the endpoint.

Use [[commands/curl-acronis-lead-request]] to test variations:

```bash
curl -X GET "https://www.acronis.com/en-us/api/v1/lead/id:929-HVV-335&token:_mch-acronis.com-<timestamp>-76556"
```

> Repeat for different integers; valid ones return user data.

### Step 3: Validate Hits

**Context**: Check responses for success.

Look for 200 OK with JSON data instead of errors.

> Expected output: Successful brute-force yields accessible leads.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Brute Force]]
- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-acronis-lead-request]]

## Tools Used


## Tags

- brute-force
- token-modification
