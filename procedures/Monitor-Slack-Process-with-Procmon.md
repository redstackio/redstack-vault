---
tags:
  - discovery
  - process-monitoring
type: procedure
tools:
  - '[[tools/Procmon]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Process Discovery]]'
updated_at: '2025-12-14T17:29:19.987Z'
sub_techniques: []
id: ec2ff57c-f33a-4a67-b996-8649b9471277
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Process Discovery]]'
---
# Monitor-Slack-Process-with-Procmon

## Summary

This procedure uses Process Monitor (Procmon) to observe file access attempts by Slack's Windows Desktop Client (slack.exe), identifying the hardcoded path to a non-existent OpenSSL configuration file.

## Description

In a Windows environment with Slack installed, attackers with local access can monitor slack.exe to discover vulnerabilities in its file loading behavior. By capturing process activity, the procedure reveals attempts to load C:\usr\local\ssl\openssl.cnf, which does not exist by default, enabling subsequent exploitation for code injection. This is useful in privilege escalation scenarios on shared systems like terminal servers.

## Requirements

1. Local access to a Windows machine with Slack installed
2. Administrative privileges not required for monitoring own processes
3. Procmon tool downloaded from Sysinternals

## Defense

Defensive measures and detection strategies:

- Monitor for Procmon or similar tools running on endpoints
- Implement application whitelisting to restrict monitoring tools
- Log file access attempts to sensitive paths like C:\usr\local\ssl\

## Objectives

1. Identify vulnerable file paths in slack.exe
2. Confirm non-existence of OpenSSL config for exploitation setup
3. Gather evidence for crafting targeted attacks

## Instructions

### Step 1: Launch Procmon and Configure Filters

**Context**: Start capturing system activity focused on slack.exe to observe file operations.

Launch Procmon as administrator for full visibility. Set filters: Process Name is slack.exe, Operation is CreateFile or QueryOpen. Start capture before launching Slack.

### Step 2: Trigger Slack Startup

**Context**: Force slack.exe to run and attempt file loads.

Start the Slack application or simulate login to trigger auto-start. Stop capture in Procmon after a few seconds.

### Step 3: Analyze Logs

**Context**: Review events for failed file accesses.

Filter results for PATH NOT FOUND results. Locate entries for C:\usr\local\ssl\openssl.cnf to confirm the hardcoded path.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Process Discovery]] Process Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Procmon]]

## Tags

- [[Discovery]]
- [[process-monitoring]]
