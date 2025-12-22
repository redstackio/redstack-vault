---
id: proc-host-csrf-phish
tags:
  - phishing
  - hosting
  - social-engineering
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:27:42.929Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Host-Malicious-Page-and-Trick-Admin

## Summary

This procedure deploys the malicious HTML on a public server and uses social engineering to lure the channel admin into visiting it, triggering the CSRF request via the browser.

## Description

The crafted HTML is hosted on a site like http://asanso.github.io/csrf.html. The attacker sends a disguised link to the admin (e.g., via email or chat). When visited, the admin's authenticated Slack session allows the forged request. Target environment is web browsers and email/Slack for delivery. Expected outcome is automatic mode switch without admin awareness.

## Requirements

1. Hosted HTML file
2. Contact method with admin (e.g., email)
3. Plausible pretext for link

## Defense

Defensive measures and detection strategies:

- Train users on phishing link avoidance
- Use URL scanners before clicking
- Log cross-site requests in Slack

## Objectives

1. Deliver malicious payload via link
2. Exploit admin's session
3. Achieve unauthorized state change

## Instructions

### Step 1: Host HTML

**Context**: Upload to public hosting.

No specific command; push to GitHub Pages or use a free host; URL becomes http://example.com/csrf.html.

> Confirm accessibility without auth.

### Step 2: Send Phishing Link

**Context**: Trick admin into visiting.

No specific command; craft message: "Check this resource: [link]" and send via email or DM.

> Admin's browser loads page, sending GET to Slack URI.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.001]] Spearphishing Attachment (adapted for link)

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[hosting]]
