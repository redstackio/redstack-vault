---
id: proc-uuid-1
tags:
  - reconnaissance
  - web-archive
  - pii-exposure
type: procedure
tools:
  - '[[tools/Wayback-Machine]]'
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
updated_at: '2025-12-14T17:25:18.010Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Archived-Confirmation-URL-via-Wayback-Machine

## Summary

This procedure involves using the Wayback Machine to retrieve historical snapshots of web pages, specifically targeting archived email confirmation URLs from Omise's dashboard that contain sensitive Base64-encoded tokens with embedded PII.

## Description

In scenarios where applications fail to protect sensitive URLs from web crawlers, public archives like the Wayback Machine can expose them indefinitely. This procedure demonstrates accessing such an archived URL from 2021 on Omise's /users/confirm_email endpoint, revealing a token that encodes user email addresses. The target environment is any public web application without robots.txt restrictions on sensitive paths. Expected outcomes include obtaining a URL with an exploitable token for further decoding, highlighting risks of PII leakage through archiving.

## Requirements

1. Internet access to archive.org
2. Browser for navigating the Wayback Machine
3. Knowledge of target URL patterns (e.g., dashboard.omise.co/users/confirm_email)

## Defense

Defensive measures and detection strategies:

- Implement robots.txt to disallow crawling of sensitive endpoints like /users/confirm_email
- Use short-lived tokens and avoid embedding PII in URLs
- Monitor for unauthorized archiving via web archive notifications or periodic searches

## Objectives

1. Retrieve historical web snapshots containing sensitive data
2. Identify exposed confirmation URLs with tokens
3. Enable downstream PII extraction for impact assessment

## Instructions

### Step 1: Search for Archived Pages

**Context**: Locate snapshots of the target confirmation endpoint to find URLs with embedded tokens.

No command required; use the web interface.

> Navigate to https://archive.org/web/, enter 'dashboard.omise.co/users/confirm_email' in the search bar, and select a calendar date from 2021. Click on a snapshot to load the archived page.

### Step 2: Extract the Confirmation URL

**Context**: Copy the full URL from the archived page, focusing on the token portion after /confirm_email/.

No command required.

> The URL should resemble: https://dashboard.omise.co/users/confirm_email/BAhbCGkD... (full token). Save this for decoding.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Wayback-Machine]]

## Tags

- [[Reconnaissance]]
- [[web-archive]]
