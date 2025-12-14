---
id: proc-intercept-invitation-burp
tags:
  - burp-suite
  - intercept
  - api
type: procedure
tools:
  - '[[tools/burp-suite]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/post-invitation-legitimate]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:20.908Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept Legitimate Invitation Request with Burp Suite

## Summary

This procedure configures Burp Suite to intercept a legitimate invitation request to the attacker's own organization, capturing the exact structure for modification in the IDOR exploit.

## Description

The /api/invitations endpoint requires a specific JSON payload for invitations. By sending a request to invite a fake account to the attacker's own org and intercepting it, the attacker obtains the full headers, cookies, and body format. This is then modified for the target org. Requires proxy setup and authenticated session.

## Requirements

1. Burp Suite installed and configured as browser proxy
2. Valid JWT token for authenticated user
3. Fake email for invitation (e.g., azraelsec+1@wearehackerone.com)
4. Own organization ID (e.g., 883b0a46-e4cf-4315-af4f-4226d1ada561)

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS and validate request origins
- Rate-limit invitation requests per user/org
- Log and monitor proxy-like traffic anomalies

## Objectives

1. Capture valid invitation request structure
2. Preserve authentication headers for reuse
3. Prepare payload for IDOR modification

## Instructions

### Step 1: Configure Proxy and Send Request

**Context**: Set up Burp Suite proxy (default 127.0.0.1:8080) in browser, then trigger the invitation via UI or curl while intercepting.

**Command** ([[commands/post-invitation-legitimate]]):
```bash
curl -X POST https://console.helium.com/api/invitations \
  -H "Authorization: Bearer eyJhbGciOiJIUzUxMiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiJjb25zb2xlIiwiZXhwIjoxNTg1NzAyODgzLCJpYXQiOjE1ODU2MTY0ODMsImlzcyI6ImNvbnNvbGUiLCJqdGkiOiIwNjUwMGRiOS1kNjNlLTRiYTQtYWJiYy0xYmQ0YTViMzUxY2YiLCJuYmYiOjE1ODU2MTY0ODIsIm9yZ2FuaXphdGlvbiI6Ijg4M2IwYTQ2LWU0Y2YtNDMxNS1hZjRmLTQyMjZkMWFkYTU2MSIsIm9yZ2FuaXphdGlvbl9uYW1lIjoibG9sIiwic3ViIjoiOGY1YWJlMTktMDAwMS00MWI1LWE5NjktZmUwYjcxZGNjZjFmIiwidHlwIjoiYWNjZXNzIiwidXNlciI6IjhmNWFiZTE5LTAwMDEtNDFiNS1hOTY5LWZlMGI3MWRjY2YxZiJ9.VMAi-07cZkCJg-dffHdR1wwJbi9JNSzpaQSRSQGDX-_vDrcTOPEfgJU_LCZ8H5tYiwsexyD-ogLFakGY1bFy-A" \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36" \
  -H "Cookie: _ga=GA1.2.356414044.1583245182; ..." \
  -d '{"invitation":{"email":"azraelsec+1@wearehackerone.com","role":"admin","organization":"883b0a46-e4cf-4315-af4f-4226d1ada561"}}'
```

> Intercept in Burp's Proxy > Intercept tab. Do not forward immediately; drop or hold to analyze.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/post-invitation-legitimate]]

## Tools Used

- [[tools/burp-suite]]

## Tags

- burp-suite
- intercept
- api
