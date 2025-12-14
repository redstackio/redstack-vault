---
tags:
  - recon
  - swagger-ui
type: procedure
tools:
  - '[[tools/Custom-Swagger-UI-Detection-Module]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 86f2a4b6-b09a-4c54-a39c-aaab7dd966d4
created_at: '2025-12-13T23:56:20.473Z'
updated_at: '2025-12-13T23:56:20.473Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Detect Exposed Swagger-UI Endpoints

## Summary

This procedure involves scanning target domains to detect exposed Swagger-UI instances, which can be vulnerable to exploits like XSS via parameters such as configUrl.

## Description

Using a custom detection module, scan multiple domains to identify old or misconfigured Swagger-UI endpoints. This is typically done in research or reconnaissance phases to find public-facing vulnerabilities. The module automates the detection at scale, checking for specific patterns indicating Swagger-UI presence.

## Requirements

1. Access to the custom detection module
2. List of target domains
3. Network access to scan publicly exposed endpoints

## Defense

Defensive measures and detection strategies:

- Restrict access to API documentation endpoints like Swagger-UI
- Monitor for unusual scanning activity on API paths

## Objectives

1. Identify vulnerable Swagger-UI instances
2. Confirm endpoint exposure
3. Prepare for further exploitation testing

## Instructions

### Step 1: Run Detection Module

**Context**: Execute the custom module to scan for Swagger-UI.

Assuming the module is a Python script:

```bash
python detect_swagger.py -d shopifycloud.com -o results.txt
```

> This scans the domain and outputs detected endpoints.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Custom-Swagger-UI-Detection-Module]]

## Tags

- [[recon]]
- [[swagger-ui]]
