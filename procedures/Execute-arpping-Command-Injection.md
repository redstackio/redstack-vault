---
tags:
  - command-injection
  - rce
  - exploit
type: procedure
tools:
  - '[[tools/arpping]]'
  - '[[tools/Node.js]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-execute]]'
  - '[[commands/touch-create-file]]'
  - '[[commands/ls-check]]'
verified: false
platforms:
  - Node.js
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:23.923Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 6522c5aa-8c70-4b9a-83f0-32789bd10804
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Unix Shell]]'
---
# Execute-arpping-Command-Injection

## Summary

This procedure executes a proof-of-concept script using the vulnerable arpping module to inject and run arbitrary OS commands via the IP parameter in arpping.ping(), achieving remote code execution on the host system.

## Description

In an application or script using arpping 2.0.0, attackers can supply a malicious IP like '127.0.0.1;touch HACKED;' to the ping function. The module passes this unsanitized to the underlying 'ping' OS command, allowing shell metacharacters to execute additional commands. This targets Node.js environments on Unix-like systems, leading to file creation, data exfiltration, or further compromise. Prerequisites: POC script from setup procedure and Node.js execution privileges.

## Requirements

1. Installed arpping 2.0.0 module
2. POC script with injection payload
3. Write access to current directory for command execution (e.g., touch)
4. Node.js executable in PATH

## Defense

Defensive measures and detection strategies:

- Input validation: Sanitize IP parameters to allow only valid IP formats (e.g., regex ^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$)
- Use safe alternatives like child_process.exec with proper escaping or libraries like 'ping' with validation
- Monitor process execution logs for unexpected commands (e.g., via auditd or sysmon) and anomalous file creations
- Update to patched versions or avoid arpping; scan for shell metacharacters in inputs

## Objectives

1. Trigger command injection to execute chained OS command
2. Verify RCE by creating a proof file
3. Assess potential for further system compromise

## Instructions

### Step 1: Run POC Script

**Context**: Execute the Node.js script to invoke arpping.ping() with the injected IP, causing the shell to interpret the semicolon and run the additional command.

**Command** ([[commands/node-execute]]):
```bash
node poc.js
```

> Runs the script, which calls arpping.ping(['127.0.0.1;touch HACKED;']). Expected output: Possible ping results or empty; no explicit error if injection succeeds. The 'touch HACKED' runs silently in background.

### Step 2: Verify Execution

**Context**: Check for the created file to confirm command injection and RCE occurred.

**Command** ([[commands/ls-check]]):
```bash
ls -la HACKED
```

> Lists details of 'HACKED' file. Expected output: File info like '-rw-r--r-- 1 user user 0 Oct 1 12:00 HACKED', confirming creation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/node-execute]]
- [[commands/touch-create-file]]
- [[commands/ls-check]]

## Tools Used

- [[tools/arpping]]
- [[tools/Node.js]]

## Tags

- command-injection
- rce
- exploit
