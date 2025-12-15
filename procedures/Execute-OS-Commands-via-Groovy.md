---
id: proc-execute-groovy-commands
tags:
  - rce
  - groovy
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/groovy-ls-execute]]'
  - '[[commands/groovy-whoami-execute]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:32.537Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute-OS-Commands-via-Groovy

## Summary

This procedure executes arbitrary OS commands on a Jenkins server by injecting Groovy scripts into the unauthenticated script console, demonstrating remote code execution (RCE) capabilities. It uses Groovy's .execute() method to run shell commands, confirming control over the server environment.

## Description

Once the script console is accessed, Groovy code can leverage the execute() method on string objects to spawn OS processes. This allows running commands like 'ls' for directory enumeration or 'whoami' for user discovery. The attack scenario involves a public Jenkins instance without auth, targeted after recon. Prerequisites include console access. Outcomes: Command output displayed in the console, validating RCE and enabling further exploitation like persistence or exfiltration.

## Requirements

1. Access to the loaded Groovy script console
2. Knowledge of target OS shell commands (e.g., Unix-like)
3. Web browser for script input and execution

## Defense

Defensive measures and detection strategies:

- Disable or protect the script console with auth
- Run Jenkins with minimal privileges (non-root user)
- Log and alert on Groovy executions or .execute() usage
- Implement endpoint protection to block unauthorized process spawning

## Objectives

1. Confirm RCE by executing diagnostic commands
2. Gather system information for further attacks
3. Establish basis for server compromise

## Instructions

### Step 1: Execute Directory Listing Command

**Context**: Run a basic command to list files, verifying command execution works.

**Command** ([[commands/groovy-ls-execute]]):
```groovy
println "ls".execute().text
```

> This executes 'ls' via Groovy, captures output with .text, and prints it. Expected: File/directory list in current working directory.

### Step 2: Identify Executing User

**Context**: Determine the process owner to assess privilege level.

**Command** ([[commands/groovy-whoami-execute]]):
```groovy
println "whoami".execute().text
```

> This runs 'whoami', prints the result. Expected: Username (e.g., 'jenkins' or system user).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques


## Commands Used

- [[commands/groovy-ls-execute]]
- [[commands/groovy-whoami-execute]]

## Tools Used


## Tags

- [[rce]]
- [[groovy]]
- [[command-injection]]
