---
tags:
  - information-disclosure
  - reconnaissance
  - nginx
  - http-headers
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Web-Login-Endpoint]]'
  - '[[procedures/Inspect-HTTP-Response-Headers]]'
step_count: 2
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:56.008Z'
description: >-
  A simple reconnaissance attack chain that demonstrates discovering the nginx
  server version through exposed HTTP response headers on a web login page,
  aiding in vulnerability research.
skill_level: beginner
impact_level: low
id: f8c24567-3a5b-44a0-8b9b-b4ee1220881a
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Nginx Server Version Disclosure via HTTP Response Headers

Multi-stage attack chain demonstrating a reconnaissance workflow to identify server software details through information leakage in HTTP headers.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Login Page] --> B[Inspect Headers]
    B --> C[Version Identified]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Web platform with HTTP services
- Access to login endpoint (e.g., https://jenkins.brew.sh/login)
- No authentication required for initial access

### Initial Access Requirements

- Public network access to the target URL
- No credentials needed
- Basic HTTP client (browser or curl)

## Detailed Attack Procedures

### Step 1: Access Login Page
procedure: [[procedures/Access-Web-Login-Endpoint]]

**Objective**: Navigate to the target's login endpoint to trigger the HTTP response containing server headers.

**Instructions**: Use a browser or [[commands/curl-fetch-headers]] to send an HTTP GET request to the login page without authenticating.

```bash
curl -I https://jenkins.brew.sh/login
```

**Expected Output**: HTTP response headers, including the 'Server' field revealing nginx details.

**Success Indicators**:
- HTTP 200 OK or redirect response received
- Access to the login page confirmed

### Step 2: Inspect Response Headers
procedure: [[procedures/Inspect-HTTP-Response-Headers]]

**Objective**: Analyze the HTTP response headers to extract and identify the disclosed server software version.

**Instructions**: Review the headers from the previous request, focusing on the 'Server' header. Use browser developer tools or parse the curl output.

```bash
curl -I https://jenkins.brew.sh/login | grep Server
```

**Expected Output**: Output showing 'Server: nginx/1.x.x' or similar, disclosing the exact version.

**Success Indicators**:
- Server header present and unredacted
- Nginx version number visible (e.g., 1.18.0)

## Attack Chain Summary

### Key Achievements

1. Successful access to the login endpoint without authentication
2. Identification of nginx server version through header inspection
3. Potential for further reconnaissance on known vulnerabilities in the disclosed version

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Host Information]]
- [[Software]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
