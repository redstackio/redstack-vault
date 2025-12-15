---
tags:
  - race-condition
  - retry-bypass
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Defense Evasion]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Disable or Modify Tools]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8648242a-f564-4cfd-aff2-533417b354ae
created_at: '2025-12-14T17:24:18.900Z'
updated_at: '2025-12-14T17:24:18.900Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Disable or Modify Tools]]'
---
# Race-Condition-Retry-Bypass

## Summary

This procedure leverages a race condition in the retry limit handling to perform excessive attempts on protected actions, bypassing enforced throttling. It targets web applications like VK.com where concurrent requests can manipulate shared retry counters, allowing automation beyond intended limits.

## Description

The VK.com retry mechanism suffered from a race condition where multiple simultaneous failure responses were not properly synchronized, enabling attackers to reset or ignore the retry count. By sending rapid, concurrent requests to the retry-protected endpoint, the server processes them out of order, failing to increment the global counter accurately. This is particularly effective against rate-limited APIs or forms. Prerequisites include scripting capability for parallel requests and endpoint access. Outcomes include unlimited retries, facilitating brute-force or spam attacks.

## Requirements

1. Ability to send concurrent HTTP requests (e.g., via scripting or multi-threaded tools).
2. Knowledge of the retry-protected endpoint and failure triggers.
3. Session or IP not already blocked by prior limits.

## Defense

Defensive measures and detection strategies:

- Use atomic operations or database locks to handle retry counters thread-safely.
- Implement distributed rate limiting with tools like Redis to synchronize across instances.
- Log and alert on bursts of concurrent requests from the same source.

## Objectives

1. Exploit concurrency to evade retry limits.
2. Enable high-volume automated interactions.
3. Validate the race condition for vulnerability assessment.

## Instructions

### Step 1: Identify Retry-Protected Endpoint

**Context**: Locate the endpoint that enforces retry limits, typically via error responses like "too many attempts."

Use browser dev tools or initial tests to trigger a retry limit (e.g., submit 5 failed actions) and note the endpoint URL.

### Step 2: Trigger Race with Concurrent Requests

**Context**: Send multiple requests in parallel to exploit the unsynchronized counter.

Use a shell script or tool to fire 10+ simultaneous POST requests immediately after a failure:

```bash
# Bash script example for concurrent curls
for i in {1..10}; do
  curl -X POST 'https://vk.com/api/retry_action' \
    -H 'Content-Type: application/json' \
    -H 'Cookie: session_id=your_session' \
    -d '{"attempt": $i, "data": "test"}' &
done
wait
```

> This launches parallel requests. Expected output includes several successful or partial successes without hitting the limit (e.g., responses beyond the 5-attempt cap), indicating the race allowed extra tries.

### Step 3: Iterate and Confirm Unlimited Access

**Context**: Repeat the concurrent burst after reaching the nominal limit to ensure bypass persistence.

Adjust concurrency based on server response times; success is confirmed if retries exceed documented limits without blocking.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Disable or Modify Tools]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[race-condition]]
- [[retry-bypass]]
