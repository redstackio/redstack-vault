---
tags:
  - information-disclosure
  - full-path-disclosure
  - web-vulnerability
  - reconnaissance
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-fetch-ooni-invalid-url]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Trigger-Full-Path-Disclosure-via-Invalid-URL]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
description: >-
  Demonstrates exploiting a full path disclosure vulnerability in the Tor
  Project's OONI Explorer web application by accessing an invalid URL path,
  leading to the leakage of internal server file paths.
skill_level: novice
impact_level: medium
id: 83693387-7a95-42e6-88c5-c7afd09ddcbd
created_at: '2025-12-14T17:26:12.123Z'
updated_at: '2025-12-14T17:26:12.123Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Full Path Disclosure in Tor OONI Explorer via Invalid URL

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Novice |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Invalid URL] --> B[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web application: OONI Explorer at https://explorer.ooni.torproject.org/
- Required services/ports: HTTP/HTTPS on port 443
- Network access requirements: Internet access to the public-facing web app

### Initial Access Requirements

- No credentials required
- External network position (public internet)
- No prior access needed

## Detailed Attack Procedures

### Step 1: Trigger Path Disclosure
procedure: [[procedures/Trigger-Full-Path-Disclosure-via-Invalid-URL]]

**Objective**: Access an invalid URL path to elicit a 404 error response that discloses the full server file path, enabling reconnaissance of the internal system structure.

**Instructions**: Use [[commands/curl-fetch-ooni-invalid-url]] to send a request to an invalid path on the OONI Explorer application:

```bash
curl https://explorer.ooni.torproject.org//x
```

This request simulates navigating to a non-existent endpoint, triggering the vulnerable 404 handler.

**Expected Output**: A 404 error page or message containing the leaked full server path, such as a string revealing the filesystem location (e.g., "/var/www/html/..." or similar internal path).

**Success Indicators**:
- HTTP 404 status code returned
- Error message includes absolute server file path (e.g., full directory structure like "/home/user/app/...")
- No authentication prompts or blocks encountered

## Attack Chain Summary

### Key Achievements

1. Successfully disclosed internal server file paths without authentication
2. Gained insights into the web server's filesystem layout for potential further reconnaissance or chaining attacks
3. Demonstrated low-effort information disclosure on a public-facing application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01*
