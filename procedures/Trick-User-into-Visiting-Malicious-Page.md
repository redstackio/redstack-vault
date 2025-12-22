---
tags:
  - phishing
  - drive-by
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 654704f5-929b-4e93-a1a3-79c1e3ae53eb
created_at: '2025-12-14T17:33:34.477Z'
updated_at: '2025-12-14T17:33:34.477Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-User-into-Visiting-Malicious-Page

## Summary

Social engineering the authenticated user to visit the attacker's malicious page hosted on the bypass domain, enabling cross-origin postMessage exploitation.

## Description

While the victim is logged into a Digits-integrated site, the attacker sends a deceptive link (e.g., disguised as a site update or feature) pointing to https://www.d.gits.co/fabric.html. This loads the page in the browser context where the site's window is accessible for postMessage targeting.

## Requirements

1. Victim's contact info (email, chat) for phishing
2. Crafted phishing message
3. Malicious page ready on bypass domain

## Defense

Defensive measures and detection strategies:

- User training on phishing links
- Browser extensions blocking suspicious domains
- Site-side warnings for external navigations

## Objectives

1. Induce victim to load the malicious page while authenticated
2. Maintain session context for postMessage
3. Avoid detection during navigation

## Instructions

### Step 1: Craft Phishing Lure

**Context**: Create a convincing pretext for the link, e.g., 'Click to verify your Fabric.io integration'.

**Instructions**: Compose email or message with the link to the malicious page.

### Step 2: Send and Monitor

**Context**: Deliver the lure and wait for interaction.

**Instructions**: Send via email/SMS; use URL shortener if needed to obscure domain.

### Step 3: Confirm Visit

**Context**: Verify the page load to proceed.

**Instructions**: Add logging script to the page to notify attacker of visit (e.g., beacon to attacker's server).

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
- [[social-engineering]]
