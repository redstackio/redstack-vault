---
id: proc-1066410-002
tags:
  - url-shortening
  - endpoint-discovery
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/grep-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:32:39.495Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify URL Shortening Endpoint

## Summary

This procedure scans application JavaScript for URL shortening endpoints, revealing potential attack vectors like misconfigured redirect services.

## Description

URL shorteners often rely on third-party APIs like Firebase Dynamic Links. By analyzing client-side code, attackers can identify endpoints such as lnk.clario.co, understanding how links are generated and validated. This sets up exploitation of misconfigurations. Target environment: Web apps with exposed JS. Outcomes: Endpoint URL and basic usage pattern identified.

## Requirements

1. Access to downloaded JS file from reconnaissance
2. Text search tools like grep
3. Understanding of URL patterns in code

## Defense

Defensive measures and detection strategies:

- Minimize exposure of internal endpoints in client-side code
- Use code splitting or server-side rendering to hide logic
- Log and monitor access to shortening services

## Objectives

1. Locate the shortening service URL
2. Infer validation mechanisms (e.g., regex)
3. Prepare for targeted exploitation

## Instructions

### Step 1: Search for Shortening Patterns

**Context**: Identify references to the shortening domain in the JS code.

**Command** ([[commands/grep-endpoint]]):
```bash
grep -i 'lnk.clario.co' main.js
```

> Finds endpoint mentions. Expected output: https://lnk.clario.co/?link=[URLHERE].

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/grep-endpoint]]

## Tools Used


## Tags

- url-shortening
- endpoint-discovery
- reconnaissance
