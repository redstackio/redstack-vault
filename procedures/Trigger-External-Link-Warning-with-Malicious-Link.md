---
id: proc-uuid-2
tags:
  - phishing
  - external-link
type: procedure
tools:
  - '[[tools/Google-Chrome-Mobile]]'
  - '[[tools/Microsoft-Edge-Mobile]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Mobile
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:45.177Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Trigger-External-Link-Warning-with-Malicious-Link

## Summary

This procedure involves clicking a crafted malicious link within an authenticated HackerOne session on mobile to invoke the External Link Warning interstitial, exploiting the lack of domain highlighting.

## Description

Attackers can embed disguised links in reports, comments, or notifications on HackerOne. Examples include URLs like https://google.com@73.150.2.210/download/safest_file (disguising an IP) or query parameter tricks like http://www.hackerone.com?text_query=@evil.com/. On mobile Chrome and Edge, the warning triggers but fails to highlight the true destination, misleading users into approving phishing sites. Prerequisites include an active session; outcomes enable social engineering by obscuring the real target.

## Requirements

1. Authenticated HackerOne session
2. Access to a page with or ability to input malicious links
3. Mobile browser (Chrome or Edge) in latest version

## Defense

Defensive measures and detection strategies:

- Implement robust URL parsing and highlighting in all browser viewports
- Educate users on verifying full URLs before clicking
- Log and alert on external link interactions

## Objectives

1. Activate the External Link Warning mechanism
2. Demonstrate disguise of malicious domains
3. Facilitate user deception for phishing

## Instructions

### Step 1: Prepare Malicious Link

**Context**: Craft or locate a disguised link within the platform.

Examples: Use https://google.com@73.150.2.210/download/safest_file or http://www.hackerone.com%2Fbugs%3F...%3D@evil.com/.

> Expected output: Link is present and clickable in the authenticated session.

### Step 2: Click the Link

**Context**: Interact with the link to trigger the warning.

Manually click the malicious link in the browser.

> Expected output: External Link Warning interstitial appears.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Chrome-Mobile]]
- [[tools/Microsoft-Edge-Mobile]]

## Tags

- phishing
- external-link
