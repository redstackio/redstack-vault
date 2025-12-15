---
tags:
  - social-engineering
  - phishing
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:15.427Z'
sub_techniques: []
id: 6bf52257-c236-4362-9fd1-0d7177a9f201
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Social-Engineering-Victim-Interaction

## Summary

This procedure outlines tricking an authenticated victim into visiting and submitting the malicious CSRF form, executing the attack within their browser session.

## Description

The attacker uses social engineering to lure the victim (who must be logged into the Uber newsroom WordPress) to the hosted malicious page. Upon visit, the form submits automatically or via click, forging the password change request due to the site's lack of CSRF protections.

## Requirements

1. Hosted malicious HTML page accessible via URL
2. Victim with active authentication to target site
3. Communication channel for luring (email, chat)

## Defense

Defensive measures and detection strategies:

- User training on suspicious links
- Browser extensions for CSRF protection
- Session monitoring for unexpected form submissions

## Objectives

1. Induce victim interaction with payload
2. Achieve unauthorized password modification
3. Access protected post with new password

## Instructions

### Step 1: Distribute the Malicious Link

**Context**: Send the URL to the victim via a pretext (e.g., "Check this Uber referral update").

Craft and send an email or message with the link to the hosted `submit.html`.

> Ensure the link appears legitimate. Expected output: Victim clicks and loads the page.

### Step 2: Confirm Exploitation

**Context**: Verify the attack success post-interaction.

After victim visit, test access to the protected post using the new password 'xxxxxxx'.

> Expected output: Successful login to the post, confirming change.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[social-engineering]]
- [[csrf]]
- [[Phishing]]
