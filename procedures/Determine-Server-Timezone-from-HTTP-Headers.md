---
id: p-determine-timezone
tags:
  - http-headers
  - timezone-recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:31:31.162Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Determine-Server-Timezone-from-HTTP-Headers

## Summary

This procedure inspects HTTP response headers, particularly the Date header, to infer the server's timezone, enabling time synchronization for predictable token generation in Revive Adserver attacks.

## Description

Servers often include a Date header in GMT format, revealing the timezone offset. For Revive Adserver, this allows attackers to align local time with the server, crucial for guessing uniqid()-based tokens. Use tools like curl or browser dev tools for inspection without alerting defenses.

## Requirements

1. Network access to the target server
2. Tool for sending HTTP requests (e.g., curl, browser)
3. Ability to parse HTTP headers

## Defense

Defensive measures and detection strategies:

- Remove or obfuscate Date headers if possible
- Use consistent UTC internally but vary external timestamps
- Monitor for anomalous header inspection requests

## Objectives

1. Extract Date header from responses
2. Infer timezone (e.g., GMT+0 from GMT format)
3. Prepare for time synchronization

## Instructions

### Step 1: Send Request to Endpoint

**Context**: Trigger a response to capture headers.

Use curl to GET any page, e.g., the homepage: curl -I https://target.com/

### Step 2: Parse Date Header

**Context**: Identify timezone from the timestamp.

Look for 'Date: Thu, 09 May 2019 21:26:20 GMT', concluding GMT+0 timezone.

**Expected Output**: Timezone as GMT.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: Hardware

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- recon
- headers
