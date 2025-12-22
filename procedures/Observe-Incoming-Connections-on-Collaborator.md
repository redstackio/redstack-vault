---
tags:
  - oob
  - leakage
  - headers
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/observe-collaborator-connection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T03:53:38.026Z'
sub_techniques: []
id: 58d550fc-560f-4f23-9e2f-31b6be15be8e
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
# Observe-Incoming-Connections-on-Collaborator

## Summary

This procedure monitors an attacker-controlled server (Burp Collaborator) to capture SSRF-induced HTTP requests and DNS interactions, revealing leaked sensitive information from the target server.

## Description

Following the Host header exploitation, the target server makes outbound connections to the collaborator domain. This step involves reviewing logs for HTTP requests containing original client headers (e.g., cookies, auth), proxy details, and source IPs, providing insights into the internal network.

## Requirements

1. Active Burp Collaborator instance with a unique subdomain
2. Prior execution of SSRF payload
3. Log analysis capabilities

## Defense

Defensive measures and detection strategies:

- Block outbound connections to unknown domains
- Log and alert on unexpected DNS resolutions or HTTP requests from servers
- Use network segmentation to limit internal exposure

## Objectives

1. Capture leaked headers and metadata
2. Identify source of connections (e.g., internal proxies)
3. Extract usable sensitive data for further attacks

## Instructions

### Step 1: Monitor Collaborator Payloads

**Context**: Poll the Burp Collaborator client for new interactions triggered by the SSRF.

**Command** ([[commands/observe-collaborator-connection]]):
```http
# Inherent to Burp Collaborator UI: View received GET / request
# Example observed: GET / HTTP/1.1 with headers like Accept-Encoding, Connection, Authorization: Basic ████████, X-BlueCoat-Via
```

> Interactions appear in the Collaborator UI, showing full request details including redacted IPs and auth tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exfiltration Over Command and Control Channel]]

### Sub-Techniques


## Commands Used

- [[commands/observe-collaborator-connection]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- oob
- leakage
- headers
