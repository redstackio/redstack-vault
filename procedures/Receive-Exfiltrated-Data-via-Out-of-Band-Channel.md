---
tags:
  - xxe
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/capture-ftp-request]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6ac080d7-c0c9-40c9-b100-e3f7a2060e0a
created_at: '2025-12-13T09:00:27.898Z'
updated_at: '2025-12-13T09:00:27.898Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Receive Exfiltrated Data via Out-of-Band Channel

## Summary

This procedure captures exfiltrated data from the vulnerable server via an out-of-band channel, such as FTP requests initiated by the XXE payload, revealing contents of sensitive files.

## Description

After the payload is processed, the server makes an outbound FTP request to the attacker's site, embedding the file contents (e.g., /etc/passwd) in the URL, allowing capture on the attacker's side.

## Requirements

1. FTP server or listener on attacker's infrastructure
2. Successful triggering of XXE payload in prior steps
3. Monitoring tools for incoming requests

## Defense

Defensive measures and detection strategies:

- Block outbound connections from servers to unknown hosts
- Use network monitoring to detect anomalous FTP traffic

## Objectives

1. Capture outbound requests from target
2. Extract embedded file contents
3. Achieve arbitrary file read impact

## Instructions

### Step 1: Monitor for Inbound Requests

**Context**: Set up listener to capture FTP requests containing exfiltrated data.

**Command** ([[commands/capture-ftp-request]]):

```bash
tcpdump -i any port 21 -vv
```

> Monitor for requests to ftp://mysite/ with appended file contents.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/capture-ftp-request]]

## Tools Used



## Tags

- [[xxe]]
- [[Exfiltration]]
