---
tags:
  - dos
  - rails
  - memory-exhaustion
  - flood
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
  - Ruby on Rails
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:37.135Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
id: 94ed5d41-c7e2-4786-88a0-4e9f64b1cc2b
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Repeat-Requests-for-Memory-Exhaustion-in-Rails

## Summary

This procedure involves flooding a vulnerable Rails server with repeated requests to non-existent controllers, causing unbounded growth in the global cache and leading to memory exhaustion and denial of service.

## Description

Once the cache is primed, each new request to a unique or repeated invalid controller adds to the hash without eviction, leading to object accumulation and heap exhaustion. This exploits the lack of bounds or validation in Action Pack's controller lookup, affecting server availability. No workarounds exist beyond patching.

## Requirements

1. Vulnerable Rails setup with confirmed wildcard routes
2. Scriptable HTTP requester for automation (e.g., script with curl loops)
3. Monitoring access to observe memory impact

## Defense

Defensive measures and detection strategies:

- Upgrade to Rails 5.0 or apply specific patches for 4.x
- Implement request throttling and IP blacklisting
- Deploy intrusion detection for anomalous request patterns
- Regularly monitor Ruby process memory usage

## Objectives

1. Induce unbounded cache growth through repetition
2. Exhaust server resources for DoS
3. Validate impact via performance degradation

## Instructions

### Step 1: Automate Request Flood

**Context**: Set up a loop to send hundreds of requests to varied invalid controllers.

Use a script to generate unique paths (e.g., /controller1, /controller2) and request them sequentially:

For example, in a bash loop:

```bash
for i in {1..1000}; do
  curl -s "http://target.com/controller$i" > /dev/null
  sleep 0.1
done
```

> This simulates traffic, populating the cache with 1000+ entries.

### Step 2: Target Repeated or Unique Names

**Context**: Maximize growth by using unique names to avoid any potential deduplication.

Vary the controller string each time, ensuring new cache keys.

> Server heap will grow as each constant attempt leaks objects.

### Step 3: Validate Exhaustion

**Context**: Monitor for DoS signs like increased response times or crashes.

Check server logs for memory errors or use external monitoring to confirm RSS growth beyond normal.

> Success when application slows, OOM killer activates, or service becomes unavailable.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used


## Tools Used


## Tags

- dos
- rails
- memory-exhaustion
- flood
