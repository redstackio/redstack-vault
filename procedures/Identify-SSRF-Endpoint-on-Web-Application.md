---
tags:
  - ssrf
  - reconnaissance
  - web-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-external-url-test]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Active Scanning]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 323948c1-ad80-43df-b73f-e5f90161014b
created_at: '2025-12-14T03:53:38.449Z'
updated_at: '2025-12-14T03:53:38.449Z'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-SSRF-Endpoint-on-Web-Application

## Summary

This procedure involves systematically testing web application endpoints to identify those vulnerable to Server-Side Request Forgery (SSRF) by supplying external URLs and observing if the server fetches and returns their content.

## Description

In the context of the Starbucks Ideas portal, SSRF was discovered in an endpoint lacking validation for user-supplied URLs, allowing arbitrary server-side HTTP requests. This procedure simulates manual testing to find such features, typically in URL parameters for imports, shares, or submissions. Prerequisites include basic web pentesting knowledge and tools like Burp Suite. Expected outcomes are confirmation of SSRF via echoed external responses, enabling further internal exploitation.

## Requirements

1. Access to the target web application (e.g., ideas.starbucks.com) over HTTPS
2. Proxy tool like [[tools/Burp-Suite]] for request interception
3. No authentication required for public endpoints

## Defense

Defensive measures and detection strategies:

- Implement URL whitelisting to restrict requests to trusted domains
- Use network segmentation to isolate internal services from public-facing apps
- Monitor server logs for unusual outbound requests to external or internal IPs

## Objectives

1. Locate endpoints accepting user-controlled URLs
2. Confirm SSRF by fetching external resources
3. Prepare for internal payload testing

## Instructions

### Step 1: Map Application Endpoints

**Context**: Browse the application to identify features involving URL inputs, such as idea submissions or link sharing.

**Command** ([[commands/curl-external-url-test]]):
```bash
curl "https://ideas.starbucks.com/endpoint?url=https://example.com" -v
```

> This sends a request with an external URL; success is indicated if the response includes content from example.com, confirming server-side fetching.

### Step 2: Intercept and Modify Requests

**Context**: Use Burp Suite to tamper with URL parameters and test for SSRF.

**Command** ([[commands/curl-external-url-test]]):
```bash
curl -X POST "https://ideas.starbucks.com/submit?url=http://httpbin.org/ip" -d "data=some" -v
```

> Replace with actual endpoint; expected output includes the client's IP from httpbin.org in the app's response.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-external-url-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssrf]]
- [[web-vulnerability]]
