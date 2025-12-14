---
id: proc-uber-js-access-001
tags:
  - info-disclosure
  - auth-bypass
  - misconfiguration
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-fetch-uber-js-file]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:11.326Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Uber-Staging-Static-JS-File-Without-Auth

## Summary

This procedure exploits a server misconfiguration on Uber's uchat-staging.uberinternal.com to access a static JavaScript file containing sensitive internal configuration data, system names, and source code without any authentication, such as OneLogin SSO. It demonstrates information disclosure via improper access controls on public-facing static assets.

## Description

The target server hosts static files intended for authenticated internal use but fails to enforce authentication checks, allowing anyone with the direct URL to retrieve sensitive information. This can reveal API keys, endpoint configurations, and code snippets that aid in mapping Uber's internal architecture for further attacks like targeted reconnaissance or exploitation. The procedure assumes public internet access and uses simple HTTP requests to fetch the file, highlighting the ease of such misconfigurations in staging environments.

## Requirements

1. Internet connectivity to reach https://uchat-staging.uberinternal.com
2. curl or a web browser for HTTP requests
3. No credentials or special permissions needed due to the bypass

## Defense

Defensive measures and detection strategies:

- Enforce authentication middleware on all static file routes, including CDN configurations
- Implement URL signing or access tokens for sensitive assets
- Monitor access logs for anomalous requests to internal/staging domains from external IPs
- Use web application firewalls (WAF) to block direct access to config files

## Objectives

1. Retrieve the unencrypted JavaScript file with internal details
2. Analyze disclosed configurations for further attack vectors
3. Demonstrate the impact of missing auth checks on staging servers

## Instructions

### Step 1: Fetch the Static JavaScript File

**Context**: Directly request the file using curl to bypass any browser-based restrictions and capture the raw content for analysis.

**Command** ([[commands/curl-fetch-uber-js-file]]):
```bash
curl https://uchat-staging.uberinternal.com/static/main.740f5a0b92c00e72e2e1.js -o uber-config.js
```

> This command downloads the file to uber-config.js. If successful, the file will contain JavaScript code with embedded configuration objects, such as server URLs, API paths, and potentially hardcoded secrets. Review the file with a text editor or grep for keywords like 'api', 'endpoint', or 'config'.

### Step 2: Verify and Analyze Content

**Context**: Inspect the downloaded file to confirm disclosure of sensitive information.

**Command** (grep for analysis):
```bash
grep -i "config\|api\|uberinternal" uber-config.js
```

> Expected output includes lines revealing internal systems, e.g., references to other uberinternal.com subdomains or source code functions. Success is indicated by the presence of non-public data without authentication prompts.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-uber-js-file]]

## Tools Used


## Tags

- info-disclosure
- auth-bypass
- misconfiguration
