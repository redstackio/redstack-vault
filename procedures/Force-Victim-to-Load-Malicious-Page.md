---
id: proc-force-victim-load-171398
tags:
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
  - '[[T1566.001]]'
updated_at: '2025-12-13T23:52:39.390Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.001]]'
---
# Force-Victim-to-Load-Malicious-Page

## Summary

This procedure involves social engineering to direct the victim to the malicious HTML page, ensuring their browser executes the Login CSRF payload with clear cookies to initiate the SSO-SAML flow.

## Description

The attacker hosts the malicious page and uses phishing (e.g., email or link in a message) to lure the victim. The page must be visited with clear cookies to avoid session interference. Upon loading, the iframe manipulates the session, and the script auto-starts the login to HackerOne's SAML endpoint. This exploits the absence of CSRF protections in the login initiation. Prerequisites: Victim's email and a convincing pretext. Outcome: Victim's browser authenticates automatically, enabling further chain attacks.

## Requirements

1. Hosted malicious HTML page
2. Phishing vector (email, social media)
3. Victim's email for personalization

## Defense

Defensive measures and detection strategies:

- Educate users on phishing links
- Block or warn on suspicious redirects/iframes
- Log and alert on login attempts from unusual referrers

## Objectives

1. Ensure victim visits page without suspicion
2. Trigger session manipulation and login start
3. Maintain chain integrity for subsequent exploits

## Instructions

### Step 1: Prepare Phishing Link

**Context**: Create a lure to the hosted page.

Generate a shortened URL or embed in email: `http://attacker-site.com/malicious.html`.

> Use services like Bitly for obfuscation if needed.

### Step 2: Send to Victim

**Context**: Deliver via social engineering.

Send email: "Click here to view urgent report: [link]". Ensure victim has clear cookies (advise logout if possible).

> Victim loads page; monitor access logs for confirmation.

### Step 3: Verify Execution

**Context**: Confirm the login flow initiates.

Check network traces or add a callback beacon in JS to notify attacker.

> Expected: Redirect to SAML sign_in observed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.001]] Phishing: Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[csrf]]
