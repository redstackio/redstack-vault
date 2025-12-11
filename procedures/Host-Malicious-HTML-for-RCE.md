---
tags:
  - hosting
  - payload
  - rce
type: procedure
tools:
  - '[[tools/headless_shell]]'
  - '[[tools/Metasploit]]'
  - '[[tools/Python-SimpleHTTPServer]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Linux
techniques:
  - '[[Command-Line Interface]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: b986c4ac-2363-45a3-8b54-db66ab66c30e
created_at: '2025-12-11T03:47:47.806Z'
updated_at: '2025-12-11T03:47:47.806Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059]]'
---
# Host Malicious HTML for RCE

## Summary

This procedure hosts a malicious HTML file using a simple Python HTTP server, which is loaded by the vulnerable Chromium to trigger RCE.

## Description

The malicious HTML contains JavaScript that exploits the outdated Chromium version, executing commands like uname or curl when loaded. Hosting it on port 8000 allows the target Kibana instance to fetch and process it during reporting jobs.

## Requirements

1. Python installed
2. Malicious HTML file prepared (e.g., with RCE payload)
3. Open port 8000 on the attacker machine

## Defense

Defensive measures and detection strategies:

- Monitor outbound connections from Kibana to unknown hosts
- Implement URL whitelisting in reporting features

## Objectives

1. Serve the exploit payload
2. Enable remote loading by the target
3. Prepare for RCE triggering

## Instructions

### Step 1: Start HTTP Server

**Context**: Launch the simple HTTP server to host the current directory's files.

**Command** (#python-simplehttpserver):
```bash
python -m SimpleHTTPServer 8000
```

> This serves files like alexb-says-hi.html on port 8000, accessible via http://[attacker-ip]:8000/alexb-says-hi.html.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- None

## Commands Used

- #python-simplehttpserver

## Tools Used

- #python-simplehttpserver

## Tags

- hosting
- payload
- rce
