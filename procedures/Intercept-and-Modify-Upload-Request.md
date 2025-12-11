---
tags:
  - dos
  - file-upload
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 43127328-7168-49ca-9cf5-e7b21f518552
created_at: '2025-12-11T06:10:22.286Z'
updated_at: '2025-12-11T06:10:22.286Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0040]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1499]]'
---
# Intercept and Modify Upload Request

## Summary

This procedure uses a proxy tool to intercept and alter HTTP requests during file uploads, injecting oversized payloads into parameters like filenames to exploit validation weaknesses and cause denial of service.

## Description

By intercepting the profile picture upload request on platforms like HackerOne, attackers can modify the filename to include extremely large strings (e.g., 3MB), which are not validated and propagate to backend systems, leading to oversized responses in GraphQL queries.

## Requirements

1. Burp Suite configured as a proxy
2. Valid account with upload access
3. Large payload file (e.g., payload.txt with 3MB text)

## Defense

Defensive measures and detection strategies:

- Enforce strict length limits on upload parameters
- Monitor for anomalous request sizes in proxy logs

## Objectives

1. Inject oversized filename
2. Bypass validation checks
3. Store malicious data for later propagation

## Instructions

### Step 1: Set Up Interception

**Context**: Configure Burp Suite to intercept the upload request.

Launch Burp Suite and set your browser to proxy through it. Initiate the profile picture upload.

> Ensure interception is enabled for outgoing requests.

### Step 2: Modify Filename Parameter

**Context**: Edit the intercepted request to include the large payload.

In Burp Suite's interceptor, locate the filename parameter and prefix it with the large payload, e.g., <payload>abcd.png. Forward the request.

> This uploads the file with the oversized filename to S3 storage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[dos]]
- [[file-upload]]
- [[web]]
