---
id: proc-deliver-csrf-payload
tags:
  - csrf
  - social-engineering
  - account-takeover
type: procedure
tools: []
tactics:
  - '[[Persistence]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:27:29.522Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Deliver-and-Trigger-CSRF-Payload

## Summary

This procedure involves delivering the crafted HTML form to the victim and triggering submission to execute the CSRF attack, resulting in unauthorized provider addition and account takeover.

## Description

The attacker hosts or emails the malicious HTML page, which the victim loads while authenticated on onpatient.com. The form auto-submits or prompts a click, sending the POST to /api/v3/providers and linking the attacker's email to the patient's account. This grants the attacker control over the providers list, enabling full takeover.

## Requirements

1. Method to deliver HTML (e.g., phishing email, malicious link)
2. Victim's authentication on the target site
3. Optional hosting for the HTML page

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and suspicious links
- Monitor for rapid provider additions or from unknown IPs
- Use multi-factor authentication for account changes

## Objectives

1. Ensure victim loads the payload in an authenticated session
2. Trigger the form submission seamlessly
3. Achieve provider addition leading to takeover

## Instructions

### Step 1: Host or Distribute the HTML

**Context**: Make the malicious page accessible to the victim via a lure.

Upload the HTML to a web server or attach to an email disguised as a legitimate notification (e.g., 'Update your providers'). Include a link or inline the form.

**Expected Output**: Victim receives and clicks the link, loading the page.

### Step 2: Trigger Submission

**Context**: The page executes the POST upon load or button click.

If auto-submit: Use <script>document.forms[0].submit();</script>. For manual: Add a button like 'Click to Update'. The victim's cookies authenticate the request.

**Expected Output**: Server adds attacker's details as provider; attacker verifies via login.

**Success Indicators**:
- Provider list updated with attacker's email
- Attacker accesses victim's account functions

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Phishing]]
