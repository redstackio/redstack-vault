---
tags:
  - xss-trigger
  - exfiltration
  - admin-compromise
type: procedure
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Keylogging]]'
updated_at: '2025-12-14T00:11:09.778Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: e40d3bcd-18c2-404b-99d8-33ee9cacfd5e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Keylogging]]'
---
# Trigger-Blind-XSS-on-Admin-Review

## Summary

This procedure monitors for the execution of the injected Blind XSS payload when an administrator reviews the submitted feedback on an internal domain, capturing exfiltrated data like session cookies.

## Description

After submission, the payload remains dormant until an admin accesses the internal review panel (on a non-public Rockstar domain). Upon rendering the comment, the script executes in the admin's browser context, loading the external resource and enabling theft of sensitive data. Impacts include cookie exfiltration for account takeover, exposure of internal paths, user IPs/usernames, and potential RCE via Angular JS if the panel uses it.

## Requirements

1. External server logging callback requests (e.g., xss.ht with logging)
2. Patience for admin interaction (may take hours/days)
3. Tools to analyze captured data (e.g., cookie parsers)

## Defense

Defensive measures and detection strategies:

- Isolate admin panels with separate authentication and CSP
- Audit comment rendering for XSS with automated scanners
- Alert on external domain accesses from internal IPs

## Objectives

1. Confirm payload execution via callback
2. Exfiltrate admin session data and internal info
3. Assess escalation potential (e.g., to RCE)

## Instructions

### Step 1: Monitor Callback Server

**Context**: Set up logging on the external domain to capture requests from the admin's browser.

Configure your server at https://abhartiya.xss.ht to log incoming GET requests, including headers (cookies, User-Agent) and query params.

**Expected Output**: Log entries showing script load from internal Rockstar IP, with stolen data.

### Step 2: Analyze Exfiltrated Data

**Context**: Review captured info for further exploitation.

Parse logs for session cookies, internal URLs, user data. Use them to hijack admin sessions or map internal network.

**Expected Output**: Valid cookies for takeover; exposed paths like internal admin domains.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Keylogging]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- exfiltration
