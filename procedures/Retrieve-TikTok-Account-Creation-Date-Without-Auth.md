---
id: proc-tiktok-creation-date-retrieval
name: Retrieve TikTok Account Creation Date Without Auth
tags:
  - information-disclosure
  - privacy
  - tiktok
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-profile-fetch]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Employee Names]]'
updated_at: '2025-12-14T17:25:13.120Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Employee Names]]'
---
# Retrieve TikTok Account Creation Date Without Auth

## Summary

This procedure exploits an information disclosure vulnerability in TikTok, allowing an attacker to retrieve the creation date of any user's account without authentication. It enables reconnaissance by revealing account age metadata, which can aid in user profiling or enumeration attacks, though the impact is limited to privacy concerns.

## Description

The vulnerability stems from inadequate access controls on user profile metadata endpoints or page elements in TikTok's web application. By accessing a user's public profile page without logging in, the creation date is exposed in the response payload or DOM. This was reported via HackerOne on May 6, 2022, as a low-severity issue. The procedure assumes external access to TikTok's website and uses standard HTTP requests to fetch and parse the data. Prerequisites include knowledge of the target username and basic web inspection skills. Expected outcomes include obtaining a timestamp like the account's join date, which could be used to infer user behavior patterns.

## Requirements

1. Internet access to TikTok's domain (www.tiktok.com)
2. Target username (e.g., @exampleuser)
3. Web browser with developer tools or HTTP client like curl
4. Basic parsing tools (e.g., grep for command-line extraction)

## Defense

Defensive measures and detection strategies:

- Implement authentication checks on all user metadata endpoints
- Rate-limit profile access to prevent enumeration
- Monitor for anomalous profile requests from unauthenticated IPs
- Use content security policies to obscure metadata in responses

## Objectives

1. Disclose sensitive account creation metadata without credentials
2. Enable profiling of user account longevity
3. Demonstrate bypass of privacy controls for reconnaissance

## Instructions

### Step 1: Access Target Profile

**Context**: Load the target user's profile page to trigger the metadata response.

**Command** ([[commands/curl-profile-fetch]]):
```bash
curl -s "https://www.tiktok.com/@username" -H "User-Agent: Mozilla/5.0"
```

> This command fetches the profile page HTML without authentication. The response includes embedded JSON with user data. Successful execution returns the full page source; look for scripts or data attributes containing creation date.

### Step 2: Extract Creation Date

**Context**: Parse the response to isolate the creation date field.

**Command** ([[commands/curl-profile-fetch]] with grep):
```bash
curl -s "https://www.tiktok.com/@username" | grep -o 'join_date:\"[^\"]*\"' || grep -o 'creation_time:\"[^\"]*\"'
```

> This extracts the join or creation date from the HTML/JSON. Expected output is a string like "join_date:\"2020-05-06\"", confirming disclosure. If no match, inspect via browser dev tools for the exact field name.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Employee Names]]

### Sub-Techniques


## Commands Used

- [[commands/curl-profile-fetch]]

## Tools Used


## Tags

- information-disclosure
- tiktok
- privacy-violation
