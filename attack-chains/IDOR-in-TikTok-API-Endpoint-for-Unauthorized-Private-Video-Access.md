---
tags:
  - idor
  - api
  - unauthorized-access
  - private-media
  - tiktok
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-api-request]]'
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-IDOR-in-TikTok-API-for-Private-Video-Access]]'
step_count: 1
techniques:
  - '[[Account Discovery]]'
description: >-
  An attack chain exploiting an Insecure Direct Object Reference (IDOR)
  vulnerability in the TikTok API to gain unauthorized access to private videos
  from other user accounts without proper authentication checks.
skill_level: intermediate
impact_level: medium
id: 951adedc-944e-4b3b-ac5d-3c1f8579c497
created_at: '2025-12-14T17:32:48.540Z'
updated_at: '2025-12-14T17:32:48.540Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# IDOR in TikTok API Endpoint for Unauthorized Private Video Access

## Overview

This attack chain demonstrates the exploitation of an Insecure Direct Object Reference (IDOR) vulnerability in a TikTok API endpoint. The vulnerability allows attackers to access private videos from other user accounts by manipulating object references in API requests, bypassing authentication and access controls. Reported via HackerOne (Report #2868084), this medium-severity issue exposed private user media, leading to TikTok's remediation. The chain focuses on identifying and exploiting the flaw to retrieve unauthorized content, highlighting risks in API design without proper authorization checks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance and Identification] --> B[Exploitation]
    B --> C[Data Access and Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- TikTok API endpoints
- No specific ports required (HTTPS/443)
- Network access to TikTok's public API

### Initial Access Requirements

- No credentials needed due to the public-facing nature of the API
- Internet connectivity
- Basic knowledge of API request crafting

## Detailed Attack Procedures

### Step 1: Exploit IDOR Vulnerability
procedure: [[procedures/Exploit-IDOR-in-TikTok-API-for-Private-Video-Access]]

**Objective**: Manipulate the API request to reference private videos from unauthorized user accounts, retrieving content that should be restricted.

**Instructions**: Identify the vulnerable API endpoint (e.g., one handling video retrieval by ID or user ID). Craft an HTTP request to access a private video by altering the object reference parameter (e.g., user_id or video_id) to target another account's private media. Use [[commands/curl-api-request]] to send the manipulated request:

```bash
curl -X GET "https://api.tiktok.com/v1/videos/{video_id}?user_id={target_user_id}" -H "User-Agent: Mozilla/5.0"
```

Validate the response for unauthorized content. If successful, the API returns private video data without requiring ownership authentication.

**Expected Output**: JSON response containing video metadata and access to private media, such as video URLs or thumbnails, that would otherwise be inaccessible.

**Success Indicators**:
- API returns private video data for a non-owned account
- No authentication errors; content loads successfully
- Video metadata includes restricted fields (e.g., private status bypassed)

## Attack Chain Summary

### Key Achievements

1. Bypassed access controls to view private TikTok videos
2. Demonstrated unauthorized data exposure via API manipulation
3. Highlighted remediation needs for object reference validation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Account Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Collection]]

---
*Last updated: 2023-10-01*
