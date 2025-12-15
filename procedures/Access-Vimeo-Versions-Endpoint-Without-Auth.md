---
tags:
  - improper-auth
  - api-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-versions-endpoint]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 16292480-ec40-4aad-b596-0ae054cdeab7
created_at: '2025-12-14T17:32:39.456Z'
updated_at: '2025-12-14T17:32:39.456Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Vimeo-Versions-Endpoint-Without-Auth

## Summary

This procedure exploits the lack of proper authorization checks in Vimeo's API 'versions' endpoint, allowing non-pro or business accounts to access video version information intended only for pro/business users.

## Description

The vulnerability stems from the endpoint not enforcing account type restrictions, enabling any authenticated user to interact with video versions. In the attack scenario, an attacker with a basic Vimeo account uses their API token to query the endpoint for a target's video ID, retrieving sensitive version metadata. This serves as the initial access point for further manipulation. Prerequisites include a valid Vimeo API token and knowledge of a target video ID. Expected outcomes include successful retrieval of version data without errors.

## Requirements

1. Valid Vimeo API token from a non-pro/business account
2. Target video ID (publicly discoverable or known)
3. HTTP client like curl for API requests

## Defense

Defensive measures and detection strategies:

- Implement strict authorization checks based on account type for sensitive endpoints
- Monitor API access logs for unusual account type interactions with pro features
- Rate-limit and audit version endpoint requests

## Objectives

1. Gain unauthorized read access to video versions
2. Identify exploitable video resources
3. Establish foothold for version manipulation

## Instructions

### Step 1: Authenticate and Query Endpoint

**Context**: Use the attacker's API token to access the versions endpoint for a target video, confirming the auth bypass.

**Command** ([[commands/curl-access-versions-endpoint]]):
```bash
curl -H "Authorization: bearer YOUR_ATTACKER_TOKEN" https://api.vimeo.com/videos/VIDEO_ID/versions
```

> This command sends a GET request to the endpoint. Expected output is a JSON array of version objects if successful, indicating the bypass worked. Errors would indicate proper restrictions, but in this vuln, it succeeds for non-pro accounts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-versions-endpoint]]

## Tools Used


## Tags

- [[improper-auth]]
- [[api-access]]
