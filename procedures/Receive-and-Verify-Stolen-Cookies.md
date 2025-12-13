---
tags:
  - cookie-theft
  - exfiltration
  - session-hijacking
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 91b9b2d2-63ec-4089-9a7d-4bf562b73f95
created_at: '2025-12-13T09:01:26.234Z'
updated_at: '2025-12-13T09:01:26.234Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Steal Web Session Cookie]]'
---
# Receive and Verify Stolen Cookies

## Summary

This procedure covers polling an attacker-controlled server to receive and verify stolen session cookies from hijacked victim requests via the exploited vulnerability.

## Description

Using Burp Collaborator, interactions are polled to retrieve leaked data including IP addresses and cookies like the 'd' session cookie. This enables account takeovers. The procedure assumes prior payload sending and requires the Collaborator Client.

## Requirements

1. Burp Suite Collaborator Client
2. Successful payload execution
3. Active polling setup

## Defense

Defensive measures and detection strategies:

- Implement secure cookie flags (HttpOnly, Secure)
- Monitor for unexpected outbound connections

## Objectives

1. Exfiltrate session cookies
2. Verify stolen data usability
3. Achieve account takeover potential

## Instructions

### Step 1: Poll Burp Collaborator

**Context**: Retrieve interactions to view stolen cookies.

> Click 'Poll now' in the Collaborator Client to fetch DNS and HTTP data, including victim cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Steal Web Session Cookie]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- cookie-theft
- exfiltration
