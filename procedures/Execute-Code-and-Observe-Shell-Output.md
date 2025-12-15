---
id: proc-execute-ruby-observe
tags:
  - rce
  - observation
  - poc
type: procedure
tools:
  - '[[tools/Online-Ruby-Execution-Site]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ruby-system-shell-invocation]]'
verified: false
platforms:
  - Web
  - Ruby
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:23:27.877Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Execute-Code-and-Observe-Shell-Output

## Summary

This procedure triggers the execution of the submitted Ruby code on the online platform and captures the resulting shell command output to confirm remote code execution on the server.

## Description

Following code submission, this step runs the Ruby script server-side, leveraging the system function to execute OS shell commands. The target is the online interpreter's execution endpoint, with outcomes including visible server environment details. The approach observes console output for RCE indicators; prerequisites are a loaded malicious code in the editor.

## Requirements

1. Submitted malicious Ruby code in the online site's editor
2. Ability to trigger execution (e.g., run button)
3. Screen recording tool for POC documentation

## Defense

Defensive measures and detection strategies:

- Isolate execution environments to prevent shell access leakage
- Alert on anomalous output like system info or file listings
- Review execution logs for non-standard command patterns

## Objectives

1. Trigger server-side code execution
2. Verify shell commands run successfully
3. Document RCE proof through output capture

## Instructions

### Step 1: Trigger Code Execution

**Context**: Initiate the run process to execute the Ruby code on the server.

**Command** (Site Interaction):

```bash
# Click the 'Run' or 'Execute' button on the online Ruby site
```

> The server processes the code, invoking the system call and running shell commands.

### Step 2: Observe and Capture Output

**Context**: Monitor the output console for shell results and record the session.

**Command** ([[commands/ruby-system-shell-invocation]] Output Observation):

```bash
# Expected shell execution via Ruby: clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE
```

> Output includes cleared console, directory listing (e.g., files in server dir), system details (e.g., Linux 5.x kernel), and the echo message. Use video recording to capture as POC.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques


## Commands Used

- [[commands/ruby-system-shell-invocation]]

## Tools Used

- [[tools/Online-Ruby-Execution-Site]]

## Tags

- rce
- poc
