---
id: 1a5dae8d-b19a-4726-995d-0d820b2df36e
name: Perform DNS Rebinding Switch
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T06:10:15.599Z'
updated_at: '2025-12-11T06:10:15.599Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Unsecured Credentials]]'
sub_techniques: []
tags:
  - dns-rebinding
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
platforms:
  - Web
  - GCP
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1552]]'
---

# Perform DNS Rebinding Switch

## Summary

This procedure switches the DNS record of the attack domain to the internal metadata IP to enable rebinding.

## Description

Immediately after triggering SSRF, update DNS to point to 169.254.169.254 and wait for the JS to execute against the internal service.

## Requirements

1. Control over DNS records for the domain
2. Timing coordination with SSRF trigger
3. Patience for 3-minute window

## Defense

Defensive measures and detection strategies:

- Use DNS rebinding protections in browsers and servers
- Monitor DNS changes and anomalous resolutions

## Objectives

1. Rebind domain to internal IP
2. Allow JS access to metadata service
3. Facilitate exfiltration

## Instructions

### Step 1: Switch DNS Record

**Context**: Update DNS after SSRF trigger.

Switch the DNS record of demon.███████ to 169.254.169.254 and wait 3 minutes.

> This enables the rebinding attack.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Unsecured Credentials]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[dns-rebinding]]
