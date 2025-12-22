---
id: p-smokescreen-trailing-dot-bypass
tags:
  - ssrf
  - bypass
  - domain
type: procedure
tools:
  - '[[tools/Smokescreen]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:08.922Z'
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
# Bypass-Deny-List-with-Trailing-Dot

## Summary

This procedure exploits a flaw in Smokescreen's deny_list by appending a trailing dot to a denied domain, evading the domain matching logic and allowing unauthorized URL access.

## Description

The deny_list in Smokescreen relies on exact domain string matching without normalization for trailing characters like dots. In an attack scenario, an adversary supplies a URL such as 'http://example.com.' to an internal service, causing the proxy to fail the match against 'example.com' in the list. This bypass enables connections to restricted external or internal resources in web environments using the proxy, highlighting the need for robust input sanitization.

## Requirements

1. Confirmed active deny_list from prior testing
2. Ability to inject modified URLs into internal service requests
3. Proxy access via internal network

## Defense

Defensive measures and detection strategies:

- Normalize URLs by stripping trailing dots before matching in deny_list
- Monitor for anomalous URL patterns in proxy logs, such as trailing punctuation
- Use regex-based matching that accounts for common evasion tactics

## Objectives

1. Evade deny_list restrictions on specific domains
2. Establish connectivity to previously blocked URLs
3. Validate bypass for SSRF exploitation

## Instructions

### Step 1: Modify Denied URL

**Context**: Append a trailing dot to a known denied domain to alter the string for matching evasion.

Prepare the URL, e.g., transform 'http://example.com' to 'http://example.com.'.

No command; this is a manual URL modification step.

> Expected: The modified URL string ready for submission.

### Step 2: Submit Bypassed URL

**Context**: Inject the modified URL via the internal service to test proxy allowance.

**Command** ([[commands/curl-bypass-url]]):
```bash
curl -X GET "http://internal-service-endpoint?url=http://example.com."
```

> This proxies the request; expected output: Successful connection or 200 response, unlike the non-bypassed version.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-bypass-url]]

## Tools Used

- [[tools/Smokescreen]]

## Tags

- [[bypass]]
- [[ssrf]]
