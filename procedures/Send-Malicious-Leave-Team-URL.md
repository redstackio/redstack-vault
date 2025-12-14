---
id: proc-liberapay-malicious-url-001
tags:
  - phishing
  - url-crafting
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
  - '[[T1566.001]]'
updated_at: '2025-12-14T03:47:18.339Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Send-Malicious-Leave-Team-URL

## Summary

This procedure constructs a malicious URL targeting the team leave endpoint with a tainted back_to parameter and delivers it to the victim via social engineering.

## Description

Using the team slug, craft a URL like https://en.liberapay.com/jio/membership/leave?back_to=http://example.com/ for open redirect or ?back_to=javascript:alert(document.domain) for XSS. The victim must be a team member and authenticated. Send via email or chat to lure the victim to click it, prompting the leave confirmation page.

## Requirements

1. Team slug from creation step
2. Attacker-controlled domain or JS payload
3. Victim's contact method (email/messaging)
4. Victim as team member

## Defense

Defensive measures and detection strategies:

- Validate back_to parameter against allowlist of domains
- Block javascript: and other dangerous protocols
- Educate users on suspicious URLs

## Objectives

1. Deliver payload to victim for interaction
2. Ensure authentication on the leave page
3. Set up for redirect trigger on cancel

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the URL with open redirect or XSS payload.

No specific command; manually craft https://en.liberapay.com/jio/membership/leave?back_to=javascript:alert(document.domain).

> URL ready for sharing; test in browser to confirm reflection.

### Step 2: Deliver to Victim

**Context**: Social engineer the victim to access the URL.

No specific command; send via email: "Please review team leave: [URL]".

> Victim clicks, authenticates if needed, and sees leave page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment (adapted for URL)

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- phishing
- url-crafting
