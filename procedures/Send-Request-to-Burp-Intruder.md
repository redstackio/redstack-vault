---
tags:
  - intruder
  - burp
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:56.429Z'
sub_techniques: []
id: a5e9a651-7801-4653-a06a-13f970a5dfe6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Send-Request-to-Burp-Intruder

## Summary

This procedure transfers an intercepted HTTP request from Burp Proxy to the Intruder module, preparing it for automated fuzzing of parameters like category IDs in API endpoints.

## Description

Following request interception, this step loads the request into Burp Intruder for payload-based attacks. In the Brave community forum scenario, it enables fuzzing the category ID to discover unprotected endpoints. No additional tools are needed beyond Burp. Expected outcome is the request ready in Intruder with default attack positions.

## Requirements

1. Valid intercepted request in Burp Proxy history
2. Burp Suite Intruder module accessible
3. Basic understanding of Burp interface

## Defense

Defensive measures and detection strategies:

- Rate limiting on API endpoints to detect rapid sequential requests
- Log analysis for unusual payload insertions or high request volumes from single IPs

## Objectives

1. Load request into fuzzing engine
2. Set stage for parameter manipulation
3. Ensure compatibility for payload injection

## Instructions

### Step 1: Select and Send Request

**Context**: Identify the target request and forward it to Intruder.

In Burp Proxy > HTTP History, locate the captured GET request (e.g., to /c/beta-builds/38.json). Right-click it and select "Send to Intruder".

> The request transfers seamlessly, appearing in the Intruder tab with raw request view populated.

### Step 2: Verify Load

**Context**: Confirm the request is correctly loaded.

Switch to the Intruder tab and review the request in the raw editor. Ensure the full URL, headers, and body (if any) match the original.

> No errors indicate successful transfer; proceed to position marking.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Vulnerability Scanning

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intruder]]
- [[fuzzing]]
