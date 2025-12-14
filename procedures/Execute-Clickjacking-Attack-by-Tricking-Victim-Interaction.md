---
tags:
  - clickjacking
  - social-engineering
  - credential-theft
  - phishing
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.871Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 1883e708-a5fb-4caa-b91f-0c8c3f5bda59
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-Clickjacking-Attack-by-Tricking-Victim-Interaction

## Summary

This procedure operationalizes the clickjacking setup by luring victims to the malicious page and inducing clicks on the embedded Twitter card button, resulting in the theft of their email addresses and usernames.

## Description

In the attack scenario, the victim is directed to the attacker's hosted page via deceptive means. The iframe makes the click seem innocuous, but it submits credentials to the attacker's server. This targets unsuspecting Twitter users in a web environment, with expected outcomes of successful data exfiltration logged on the attacker's endpoint.

## Requirements

1. Hosted malicious HTML page from prior step
2. Method to distribute URL (e.g., email, social media)
3. Server to receive and log POSTed data

## Defense

Defensive measures and detection strategies:

- User training on recognizing phishing and suspicious sites
- Endpoint detection for anomalous data submissions
- Rate limiting on form submissions from Twitter pages

## Objectives

1. Induce victim visit and interaction
2. Capture submitted credentials
3. Maintain stealth to avoid detection

## Instructions

### Step 1: Distribute Malicious Page

**Context**: Use social engineering to get the victim to visit the hosted URL.

Send the page link via a phishing email or tweet, e.g., "Click here to claim your Twitter promotion: [attacker-url]." Ensure the page overlays the iframe convincingly.

> Victim loads the page, seeing what appears to be a legitimate Twitter interface.

### Step 2: Monitor for Interaction

**Context**: Wait for the victim to click the embedded button, triggering data theft.

On the attacker's server, set up a simple endpoint (e.g., PHP or Node.js) to log POST requests containing email and username.

> Upon click, data is submitted automatically to the external domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[clickjacking]]
- [[social-engineering]]
- [[credential-theft]]
- [[Phishing]]
