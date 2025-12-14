---
id: proc-001-inspect-endpoints
tags:
  - information-disclosure
  - api-key-leak
type: procedure
tools: []
tactics:
  - '[[Credential Access]]'
commands:
  - '[[commands/curl]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T12:00:00Z'
techniques:
  - '[[Unsecured Credentials]]'
updated_at: '2025-12-14T17:32:48.555Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques:
  - '[[Cloud Instance Metadata API]]'
validated: true
mitre_tactics:
  - '[[Credential Access]]'
mitre_techniques:
  - '[[Unsecured Credentials]]'
---
# Inspect-Endpoints-for-Exposed-API-Keys

## Summary

This procedure involves manually inspecting web endpoints and subdomains for publicly exposed API keys, such as Google API keys hardcoded in client-side JavaScript or response data, enabling credential harvesting without authentication.

## Description

In scenarios like the FetLife vulnerability, API keys are often embedded in public-facing web pages or API responses without server-side restrictions. Attackers use browser tools to scan multiple subdomains (e.g., ass0.fetlife.com, app.fetlife.com) for patterns like 'AIza...' indicating Google services. This reconnaissance step uncovers credentials for further exploitation, such as API abuse leading to financial costs or service disruption. Prerequisites include basic web knowledge; no special access is needed as endpoints are public.

## Requirements

1. Web browser with developer tools (e.g., Chrome)
2. List of target subdomains
3. Internet access to public sites

## Defense

Defensive measures and detection strategies:

- Restrict API keys to specific referrers or IP ranges in Google Cloud Console
- Scan client-side code for hardcoded secrets using tools like TruffleHog
- Monitor API usage logs for anomalous patterns from unauthorized sources

## Objectives

1. Extract valid API keys from exposed endpoints
2. Identify unrestricted keys vulnerable to abuse
3. Assess potential impact on target services

## Instructions

### Step 1: Enumerate and Access Subdomains

**Context**: Compile a list of target subdomains and access them to inspect for leaks.

Navigate to each subdomain (e.g., https://ass0.fetlife.com/, https://app.fetlife.com/) using a browser.

**Command** ([[browse-subdomain]]):
```bash
# Use curl to fetch page content for inspection
curl -s https://ass0.fetlife.com/ | grep -i "AIza"
```

> This command fetches the page and greps for Google API key patterns. Expected output: Lines containing 'AIza████████DM' if exposed.

### Step 2: Inspect Developer Tools

**Context**: Use browser dev tools to examine network requests and source code.

Open F12, go to Network tab, reload the page, and search for API-related responses.

**Command** ([[curl-inspect-response]]):
```bash
curl -v https://fetlife.com/ 2>&1 | grep -i "api"
```

> Verbose curl output reveals headers and body; grep for API mentions. Success shows key in response body.

## MITRE ATT&CK Mapping

### Tactics

- [[Credential Access]] Credential Access

### Techniques

- [[Unsecured Credentials]] Unsecured Credentials

### Sub-Techniques

- [[Cloud Instance Metadata API]] Unsecured Stored Credentials

## Commands Used

- [[curl]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[api-key-leak]]
