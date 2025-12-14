---
id: proc-submit-ruby-rce
tags:
  - rce
  - ruby
  - system-command
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
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:27.881Z'
skill_level: beginner
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
---
# Submit-Malicious-Ruby-Code-for-RCE

## Summary

This procedure crafts and submits Ruby code to an online interpreter that exploits the built-in system function to invoke arbitrary shell commands, enabling remote code execution on the hosting server.

## Description

The attack targets online Ruby execution sites lacking proper sandboxing, where user-submitted code runs with server privileges. By using Ruby's system method, shell commands are executed directly on the OS. The scenario involves pasting code into a web form, and the expected outcome is the code being queued for server-side execution. Technical approach relies on Ruby's unrestricted access to OS calls; prerequisites include access to a vulnerable online interpreter.

## Requirements

1. Access to an online Ruby execution site from the previous procedure
2. Knowledge of basic Ruby syntax and shell commands
3. Web browser for code input

## Defense

Defensive measures and detection strategies:

- Sandbox Ruby execution with seccomp or containers to block system calls
- Parse and filter input code for dangerous functions like system or exec
- Log all executed code and monitor for shell invocations

## Objectives

1. Inject Ruby code that triggers shell execution
2. Bypass any basic input validation on the platform
3. Set up for observation of RCE effects

## Instructions

### Step 1: Craft the Malicious Ruby Code

**Context**: Prepare Ruby code that includes a comment for disguise and a system call to run shell commands.

**Command** ([[commands/ruby-system-shell-invocation]]):

```ruby
# Hello World Program in Ruby
system "clear;ls;uname -a;echo RCE in Ruby Language By Black_EyE";
```

> This code disguises as a hello world program but executes the shell chain via system, clearing the screen, listing files, showing system info, and echoing a message.

### Step 2: Input Code into Online Interpreter

**Context**: Paste the code into the site's code editor to submit it for execution.

**Command** (Site Interaction):

```bash
# Paste the Ruby code into the web form's code input field
```

> The site should accept the code without immediate rejection, preparing it for the run button click.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[JavaScript]] JavaScript (adapted for Ruby scripting)

## Commands Used

- [[commands/ruby-system-shell-invocation]]

## Tools Used

- [[tools/Online-Ruby-Execution-Site]]

## Tags

- rce
- ruby
