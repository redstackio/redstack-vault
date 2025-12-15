---
tags:
  - reconnaissance
  - subdomain-enumeration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Turbo-Intruder]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/turbo-intruder-subdomain-enum]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:32:58.011Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: a6b26776-8df3-42e3-a36b-5c1216371c1d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Enumerate Subdomains of Target Domain

## Summary

This procedure uses high-speed fuzzing to discover subdomains of a target domain, identifying potential entry points like app.bountypay.h1ctf.com for further exploitation.

## Description

In web attack scenarios, subdomain enumeration reveals hidden services. Here, Turbo Intruder within Burp Suite scans *.bountypay.h1ctf.com using a common domain wordlist, confirming live hosts via HTTP responses. Prerequisites include Burp Suite setup and a wordlist like those from SecLists.

## Requirements

1. Burp Suite Professional with Turbo Intruder extension
2. Wordlist of common subdomains (e.g., app, admin, api)
3. Network access to target domain

## Defense

Defensive measures: Implement DNS rate limiting, monitor for anomalous queries; Detection: Log high-volume subdomain probes.

## Objectives

1. Identify live subdomains
2. Expand attack surface
3. Expected outcome: List of accessible subdomains

## Instructions

### Step 1: Configure Turbo Intruder

**Context**: Set up the fuzzer for subdomain discovery.

**Command** ([[commands/turbo-intruder-subdomain-enum]]):
```bash
# In Burp Suite Turbo Intruder: Payloads from wordlist, request: GET / HTTP/1.1\nHost: §s.bountypay.h1ctf.com
```

> This sends requests to potential subdomains, checking for 200 OK responses. Expected output: Live subdomains logged.

### Step 2: Analyze Results

**Context**: Filter valid responses.

No specific command; review Burp logs for successful connections.

> Expected output: Confirmed subdomains like app.bountypay.h1ctf.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques

- None

## Commands Used

- [[commands/turbo-intruder-subdomain-enum]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Turbo-Intruder]]

## Tags

- reconnaissance
- subdomain-enumeration
