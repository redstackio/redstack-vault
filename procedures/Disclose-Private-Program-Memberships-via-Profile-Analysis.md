---
tags:
  - information-disclosure
  - privacy-bypass
  - hackerone
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-profile]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Identity Information]]'
updated_at: '2025-12-14T17:32:39.586Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 290e44d3-c729-4db4-86e2-b9f66ad7c58e
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Disclose-Private-Program-Memberships-via-Profile-Analysis

## Summary

This procedure exploits a flaw in HackerOne's program visibility preference feature, allowing attackers to view private or restricted program memberships on user profiles despite configured privacy settings, enabling identification of participants in sensitive bug bounty programs.

## Description

HackerOne's platform allows users to set preferences for hiding their program memberships, but the implementation fails to enforce these controls effectively. By inspecting user profile pages, attackers can reveal memberships in blocked or private programs. This occurs because the visibility feature does not properly sanitize or hide the relevant data in the profile's HTML structure. The target environment is the HackerOne web application, and the procedure requires only public access to profiles. Expected outcomes include a list of disclosed programs, which can be used for targeted reconnaissance or social engineering.

## Requirements

1. Internet access to hackerone.com
2. Target user profile URL (publicly accessible)
3. Browser or curl for fetching and inspecting content

## Defense

Defensive measures and detection strategies:

- Implement server-side enforcement of visibility preferences to prevent client-side bypasses
- Monitor for anomalous profile scraping or API queries targeting user data
- Use rate limiting on profile views to detect bulk enumeration

## Objectives

1. Bypass privacy controls to list private program memberships
2. Identify participants in restricted bug bounty programs
3. Gather intelligence for further attacks like targeted phishing

## Instructions

### Step 1: Fetch User Profile

**Context**: Retrieve the raw HTML of the target user's profile to inspect visibility controls.

**Command** ([[commands/curl-fetch-profile]]):
```bash
curl -s "https://hackerone.com/{user-handle}" > profile.html
```

> This command downloads the profile page silently. Expected output is the full HTML file, which can be opened in a text editor or browser for inspection.

### Step 2: Analyze Program Visibility Section

**Context**: Search the HTML for program-related elements to confirm disclosure despite privacy settings.

**Command** ([[commands/grep-program-search]]):
```bash
grep -i "program\|membership\|visibility" profile.html
```

> This extracts lines containing program indicators. Successful execution reveals memberships like "Member of Private Program X" even if hidden in the UI.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance
- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-profile]]
- [[commands/grep-program-search]]

## Tools Used

- [[tools/curl]]

## Tags

- information-disclosure
- privacy-bypass
- web-enumeration
