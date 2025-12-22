---
tags:
  - link-hijacking
  - impersonation
  - phishing-test
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
updated_at: '2025-12-14T17:33:12.469Z'
skill_level: novice
impact_level: high
detection_risk: low
sub_techniques: []
id: 49816864-ed2e-4237-abc5-01a049c2b895
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test Instagram Link for Hijacking

## Summary

This procedure tests the Instagram social media link on the target website by clicking it to verify if it redirects to an attacker-controlled account, confirming a broken link hijacking vulnerability that enables brand impersonation and phishing risks.

## Description

Once the social media section is located, clicking the Instagram link should redirect to https://www.instagram.com/[handle]/. Due to the company losing control of the handle, it now points to an unauthorized profile. This simple interaction demonstrates the vulnerability, where users are diverted to malicious content, leading to misinformation, scams, or data theft. The procedure is performed in a standard browser and requires no additional setup. Outcomes include observing the redirect and assessing the profile's legitimacy.

## Requirements

1. Access to the website from Step 1
2. Web browser capable of following hyperlinks
3. Awareness of the official company Instagram handle for comparison

## Defense

Defensive measures and detection strategies:

- Verify and update social media links to owned handles
- Use URL shorteners or proxies with monitoring for redirects
- Implement website monitoring tools to detect changes in external link destinations
- Educate users on verifying social media profiles

## Objectives

1. Confirm redirect to unauthorized Instagram account
2. Assess potential for impersonation or phishing
3. Document the hijacked profile for reporting

## Instructions

### Step 1: Click the Instagram Link

**Context**: Interact with the link to trigger the redirect and observe the destination.

Locate the Instagram icon or hyperlink in the social media section and click it with the mouse.

> The browser should navigate away from the website to Instagram, loading a profile page. Check the URL for the handle and compare to known official one.

### Step 2: Verify Profile Ownership

**Context**: Inspect the loaded Instagram page for signs of hijacking.

Once redirected, examine the profile: look for verification badges, post content, follower count, and any discrepancies from the company's official presence.

> If the profile lacks company branding or shows unrelated content, it confirms hijacking. Take screenshots for evidence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[link-hijacking]]
- [[impersonation]]
