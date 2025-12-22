---
id: proc-uuid-003
tags:
  - phishing
  - drive-by
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:50.103Z'
skill_level: low
impact_level: low
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure-Victim-to-Attacker-Page

## Summary

This procedure describes social engineering the victim to visit the attacker-controlled webpage, triggering cross-origin requests to HackerOne endpoints in their authenticated session.

## Description

In a web-based attack scenario, the victim must be logged into HackerOne. The attacker uses phishing or links to direct them to the malicious page, where the browser automatically loads `<img>` resources from the endpoints, allowing timing measurements without further interaction.

## Requirements

1. Victim authenticated on HackerOne
2. Social engineering vector (email, link)
3. No technical barriers like pop-up blockers

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Browser extensions blocking cross-origin trackers
- Endpoint logging for unusual referrers

## Objectives

1. Gain victim's browser execution context
2. Trigger authenticated requests passively
3. Capture timings from successful responses only

## Instructions

### Step 1: Distribute Malicious Link

**Context**: Send the page URL via email or message pretending legitimacy.

**Command** (No technical command; social):
Craft phishing email: "Check this HackerOne update: [attacker-page-url]"

> Victim clicks and loads page.

### Step 2: Verify Request Trigger

**Context**: Monitor for page load; errors (400/500) won't yield timings.

**Command** (Console Check):
On victim side (unseen), page executes JS to log resources.

> Success if 200 responses appear in performance entries.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[initial-access]]
