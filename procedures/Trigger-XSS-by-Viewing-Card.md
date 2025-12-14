---
id: proc-uuid-4
tags:
  - xss
  - execution
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.079Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Viewing-Card

## Summary

This procedure accesses the malicious card's view page to execute the persisted XSS payload, demonstrating arbitrary JavaScript execution and potential data exfiltration like cookie theft.

## Description

In the Twitter Ads web application, viewing a card renders the stored card[name] without proper escaping, triggering the injected script in the authenticated viewer's context. This leads to JS execution, such as alerting document.cookie for session hijacking. Prerequisites: Created card with payload and its URL ID.

## Requirements

1. URL of the created card (e.g., with url_id)
2. Authenticated session of a target user (attacker or victim)
3. Browser to observe execution

## Defense

Defensive measures and detection strategies:

- Output encoding for all user-controlled data in HTML contexts
- Monitor for anomalous JS alerts or network requests from card views

## Objectives

1. Execute injected JavaScript in victim browser
2. Steal sensitive data like session cookies
3. Validate full exploit chain success

## Instructions

### Step 1: Navigate to Card View

**Context**: Load the page that renders the malicious card.

Enter the URL: https://ads.twitter.com/accounts/18ce53wrkma/cards/show?url_id=42qj.

> Page loads, injecting the payload into the DOM.

### Step 2: Observe Execution

**Context**: Confirm JS runs and impacts the session.

Watch for the alert box displaying document.cookie contents.

> Alert appears with cookie data; replace alert with exfil code for real attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
