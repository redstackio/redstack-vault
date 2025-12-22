---
tags:
  - subdomain-enumeration
  - recon
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-tamper-htmlencode]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 4e57f277-3426-4719-8347-1b945c081376
created_at: '2025-12-11T06:10:30.948Z'
updated_at: '2025-12-11T06:10:30.948Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Enumerate Subdomains to Discover Upload Endpoint

## Summary

This procedure involves enumerating subdomains to identify potential entry points like file upload forms in web applications.

## Description

Subdomain enumeration helps discover hidden endpoints, such as the XML upload form in Microsoft Dynamics AX systems, which can be tested for vulnerabilities like SQL injection or XXE.

## Requirements

1. Target domain name
2. Network access to the target
3. Subdomain enumeration tool like subfinder

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring and alerting
- Use web application firewalls to detect enumeration patterns

## Objectives

1. Identify subdomains with upload functionality
2. Map the attack surface
3. Discover vulnerable endpoints

## Instructions

### Step 1: Run Subdomain Enumeration

**Context**: Enumerate subdomains to find the target endpoint.

Execute a subdomain enumeration tool:

```bash
subfinder -d example.com -o subdomains.txt
```

> This command lists potential subdomains for further testing.

### Step 2: Verify Discovered Endpoints

**Context**: Check for file upload forms.

Manually browse or use probing tools to confirm the presence of XML upload functionality.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[subdomain-enumeration]]
- [[recon]]
