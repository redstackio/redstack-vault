---
tags:
  - csrf
  - phishing
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.875Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: fd37b6d8-481b-4957-817f-0e6836d3065d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Deliver-CSRF-Payload-to-Victim-via-Social-Engineering

## Summary

This procedure covers tricking a Twitter user into visiting a malicious page hosting the CSRF form, executing the attack when their authenticated session submits the forged request.

## Description

Delivery relies on social engineering, such as phishing emails, malicious links in messages, or compromised sites redirecting to the payload. The victim must be logged into Twitter for session cookies to authenticate the request. Upon page load, the form submits to the curator endpoint, adding the tweet. This disrupts curated content or enables further spam/phishing. Prerequisites: Hosted payload and victim contact method. Expected outcome: Silent execution leading to unauthorized changes.

## Requirements

1. Hosted malicious HTML page accessible via URL
2. Social engineering vector (email, DM, etc.)
3. Victim's Twitter login state (no direct control needed)

## Defense

Defensive measures and detection strategies:

- User training on suspicious links and staying logged out on untrusted sites
- Web application firewalls to detect cross-site POSTs
- Anomaly detection in user behavior and collection edits

## Objectives

1. Lure victim to payload without raising suspicion
2. Ensure execution in authenticated context
3. Confirm impact via collection verification

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Select and set up a method to send the link, disguising it as legitimate (e.g., 'Check this tweet' in a DM).

Craft a message with the URL to your hosted HTML, e.g., via email or Twitter DM: "Hey, thought you'd like this tweet: [malicious-link.com]".

**Expected Output**: Convincing lure ready for distribution.

### Step 2: Execute Delivery and Monitor

**Context**: Send the link and wait for victim interaction.

Distribute the lure to the target. Once clicked and loaded in their browser (while logged in), the form submits automatically.

**Expected Output**: Tweet added; verify by checking victim's public collection or follow-up.

**Success Indicators**:
- Page load confirmed (e.g., via server logs)
- Collection modified as intended

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
- [[social-engineering]]
