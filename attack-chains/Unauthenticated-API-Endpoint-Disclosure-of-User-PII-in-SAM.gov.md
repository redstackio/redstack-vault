---
tags:
  - information-disclosure
  - api-exposure
  - pii-leak
  - unauthenticated-access
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-get-sam-api-applications]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Retrieve-Sensitive-User-Data-via-Exposed-API-Endpoint]]'
step_count: 1
techniques:
  - '[[T1213.003]]'
description: >-
  An attack chain exploiting an unauthenticated API endpoint in SAM.gov to
  disclose sensitive user information including PII, emails, names, IP
  addresses, physical locations, and Okta integration details.
skill_level: beginner
impact_level: high
id: 75dd0aac-8eae-4ef6-be48-fa664dd5bf6f
created_at: '2025-12-14T17:32:10.319Z'
updated_at: '2025-12-14T17:32:10.319Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[T1213.003]]'
---
# Unauthenticated API Endpoint Disclosure of User PII in SAM.gov

## Overview

This attack chain demonstrates the exploitation of an unauthenticated API endpoint in the U.S. General Services Administration's SAM.gov system, which exposes sensitive user information related to system accounts. By directly accessing the endpoint via a simple HTTP GET request, an attacker can retrieve JSON data containing personally identifiable information (PII) such as user emails, names, IP addresses, physical locations, and details on integrations like Okta usage. This disclosure enables threat actors to identify targets for phishing, social engineering, or further attacks, potentially compromising user privacy and system security.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance via API Access] --> B[Data Collection and Exfiltration]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-get-sam-api-applications]] (or any HTTP client like browser or wget)

### Target Environment

- Web platform
- Accessible public internet
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- No credentials required
- Direct network access to https://sam.gov
- No prior access needed

## Detailed Attack Procedures

### Step 1: Access Exposed API Endpoint
procedure: [[procedures/Retrieve-Sensitive-User-Data-via-Exposed-API-Endpoint]]

**Objective**: Retrieve a list of application objects containing sensitive user PII without authentication, enabling identification of targets and system details.

**Instructions**: Use [[commands/curl-get-sam-api-applications]] to send a GET request to the vulnerable endpoint:

```bash
curl -X GET "https://sam.gov/api/prod/iam/cws/v1/applications/"
```

Parse the returned JSON for user details such as emails, names, IP addresses, locations, and Okta integration status.

**Expected Output**: JSON array of application objects with fields like user emails, names, organization IPs, physical addresses, and integration flags (e.g., Okta usage).

**Success Indicators**:
- HTTP 200 response with JSON data
- Presence of PII fields in the response (e.g., email addresses, IP details)
- No authentication prompt or error

## Attack Chain Summary

### Key Achievements

1. Successful unauthenticated access to sensitive API data
2. Disclosure of PII for multiple users and organizations
3. Identification of potential targets via emails, locations, and integrations like Okta

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[T1213.003]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]
- [[Collection]]

---
*Last updated: 2023-10-01*
