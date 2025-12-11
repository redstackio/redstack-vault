---
tags:
  - subdomain-takeover
  - content-hosting
type: procedure
tools:
  - '[[tools/HubSpot]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/dig-dns-lookup]]'
  - '[[commands/curl-host-content]]'
platforms:
  - Web
techniques:
  - '[[Compromise Infrastructure]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 624bc47c-56e4-4cb5-bd9c-0a4173eede98
created_at: '2025-12-11T06:10:30.544Z'
updated_at: '2025-12-11T06:10:30.544Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0003]]'
mitre_techniques:
  - '[[T1584]]'
---
# Host Malicious Content on Taken-Over Subdomain

## Summary

This procedure uploads and serves malicious content like proof-of-concept pages or scripts on the claimed subdomain via HubSpot.

## Description

After claiming, attackers can upload HTML, PHP, or JS files to demonstrate control or execute attacks. In the report, a PoC page was hosted at /subdomain-takeover on devrel.roblox.com.

## Requirements

1. Claimed HubSpot instance
2. Malicious content files (e.g., HTML, PHP)
3. Access to HubSpot dashboard

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring tools
- Use DNSSEC to prevent unauthorized changes

## Objectives

1. Serve arbitrary content on target subdomain
2. Demonstrate takeover
3. Prepare for further exploitation

## Instructions

### Step 1: Upload Content via HubSpot

**Context**: Use HubSpot interface to upload files.

Manual step: In HubSpot dashboard, create and upload content to /subdomain-takeover.

> Expected: Content is published.

### Step 2: Verify Hosting

**Context**: Test access to hosted content.

**Command** ([[commands/curl-host-content]]):

```bash
curl https://devrel.roblox.com/subdomain-takeover
```

> Expected: Returns the uploaded PoC content.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Compromise Infrastructure]]

### Sub-Techniques



## Commands Used

- [[commands/curl-host-content]]

## Tools Used

- [[tools/HubSpot]]

## Tags

- [[subdomain-takeover]]
- [[content-hosting]]
