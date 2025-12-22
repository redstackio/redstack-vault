---
id: proc-demonstrate-token-stealing-poc
tags:
  - csrf-leak
  - poc
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:52:34.301Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Token Stealing in POC Setup

## Summary

This procedure sets up and triggers a proof-of-concept to capture a CSRF token via the CSS injection exploit in a simulated environment.

## Description

Using a provided POC site, reset the environment and inject the CSS payload to steal the token. This mirrors real-world impact where an attacker tricks a victim into loading the malicious embed URL, leaking their token for CSRF attacks. Outcomes include token capture in logs or interface.

## Requirements

1. Access to POC URLs (e.g., pythonanywhere.com demo).
2. Browser for URL navigation.
3. Basic understanding of the injection from prior steps.

## Defense

Defensive measures and detection strategies:

- Validate embed parameters server-side with strict parsing.
- Log and alert on embed loads with suspicious bgcolor values.
- Educate users on phishing risks with embedded content.

## Objectives

1. Reset POC for clean test.
2. Trigger injection and capture token.
3. Validate leak mechanism.

## Instructions

### Step 1: Reset POC Environment

**Context**: Clear any prior state to start fresh.

Navigate to:

```url
http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR/reset
```

> This resets the token and setup.

### Step 2: Trigger Injection and Capture

**Context**: Load the main POC with the vulnerable embed.

Navigate to:

```url
http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR
```

> Observe the CSS injection applying styles; check POC output for captured token.

**Expected Output**: Token displayed or logged in the POC demo.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf-leak]]
- [[poc]]
