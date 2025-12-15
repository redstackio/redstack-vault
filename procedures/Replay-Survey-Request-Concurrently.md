---
id: proc-slack-replay-concurrent
name: Replay-Survey-Request-Concurrently
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:22.307Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - race-condition
  - web
  - slack
commands:
  - '[[commands/run-concurrent-curl-requests]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Replay-Survey-Request-Concurrently

## Summary

This procedure exploits the race condition by replaying the intercepted survey completion request multiple times asynchronously using background curl commands, allowing duplicate submissions before the server enforces uniqueness.

## Description

Following interception, the POST request to Slack's survey endpoint lacks proper synchronization, permitting concurrent submissions to be processed as separate events. By executing 3-4 curl commands in parallel via background processes (& operator), the attacker overwhelms the system's duplicate checks. This targets the /survey/6-23387113491-bed6344a95 endpoint and relies on the absence of idempotency. Prerequisites include the captured request from Burp Suite. Successful execution results in multiple credits without rejection.

## Requirements

1. Captured curl command from Burp Suite (including headers like Cookie, POST data)
2. Terminal access on Linux/macOS or compatible environment
3. Valid session cookies from the intercepted request
4. Awareness of timing; execute immediately after initial submission

## Defense

Defensive measures and detection strategies:

- Add database locks or transaction isolation for survey completions
- Implement nonce or unique tokens per submission
- Rate limit API endpoints per user/session
- Anomaly detection on rapid successive API calls from the same source

## Objectives

1. Send multiple identical requests concurrently
2. Bypass duplicate prevention due to race condition
3. Trigger multiple credit awards

## Instructions

### Step 1: Copy Request from Burp

**Context**: Extract the curl equivalent of the intercepted POST.

In Burp, right-click the request > Copy as curl. Ensure it includes all headers (e.g., Authorization, Cookie) and POST parameters.

> The command will look like: curl -X POST https://slack.com/api/survey.complete -H "Cookie: d=..." -d "done2=1&..."

### Step 2: Execute Concurrently

**Context**: Run the curl multiple times in background to simulate the race.

Use [[commands/run-concurrent-curl-requests]] to fire 3-4 instances:

```bash
(curl -X POST https://slack.com/api/survey.complete -H "Cookie: d=..." -d "done2=1&crumb=...&referral_options=..." ) & (curl -X POST https://slack.com/api/survey.complete -H "Cookie: d=..." -d "done2=1&crumb=...&referral_options=..." ) & (curl -X POST https://slack.com/api/survey.complete -H "Cookie: d=..." -d "done2=1&crumb=...&referral_options=..." )
```

> Expect multiple 200 OK responses; success rate increases with more parallels, but avoid over 4 to prevent session invalidation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/run-concurrent-curl-requests]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[race-condition]]
- [[web]]
- [[slack]]
