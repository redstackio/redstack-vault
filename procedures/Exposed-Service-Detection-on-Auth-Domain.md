---
id: proc-exposed-auth-service-927413
tags:
  - misconfig
  - exposure
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/nmap-service-scan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T17:27:35.641Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Exposed-Service-Detection-on-Auth-Domain

## Summary

Detect an exposed or misconfigured service on auth.zomato.com port 443, potentially brute-forceable despite being HTTPS (misdescribed as SSH).

## Description

Scanning reveals a service on standard HTTPS port that could be vulnerable to brute-force or other attacks due to misconfig, impacting authentication security.

## Requirements

1. Nmap installed
2. Target subdomain (auth.zomato.com)
3. Port 443 access

## Defense

Defensive measures and detection strategies:

- Harden auth services with rate-limiting
- Correct port configs and monitor scans

## Objectives

1. Confirm exposed service
2. Assess brute-force risk
3. Document misconfig

## Instructions

### Step 1: Scan Specific Port

**Context**: Target port 443 on auth domain.

**Command** ([[commands/nmap-service-scan]]):
```bash
nmap -p 443 -sV auth.zomato.com
```

> Output shows service details; check for weaknesses like weak auth.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/nmap-service-scan]]

## Tools Used

- [[tools/nmap]]

## Tags

- [[misconfig]]
- [[exposure]]
