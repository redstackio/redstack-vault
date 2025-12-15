---
tags:
  - csrf
  - web
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:35.707Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 8d6ec0f0-a451-4d6a-bc39-0b02e7c1bae3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-and-Lure-Victim-to-Starbucks-CSRF-Page

## Summary

This procedure deploys the malicious HTML on an attacker-controlled site and uses social engineering to direct an authenticated Starbucks user to it, executing the CSRF to add unauthorized card details.

## Description

Hosting the page on a public or controlled server (e.g., GitHub Pages or a VPS) allows the attacker to share a URL via email, SMS, or links disguised as legitimate Starbucks communications. When the victim clicks while logged in, the form submits, adding the attacker's card. This can lead to financial loss, such as unauthorized charges or replacement of family payment methods.

## Requirements

1. Web hosting service (e.g., free tier on Vercel or local ngrok for testing)
2. Social engineering capability to lure victim
3. Victim's authentication to Starbucks active

## Defense

Defensive measures and detection strategies:

- Multi-factor authentication for payment changes
- Alert users to suspicious login or form submissions
- Web Application Firewall (WAF) rules for anomalous POSTs

## Objectives

1. Make the exploit accessible via URL
2. Trick victim into loading the page
3. Achieve unauthorized payment method addition

## Instructions

### Step 1: Host the Malicious HTML

**Context**: Upload the file to a server for public access.

Use a simple web server: Save malicious.html and run `python -m http.server 8000` locally, or deploy to a hosting platform. Obtain the URL (e.g., http://attacker-site.com/malicious.html).

### Step 2: Craft Lure Message

**Context**: Create a convincing pretext to get the victim to click.

Send an email like: "Update your Starbucks rewards: Click here to verify your payment method." Link to the malicious URL.

### Step 3: Monitor and Verify

**Context**: Confirm execution post-lure.

Instruct victim subtly or check account changes. Victim should see no popup, but card added in settings.

**Expected Output**: Attacker's card listed in victim's Starbucks payment methods.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[web]]
- [[Phishing]]
