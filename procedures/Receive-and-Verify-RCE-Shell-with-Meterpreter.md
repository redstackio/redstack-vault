---
id: proc-receive-rce-shell
tags:
  - meterpreter
  - reverse-shell
type: procedure
tools:
  - '[[tools/Metasploit]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Linux
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:37.219Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Receive-and-Verify-RCE-Shell-with-Meterpreter

## Summary

This procedure monitors the Metasploit console to receive the Meterpreter reverse shell established by the exploited Chromium during the reporting job, verifying full RCE control.

## Description

Once the reporting job triggers, Chromium loads the redirected exploit page, executes the payload, and connects back to the attacker's Metasploit instance. Verify with commands like sysinfo or shell. This grants arbitrary execution on the Kibana host, potentially escalating to Elasticsearch.

## Requirements

1. Metasploit exploit server running.
2. Reporting job triggered.
3. Firewall allows inbound from target.
4. Public IP configured.

## Defense

Defensive measures and detection strategies:

- Block outbound connections from Kibana to unknown IPs.
- Monitor for Meterpreter beacons or unusual processes.
- Isolate reporting Chromium in sandboxed environments.

## Objectives

1. Establish persistent shell.
2. Confirm host compromise.
3. Enable further exploitation.

## Instructions

### Step 1: Monitor for Session

**Context**: Watch Metasploit for incoming connection post-job.

In msfconsole, the session appears automatically. Expected: 'Meterpreter session 1 opened'.

### Step 2: Interact and Verify

**Context**: Use shell to run commands.

```msf
sessions -i 1
sysinfo
shell
uname -a
```

> Expected output: System details matching Kibana container; full command execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Metasploit]]

## Tags

- meterpreter
- reverse-shell
