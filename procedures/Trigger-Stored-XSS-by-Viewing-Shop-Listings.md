---
tags:
  - xss
  - execution
  - session-theft
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T03:46:31.330Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3a54d03d-b445-49a8-85f3-902b690a2cfc
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Trigger Stored XSS by Viewing Shop Listings

## Summary

This procedure demonstrates rendering the shop listings page to execute the stored XSS payload, potentially stealing viewer session cookies.

## Description

The shop name is displayed without encoding on the listings page, causing the injected script to run in the viewer's browser. This can lead to cookie exfiltration or other actions. Use a separate session to simulate victim viewing. Expected outcome: Script execution and data theft.

## Requirements

1. Payload successfully saved
2. Public or shareable shop URL
3. Attacker server to receive exfiltrated data

## Defense

Defensive measures and detection strategies:

- Output encode all user-generated content (e.g., HTML-escape shop names)
- Monitor for unexpected script executions via CSP violation reports
- Detect anomalous network requests from client-side scripts

## Objectives

1. Execute the stored JavaScript
2. Steal session information
3. Confirm impact on victim browsers

## Instructions

### Step 1: Access Listings Page

**Context**: Visit the shop URL to render the vulnerable shop name.

Navigate to `https://lp.reverb.com/shops/{shop-slug}/listings` in a new browser session.

> The page loads, and the shop name triggers the script. Expected output: Alert (test) or HTTP request to attacker domain with cookies.

### Step 2: Verify Execution

**Context**: Check for signs of payload success.

Monitor browser console or network tab for script activity.

> Look for alert dialog or outgoing request containing `document.cookie`. Success if data is exfiltrated.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[session-theft]]
