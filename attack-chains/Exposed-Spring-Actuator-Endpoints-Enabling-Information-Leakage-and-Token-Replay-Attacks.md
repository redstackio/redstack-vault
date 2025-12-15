---
id: ac-838635-001
tags:
  - spring-boot
  - actuator
  - information-leakage
  - broken-authentication
  - token-replay
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Spring Boot
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Exposed-Spring-Actuator-Endpoints]]'
  - '[[procedures/Access-Actuator-Endpoints-for-Data-Leakage]]'
  - '[[procedures/Exploit-Broken-Authentication-for-Token-Replay]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T17:31:52.930Z'
description: >-
  A multi-stage attack exploiting publicly accessible Spring Boot Actuator
  endpoints for sensitive data leakage and a broken authentication mechanism
  allowing token replay attacks on sensitive applications.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
  - '[[Use Alternate Authentication Material]]'
---
# Exposed Spring Actuator Endpoints Enabling Information Leakage and Token Replay Attacks

Multi-stage attack chain demonstrating exploitation of misconfigured Spring Boot Actuator endpoints and flawed authentication in shared libraries, leading to unauthorized data access and potential application compromise in sensitive environments.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discovery of Exposed Endpoints] --> B[Access and Leakage of Sensitive Data]
    B --> C[Token Replay for Unauthorized Access]
    C --> D[Data Exposure and Application Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser or [[curl]] for endpoint access
- No specialized tools required; standard HTTP clients suffice

### Target Environment

- Web platform with Spring Boot applications
- Exposed Actuator endpoints on default ports (e.g., 8080)
- Network access to the target applications

### Initial Access Requirements

- Public internet access to the target URLs
- No prior credentials needed for endpoint discovery and access
- Knowledge of target application URLs

## Detailed Attack Procedures

### Step 1: Discovery of Exposed Endpoints
procedure: [[procedures/Discover-Exposed-Spring-Actuator-Endpoints]]

**Objective**: Identify publicly accessible Spring Boot Actuator endpoints without authentication controls to reveal potential information leakage vectors.

**Instructions**: Manually inspect the target application URLs for common Actuator paths or use directory enumeration techniques to probe for /heapdump and /env. For example, append these paths to the base URL and check for responses.

**Expected Output**: HTTP 200 responses from /heapdump (binary heap dump) or /env (JSON environment variables), indicating exposure.

**Success Indicators**:
- Endpoints return data without prompting for authentication
- Sensitive details like environment variables or memory dumps are accessible

### Step 2: Access Endpoints for Data Leakage
procedure: [[procedures/Access-Actuator-Endpoints-for-Data-Leakage]]

**Objective**: Retrieve sensitive information from exposed endpoints, including heap dumps and environment variables, to assess the scope of data exposure.

**Instructions**: Use a browser or HTTP client to directly access the endpoints. For /env, fetch the JSON response to extract variables; for /heapdump, download the binary file for analysis.

**Expected Output**: JSON payload from /env revealing database credentials, API keys, or config details; binary heap dump containing in-memory objects like session tokens.

**Success Indicators**:
- Environment variables include sensitive configs (e.g., passwords, secrets)
- Heap dump parses to show application internals

### Step 3: Exploit Broken Authentication for Token Replay
procedure: [[procedures/Exploit-Broken-Authentication-for-Token-Replay]]

**Objective**: Leverage non-expiring tokens from the shared library's authentication flaw to perform replay attacks, gaining unauthorized access to application features.

**Instructions**: Capture an old authentication token (e.g., from prior sessions or leaked via endpoints), then replay it in subsequent requests to bypass validation. Test by sending requests with the stale token to protected resources.

**Expected Output**: Successful authentication and access to restricted areas using the replayed token.

**Success Indicators**:
- Old token grants access without expiration checks
- Replay succeeds across sessions, confirming the invalidation failure

## Attack Chain Summary

### Key Achievements

1. Exposed Actuator endpoints leading to immediate sensitive data leakage
2. Identification of broken token handling in shared libraries
3. Potential for full unauthorized access via replay, resulting in application shutdown and bounty award

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts
- [[Use Alternate Authentication Material]] Use Alternate Authentication Material

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
