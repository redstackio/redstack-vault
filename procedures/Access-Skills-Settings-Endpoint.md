---
tags:
  - information-disclosure
  - endpoint-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c53166fc-ff37-4c69-8ad5-7f305026f69a
created_at: '2025-12-11T03:47:39.374Z'
updated_at: '2025-12-11T03:47:39.374Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
---
# Access Skills Settings Endpoint

## Summary

This procedure involves accessing the HackerOne skills settings endpoint to retrieve endorsement data, which inadvertently exposes report titles due to a vulnerability.

## Description

In the context of HackerOne's platform, accessing the /settings/skills endpoint via an authenticated request returns a JSON response with skill endorsements. This procedure is the initial step in exploiting the information disclosure vulnerability, where the endpoint's query fails to restrict data visibility, leading to exposure of other users' report titles.

## Requirements

1. Authenticated HackerOne account
2. Web browser or HTTP client (e.g., curl)
3. Network access to hackerone.com

## Defense

Defensive measures and detection strategies:

- Implement proper access controls and query restrictions on endpoints
- Monitor for unusual access patterns to settings endpoints

## Objectives

1. Retrieve skills endorsement data
2. Initiate observation of potential disclosures
3. Confirm endpoint accessibility

## Instructions

### Step 1: Make Request to Endpoint

**Context**: Send an HTTP GET request to the skills settings page.

Navigate to https://hackerone.com/settings/skills or use an HTTP client to fetch the data.

> This returns a JSON response with skill categories and endorsements.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- #information-disclosure
- [[procedures/Access-Skills-Settings-Endpoint]]
