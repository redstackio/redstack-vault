---
tags:
  - xss
  - shopify
  - session-management
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 668c8e3b-2f9b-4465-af66-158bb5040779
created_at: '2025-12-14T00:11:16.775Z'
updated_at: '2025-12-14T00:11:16.775Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Logout from Shopify Account

## Summary

This procedure logs out from the Shopify account to access the login page where the XSS vulnerability can be exploited.

## Description

Logging out ensures the user is directed to the login interface, which includes the vulnerable Google login option. This is a simple preparatory step in the attack chain for web-based exploits.

## Requirements

1. Active Shopify session
2. Web browser

## Defense

Defensive measures and detection strategies:

- Implement session monitoring
- Use multi-factor authentication

## Objectives

1. Clear current session
2. Access login page
3. Prepare for URL manipulation

## Instructions

### Step 1: Initiate Logout

**Context**: Use the logout function in the Shopify interface.

Click the logout button or navigate to the logout endpoint.

> Redirects to login page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- xss
- shopify
