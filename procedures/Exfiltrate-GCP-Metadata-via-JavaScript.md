---
id: 383dff5f-b6d1-41bb-83f1-405bffa2249a
name: Exfiltrate GCP Metadata via JavaScript
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.593Z'
updated_at: '2025-12-11T06:10:15.593Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - exfiltration
  - metadata
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
platforms:
  - GCP
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
skill_level: advanced
impact_level: critical
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1552]]'
---

# Exfiltrate GCP Metadata via JavaScript

## Summary

This procedure uses the rebound JavaScript to fetch and exfiltrate sensitive GCP metadata to the logging server.

## Description

The JS fetches from endpoints like /computeMetadata/v1/instance/service-accounts/ and logs SSH keys, service accounts, and hostnames.

## Requirements

1. Successful rebinding
2. Active logging server
3. Metadata service accessible internally

## Defense

Defensive measures and detection strategies:

- Restrict metadata API access with firewalls
- Monitor for unauthorized metadata queries

## Objectives

1. Retrieve sensitive data
2. Log exfiltrated information
3. Enable further compromise (e.g., token minting)

## Instructions

### Step 1: Fetch and Log Data

**Context**: Execute JS to query metadata endpoints.

The JavaScript uses [[tools/XMLHttpRequest]] to fetch from /computeMetadata/v1beta1/project/attributes/ssh-keys, /computeMetadata/v1/instance/service-accounts/, and /computeMetadata/v1/instance/hostname, logging to the server.

> Data is exfiltrated and printed on the logging server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/XMLHttpRequest]]

## Tags

- [[Exfiltration]]
- [[metadata]]
