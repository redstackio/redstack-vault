---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567894
tags:
  - information-disclosure
  - privacy-misconfiguration
  - wakatime
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Employee Names]]'
updated_at: '2025-12-14T17:30:35.730Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Employee Names]]'
---
# Observe-Private-Email-Disclosure-on-WakaTime-Leaderboard

## Summary

This procedure involves inspecting the leaderboard page after the target joins to capture the disclosed private email, confirming the vulnerability.

## Description

The core flaw lies in the leaderboard UI and data responses, which include private email fields without user consent checks. This step demonstrates the impact by viewing the exposed PII, potentially for harvesting. Assumes prior steps completed. Outcome: Visible email address, violating privacy controls.

## Requirements

1. Active membership including target
2. Access to the private leaderboard URL
3. Browser developer tools for inspection if needed

## Defense

Defensive measures and detection strategies:

- Filter private fields in API responses based on user settings
- Implement client-side privacy masks for sensitive data
- Regularly scan for PII leaks in web interfaces

## Objectives

1. Access and view member details
2. Document the unauthorized exposure
3. Assess potential for broader harvesting

## Instructions

### Step 1: Navigate to Leaderboard

**Context**: Load the member view.

Open the private leaderboard URL in your browser and ensure you're authenticated.

### Step 2: Inspect Member List

**Context**: Locate the target's profile.

Scroll to the member roster or click on the target's entry to view details.

### Step 3: Capture Exposed Email

**Context**: Confirm disclosure.

Observe the private email displayed in the UI; screenshot or copy for evidence. Use browser inspector to check underlying data if not visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Employee Names]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[privacy-misconfiguration]]
