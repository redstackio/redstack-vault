---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - phishing
  - social-engineering
  - csrf
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
  - '[[Phishing]]'
updated_at: '2025-12-14T17:27:36.171Z'
sub_techniques:
  - '[[T1566.001]]'
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Trick-Victim-into-Submission

## Summary

This procedure uses social engineering to deliver the malicious CSRF form to the victim, tricking them into loading it while authenticated on TikTok, resulting in unauthorized video deletion.

## Description

The final step in the CSRF attack involves phishing the victim with a link to the malicious HTML page. Disguised as a legitimate TikTok-related lure (e.g., "View this viral video"), the link loads the auto-submitting form. Since the victim is logged in, their session cookies authenticate the request, deleting the targeted video silently. This exploits user trust and the vulnerability's lack of origin checks.

## Requirements

1. Hosted malicious HTML accessible via URL
2. Contact method for victim (email, DM, etc.)
3. Knowledge of victim's TikTok authentication status

## Defense

Defensive measures and detection strategies:

- User education on suspicious links
- Browser protections like uBlock Origin blocking auto-submits
- TikTok-side logging of cross-origin requests

## Objectives

1. Induce victim to load the payload
2. Ensure session is active for authentication
3. Achieve deletion without detection

## Instructions

### Step 1: Prepare Delivery Mechanism

**Context**: Host the HTML and craft a phishing message.

Upload the HTML to a free host (e.g., GitHub Pages) or use a shortener. Message: "Hey, check out this hilarious TikTok: [malicious-link]"

**Expected Output**: Clickable link ready for distribution.

### Step 2: Deliver and Monitor

**Context**: Send to victim and wait for interaction.

Send via email or social media. Monitor for deletion by checking the public video status.

**Expected Output**: Video disappears from TikTok.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[social-engineering]]
