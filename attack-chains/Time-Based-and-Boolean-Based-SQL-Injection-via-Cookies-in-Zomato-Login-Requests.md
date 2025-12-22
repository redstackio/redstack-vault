---
tags:
  - sqli
  - time-based
  - boolean-based
  - cookies
  - web
  - mysql
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Observe-Cookies-During-Login-Request]]'
  - '[[procedures/Fuzz-Cookies-for-SQL-Injection-Vulnerabilities]]'
  - '[[procedures/Test-Orange-Cookie-with-Time-Based-Payload]]'
  - '[[procedures/Extract-Database-Version-Using-Orange-Cookie]]'
  - '[[procedures/Test-Squeeze-Cookie-with-Boolean-Based-Payloads]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.849Z'
description: >-
  Multi-stage attack exploiting SQL injection vulnerabilities in 'orange' and
  'squeeze' cookies on the Zomato reviews login page, enabling database version
  inference and potential data extraction through timing and boolean techniques.
skill_level: intermediate
impact_level: high
id: 4af46b58-7760-4f80-af85-e4801ff5bc66
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based and Boolean-Based SQL Injection via Cookies in Zomato Login Requests

Multi-stage attack chain demonstrating the discovery and exploitation of SQL injection vulnerabilities in oddly named cookies ('orange' and 'squeeze') submitted to the login page of https://reviews.zomato.com, allowing inference of database information through time delays and boolean responses, with critical impact on unauthorized data access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Observe Cookies] --> B[Fuzz for Vulnerabilities]
    B --> C[Test Time-Based on Orange Cookie]
    C --> D[Extract Database Info]
    D --> E[Test Boolean on Squeeze Cookie]
    E --> F[Potential Data Exfiltration]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#9b59b6
    style E fill:#1abc9c
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Browser developer tools or proxy like Burp Suite for cookie manipulation

### Target Environment

- Web application at https://reviews.zomato.com/login
- MySQL database backend
- No specific ports required beyond standard HTTPS (443)

### Initial Access Requirements

- Public access to the login page
- Ability to intercept and modify HTTP requests (e.g., via proxy)
- No credentials needed for initial observation

## Detailed Attack Procedures

### Step 1: Observe Cookies During Login
procedure: [[procedures/Observe-Cookies-During-Login-Request]]

**Objective**: Identify unusual cookies in login requests to uncover potential injection points.

**Instructions**: Access the login page at https://reviews.zomato.com and monitor the HTTP request using browser dev tools or a proxy. Look for cookies named 'orange' and 'squeeze' in the request headers.

**Expected Output**: Request headers showing 'Cookie: orange=...; squeeze=...' in POST to /login.

**Success Indicators**:
- Cookies 'orange' and 'squeeze' observed in login request
- Normal response is HTTP 302 redirect on failed login

### Step 2: Fuzz Cookies for Vulnerabilities
procedure: [[procedures/Fuzz-Cookies-for-SQL-Injection-Vulnerabilities]]

**Objective**: Test cookie values for SQL injection by injecting common payloads and observing response anomalies.

**Instructions**: Intercept the login request and replace 'orange' and 'squeeze' values with fuzzing payloads like '1' OR '1'='1', single quotes, or SQL keywords. Send multiple variations and note any errors or delays.

**Expected Output**: Variations in response times or status codes indicating potential injection.

**Success Indicators**:
- Anomalous responses (e.g., delays or different redirects) when fuzzing cookies
- Confirmation of unsanitized cookie handling

### Step 3: Test Orange Cookie with Time-Based Payload
procedure: [[procedures/Test-Orange-Cookie-with-Time-Based-Payload]]

**Objective**: Confirm time-based blind SQL injection in the 'orange' cookie by inducing server delays.

**Instructions**: Modify the 'orange' cookie value to '1'=sleep(10)='1' and submit the login request. Time the response.

**Expected Output**: HTTP 200 response after ~10-second delay instead of immediate 302.

**Success Indicators**:
- Response delay matching sleep duration
- No redirect, indicating query execution

### Step 4: Extract Database Version Using Orange Cookie
procedure: [[procedures/Extract-Database-Version-Using-Orange-Cookie]]

**Objective**: Infer database version through conditional timing attacks on the 'orange' cookie.

**Instructions**: Inject payloads like '1'=IF(MID(VERSION(),1,1)=1,SLEEP(10),0)='1' and '1'=IF(MID(VERSION(),1,1)=5,SLEEP(10),0)='1' into 'orange'. Compare response times to binary search the version string.

**Expected Output**: Delays on true conditions, revealing version (e.g., MySQL 5.x).

**Success Indicators**:
- Selective delays confirming version characters
- Successful inference of full database version

### Step 5: Test Squeeze Cookie with Boolean-Based Payloads
procedure: [[procedures/Test-Squeeze-Cookie-with-Boolean-Based-Payloads]]

**Objective**: Verify boolean-based blind SQL injection in the 'squeeze' cookie using true/false conditions.

**Instructions**: Set 'squeeze' to '1 ' OR true#' and '1 ' OR false#', submit requests, and observe response differences (e.g., success vs. failure).

**Expected Output**: Different behaviors (e.g., 302 on true, 200 on false) indicating injection.

**Success Indicators**:
- Response variance based on boolean payload truthiness
- Confirmation of query manipulation via cookies

## Attack Chain Summary

### Key Achievements

1. Discovered injectable cookies in login flow
2. Confirmed time-based SQLi in 'orange' cookie with delays
3. Verified boolean-based SQLi in 'squeeze' cookie
4. Inferred MySQL version, paving way for data extraction
5. Reported vulnerability, earning $1,000 bounty

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
