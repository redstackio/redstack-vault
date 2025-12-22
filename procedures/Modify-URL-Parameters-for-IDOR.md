---
id: proc-uuid-2
tags:
  - idor
  - parameter-tampering
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:23.634Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Modify-URL-Parameters-for-IDOR

## Summary

This procedure exploits IDOR by manually altering euid and ri URL parameters in Airbnb referral links to arbitrary values, allowing unauthorized generation of valid invites.

## Description

Airbnb's referral system fails to validate user ID (euid) and referral ID (ri) parameters, treating arbitrary inputs as legitimate. This enables attackers to craft functional links without owning the referenced IDs, leading to potential abuse.

## Requirements

1. Original referral URL from a registered account
2. Text editor or browser developer tools for URL modification
3. Access to the modified URL via browser

## Defense

Defensive measures and detection strategies:

- Enforce server-side validation of euid and ri against authenticated user sessions
- Use signed tokens or HMAC for URL parameters to prevent tampering
- Log and alert on anomalous parameter values (e.g., low numeric IDs)

## Objectives

1. Bypass object reference checks to access unauthorized referrals
2. Validate that arbitrary IDs produce functional links
3. Enable scalable invite generation

## Instructions

### Step 1: Inspect Original URL

**Context**: Identify the euid and ri parameters in the base referral link.

Copy the URL and note the values, e.g., euid=ed736125-704e-f1ec-bb76-4ca60026141d&ri=14052412.

### Step 2: Tamper with Parameters

**Context**: Replace with arbitrary values to test IDOR.

Change euid to '2' and ri to '14052213', forming `https://www.airbnb.com/c/spent1?euid=2&ri=14052213&s=30`. Load in browser.

**Expected Output**: Page loads and offers invite generation without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[idor]]
- [[parameter-tampering]]
- [[web]]
