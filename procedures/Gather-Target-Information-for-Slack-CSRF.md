---
id: 00000000-0000-0000-0000-000000000002
tags:
  - reconnaissance
  - csrf
  - slack
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-09-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:03.866Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Gather-Target-Information-for-Slack-CSRF

## Summary

This procedure involves collecting necessary details about the target victim and Slack help request to prepare for a CSRF exploit, focusing on obtaining the request ID and username without alerting the target.

## Description

In a CSRF attack on Slack's help requests, the attacker needs the specific help request ID (e.g., 237956) and the victim's username to forge a targeted form submission. This step uses passive reconnaissance or social engineering to gather this information, such as monitoring shared links in conversations or querying Slack's public directories. The target environment is the web-based Slack application, and success enables precise targeting for impersonation via fake comments.

## Requirements

1. Access to Slack (as attacker or via observation)
2. Knowledge of victim's interactions or shared help request links
3. Basic social engineering skills for phishing or observation

## Defense

Defensive measures and detection strategies:

- Monitor for unusual information gathering attempts in Slack logs
- Educate users on not sharing help request links externally
- Implement rate limiting on help request access

## Objectives

1. Obtain valid help request ID for targeting
2. Identify victim's exact username
3. Prepare for vulnerability verification without execution

## Instructions

### Step 1: Identify Help Request ID

**Context**: Locate a specific help request by observing victim communications or guessing from patterns.

No command required; manually note the ID from URLs like https://slack.com/help/requests/237956.

> Expected output: Request ID such as "237956".

### Step 2: Confirm Victim Username

**Context**: Verify the username to include in the forged request if needed for targeting.

Search Slack directory or review messages to confirm username (e.g., "john.doe@company.com").

> Expected output: Accurate username string.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[csrf]]
- [[slack]]
