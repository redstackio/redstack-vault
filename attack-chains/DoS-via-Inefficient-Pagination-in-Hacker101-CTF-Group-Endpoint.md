---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - dos
  - resource-exhaustion
  - pagination
  - web
type: attack_chain
tools: []
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]'
step_count: 5
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.229Z'
description: >-
  Multi-stage attack exploiting uncontrolled resource consumption in a paginated
  web endpoint, leading to server delays and potential DoS.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# DoS via Inefficient Pagination in Hacker101 CTF Group Endpoint

Multi-stage attack chain demonstrating a complete DoS workflow by exploiting inefficient pagination in a web application's group listing endpoint, causing high memory usage and server crashes for users with large datasets.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~45 seconds per request |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Website] --> B[Authenticate with Large Dataset Account]
    B --> C[Send Crafted Request]
    C --> D[Observe Delay and Error]
    D --> E[Scale for DoS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or HTTP client like curl

### Target Environment

- Web platform with SQLAlchemy backend
- Paginated endpoints using SQLAlchemy-Paginator
- Services: Cloudflare, SQL database

### Initial Access Requirements

- Valid credentials for an account with 3000+ groups
- Network access to the target site (e.g., ctf.hacker101.com)
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Access the Target Website
procedure: [[procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]

**Objective**: Gain initial access to the vulnerable web application.

**Instructions**: Open a web browser and navigate to the target site.

**Expected Output**: The homepage loads successfully.

**Success Indicators**:
- Site is accessible without errors
- No rate limiting or blocks encountered

### Step 2: Log in to a Test Account with a Large Number of Groups
procedure: [[procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]

**Objective**: Authenticate using an account that triggers high resource usage due to many groups.

**Instructions**: Use the site's login form with credentials for an old account having around 3000+ groups.

**Expected Output**: Successful login, session cookie established.

**Success Indicators**:
- Dashboard or group listing page loads
- Account has verifiable large group count

### Step 3: Send a Crafted HTTP Request to the /group Endpoint
procedure: [[procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]

**Objective**: Trigger resource exhaustion by requesting the paginated group list.

**Instructions**: Use [[commands/crafted-get-group-dos]] to send a GET request with specific headers while authenticated:

```bash
curl -X GET "https://ctf.hacker101.com/group" \
  -H "User-Agent: Mozilla/5.0 (Linux; Android 10; ONEPLUS A6000) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.117 Mobile Safari/537.36" \
  -H "Accept-Encoding: gzip, gzip,deflate,br" \
  -H "Cookie: [valid_session_cookie]" \
  -H "Referer: https://ctf.hacker101.com/group"
```

**Expected Output**: Request hangs for 40-50 seconds before returning a 502 Bad Gateway.

**Success Indicators**:
- Significant delay observed
- Server returns error page from Cloudflare

### Step 4: Observe the Server Response
procedure: [[procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]

**Objective**: Confirm the vulnerability by noting the delay and error.

**Instructions**: Monitor the response time and content after sending the request.

**Expected Output**: HTTP/1.1 502 Bad Gateway with Cloudflare error indicating host error.

**Success Indicators**:
- Response time exceeds 40 seconds
- Error code 502 received

### Step 5: Note Potential for DoS with Multiple Requests
procedure: [[procedures/Trigger-Pagination-DoS-in-Web-Endpoint]]

**Objective**: Understand scalability to full DoS without executing.

**Instructions**: Simulate mentally or in a controlled environment; avoid concurrent requests on production.

**Expected Output**: Hypothetical server crash from multiple tabs or parallel requests.

**Success Indicators**:
- Single request causes delay; multiples would amplify to outage

## Attack Chain Summary

### Key Achievements

1. Identified inefficient pagination loading all results into memory
2. Triggered 40-50 second delays and 502 errors
3. Demonstrated potential for site-wide DoS via concurrent requests

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T12:00:00Z*
