---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - intercept
  - proxy
  - burp-suite
  - web-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:48.904Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Capture-Search-Request-with-Burp-Suite

## Summary

This procedure outlines how to configure Burp Suite to intercept and capture HTTP POST requests from the CS.Money search functionality, enabling inspection and modification for vulnerability testing such as ReDoS exploitation.

## Description

In the context of testing web applications like 3d.cs.money, intercepting requests allows security researchers to analyze API calls, such as the /api/skin/search endpoint, which processes JSON payloads for item searches. By capturing a legitimate request, attackers can replicate and alter it to inject malicious inputs that exploit parsing vulnerabilities. This step requires a man-in-the-middle proxy setup and is typically performed in a controlled environment to avoid unintended disruptions.

## Requirements

1. Burp Suite installed and running with proxy listener on port 8080.
2. Browser configured to use Burp as proxy (e.g., via FoxyProxy extension).
3. Access to the target site https://3d.cs.money.
4. Basic knowledge of HTTP requests and JSON formatting.

## Defense

Defensive measures and detection strategies:

- Implement client-side certificate pinning to prevent proxy interception in production.
- Use Web Application Firewalls (WAF) to monitor and block anomalous proxy traffic patterns.
- Log all API requests and alert on unusual user-agent strings associated with tools like Burp.

## Objectives

1. Capture a legitimate search request to understand the API structure.
2. Prepare the request for payload modification.
3. Ensure seamless forwarding without alerting the server.

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up Burp Suite to intercept traffic from the browser.

In Burp Suite, navigate to the Proxy tab, ensure the intercept is on (Intercept is on), and confirm the listener is active on 127.0.0.1:8080.

### Step 2: Perform Normal Search

**Context**: Trigger a search to generate an interceptable request.

Open the browser, navigate to https://3d.cs.money/item/default, and enter a search term like "AK-47" in the search box, then submit.

### Step 3: Inspect and Forward Request

**Context**: Analyze the captured POST request and send it to Repeater.

Review the request details: Method POST to /api/skin/search, body {"name":"AK-47","item_name":"AK-47"}, headers including Content-Type: application/json;charset=utf-8. Click Forward to continue, or right-click and Send to Repeater.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[proxy]]
- [[tools/Burp-Suite]]
- [[web-testing]]
