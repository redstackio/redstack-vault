---
id: proc-cms-discovery-001
tags:
  - path-discovery
  - cms-enumeration
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-browse]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:24:15.251Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Discover-and-Access-CMS-Login

## Summary

Procedure to guess and access hidden CMS paths based on footer hints, leading to a login form in legacy systems.

## Description

After identifying the 'xxxx CMS' from the footer, the attacker tried common paths and accessed /xxxx, which redirected to /josso/signin. This targets misconfigured or forgotten admin interfaces on subdomains.

## Requirements

1. Identified CMS name from prior recon
2. Access to common web paths
3. No credentials initially

## Defense

- Remove default or guessable paths
- Enforce authentication on all admin endpoints
- Log and alert on path probing attempts

## Objectives

1. Locate admin login interfaces
2. Confirm CMS presence
3. Prepare for credential testing

## Instructions

### Step 1: Test Common Paths

**Context**: Probe for robots.txt and guessed CMS path.

**Command** ([[commands/curl-browse]]):
```bash
curl -i http://www.example.starbucks.com.sg/robots.txt
curl -i http://www.example.starbucks.com.sg/xxxx
```

> robots.txt yields no results; /xxxx redirects to login form.

### Step 2: Access Login Form

**Context**: Follow redirect to /josso/signin.

**Command** ([[commands/curl-browse]]):
```bash
curl -L http://www.example.starbucks.com.sg/xxxx
```

> Displays login page for credential attempts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-browse]]

## Tools Used

- None

## Tags

- [[path-discovery]]
- [[cms-enumeration]]
