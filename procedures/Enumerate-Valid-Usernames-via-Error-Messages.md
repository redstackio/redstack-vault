---
tags:
  - username-enumeration
  - information-disclosure
type: procedure
tools:
  - '[[tools/grep]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/grep-username-error]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:33:12.177Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques:
  - '[[T1087.002]]'
id: 3e115f3e-ba63-403d-85e9-15b5874bb6de
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Enumerate-Valid-Usernames-via-Error-Messages

## Summary

This procedure exploits distinct error messages returned by the login API to enumerate valid usernames by brute-forcing a list of potential usernames, filtering responses to identify those that exist without triggering rate limits.

## Description

The Outpost login API at https://api.outpost.co/api/v1/login returns 'Username does not exist' for invalid usernames and 'Password does not match username' for valid ones with wrong passwords. By sending POST requests with a dummy password and a wordlist of usernames (e.g., common names or from data leaks), attackers can make over 33,000 requests without IP blocking due to absent rate limiting. Responses are logged and filtered to isolate valid usernames. This targets web-based authentication in environments lacking uniform error handling.

## Requirements

1. List of potential usernames (e.g., text file with variations)
2. Tool for automating HTTP requests (e.g., Burp Intruder, ffuf, or curl scripting)
3. Ability to log API responses for analysis
4. No authentication required for enumeration

## Defense

Defensive measures and detection strategies:

- Use generic error messages (e.g., 'Invalid credentials') to prevent enumeration
- Implement strict IP-based rate limiting (e.g., <10 requests/minute)
- Log and alert on high-volume login attempts
- Employ CAPTCHA or multi-factor after failed logins

## Objectives

1. Identify a list of valid usernames on the target
2. Confirm lack of rate limiting for scalability
3. Prepare targeted password brute-forcing

## Instructions

### Step 1: Automate Username Requests

**Context**: Send brute-force requests to the API using a username list and fixed dummy password to trigger responses.

Use a tool like Burp Intruder or a script to POST to https://api.outpost.co/api/v1/login with payloads like {"username": "<username>", "password": "dummy"}. Log all responses.

> Expected: JSON responses with error messages; over 33,000 requests possible without blocks.

### Step 2: Filter Valid Usernames

**Context**: Analyze response logs to exclude invalid usernames using pattern matching.

Execute [[commands/grep-username-error]] on the response log file:

```bash
grep "Username does not exist" responses.log
```

> This identifies invalid attempts; valid usernames are those without this message. Export the filtered list for next steps.

**Expected Output**: List of lines with error for invalids; subtract from input list to get valids.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Account Discovery]] Account Discovery

### Sub-Techniques

- [[T1087.002]] Domain Account

## Commands Used

- [[commands/grep-username-error]]

## Tools Used

- [[tools/grep]]

## Tags

- [[username-enumeration]]
- [[information-disclosure]]
