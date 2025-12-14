---
id: proc-bypass-ssrf-spoofed-913276
tags:
  - ssrf
  - bypass
  - host-discovery
  - internal-recon
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-http-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T04:08:48.320Z'
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
  - '[[Gather Victim Host Information]]'
---
# Bypass-SSRF-Localhost-via-Spoofed-Domain

## Summary

This procedure exploits SSRF by using a collaborator-generated domain that resolves to 127.0.0.1, bypassing localhost restrictions to confirm internal requests and enable host discovery, port scanning, and infrastructure info retrieval in the Bitwarden icons endpoint.

## Description

The Bitwarden icons.bitwarden.net endpoint fetches icons from user-supplied domains without resolving them client-side, allowing SSRF. After confirming localhost blocks, this step uses a spoofed domain (e.g., from Burp Collaborator) that DNS-resolves to internal IPs. The server makes the request internally, returning 404 Not Found while triggering out-of-band interactions. This enables further exploitation like scanning internal ports (e.g., appending :port to the domain) or accessing metadata services, though limited by report scope. Target is .NET Core web app.

## Requirements

1. Access to Burp Suite or similar for collaborator domain generation
2. HTTP client like curl for request sending
3. DNS resolution control via collaborator service

## Defense

Defensive measures and detection strategies:

- Resolve and validate domains server-side against public DNS before fetching
- Block requests to private/reserved IP ranges post-resolution
- Log and alert on out-of-band DNS/HTTP interactions to collaborator-like domains
- Deploy network segmentation to limit internal access from public endpoints

## Objectives

1. Bypass domain validation to force internal server requests
2. Confirm SSRF via out-of-band detection
3. Enable reconnaissance of internal hosts and ports

## Instructions

### Step 1: Generate Spoofed Domain

**Context**: Create a unique domain in Burp Collaborator that can be configured to resolve to 127.0.0.1 for internal spoofing.

No command; use Burp Suite Collaborator interface to poll for a new domain like 'spoofed.burpcollaborator.net' and set its resolution to localhost.

> Expected: Unique domain ready for use in requests.

### Step 2: Send Request to Spoofed Domain

**Context**: Trigger the SSRF by requesting the icon from the spoofed domain, causing the server to resolve and request internally.

**Command** ([[commands/curl-http-request]]):
```bash
curl -i https://icons.bitwarden.net/spoofed.burpcollaborator.net/icon.png
```

> This sends the request; expect HTTP 404 Not Found. Check Burp Collaborator for DNS resolution from the target's IP, confirming the server followed the domain to 127.0.0.1.

### Step 3: Validate Internal Interaction

**Context**: Monitor for signs of internal request, such as collaborator pings, to verify exploitation.

No command; refresh Burp Collaborator poll for interactions.

> Success: Incoming DNS query or HTTP request logged, indicating SSRF success. Extend by testing ports (e.g., spoofed.burpcollaborator.net:8080) for scanning.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-http-request]]

## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[bypass]]
- [[Reconnaissance]]
