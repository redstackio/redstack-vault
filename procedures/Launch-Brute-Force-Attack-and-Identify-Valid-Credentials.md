---
tags:
  - execution
  - credential-harvesting
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/lichess-login-brute-force-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Brute Force]]'
updated_at: '2025-12-14T17:26:49.063Z'
sub_techniques: []
id: 988d90df-c50c-4a8a-ae6d-f68159171aa2
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Brute Force]]'
---
# Launch-Brute-Force-Attack-and-Identify-Valid-Credentials

## Summary

Execute the Burp Intruder attack on the Lichess login endpoint and analyze responses to pinpoint valid credential pairs for account takeover.

## Description

Finalizing the exploit of weak rate limiting, this procedure runs the automated brute force, monitoring for 200 OK responses that indicate successful logins. Due to per-username limits only, varied usernames prevent quick blocks. Successful outcomes include harvested credentials, enabling data theft or DoS, though IP mitigations may slow distributed scenarios.

## Requirements

1. Configured Intruder with wordlists
2. Stable network to target
3. Manual login capability for validation

## Defense

Defensive measures and detection strategies:

- Enhance IP trustworthiness scoring to block brute force faster
- Alert on high volumes of 200/401 responses from single sources
- Ban common passwords and monitor for wordlist patterns

## Objectives

1. Run the full payload combination
2. Identify successful logins via response codes
3. Validate and exploit found credentials

## Instructions

### Step 1: Start Attack

**Context**: Initiate the automated requests.

In Intruder, click 'Start attack'; monitor progress in the results table.

### Step 2: Monitor Responses

**Context**: Filter for success indicators.

Sort by status code; 200 OK signals valid creds (shorter response body than 401 errors). Note the system lacks noticeable reactions to correct passwords during runs.

### Step 3: Validate Hits

**Context**: Confirm takeover potential.

For 200 OK entries, extract username/password and test manually at https://lichess.org/login using [[commands/lichess-login-brute-force-request]] structure without payloads.

> Successful manual login grants account access; check for sensitive data.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Brute Force]] Brute Force

### Sub-Techniques


## Commands Used

- [[commands/lichess-login-brute-force-request]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- execution
- credential-harvesting
