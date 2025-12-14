---
tags:
  - csrf
  - social-engineering
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:03.809Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 76ceeecb-3439-42c3-bf55-737025b57b78
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victim-into-Loading-Malicious-CSRF-Page

## Summary

This procedure uses social engineering to lure an authenticated Localize user to load the malicious HTML page, triggering the CSRF request and forcing invitation acceptance.

## Description

By hosting the forged form on an attacker-controlled domain and sending a deceptive link (e.g., via email claiming urgent collaboration), the victim's browser executes the request in their session context. This grants the attacker access to the private project without direct interaction.

## Requirements

1. Hosted malicious HTML page accessible via URL
2. Victim's email or contact method
3. Victim authenticated to Localize

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and unexpected links
- Implement CSRF tokens and SameSite=Strict cookies
- Monitor for rapid or anomalous access grants

## Objectives

1. Induce victim to visit malicious page
2. Execute forged request silently
3. Achieve unauthorized project access

## Instructions

### Step 1: Host the Malicious Page

**Context**: Make the HTML accessible over the web.

Upload the HTML to a hosting service (e.g., GitHub Pages, free web host) and obtain the public URL.

### Step 2: Craft Deceptive Lure

**Context**: Create a convincing pretext to click the link.

Send an email or message like "Check out this important update: [malicious-url]" while victim is likely logged into Localize.

**Expected Output**: Victim clicks and loads the page.

### Step 3: Verify Exploitation

**Context**: Confirm acceptance in attacker's dashboard.

Check Localize for new member in the project after victim interaction.

**Expected Output**: Invitation accepted, access granted.

**Success Indicators**:
- Project members list updated
- Sensitive data accessible

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[csrf]]
