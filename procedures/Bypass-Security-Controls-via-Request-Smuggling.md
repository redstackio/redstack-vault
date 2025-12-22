---
tags:
  - bypass
  - cloudflare-access
  - http-request-smuggling
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/curl-bypass-access]]'
platforms:
  - Cloud (Cloudflare)
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 5fde655d-6d40-44ba-9ab3-5fed537056ad
created_at: '2025-12-13T09:01:22.256Z'
updated_at: '2025-12-13T09:01:22.256Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Bypass Security Controls via Request Smuggling

## Summary

This procedure utilizes the smuggled requests from prior injection to bypass Cloudflare Access and gain unauthorized access to internal origin server content.

## Description

Leveraging the desynchronized requests, attackers can route traffic past security layers, accessing protected resources. This is specific to Cloudflare setups and highlights risks in API-driven configurations.

## Requirements

1. Successfully injected rules from previous steps
2. Target domain under Cloudflare management
3. Monitoring tools to verify bypass

## Defense

Defensive measures and detection strategies:

- Regularly audit Origin Rules for anomalies
- Implement rate limiting and anomaly detection on API calls

## Objectives

1. Bypass Cloudflare Access
2. Access internal content
3. Demonstrate full impact

## Instructions

### Step 1: Send Smuggled Request

**Context**: Craft a request that exploits the smuggling to bypass controls.

Execute [[commands/curl-bypass-access]]:

```bash
curl 'https://target.cloudflare-managed-domain.com/' \
  -H 'Host: example.com\r\nX-Forwarded-Host: internal.origin' \
  --data 'smuggled_request_body'
```

> This should route to internal servers.

### Step 2: Validate Access

**Context**: Check the response for internal data.

Review the output for signs of bypassed access, such as internal server responses.

> Expected: Content from protected origins.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-bypass-access]]

## Tools Used

- [[tools/curl]]

## Tags

- [[bypass]]
- [[cloudflare-access]]
