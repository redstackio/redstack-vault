---
tags:
  - information-disclosure
  - unauthorized-access
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-get-invitation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Gather Victim Org Information]]'
updated_at: '2025-12-14T17:25:12.949Z'
skill_level: novice
impact_level: medium
detection_risk: low
sub_techniques: []
id: c8cae604-b576-443f-ba79-0e11df2409c7
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Org Information]]'
---
# Access Invitation Endpoint

## Summary

This procedure performs an unauthorized GET request to the HackerOne /invitations/<token>.json endpoint using an exposed unaccepted token, retrieving sensitive invitation details without authentication.

## Description

The /invitations/<token>.json endpoint lacks proper access controls for valid but unaccepted tokens, allowing anyone with the token to fetch JSON data containing the researcher's email and private program information (e.g., name, handle, profile picture URL). This exploits a misconfiguration combined with human error in token exposure, targeting web APIs in bug bounty platforms. Expected outcome is direct disclosure of private data, compromising privacy and program confidentiality.

## Requirements

1. Valid exposed invitation token
2. HTTP client like curl or browser
3. Public internet access

## Defense

Defensive measures and detection strategies:

- Enforce authentication or token validation on invitation endpoints, even for unaccepted tokens
- Expire or invalidate tokens immediately upon exposure detection
- Log and alert on requests to invitation endpoints from non-authorized IPs

## Objectives

1. Retrieve JSON response with sensitive invitation data
2. Bypass access controls via exposed token
3. Expose researcher and program private information

## Instructions

### Step 1: Prepare Request

**Context**: Substitute the extracted token into the endpoint URL.

No command; construct the full URL: https://hackerone.com/invitations/<token>.json.

> Ensure the token is valid and unaccepted to avoid errors.

### Step 2: Execute GET Request

**Context**: Send the HTTP GET request to fetch the JSON data.

**Command** ([[commands/curl-get-invitation]]):
```bash
curl -X GET "https://hackerone.com/invitations/<token>.json"
```

> This command performs a simple GET request. Expected output: A JSON object with fields like {"email": "researcher@example.com", "team": {"name": "Private Program", "handle": "prog-handle", "profile_picture": "url", "url": "prog-url"}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Org Information]] Gather Victim Org Information

### Sub-Techniques

-

## Commands Used

- [[commands/curl-get-invitation]]

## Tools Used

-

## Tags

- [[information-disclosure]]
- [[unauthorized-access]]
