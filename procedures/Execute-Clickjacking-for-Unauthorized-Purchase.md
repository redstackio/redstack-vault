---
id: proc-clickjacking-execute-001
tags:
  - clickjacking
  - user-execution
  - unauthorized-purchase
  - web
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
  - '[[User Execution]]'
updated_at: '2025-12-14T17:28:51.943Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[User Execution]]'
---
# Execute-Clickjacking-for-Unauthorized-Purchase

## Summary

This procedure executes the clickjacking attack by luring a logged-in victim to interact with the malicious page, resulting in an invisible purchase using their saved credit card.

## Description

With the victim logged into Yelp and visiting the attacker's page, the overlaid button captures the click and forwards it to the hidden iframe's checkout form. This bypasses user awareness, charging the card for a deal (e.g., $450) without displaying the Yelp interface. The attack exploits user trust in the benign-looking page. Success is confirmed by transaction records; in testing, use a test account to avoid real charges.

## Requirements

1. Victim logged into Yelp in the same browser session
2. Hosted malicious clickjacking page ready
3. Social engineering method to direct victim to the page (e.g., email link)
4. Access to victim's account for verification post-attack

## Defense

Defensive measures and detection strategies:

- User training on suspicious links and unexpected prompts
- Browser extensions or settings to warn about iframes and overlays
- Anomaly detection in transaction logs for sudden purchases without search history
- Rate limiting on checkout endpoints

## Objectives

1. Induce victim interaction with the overlay
2. Propagate click to complete hidden purchase
3. Achieve monetary impact without direct credential theft

## Instructions

### Step 1: Lure Victim to Malicious Page

**Context**: Use phishing or direct inducement to get the logged-in victim to load the attack page.

Send a link disguised as a deal alert (e.g., "Click here for free Yelp deal!") pointing to the hosted HTML.

### Step 2: Trigger the Click

**Context**: Have the victim interact with the visible button, which hijacks the click event to the iframe.

Instruct or observe the victim clicking "Purchase Now"; the event targets the iframe's submit button coordinates.

### Step 3: Verify Unauthorized Transaction

**Context**: Confirm the attack success by checking Yelp account activity.

Log into the victim's account or monitor email for purchase confirmation; inspect for the charged deal ID.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[User Execution]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[clickjacking]]
- [[user-execution]]
- [[unauthorized-purchase]]
- [[web]]
