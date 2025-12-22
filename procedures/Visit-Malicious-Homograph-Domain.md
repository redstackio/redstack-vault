---
tags:
  - phishing
  - idn-homograph
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:24:41.775Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: 77056640-7263-480d-b684-e46ce20701a2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Visit-Malicious-Homograph-Domain

## Summary

This procedure involves navigating to a punycode-encoded Internationalized Domain Name (IDN) that visually spoofs a legitimate domain, setting up the initial deception for a phishing attack in the Brave iOS browser.

## Description

In an IDN homograph attack, attackers register domains using Unicode characters that look identical to Latin characters in legitimate domains (e.g., using Cyrillic 'a' to mimic 'apple.com'). These are encoded as punycode (xn-- prefix) for DNS. The Brave address bar correctly displays the punycode, but the goal is to leverage subsequent UI flaws for deception. This step requires user interaction, such as clicking a link in an email or directly entering the URL, and targets iOS users of Brave Browser. Expected outcome: The site loads, presenting phishing content under the guise of legitimacy.

## Requirements

1. Brave Browser installed on iOS device.
2. Access to a malicious punycode URL (e.g., https://www.xn--80ak6aa92e.com/).
3. User permissions to navigate in the browser (no elevated access needed).

## Defense

Defensive measures and detection strategies:

- Enable strict IDN blocking in browser settings or use extensions like uBlock Origin that warn on homographs.
- Train users to check for punycode (xn--) in URLs and avoid visual similarity checks alone.
- Monitor for registrations of suspicious IDN domains via threat intelligence feeds.

## Objectives

1. Deliver the user to the spoofed phishing site.
2. Initiate the visual deception without triggering browser warnings.
3. Prepare for further exploitation via UI flaws.

## Instructions

### Step 1: Prepare the Malicious URL

**Context**: Identify or craft a punycode domain that homographs a target like apple.com. Tools like IDN encoders can generate these, but for this attack, use a pre-registered one.

No command required; manually copy the URL https://www.xn--80ak6aa92e.com/.

> Ensure the domain is active and hosts phishing content mimicking the legitimate site.

### Step 2: Navigate in Brave iOS

**Context**: Direct the browser to load the spoofed domain, confirming the address bar shows punycode while content appears legitimate.

Open Brave on iOS and enter or click the URL.

> The page should load, displaying spoofed visuals. Verify no immediate redirects or blocks occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[idn-homograph]]
