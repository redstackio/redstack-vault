---
tags:
  - exfiltration
  - clickjacking
  - data-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:28:12.539Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 359d69b0-daf2-4616-b506-5b60ff6191a1
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Exfiltrate User Information via Clickjacking

## Summary

This procedure executes the clickjacking attack by luring a VK.com user to the malicious site, tricking them into submitting personal details (phone and email) through the disguised form, and capturing the data for the attacker.

## Description

Once the malicious iframe is set up, the attacker directs victims (authenticated on VK.com) to the fake site. The user's session allows the form to submit their pre-filled or prompted details invisibly. Data is exfiltrated via the form's backend or by monitoring the submission response. This high-impact step relies on social engineering for victim interaction and assumes the target's lack of clickjacking defenses.

## Requirements

1. Hosted malicious site from previous setup
2. Method to lure users (e.g., phishing link)
3. Server-side logging to capture submitted data

## Defense

Defensive measures and detection strategies:

- Educate users on verifying site authenticity and disabling iframes
- Implement multi-factor authentication (MFA) for sensitive submissions
- Monitor for anomalous form submissions from embedded contexts in application logs

## Objectives

1. Induce unwitting form submission from authenticated users
2. Capture phone numbers and emails submitted to the lead form
3. Achieve data theft without direct access to victim accounts

## Instructions

### Step 1: Lure the Victim

**Context**: Direct the target to the malicious page while they are logged into VK.com.

Send a phishing link disguised as a legitimate poll or survey, e.g., via email or social media.

**Expected Output**: User visits the site with active VK session.

### Step 2: Trigger Submission and Capture

**Context**: User clicks the fake button, submitting the iframe form.

On the server side, if the form posts to an attacker-controlled endpoint (or monitor VK's response), log the POST data containing phone and email.

For VK, the submission goes to their server, but as the app owner, the attacker can access collected leads; alternatively, use JavaScript to intercept form data before submission.

**Expected Output**: Submitted data (e.g., {phone: "+123456789", email: "user@example.com"}) is logged or sent to attacker's server.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Exfiltration]]
- [[clickjacking]]
- [[data-theft]]
