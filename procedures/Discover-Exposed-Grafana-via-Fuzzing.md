---
tags:
  - fuzzing
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 4df94536-a6ed-4455-bdbc-d9b4e59f82dd
created_at: '2025-12-11T03:47:39.553Z'
updated_at: '2025-12-11T03:47:39.553Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1595]]'
---
# Discover Exposed Grafana via Fuzzing

## Summary

This procedure involves fuzzing URL patterns related to target projects to discover exposed Grafana instances, enabling initial reconnaissance for further exploitation.

## Description

By systematically testing variations in subdomains and paths associated with Snapchat projects, attackers can identify misconfigured Grafana endpoints that are publicly accessible. This targets web-based services without authentication, leading to potential information disclosure.

## Requirements

1. Access to the target's base domain (e.g., snapchat.com)
2. Wordlist for fuzzing (e.g., common project names, 'grafana' patterns)
3. Fuzzing tool like ffuf installed

## Defense

Defensive measures and detection strategies:

- Implement proper access controls on monitoring tools like Grafana
- Monitor for unusual HTTP traffic patterns indicating fuzzing attempts

## Objectives

1. Identify accessible Grafana endpoints
2. Confirm exposure without authentication
3. Map out potential attack surface

## Instructions

### Step 1: Prepare Fuzzing Wordlist

**Context**: Create or use a wordlist with Snapchat-related patterns like 'grafana', 'metrics', 'dashboards'.

**Command** ([[commands/ffuf-fuzz-subdomains]]):
```bash
ffuf -u https://snapchat.com/FUZZ -w wordlist.txt -fc 404
```

> This command fuzzes the URL and filters out 404 responses to find valid endpoints.

### Step 2: Analyze Results

**Context**: Review output for Grafana instances.

> Manually verify discovered URLs in a browser or with curl.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques

## Commands Used

- [[commands/ffuf-fuzz-subdomains]]

## Tools Used

- #ffuf

## Tags

- #fuzzing
- #recon
