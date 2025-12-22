---
tags:
  - clickjacking
  - demonstration
  - user-trickery
  - web
type: procedure
tools:
  - '[[tools/Bootstrap]]'
  - '[[tools/jQuery]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:04.369Z'
sub_techniques: []
id: 05d60427-8321-4401-be6c-82d70b073403
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-ClickJacking-Attack-on-Yelp

## Summary

This procedure simulates the full ClickJacking attack by hosting the POC page and guiding a victim to interact with it, resulting in unauthorized changes to Yelp business information.

## Description

In this web attack on Yelp, an authenticated user is lured to the malicious page, where visible fake elements overlay a hidden iframe of the editing endpoint. User interactions (e.g., filling fake fields and submitting) trigger real submissions, altering details like address or website. This leads to impacts such as customer confusion or attacker site diversion. Prerequisites: Hosted POC and victim with Yelp login. Outcomes: Verified unauthorized modifications.

## Requirements

1. Hosted malicious page accessible via URL
2. Victim with active Yelp session and business edit access
3. Monitoring tools to verify changes on Yelp

## Defense

Defensive measures and detection strategies:

- Enable frame-ancestors in CSP to block external iframes
- Log and alert on anomalous business edits
- User training on verifying form legitimacy

## Objectives

1. Lure and trick the victim into interacting with the page
2. Execute hidden form submission
3. Confirm impact through modified business data

## Instructions

### Step 1: Host and Lure Victim

**Context**: Deploy the POC and direct the victim to it, e.g., via phishing email posing as a survey.

Upload the HTML to a web server and share the URL.

> Ensure the victim is logged into Yelp before visiting.

### Step 2: Observe Interaction and Submission

**Context**: Monitor as the victim clicks fake elements, triggering the iframe.

The submit button at margin-top: 1311px aligns with the hidden form's submit.

> Expected output: Yelp business page shows changes (e.g., new website URL) after submission.

### Step 3: Validate Impact

**Context**: Check the target business on Yelp for modifications.

Visit https://www.yelp.com/biz/RIyHYSf3lyJcFb4El9T4tQ directly.

> Success if details like email or hours are altered without direct user intent.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Bootstrap]]
- [[tools/jQuery]]

## Tags

- clickjacking
- demonstration
- phishing
