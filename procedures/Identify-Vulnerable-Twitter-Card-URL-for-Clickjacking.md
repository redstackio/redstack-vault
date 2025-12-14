---
tags:
  - clickjacking
  - ui-redressing
  - twitter
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:12.876Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 5ffc8a5d-0e86-4915-8b36-cc77f0ff480d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-Vulnerable-Twitter-Card-URL-for-Clickjacking

## Summary

This procedure involves scouting Twitter's card creation pages to find endpoints vulnerable to clickjacking due to absent frame-busting headers, enabling subsequent embedding and exploitation for credential theft.

## Description

In this attack scenario, the attacker probes Twitter's public-facing web application for pages that can be iframed without restrictions. The target environment is Twitter's web platform, specifically card URLs like those used for promotions. Expected outcomes include identifying a URL where user interactions, such as button clicks, submit sensitive data (email and username) to an external domain. Prerequisites include basic web knowledge and access to browser developer tools for header inspection.

## Requirements

1. Internet access to Twitter services
2. Browser with developer tools (e.g., Chrome DevTools) for header checking
3. Control over a domain to receive test submissions

## Defense

Defensive measures and detection strategies:

- Implement X-Frame-Options: DENY or SAMEORIGIN headers on all pages
- Monitor for unusual iframe embedding attempts via web application firewalls
- Educate users on avoiding suspicious links

## Objectives

1. Locate iframable Twitter card pages
2. Verify data exfiltration potential on interaction
3. Prepare for embedding in malicious pages

## Instructions

### Step 1: Probe Twitter Card URLs

**Context**: Use browser tools to test specific Twitter card URLs for missing X-Frame-Options headers and confirm iframing capability.

Inspect the response headers of a URL like https://twitter.com/i/cards/tfw/v1/759046372544741376?cardname=promotion&autoplay_disabled=true&earned=true&lang=en&card_height=357. Load it in a browser and check the Network tab for headers.

> If no X-Frame-Options is present, the page is vulnerable to embedding.

### Step 2: Test Data Submission

**Context**: Simulate a button click to ensure it sends user data externally.

Visit the URL, interact with the button, and monitor network requests. Confirm that the POST includes email and username fields directed to an attacker-controlled endpoint.

> Successful test shows data transmission without additional authentication.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[clickjacking]]
- [[ui-redressing]]
- [[twitter]]
- [[Reconnaissance]]
