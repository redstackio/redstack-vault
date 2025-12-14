---
id: proc-vimeo-observe-changes-001
tags:
  - information-disclosure
  - verification
  - collection
type: procedure
tools:
  - '[[tools/evil-swf]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
  - '[[Steal Web Session Cookie]]'
updated_at: '2025-12-14T17:27:36.202Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Steal Web Session Cookie]]'
---
# Observe-Leaked-Information-and-Verify-Changes

## Summary

This procedure captures and displays the disclosed user information from the 404 page and verifies the success of CSRF actions by checking the victim's Vimeo account for changes, confirming the attack's impact on privacy and settings.

## Description

After token theft and CSRF execution, the malicious page shows extracted data like user name, ID, and account type in UI boxes. The attacker or victim then logs into Vimeo to observe updates: immediate name change and delayed video privacy shifts, demonstrating full compromise including info leak and unauthorized exposure of private videos.

## Requirements

1. Data extracted from previous token theft step
2. Access to victim's Vimeo account for verification
3. Malicious page with display capabilities

## Defense

Defensive measures and detection strategies:

- Sanitize error pages to exclude sensitive data
- Implement account change notifications via email/SMS
- Monitor for bulk privacy changes or unusual settings updates

## Objectives

1. Display stolen user information for attacker use
2. Confirm CSRF success through account inspection
3. Assess overall impact like public video exposure

## Instructions

### Step 1: Display Leaked Information

**Context**: Parse and show user details from the 404 HTML on the POC page.

In the HTML/JS accompanying evil.swf:

```javascript
// Assuming token theft callback passes data
document.getElementById('info-box').innerHTML = `Name: ${userName}<br>ID: ${userId}<br>Type: ${accountType}`;
```

> Populates boxes with data. Expected: Visible disclosure of sensitive info.

### Step 2: Verify Account Changes

**Context**: Manually check Vimeo's dashboard for modifications.

Log into https://vimeo.com/settings and inspect:

- Name field for updates
- Videos tab for privacy status (wait 1-2 minutes if needed)

> Expected: Name changed; private videos now public. Success: Changes confirmed.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System (adapted to web)
- [[Steal Web Session Cookie]] Steal Web Session Cookie

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/evil-swf]]

## Tags

- verification
- data-leak
- account-compromise
