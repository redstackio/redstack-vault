---
id: proc-uuid-automate-burp-intruder
tags:
  - brute-force
  - automation
  - burp-intruder
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:29:20.491Z'
sub_techniques:
  - '[[Password Guessing]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Automate Brute Force Attack with Burp Intruder

## Summary

This procedure automates credential guessing on the WordPress login using Burp Intruder's payload injection, demonstrating the vulnerability with multiple attempts as proof-of-concept.

## Description

After capturing a request, Intruder sends variations by marking payload positions (e.g., §username§, §password§) and loading wordlists. For POC, 9 attempts show no blocking, but in reality, this could crack weak passwords, leading to admin access and site compromise.

## Requirements

1. Captured request from previous step
2. Wordlists for usernames/passwords (e.g., common.txt)
3. Burp Suite Professional or Community

## Defense

Defensive measures and detection strategies:

- Implement fail2ban or similar for IP blocking
- Use strong, unique admin credentials
- Monitor for high-volume POST to /wp-login.php

## Objectives

1. Simulate automated attack
2. Confirm unlimited attempts
3. Achieve potential credential success

## Instructions

### Step 1: Send to Intruder

**Context**: Load the captured request into Intruder for payload setup.

Right-click the request in Proxy > Send to Intruder.

> Intruder tab opens with the request template.

### Step 2: Configure Positions and Payloads

**Context**: Mark fields for brute forcing and set payloads.

Highlight username and password fields, click Add §.

In Positions tab, clear extras. In Payloads, load lists (e.g., usernames: admin, test; passwords: 123456, password).

Set attack type to Sniper or Cluster bomb.

### Step 3: Launch Attack

**Context**: Execute and analyze responses.

Click Start attack; review results for 200 vs 401 statuses.

> For POC, 9 attempts all return failures without blocks; success indicated by redirect to dashboard.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques

- [[Password Guessing]] Password Guessing

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[brute-force]]
- [[automation]]
