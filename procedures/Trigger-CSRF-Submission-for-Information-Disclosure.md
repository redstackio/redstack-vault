---
id: proc-uuid-4
tags:
  - csrf
  - information-disclosure
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:50.262Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger CSRF Submission for Information Disclosure

## Summary

This procedure executes the CSRF attack by having the victim load the malicious page, causing their browser to submit the forged request to the password reset endpoint and resulting in the attacker receiving the victim's sensitive information via email.

## Description

Once the victim opens the link, their browser parses the HTML and auto-submits the form to https://accounts.firefox.com/reset_password using their real IP and browser context. The server processes it as a legitimate request from the victim, sending a reset email to the attacker's specified address containing the victim's IP address, geolocation, and browser details. This requires no further attacker action post-delivery and achieves unauthorized disclosure; monitor the attacker's inbox for success.

## Requirements

1. Victim has opened the malicious link
2. Attacker's email configured in the PoC
3. Access to email inbox for receiving disclosure

## Defense

Defensive measures and detection strategies:

- Rate-limit password reset requests per IP
- Audit logs for reset emails sent to unexpected addresses
- Implement client-side checks for unexpected form submissions

## Objectives

1. Forge reset request from victim's browser
2. Capture and disclose victim metadata in email
3. Confirm exploitation success via received data

## Instructions

### Step 1: Await Victim Interaction

**Context**: Monitor for the victim loading the page.

No active command; use analytics on hosting (if available) or wait for email.

**Expected Output**: Page view log if tracked.

### Step 2: Verify Form Submission

**Context**: The browser submits POST to endpoint with victim's details.

The JavaScript executes: form.action = 'https://accounts.firefox.com/reset_password'; form.submit();

**Expected Output**: Server-side processing without CSRF block.

### Step 3: Receive and Analyze Disclosure Email

**Context**: Collect the unauthorized information.

Check inbox for email from accounts.firefox.com with subject like "Reset your password" containing victim's IP, location (e.g., via GeoIP), and User-Agent string.

**Expected Output**: Email with details: "IP: 192.0.2.1, Location: US, Browser: Chrome 120".

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[information-disclosure]]
- [[exploitation]]
