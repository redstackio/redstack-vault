---
tags:
  - social-engineering
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
updated_at: '2025-12-14T17:27:30.088Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 8bd59777-9998-45db-8cbd-ce9e485684d2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victim-into-Loading-CSRF-Page

## Summary

This procedure uses social engineering to lure a victim into visiting an attacker-controlled page that triggers the CSRF exploit, relying on the victim's active authentication to Zomato.

## Description

CSRF attacks require the victim to be logged in and interact with a malicious site. Here, the attacker delivers a link disguised as benign content, leading the victim to load the page and inadvertently submit the forged request. This step is crucial for the attack's success, as it bridges the gap between preparation and execution in a web environment.

## Requirements

1. Contact method with the victim (email, chat, social media)
2. Crafted pretext to make the link appear legitimate
3. Hosted malicious page from previous procedure

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Use browser extensions to warn about cross-site requests
- Implement site isolation and strict CSP headers

## Objectives

1. Gain victim's browser interaction with malicious site
2. Ensure session cookies are present for authentication
3. Trigger the CSRF without alerting the user

## Instructions

### Step 1: Prepare Delivery Vector

**Context**: Choose and set up a method to send the link.

Select email or messaging; craft a message like "Check out this Zomato deal: [malicious URL]" to entice clicks.

### Step 2: Send the Link

**Context**: Deliver the payload to the victim.

Send the message containing the hosted HTML page URL. Time it when the victim is likely active on Zomato.

### Step 3: Monitor Execution

**Context**: Verify the victim loads the page.

If possible, log accesses to the hosted page or follow up to confirm the disconnect occurred on the victim's profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[Phishing]]
