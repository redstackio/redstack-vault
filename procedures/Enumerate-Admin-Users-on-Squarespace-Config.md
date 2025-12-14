---
id: proc-squarespace-admin-enum-001
tags:
  - user-enumeration
  - admin-discovery
  - squarespace
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-json]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:24:56.028Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[T1087.002]]'
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate Admin Users on Squarespace Config

## Summary

This procedure uses data disclosed from a Squarespace site's JSON endpoint to enumerate admin users by accessing the unprotected config page, identifying email addresses like admin@gmail.com and jason@jasonbarone.com without authentication.

## Description

Following an information disclosure, attackers can probe the site's admin console endpoint (e.g., /config) which may lack enumeration protections. By leveraging hints from the JSON data, such as user patterns or IDs, the config page can reveal admin details. This targets Squarespace's default configurations and is effective on public sites without rate limiting or access controls.

## Requirements

1. Data from prior information disclosure (e.g., JSON output)
2. Access to the target site's config endpoint
3. Browser or HTTP client for probing

## Defense

Defensive measures and detection strategies:

- Restrict access to admin endpoints like /config with authentication or IP whitelisting
- Implement rate limiting on config page requests
- Log and monitor anomalous access to administrative paths

## Objectives

1. Identify admin email addresses using disclosed data
2. Confirm user enumeration without credentials
3. Gather targets for potential phishing or further attacks

## Instructions

### Step 1: Access the Config Endpoint

**Context**: Directly query the admin config page to retrieve user-related information, correlating with prior JSON data.

**Command** ([[commands/curl-fetch-json]]):
```bash
curl "https://uber-movement.squarespace.com/config" -o config_data.html
```

> This fetches the config page content. Expected output is HTML or data revealing user lists. Inspect for email addresses or admin indicators.

### Step 2: Correlate and Enumerate Users

**Context**: Manually match elements from the config response with JSON disclosure to enumerate admins.

**Command** (No specific command; analysis):

Review `config_data.html` alongside `disclosed_data.json` for patterns like email domains or user IDs.

> In this exploit, it exposed admin@gmail.com and jason@jasonbarone.com. Success is confirmed by listing valid admin contacts.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- [[T1087.002]] Domain Account

## Commands Used

- [[commands/curl-fetch-json]]

## Tools Used

- None

## Tags

- [[user-enumeration]]
- [[squarespace]]
- [[admin-discovery]]
