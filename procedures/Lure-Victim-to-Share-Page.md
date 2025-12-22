---
tags:
  - xss
  - stored-xss
  - social-engineering
  - phishing
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.170Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 94e2309f-91f0-4373-a0d0-69994ec7c9e7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Lure-Victim-to-Share-Page

## Summary

This procedure uses social engineering to direct a victim to the malicious share URL, exposing their browser to the stored XSS payload on the api.mapbox.com page.

## Description

The share page displays the map and unsanitized title, but execution requires clicking the share control. Attackers employ phishing emails, messages, or links disguised as legitimate map shares to lure victims. Prerequisites include the share URL and a delivery method. Expected outcomes: Victim loads the page, rendering the payload in a non-executing context initially.

## Requirements

1. Valid share URL from previous step
2. Communication channel to victim (email, chat)
3. Plausible pretext for sharing the map

## Defense

Defensive measures and detection strategies:

- Educate users on suspicious links from unknown sources
- Implement URL scanning in email gateways for known malicious domains
- Monitor access logs on api.mapbox.com for unusual traffic patterns

## Objectives

1. Get victim to visit the share page
2. Ensure page loads without blocking
3. Position for the triggering interaction

## Instructions

### Step 1: Craft Lure Message

**Context**: Create a convincing pretext.

Prepare a message like "Check out this interesting map I found: [URL]".

### Step 2: Deliver URL

**Context**: Send to victim.

Distribute via email, social media, or direct message.

### Step 3: Confirm Access

**Context**: Verify victim interaction.

Ask the victim if they viewed the map or monitor for execution if payload includes callbacks.

**Expected Output**: Victim reports seeing the map page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[social-engineering]]
- [[Phishing]]
