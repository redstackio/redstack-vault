---
tags:
  - server-verification
  - discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/view-hosts-file]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:24:17.698Z'
sub_techniques: []
id: e8908143-35dd-4505-8fae-eadaf5a50e66
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Verify Compromised Server Identity

## Summary

This procedure cross-references shell outputs with external Semrush resources to confirm the RCE occurred on a production server.

## Description

Using outputs from ls and cat /etc/hosts, manually inspect Semrush web paths like https://www.semrush.com/my_reports/[redacted] to match files. The /etc/hosts file should contain semrush.net entries, proving the target is the production instance vulnerable to ImageTragick.

## Requirements

1. Outputs from previous shell interaction
2. Browser access to Semrush domain
3. Noted paths from ls commands

## Defense

Defensive measures and detection strategies:

- Log file access attempts
- Monitor for cross-references between internal paths and external views
- Implement file integrity monitoring

## Objectives

1. Match shell-discovered files to web-visible resources
2. Confirm domain ownership via hosts
3. Validate production environment compromise

## Instructions

### Step 1: Review Shell Outputs

**Context**: Identify key indicators.

From previous session, note directories from [[commands/list-directory]] and hosts from [[commands/view-hosts-file]].

### Step 2: Cross-Verify Web Paths

**Context**: Confirm files exist publicly.

Navigate to https://www.semrush.com/my_reports/[redacted] and https://www.semrush.com/my_reports/[redacted] to check for matching files from ls [redacted dir].

**Expected Output**: Pages display expected Semrush application files.

### Step 3: Confirm Hosts

**Context**: Verify server affiliation.

Ensure /etc/hosts output includes entries like 127.0.0.1 localhost and semrush.net domains.

**Expected Output**: Semrush-specific hosts confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[System Information Discovery]] System Information Discovery

### Sub-Techniques


## Commands Used

- [[commands/view-hosts-file]]

## Tools Used


## Tags

- server-verification
- discovery
