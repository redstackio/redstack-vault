---
id: proc-uuid-1
tags:
  - web-recon
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:35.686Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Navigate-to-Target-Website

## Summary

This procedure involves using a web browser to access the public homepage of a target website, serving as the entry point for reconnaissance on web-based applications like the MTN NIN linking site.

## Description

In web vulnerability assessments, initial navigation establishes connectivity and confirms site availability. For the MTN NIN site, this loads https://nin.mtn.ng/, a WordPress-powered portal for National Identification Number (NIN) linking services in Nigeria. No authentication is required, making it accessible to any internet user. The procedure sets the stage for deeper inspection without triggering alerts, as it mimics legitimate user behavior.

## Requirements

1. Web browser (e.g., Google Chrome, Firefox) with internet connectivity
2. Knowledge of the target URL: https://nin.mtn.ng/
3. No special permissions or tools needed

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor unusual traffic patterns
- Use server-side logging to track access to public endpoints
- Ensure HTTPS enforcement to prevent man-in-the-middle inspection

## Objectives

1. Confirm target site accessibility and load the homepage
2. Establish baseline for subsequent interactions
3. Identify any immediate client-side indicators of the tech stack

## Instructions

### Step 1: Launch Browser and Enter URL

**Context**: Open the browser to directly reach the target without intermediaries.

No command required; manually enter the URL in the address bar.

> The page should load the MTN NIN homepage, displaying branding and service options.

### Step 2: Verify Page Load

**Context**: Ensure the site is operational and responsive.

Interact with basic elements like scrolling or hovering to confirm functionality.

> Expected: No errors, full page renders with interactive buttons.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web-recon
- initial-access
