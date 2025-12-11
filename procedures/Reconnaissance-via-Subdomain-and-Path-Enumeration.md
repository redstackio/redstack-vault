---
tags:
  - recon
  - subdomain-enum
type: procedure
tools:
  - '[[tools/jexboss]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-path-manipulation]]'
  - '[[commands/curl-directory-traversal]]'
  - '[[commands/jexboss-exploit]]'
platforms:
  - Web
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0aec3774-a71d-4296-b5e7-cb3efecb9dae
created_at: '2025-12-11T06:10:24.967Z'
updated_at: '2025-12-11T06:10:24.967Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0043]]'
mitre_techniques:
  - '[[T1595]]'
---
# Reconnaissance via Subdomain and Path Enumeration

## Summary

This procedure involves enumerating subdomains and fuzzing paths to identify exposed CMS components and login forms on a target web server.

## Description

In this attack scenario, reconnaissance targets an old subdomain running a custom CMS. By appending the CMS name to paths, a redirect to a login form is triggered, revealing potential entry points for further exploitation. This is useful in mapping the attack surface without authentication.

## Requirements

1. Access to the target subdomain via HTTP
2. Basic HTTP client like curl
3. Knowledge of potential CMS names from footer or source code

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on paths to prevent fuzzing
- Monitor logs for unusual path requests and redirects

## Objectives

1. Discover login forms and internal paths
2. Identify CMS for targeted exploitation
3. Map the web application's structure

## Instructions

### Step 1: Enumerate Subdomains and Paths

**Context**: Scan for subdomains and append CMS name to trigger redirects.

**Command** ([[commands/curl-path-manipulation]]):
```bash
curl -i "http://subdomain.starbucks.com/<CMS-name>"
```

> This requests the path and observes redirects to /josso/signin.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques



## Commands Used

- [[commands/curl-path-manipulation]]

## Tools Used



## Tags

- [[recon]]
- [[subdomain-enum]]
