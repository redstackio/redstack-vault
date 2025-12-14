---
tags:
  - phishing
  - idn-homograph
  - ui-deception
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:41.766Z'
skill_level: low
impact_level: medium
detection_risk: low
sub_techniques: []
id: f2eb496e-5d3c-4d8c-91ab-dd6cf446b6cb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Observe-Domain-Misdisplay

## Summary

This procedure verifies the core vulnerability by checking the Brave Shield panel's incorrect rendering of the punycode domain as a legitimate one, completing the phishing deception.

## Description

The Brave Shield panel on iOS fails to implement IDN homograph countermeasures, unlike the main address bar. When viewing a punycode domain like xn--80ak6aa92e.com (spoofing apple.com), the panel decodes and displays it as 'apple.com', leading users to trust the site. This UI flaw facilitates phishing by removing suspicion. No automation is involved; it's observational. Expected outcome: User believes the site is legitimate and engages with phishing elements.

## Requirements

1. Brave Shield panel open on the homograph site.
2. Visual inspection capability.
3. Awareness of the expected spoof (e.g., apple.com).

## Defense

Defensive measures and detection strategies:

- Patch Brave to versions that enforce punycode display in all UI elements.
- Deploy endpoint detection for anomalous browser behaviors or homograph accesses.
- Educate users to cross-verify domains across browser components and hover/inspect carefully.

## Objectives

1. Confirm the misdisplay to validate the exploit.
2. Exploit user trust to enable credential theft or malware delivery.
3. Achieve phishing success through deception.

## Instructions

### Step 1: Inspect Domain Field

**Context**: Focus on the domain information section in the Shield panel to spot the flaw.

Look at the domain display area in the panel.

> It should show 'apple.com' instead of 'xn--80ak6aa92e.com', confirming the vulnerability.

### Step 2: Validate Deception

**Context**: Ensure the misdisplay aligns with the attack goal by noting user reaction.

Observe if the user proceeds confidently (e.g., enters login details).

> Success if no suspicion arises; the panel's 'legitimate' display builds false security.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[idn-homograph]]
- [[ui-deception]]
