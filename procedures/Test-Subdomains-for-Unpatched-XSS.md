---
id: proc-test-subdomains-unpatched
tags:
  - xss
  - subdomain-testing
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:37.524Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Test-Subdomains-for-Unpatched-XSS

## Summary

This procedure tests web subdomains for unpatched XSS vulnerabilities by loading error pages with reflected parameters, checking for sanitization gaps based on prior known issues.

## Description

Following research on a main domain fix, this targets proxy subdomains like proxy.duckduckgo.com to verify if the 'atb' parameter in 50x.html is still unsanitized, allowing reflection without escaping. It simulates error conditions to observe parameter handling in the DOM.

## Requirements

1. Public access to target subdomains
2. Tool for URL fetching (browser or curl)
3. Knowledge of the parameter to test (e.g., 'atb')

## Defense

Defensive measures and detection strategies:

- Deploy fixes uniformly across all subdomains
- Input validation on error pages
- Log and alert on suspicious parameter tests

## Objectives

1. Confirm lack of sanitization on subdomains
2. Identify vulnerable endpoints
3. Prepare for payload injection

## Instructions

### Step 1: Load Basic Test URL

**Context**: Fetch the error page with empty parameters to inspect reflection.

Execute [[commands/curl-fetch-url]] to retrieve the page:

```bash
curl -s "https://proxy.duckduckgo.com/50x.html?e=&atb=" | grep atb
```

> This command fetches the page silently and greps for 'atb' to check if it's reflected in HTML attributes. Expected output: 'atb' appears unescaped in source.

### Step 2: Inspect in Browser

**Context**: View source to confirm DOM insertion.

Manually load https://proxy.duckduckgo.com/50x.html?e=&atb=test in a browser and inspect the element containing 'atb'.

> Expected output: Value 'test' inserted directly into an attribute without quotes or escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-url]]

## Tools Used


## Tags

- [[xss]]
- [[subdomain-testing]]
