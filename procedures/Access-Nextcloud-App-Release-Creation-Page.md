---
tags:
  - ssrf
  - nextcloud
  - access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.317Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 542d02ec-b647-4f09-b069-69ce0100d28c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Nextcloud-App-Release-Creation-Page

## Summary

This procedure outlines navigating to the Nextcloud app release creation page, which contains the vulnerable 'Download Link' field exploitable for SSRF.

## Description

The Nextcloud apps developer portal allows public access to the release creation form at https://apps.nextcloud.com/developer/apps/releases/new. This page is the entry point for the SSRF attack, as it lacks validation on the 'Download Link' field, enabling requests to internal localhost addresses. The procedure assumes no authentication is required, making it accessible to unauthenticated attackers for reconnaissance purposes.

## Requirements

1. Web browser with internet access
2. No credentials or prior access needed
3. Target site: https://apps.nextcloud.com

## Defense

Defensive measures and detection strategies:

- Implement authentication on developer portals to restrict form access
- Monitor access logs for repeated visits to release creation endpoints
- Use web application firewalls (WAF) to block anomalous form submissions

## Objectives

1. Gain access to the vulnerable form for SSRF exploitation
2. Verify the 'Download Link' field is present and editable
3. Prepare for subsequent SSRF payload injection

## Instructions

### Step 1: Open Web Browser and Navigate

**Context**: Launch a browser to reach the public-facing form without any setup.

No command required; use the browser's address bar:

```plaintext
https://apps.nextcloud.com/developer/apps/releases/new
```

> Enter the URL directly. The page should load the form interface.

### Step 2: Verify Form Elements

**Context**: Confirm the presence of the exploitable field to ensure the target is vulnerable.

Inspect the page source or visually check for the 'Download Link' input field.

**Expected Output**: Form with fields for app release details, including 'Download Link'.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- ssrf
- nextcloud
- web-access
