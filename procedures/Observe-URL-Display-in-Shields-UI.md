---
tags:
  - url-spoofing
  - brave-browser
  - android
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Android
  - Mobile Browser
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
updated_at: '2025-12-14T17:24:44.963Z'
sub_techniques: []
id: 8edca89b-93ef-4715-aef5-074c109f776f
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
---
# Observe-URL-Display-in-Shields-UI

## Summary

This procedure examines the URL rendering in the Brave Shields popup on Android to confirm the lack of proper subdomain eliding, demonstrating potential for user confusion and spoofing.

## Description

In the Shields UI, the Android version of Brave fails to follow Chromium's guidelines by not truncating long subdomains from the front (e.g., showing '...' + domain instead of full prefix). This can make a malicious long-subdomain site appear more trustworthy, especially when users are deciding on security settings. The observation was validated against desktop Brave, which elides correctly.

## Requirements

1. Shields popup open from previous procedure.
2. Test site with long subdomain loaded.
3. Ability to screenshot or note UI elements for comparison.

## Defense

Defensive measures and detection strategies:

- Audit browser UI for compliance with secure URL display standards.
- Use automated testing tools to compare mobile vs. desktop behaviors.
- Alert users via in-app notifications about potential UI flaws.

## Objectives

1. Identify the full display of the long subdomain in the popup.
2. Assess confusion risk for users interacting with Shields.
3. Note potential extension to other UIs like Brave Rewards.

## Instructions

### Step 1: Examine URL in Popup

**Context**: Focus on the URL element within the Shields interface.

Look at the URL shown in the Shields popup header or site info section.

> The full long subdomain (e.g., 'long-extended-subdomain-name-containing-many-letters-and-dashes') is visible without front truncation.

### Step 2: Compare to Expected Behavior

**Context**: Validate against secure guidelines to confirm the flaw.

Mentally compare to Chromium standards: the URL should elide as '...subdomain.badssl.com' but shows fully, potentially hiding the real domain.

> Note the discrepancy, which could confuse users into thinking it's a different site.

### Step 3: Document Observation

**Context**: Capture evidence of the vulnerability.

Take a screenshot of the popup showing the unelided URL.

> Screenshot includes the full URL and Shields controls, proving the issue.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Phishing]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- url-spoofing
- brave-browser
- android
