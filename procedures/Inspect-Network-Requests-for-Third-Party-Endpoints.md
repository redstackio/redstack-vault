---
id: proc-433792-inspect-network
tags:
  - reconnaissance
  - network-inspection
  - third-party
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-inspect-endpoint]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T03:16:07.775Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Inspect-Network-Requests-for-Third-Party-Endpoints

## Summary

This procedure involves using browser developer tools to monitor and analyze network requests on a target website, identifying third-party endpoints that may serve as attack vectors, such as stats trackers integrated via JavaScript.

## Description

In the context of web applications like Rocket.Chat, static sites often load external scripts for analytics or tracking, which can expose backend APIs. By inspecting these requests, attackers can uncover unsanitized parameters vulnerable to injection attacks. This step requires no special privileges and focuses on passive reconnaissance to map the attack surface, particularly endpoints like AgileCRM's stats API.

## Requirements

1. Web browser with developer tools enabled (e.g., Chrome or Firefox)
2. Public access to the target site (https://rocket.chat/)
3. Basic knowledge of HTTP requests and parameters

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to restrict third-party script loading
- Monitor for anomalous network inspection patterns in web logs
- Use web application firewalls (WAF) to detect request tampering

## Objectives

1. Identify loaded third-party endpoints and their parameters
2. Uncover potential injection points in query strings
3. Establish baseline for further fuzzing

## Instructions

### Step 1: Load Target Page and Open DevTools

**Context**: Navigate to the target website and prepare to capture network activity to spot external API calls.

**Command** ([[commands/curl-inspect-endpoint]]):
```bash
curl -v 'https://rocket.chat/'
```

> This command fetches the page and shows verbose output, including any redirected or embedded requests. In a browser, open DevTools (F12), go to the Network tab, and reload the page to filter for XHR/Fetch requests.

### Step 2: Analyze Requests for Third-Party Domains

**Context**: Filter and examine requests to external domains, noting parameters in URLs.

No specific command; manually inspect in DevTools for requests to domains like stats2.agilecrm.com, documenting parameters such as callback, guid, sid, url, agile, domain, and new.

> Expected output includes full URL: https://stats2.agilecrm.com/addstats?callback=...&new=... confirming the endpoint structure.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-inspect-endpoint]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[network-inspection]]
