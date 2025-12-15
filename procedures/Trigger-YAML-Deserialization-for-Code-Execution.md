---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - deserialization
  - rce
type: procedure
tools:
  - '[[tools/paper_trail]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/system-sleep-600]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:29:56.600Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Command-Line Interface]]'
---
---

# Trigger-YAML-Deserialization-for-Code-Execution

## Summary

This procedure triggers the deserialization of the injected YAML payload in the historic users feature, calling the vulnerable reify method in the paper_trail gem to execute arbitrary Ruby code on the server.

## Description

The historic_users endpoint queries UserVersion records by email and invokes reify, which deserializes the YAML object without validation. The crafted payload exploits Ruby's YAML parser to instantiate objects leading to system command execution.

## Requirements

1. Persisted payload in user_versions (from previous procedure)
2. Access to /support/historic_users endpoint
3. Server running Ruby on Rails with paper_trail gem

## Defense

Defensive measures and detection strategies:

- Avoid deserializing untrusted YAML; use safe YAML parsers or JSON
- Validate object types and contents before reify calls
- Monitor for long-running processes or unexpected system calls in logs

## Objectives

1. Query the malicious record
2. Invoke reify to deserialize and execute code
3. Demonstrate RCE with a delay command

## Instructions

### Step 1: Access Historic Users with Trigger

**Context**: Use the email from the payload to load the record.

**Command** (HTTP request):
```bash
curl http://localhost:8080/support/historic_users?historic_user_input=uniquekeywordtotriggercode@hackerone.com
```

> This queries by email, finds the record, and calls reify, deserializing the YAML to execute system('sleep 600'). Expected: 600-second hang, then 500 error.

### Step 2: Observe Execution

**Context**: Monitor server for code execution indicators.

Check server logs for the sleep command or process delay.

> Success: Application response delayed, confirming RCE.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]
- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/system-sleep-600]]

## Tools Used

- [[tools/paper_trail]]

## Tags

- [[deserialization]]
- [[rce]]

---
