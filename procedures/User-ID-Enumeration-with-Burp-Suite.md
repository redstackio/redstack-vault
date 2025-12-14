---
id: proc-uuid-002
tags:
  - enumeration
  - idor
  - discovery
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.139Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# User-ID-Enumeration-with-Burp-Suite

## Summary

This procedure uses Burp Suite to enumerate predictable sequential user IDs on the DoD website, exploiting IDOR to access unauthorized profiles and identify targets for connection requests.

## Description

The attack scenario targets a web application where user profiles are accessible via URLs with sequential ID parameters (e.g., https://█████/███████?id=1). By incrementing IDs in intercepted requests, an attacker can discover valid accounts without proper authorization checks. This is performed in an authenticated session post-signup. Prerequisites include an active Burp Suite proxy setup and knowledge of the profile endpoint. Expected outcomes are a list of enumerable user IDs leading to partial profile leaks.

## Requirements

1. Authenticated session from account creation
2. Burp Suite configured as browser proxy
3. Target profile URL identified (e.g., https://█████/███████)

## Defense

Defensive measures and detection strategies:

- Enforce indirect object references with server-side authorization checks
- Use non-sequential, random UUIDs for user identifiers
- Log and alert on sequential ID access patterns

## Objectives

1. Discover valid user IDs through predictable sequencing
2. Access unauthorized profiles for reconnaissance
3. Compile list of targets for mass requests

## Instructions

### Step 1: Intercept Profile Request

**Context**: Capture a request to your own profile to identify the ID parameter.

Configure Burp Suite proxy and browse to your profile URL.

> Intercepted request shows ID parameter; modify to id=1 and forward to test access.

### Step 2: Sequential Enumeration

**Context**: Increment IDs to find valid users.

In Burp Repeater, change ID from your own (e.g., 1000) to 1, 2, 3..., up to thousands, checking for successful responses (200 OK with profile data).

> Valid IDs return profile snippets; invalid ones may 404 or redirect. Log accessible IDs.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[enumeration]]
- [[idor]]
