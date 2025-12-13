---
tags:
  - ssrf
  - verification
  - logs
type: procedure
tools:
  - '[[tools/Wallarm-Scanner]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ssrf-get-request]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: bc586331-a797-4fe6-a329-23e62750b730
created_at: '2025-12-13T09:00:27.207Z'
updated_at: '2025-12-13T09:00:27.207Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Verify SSRF via Access Logs

## Summary

This procedure verifies the success of an SSRF attack by checking access logs on a controlled external server for requests induced by the vulnerable application.

## Description

After triggering SSRF through vulnerabilities like XXE, monitor the logs of the external server (e.g., wallarm.tools) to confirm outbound requests from the target. This out-of-band verification proves the server's ability to make unauthorized requests, which could lead to further exploitation like internal service access.

## Requirements

1. Control over an external server with accessible logs
2. Prior exploitation attempt that targets the external URL
3. Access to server logs (e.g., Apache access.log)

## Defense

Defensive measures and detection strategies:

- Restrict outbound connections from servers
- Monitor for anomalous traffic in network logs
- Implement rate limiting on endpoints prone to SSRF

## Objectives

1. Confirm SSRF exploitation
2. Validate server-side request in logs
3. Assess potential for escalation

## Instructions

### Step 1: Check External Server Logs

**Context**: Inspect the access logs for incoming GET requests from the target server.

**Command** ([[commands/ssrf-get-request]]):
```bash
GET /ok HTTP/1.0
```

> This is the expected log entry from the vulnerable server, confirming the SSRF trigger. Check your server's access.log for similar entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/ssrf-get-request]]

## Tools Used

- [[tools/Wallarm-Scanner]]

## Tags

- [[ssrf]]
- [[logs]]
