---
tags:
  - csrf
  - account-setup
  - web
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:23.011Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 535e65fc-7388-4fd1-8b3d-5d61c3c4aede
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Account-Setup-for-CSRF-Testing

## Summary

This procedure sets up attacker and victim accounts on Glassdoor to test cross-account token reuse in a CSRF scenario, simulating the initial access phase for vulnerability assessment.

## Description

In the context of testing a potential CSRF vulnerability in Glassdoor's demographic settings, this procedure involves creating two accounts: one for the attacker to generate a valid gdToken and one for the victim to target. The attacker logs in and navigates to settings to prepare for request capture. This step ensures isolated sessions but highlights the need for same-browser testing due to cookie binding. Expected outcome: Authenticated accounts ready for further exploitation steps, with no actual impact if token reuse fails.

## Requirements

1. Valid email addresses for registration (e.g., Attacker@mail.com, Victim@mail.com)
2. Internet access to https://www.glassdoor.com
3. Browser with cookies enabled (e.g., Chrome for session persistence)

## Defense

Defensive measures and detection strategies:

- Implement account creation rate limiting to prevent bulk testing
- Monitor for unusual login patterns from testing IPs
- Use CAPTCHA on registration to deter automated setups

## Objectives

1. Establish controlled attacker and victim environments
2. Verify authentication workflows
3. Prepare for token extraction without alerting defenses

## Instructions

### Step 1: Create Accounts

**Context**: Register new accounts to simulate attacker and victim roles.

Navigate to https://www.glassdoor.com and create accounts using distinct emails. No commands required; use the web interface.

> Expected output: Confirmation emails sent; accounts verifiable via login.

### Step 2: Attacker Login and Navigation

**Context**: Authenticate the attacker and access demographic settings.

Log in to Attacker@mail.com and go to https://www.glassdoor.com/member/account/settings.htm to view modifiable fields like gender and birth year.

> Expected output: Settings page loaded with current demographics displayed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
