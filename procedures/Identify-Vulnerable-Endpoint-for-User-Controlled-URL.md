---
id: proc-uuid-1
tags:
  - web
  - recon
  - ssrf
type: procedure
tools:
  - '[[tools/Burp-Suite-Professional]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:26.534Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Endpoint for User-Controlled URL

## Summary

This procedure involves reconnaissance to identify web endpoints that accept user-supplied URLs for fetching and rendering content, potentially vulnerable to XSS or SSRF due to lack of validation.

## Description

In web applications, parameters that allow arbitrary URL inputs can lead to security issues if the server fetches and renders content without sanitization. This procedure uses proxy interception to spot such endpoints, focusing on those that process paths and domains supplied by users. The target environment is a web app like the one at https://█████/████&url=, where the server issues requests to user domains and renders paths directly.

## Requirements

1. Proxy tool like Burp Suite for intercepting and inspecting requests
2. Network access to the target web application
3. Basic understanding of HTTP parameters and server-side fetching

## Defense

Defensive measures and detection strategies:

- Implement URL validation to whitelist allowed domains and paths
- Use Content Security Policy (CSP) to prevent inline script execution
- Monitor for anomalous outbound requests from the server (SSRF detection)

## Objectives

1. Locate endpoints accepting arbitrary URLs
2. Confirm lack of sanitization in path rendering
3. Identify potential for chaining with other exploits like XSS

## Instructions

### Step 1: Intercept Application Traffic

**Context**: Use a proxy to capture requests and identify parameters handling URLs.

No specific command; configure Burp Suite as a proxy and browse the application to log traffic. Look for GET/POST parameters like 'url' that include external domains.

> Inspect responses for evidence of server-side fetching, such as dynamic content insertion from the URL path.

### Step 2: Test for Arbitrary URL Acceptance

**Context**: Submit test URLs to verify if the server processes arbitrary inputs.

Manually craft requests in Burp Repeater, e.g., https://█████/████&url=http://example.com/test, and check if the response renders content from example.com.

> Expected output: Server fetches and embeds the path content without errors or restrictions.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite-Professional]]

## Tags

- [[web]]
- [[recon]]
- [[ssrf]]
