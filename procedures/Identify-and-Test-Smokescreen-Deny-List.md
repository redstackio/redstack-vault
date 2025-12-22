---
id: p-smokescreen-deny-list-test
tags:
  - ssrf
  - recon
  - proxy
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
updated_at: '2025-12-14T03:46:08.924Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify-and-Test-Smokescreen-Deny-List

## Summary

This procedure involves reviewing and testing the deny_list feature in Stripe's Smokescreen proxy to confirm its role in restricting outbound URLs and preventing SSRF attacks from internal services.

## Description

Smokescreen is an open-source Go-based proxy designed to limit outbound connections from internal services. The deny_list provides optional additional restrictions on external URLs. In a typical attack scenario, an attacker with access to an internal service tests this feature by attempting connections to known denied domains, verifying blocks occur due to domain matching logic. This step establishes the baseline for identifying bypass opportunities, targeting environments where Smokescreen is deployed without proper URL normalization.

## Requirements

1. Access to Smokescreen proxy documentation and source code (e.g., GitHub repo)
2. Network access to an internal service using the proxy
3. Ability to submit test URLs via the service's input mechanisms

## Defense

Defensive measures and detection strategies:

- Enable comprehensive logging of proxy requests to monitor denied attempts
- Regularly audit Smokescreen configuration for deny_list completeness
- Implement URL normalization in proxy logic to handle edge cases like trailing dots

## Objectives

1. Confirm deny_list blocks access to restricted domains
2. Understand domain matching behavior for bypass identification
3. Baseline proxy responses for comparison in exploitation

## Instructions

### Step 1: Review Smokescreen Documentation

**Context**: Examine the proxy's functionality to focus on the deny_list for SSRF prevention.

No specific command; consult the Smokescreen GitHub repository at https://github.com/stripe/smokescreen to understand the optional deny_list configuration for external URL restrictions.

> Expected: Insight into how deny_list integrates with core proxy rules.

### Step 2: Test Denied Domain Access

**Context**: Submit a request to a known denied domain to verify blocking.

Use a tool like curl to simulate an internal service request through the proxy:

**Command** ([[commands/curl-test-denied-url]]):
```bash
curl -X GET "http://internal-service-endpoint?url=http://example.com"
```

> This sends a URL to the internal service, which proxies through Smokescreen. Expected output: 403 or block response if example.com is denied.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-denied-url]]

## Tools Used

- [[tools/Smokescreen]]

## Tags

- [[ssrf]]
- [[proxy]]
