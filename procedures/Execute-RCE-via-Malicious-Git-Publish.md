---
tags:
  - rce
  - command-injection
  - execution
type: procedure
tools:
  - '[[tools/node]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/node-execute-poc]]'
platforms:
  - Linux
  - Node.js
techniques:
  - '[[Unix Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e231069c-94f2-4af4-8795-9080d8eccc61
created_at: '2025-12-14T17:23:20.105Z'
updated_at: '2025-12-14T17:23:20.105Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-RCE-via-Malicious-Git-Publish

## Summary

This procedure runs the prepared PoC script to trigger RCE in npm-git-publish, injecting and executing arbitrary shell commands on the local system via the unsanitized remote URL in the publish function.

## Description

Exploitation occurs when Node.js executes the script, requiring the vulnerable module and calling git.publish with the crafted URL 'http://gihub.com ;touch HACKED; #'. The module interpolates this into a command like `git push http://gihub.com ;touch HACKED; #`, executing the injection after the failed push. This demonstrates full RCE on Linux, where shell access allows file ops or worse. The procedure assumes prior installation and PoC creation, running in a Node.js context with shell access.

## Requirements

1. Vulnerable npm-git-publish installed (0.2.4-beta)
2. poc.js script present in current directory
3. Node.js executable in PATH
4. Linux shell environment for command injection

## Defense

Defensive measures and detection strategies:

- Patch to newer module versions or implement URL whitelisting
- Run Node.js scripts in sandboxed environments (e.g., Docker with no shell)
- Monitor process execution for unexpected git or touch commands via EDR tools like OSSEC
- Static analysis of dependencies with Semgrep for command injection patterns

## Objectives

1. Invoke the vulnerable publish function with malicious input
2. Achieve shell command execution on the host
3. Simulate real-world compromise via dependency exploitation

## Instructions

### Step 1: Run the PoC Script

**Context**: Execute the JavaScript file to trigger the git.publish call and inject the command.

**Command** ([[commands/node-execute-poc]]):
```bash
node poc.js
```

> Node.js interprets the script, loads the module, and runs publish. Expected output: Possible git error ("fatal: repository not found") for the fake URL, but the `touch HACKED` executes invisibly, creating the file without stdout.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/node-execute-poc]]

## Tools Used

- [[tools/node]]

## Tags

- [[rce]]
- [[command-injection]]
- [[Execution]]
