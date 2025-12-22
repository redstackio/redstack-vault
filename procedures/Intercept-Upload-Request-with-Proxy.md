---
tags:
  - web
  - proxy
  - intercept
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Online-String-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 9befc8af-2784-44db-ae1c-eee9d6768a3c
created_at: '2025-12-11T06:10:15.978Z'
updated_at: '2025-12-11T06:10:15.978Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Intercept Upload Request with Proxy

## Summary

This procedure involves setting up a proxy to intercept and capture HTTP requests during file uploads, allowing for inspection and modification of parameters like filenames.

## Description

In web security testing, intercepting requests is crucial for identifying vulnerabilities such as improper sanitization. This targets the support.cs.money/upload_file endpoint, using Burp Suite to capture requests in a support chat image upload scenario, enabling further exploitation like XSS injection.

## Requirements

1. Burp Suite installed and configured as a proxy.
2. Browser configured to route traffic through the proxy.
3. Access to the target upload feature.

## Defense

Defensive measures and detection strategies:

- Implement proper input sanitization and encoding.
- Monitor for anomalous proxy traffic or request modifications.

## Objectives

1. Capture the upload request for modification.
2. Identify editable parameters like filename.
3. Prepare for payload injection.

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept requests.

Turn on intercept in Burp Suite and configure your browser to use the proxy.

### Step 2: Initiate Upload and Intercept

**Context**: Perform the file upload to trigger interception.

Navigate to the support chat, upload an image, and capture the request to support.cs.money/upload_file.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- web
- proxy
- intercept
