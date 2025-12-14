---
id: p-lure-user-csrf
tags:
  - phishing
  - csrf
  - drive-by
type: procedure
tools:
  - '[[tools/Flash-SWF-File]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:32:20.810Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Lure Authenticated User to Malicious Page

## Summary

This procedure involves social engineering to direct an authenticated Federalist user to the attacker's page, where Flash automatically triggers the CSRF POST via the PHP proxy.

## Description

The victim must have an active session in Federalist with Flash enabled. Visiting the page causes the SWF to POST JSON data through the PHP redirector, forging headers and executing API actions like restarting builds for specific site IDs (e.g., 1 or 35) without further interaction.

## Requirements

1. Hosted malicious page from previous procedure
2. Victim's authentication to Federalist
3. Flash player enabled in victim's browser

## Defense

Defensive measures and detection strategies:

- User training on phishing and suspicious links
- Browser policies to disable Flash by default
- Session monitoring for unexpected API calls

## Objectives

1. Ensure victim is authenticated and Flash-enabled
2. Trigger automatic request on page load
3. Execute unauthorized POST on behalf of victim

## Instructions

### Step 1: Distribute Malicious URL

**Context**: Use phishing or embedding to lure the user.

Send link to http://attacker.com/malicious.html via email or forum, targeting Federalist users.

**Expected Output**: User clicks and loads the page.

### Step 2: Execute Flash Request

**Context**: SWF auto-sends POST on embed load.

Upon page load, SWF posts to PHP with jsonData, which redirects to Federalist /v0/build/ with forged Content-Type.

**Expected Output**: API receives and processes the request using victim's session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Flash-SWF-File]]

## Tags

- [[Phishing]]
- [[drive-by]]
