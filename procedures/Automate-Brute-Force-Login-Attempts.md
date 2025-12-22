---
id: proc-uuid-004
tags:
  - automation
  - brute-force
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/python-brute-force-script]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:30:58.749Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Automate-Brute-Force-Login-Attempts

## Summary

This procedure automates multiple login attempts using a script to simulate a real brute-force attack, exploiting the lack of limits to guess passwords efficiently.

## Description

A Python script sends POST requests to the login endpoint with a wordlist against a target username, bypassing tokens if any. In the LinkedIn vulnerability, this scales to thousands of attempts, leading to takeover if passwords are weak. Requires scripting knowledge; outcomes include hit logs or failure proofs.

## Requirements

1. Python environment with requests library
2. Password wordlist file
3. Target username and endpoint URL

## Defense

Defensive measures and detection strategies:

- Web Application Firewall (WAF) rules for brute-force patterns
- Honeypot endpoints to trap automation
- Rate limiting at load balancer level (e.g., NGINX limit_req)

## Objectives

1. Scale manual tests to automated attack
2. Demonstrate feasibility of password guessing
3. Identify weak credentials if present

## Instructions

### Step 1: Prepare Script and Wordlist

**Context**: Set up the automation tool.

**Instructions**: Create or use the provided script (e.g., script_file_to_make_login_attempt.txt) with endpoint, username, and password list.

> Install requests: `pip install requests`. Expected output: Script ready with configurable params.

### Step 2: Execute Brute-Force

**Context**: Run against target.

**Command** ([[commands/python-brute-force-script]]):
```bash
python brute_force.py --url https://linkedin.com/login --username target@example.com --wordlist passwords.txt
```

> The script loops through passwords, sending POSTs. Expected output: Console logs of attempts, success on match.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used

- [[commands/python-brute-force-script]]

## Tools Used


## Tags

- [[automation]]
- [[Scripting]]
