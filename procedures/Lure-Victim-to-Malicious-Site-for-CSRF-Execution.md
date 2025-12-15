---
id: p3c4d5e6-f7g8-9012-cdef-3456789012
tags:
  - phishing
  - social-engineering
  - csrf
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.314Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure-Victim-to-Malicious-Site-for-CSRF-Execution

## Summary

This procedure uses social engineering to direct an authenticated Zomato user to the attacker's malicious site, triggering the CSRF form submission and manipulating photo likes on their behalf.

## Description

Once the malicious HTML is hosted, the attacker lures victims (who must be logged into Zomato) to the site via email, chat, or embedded links. The auto-submit executes the POST to the vulnerable endpoint, altering photo interactions without consent. This can be scaled for mass manipulation. Prerequisites: Hosted CSRF page, victim contact method. Expected outcomes: Unauthorized like/unlike actions, potential reputation damage.

## Requirements

1. Hosted malicious HTML page
2. Communication channel to victim (e.g., email, social media)
3. Victim authenticated in Zomato

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links
- Implement referrer checks or same-origin policy enforcement
- Monitor like/unlike rates for anomalies

## Objectives

1. Induce victim visit to trigger CSRF
2. Achieve unauthorized photo manipulation
3. Scale for en masse reputation impact

## Instructions

### Step 1: Craft Lure Message

**Context**: Create a convincing pretext to get the victim to click the link.

Prepare a phishing email or message: "Check out this funny Zomato photo: http://attacker-site.com/index.html".

**Expected Output**: Link shared with victim.

### Step 2: Monitor Execution

**Context**: Verify the attack succeeds upon visit.

Have the victim click; check Zomato photo for like count change. Use browser dev tools on victim side if possible.

**Expected Output**: POST request succeeds, like count updates.

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
- [[csrf]]
