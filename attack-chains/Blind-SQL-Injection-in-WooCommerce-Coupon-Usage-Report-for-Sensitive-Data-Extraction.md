---
tags:
  - sqli
  - blind-sqli
  - woocommerce
  - wordpress
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-to-WordPress-Admin-with-Reports-Privilege]]'
  - '[[procedures/Exploit-SQL-Injection-in-Coupon-Codes-Parameter]]'
  - '[[procedures/Confirm-Blind-SQL-Injection-via-Response-Delay]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:05.176Z'
description: >-
  Authenticated attack exploiting SQL injection in WooCommerce's coupon usage
  report to confirm blind SQLi and potentially extract database contents.
skill_level: intermediate
impact_level: high
id: 59e3eb6b-a78f-4938-bab0-975fc2a13d88
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Blind SQL Injection in WooCommerce Coupon Usage Report for Sensitive Data Extraction

Multi-stage attack chain demonstrating exploitation of a SQL injection vulnerability in the WooCommerce plugin's WC_Report_Coupon_Usage report feature. An authenticated attacker with view reports privileges can inject malicious SQL payloads into the coupon_codes parameter, leading to blind SQL injection that allows extraction of sensitive data like user information or orders from the MySQL database.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Login to Admin] --> B[Inject SQL Payload]
    B --> C[Observe Delay and Confirm]
    C --> D[Data Exfiltration Potential]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web platform running WordPress with WooCommerce 9.9.3 or vulnerable version
- MySQL database backend
- PHP tech stack

### Initial Access Requirements

- Valid WordPress credentials with 'view reports' privileges (e.g., shop manager role)
- Network access to the WordPress admin endpoint
- Logged-in session cookie

## Detailed Attack Procedures

### Step 1: Login to WordPress Admin

procedure: [[procedures/Login-to-WordPress-Admin-with-Reports-Privilege]]

**Objective**: Gain authenticated access to the WordPress admin dashboard with sufficient privileges to access WooCommerce reports.

**Instructions**: Use a browser or tool to log in with an account that has 'view reports' privileges. Capture the session cookie for subsequent requests.

**Expected Output**: Successful login redirect to /wp-admin/ with active session.

**Success Indicators**:
- Access to /wp-admin/admin.php?page=wc-reports
- Valid session cookie obtained

### Step 2: Inject SQL Payload

procedure: [[procedures/Exploit-SQL-Injection-in-Coupon-Codes-Parameter]]

**Objective**: Send a crafted GET request to the coupon usage report endpoint with a SQL injection payload in the coupon_codes parameter.

**Instructions**: Intercept the request using [[tools/Burp-Suite]] or execute via [[commands/curl-sqli-payload]] to the endpoint /wp-admin/admin.php?page=wc-reports&tab=orders&report=coupon_usage, injecting the payload ') union select 1,sleep(10)-- - into coupon_codes.

```bash
curl -X GET "http://<target>/wp-admin/admin.php?page=wc-reports&tab=orders&report=coupon_usage&coupon_codes=%27)%20union%20select%201,sleep(10)--%20-" -H "Cookie: <session_cookie>" -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```

Replace <target> with the host and <session_cookie> with the logged-in cookie.

**Expected Output**: HTTP response after delay, confirming injection.

**Success Indicators**:
- Request accepted without error
- Payload reaches the SQL query

### Step 3: Confirm Vulnerability

procedure: [[procedures/Confirm-Blind-SQL-Injection-via-Response-Delay]]

**Objective**: Observe the time-based delay to verify blind SQL injection success.

**Instructions**: Time the response from the injected request using [[tools/Burp-Suite]] Repeater or [[commands/curl-sqli-payload]]. A normal request should respond quickly, while the payload induces a 10-second sleep.

**Expected Output**: Response delayed by approximately 10 seconds.

**Success Indicators**:
- Noticeable delay compared to non-payload request
- No SQL error, indicating blind injection

## Attack Chain Summary

### Key Achievements

1. Authenticated access to WooCommerce reports
2. Successful SQL payload injection without syntax errors
3. Confirmation of blind SQLi via time delay, enabling potential data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
