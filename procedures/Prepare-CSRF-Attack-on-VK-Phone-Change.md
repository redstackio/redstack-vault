---
tags:
  - csrf
  - reconnaissance
  - web
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Gather Victim Org Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2472c2f5-8bb7-4b8a-be44-d62720f41342
created_at: '2025-12-14T17:27:42.373Z'
updated_at: '2025-12-14T17:27:42.373Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
---
# Prepare-CSRF-Attack-on-VK-Phone-Change

## Summary

This procedure involves gathering the victim's last name and login from VK.com to prepare a targeted CSRF payload for the phone number change endpoint, setting the stage for unauthorized modifications.

## Description

In the context of VK.com's web platform, attackers can exploit public profile information to identify targets. The phone change feature lacks proper CSRF token validation, allowing requests authenticated only by basic user details. This step ensures the payload is correctly formatted with the victim's identifiers, enabling the subsequent exploitation without alerting defenses.

## Requirements

1. Access to victim's public VK.com profile (last name and login)
2. Web browser for inspection
3. Basic knowledge of HTML form crafting

## Defense

Defensive measures and detection strategies:

- Implement strict CSRF token validation on all state-changing endpoints
- Rate-limit profile access and log suspicious queries for user details
- Educate users on phishing risks for profile info

## Objectives

1. Collect accurate victim identifiers
2. Validate endpoint details for CSRF payload
3. Prepare for seamless execution in chained attacks

## Instructions

### Step 1: Gather Victim Details

**Context**: Identify the target's last name and login from VK.com search or public posts.

Manually search VK.com for the victim and note the login (e.g., username) and last name displayed on their profile.

**Expected Output**: Noted details like "Login: victim_user, Last Name: Doe".

### Step 2: Inspect Phone Change Endpoint

**Context**: Examine VK.com's phone change form to understand required parameters.

Use browser developer tools to navigate to a phone change page (if accessible) and inspect the form fields, such as action URL, last_name, login, and new_phone inputs.

**Expected Output**: Form structure ready for replication in CSRF HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Org Information]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[Reconnaissance]]
