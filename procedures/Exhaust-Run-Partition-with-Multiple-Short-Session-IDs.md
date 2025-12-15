---
tags:
  - dos
  - resource-exhaustion
  - beaker
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-long-session-id-cookie-for-path-disclosure]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
updated_at: '2025-12-14T17:26:48.341Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: b9b6be06-e4b6-4b8f-bcef-e00ef305ed1e
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Exhaust-Run-Partition-with-Multiple-Short-Session-IDs

## Summary

This procedure performs a denial-of-service by sending thousands of unique short session IDs (1-249 characters) to the EdgeRouter web portal, each creating a persistent cache file in /var/run/beaker/container_file/ without cleanup, exhausting the /run partition and causing /var/log to fill, rendering the device unresponsive.

## Description

Beaker stores each unique session ID as a *.cache file in /var/run/beaker/container_file/. With no limits or automatic cleanup, an attacker can flood the system with requests using distinct short IDs, filling /run (tmpfs mount) to 50%+ utilization after ~15,000 iterations. This leads to write failures, log overflow in /var/log, and failure of services like web, SSH, DHCP, and DNS until power cycle or manual intervention.

## Requirements

1. Network access to management interface
2. Ability to automate HTTP requests (e.g., script or Burp Suite)
3. Patience for iterations (up to 15,681 for full effect)

## Defense

Defensive measures and detection strategies:

- Add bounds checking and cleanup for session files (e.g., limit concurrent sessions, periodic pruning)
- Increase /run partition size or use persistent storage
- Rate-limit unauthenticated requests to the portal
- Monitor disk usage on /run and /var/log; alert on rapid file creation in /var/run/beaker/

## Objectives

1. Consume all available space in /run via cache files
2. Overflow /var/log with errors to amplify DoS
3. Achieve full service denial requiring physical reboot

## Instructions

### Step 1: Generate Unique Short Session IDs

**Context**: Create varying length strings (1-249 chars) to ensure unique cache files per request.

No command; use a script loop to generate IDs like repeating 'a' characters incremented by length.

### Step 2: Send Iterative Requests

**Context**: Flood the endpoint with GET / requests, each with a unique short beaker.session.id to build cache files.

**Command** ([[commands/send-long-session-id-cookie-for-path-disclosure]] adapted for loop):
```bash
for i in {1..15681}; do
  len=$((i % 249 + 1))
  session_id=$(printf 'a%.0s' {1..$len})
  curl -X GET "http://192.168.1.1/" -H "Cookie: beaker.session.id=$session_id" -H "User-Agent: Mozilla/5.0" --silent --max-time 5
  if (( i % 1000 == 0 )); then echo "Completed $i iterations"; fi
done
```

> Each curl request creates a new *.cache file. Monitor for increasing errors after ~50% /run fill. Expected: Device slows, then fails responses.

### Step 3: Confirm Exhaustion

**Context**: Check for log errors if SSH still accessible, or observe unresponsiveness.

Attempt SSH or web access; expect failures due to full partitions.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- [[commands/send-long-session-id-cookie-for-path-disclosure]]

## Tools Used


## Tags

- dos
- resource-exhaustion
- edgerouter
