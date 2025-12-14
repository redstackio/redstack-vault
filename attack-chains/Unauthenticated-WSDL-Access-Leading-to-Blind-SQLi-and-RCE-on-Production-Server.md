---
tags:
  - unauth-access
  - sqli
  - blind-sqli
  - rce
  - webservice
  - sql-server
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/execute-sql-ping-via-xp_cmdshell]]'
verified: false
platforms:
  - Web
  - Windows
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Unauthenticated-WSDL-Service]]'
  - '[[procedures/Access-Test-Data-via-Unauthenticated-Functions]]'
  - '[[procedures/Exploit-Blind-SQL-Injection]]'
  - '[[procedures/Escalate-to-RCE-via-xp_cmdshell]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:32:48.565Z'
description: >-
  Multi-stage attack exploiting unauthenticated access to a WSDL service, blind
  SQL injection for database access, and escalation to remote code execution via
  xp_cmdshell on a production SQL Server.
skill_level: intermediate
impact_level: high
id: abace440-5a57-41fd-859a-bb4f140090e6
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Server Software Component]]'
  - '[[Windows Command Shell]]'
---
# Unauthenticated WSDL Access Leading to Blind SQLi and RCE on Production Server

Multi-stage attack chain demonstrating exploitation of an unauthenticated WSDL service on a non-standard port under the starbucks.com.cn domain, leading to exposure of test data, blind SQL injection for database access, and remote code execution on a production SQL Server via xp_cmdshell.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover WSDL Service] --> B[Access Unauthenticated Functions]
    B --> C[Exploit Blind SQLi]
    C --> D[Escalate to RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or curl for service discovery
- SQL injection tools like sqlmap for exploitation

### Target Environment

- Web platform with WSDL API webservice on non-standard port
- SQL Server backend
- Network access to starbucks.com.cn domain

### Initial Access Requirements

- No credentials required due to unauthenticated access
- Direct internet access to the target domain and port
- No prior access needed

## Detailed Attack Procedures

### Step 1: Discover the WSDL Service
procedure: [[procedures/Discover-Unauthenticated-WSDL-Service]]

**Objective**: Identify the unauthenticated browsable WSDL service on a non-standard port to expose the API endpoint.

**Instructions**: Scan the starbucks.com.cn domain for open ports and services, focusing on non-standard ports. Use tools like nmap to identify the WSDL service.

**Expected Output**: Discovery of the WSDL endpoint, e.g., http://starbucks.com.cn:nonstandardport/service?wsdl.

**Success Indicators**:
- WSDL file is browsable without authentication
- Service details including functions are visible

### Step 2: Access Unauthenticated Functions
procedure: [[procedures/Access-Test-Data-via-Unauthenticated-Functions]]

**Objective**: Interact with service functions to retrieve test data including user lists and passwords.

**Instructions**: Call the unauthenticated functions in the WSDL service using a web browser or SOAP client to list users, passwords, and personal information.

**Expected Output**: Lists of test users, hashed or plain passwords, and personal details.

**Success Indicators**:
- Data retrieval without authentication prompts
- Exposure of sensitive test information

### Step 3: Exploit Blind SQL Injection
procedure: [[procedures/Exploit-Blind-SQL-Injection]]

**Objective**: Identify and exploit a blind SQL injection vulnerability in the service to access the underlying database.

**Instructions**: Test input parameters in the webservice functions for SQL injection using boolean-based or time-based techniques. Use tools like sqlmap to automate blind SQLi exploitation.

**Expected Output**: Successful database queries revealing schema, tables, or data.

**Success Indicators**:
- Delayed responses or boolean conditions confirming injection
- Database content extraction

### Step 4: Escalate to RCE via xp_cmdshell
procedure: [[procedures/Escalate-to-RCE-via-xp_cmdshell]]

**Objective**: Use the SQL injection to execute OS commands via xp_cmdshell, demonstrating RCE on the production server.

**Instructions**: Through the blind SQLi, inject SQL to enable and call xp_cmdshell with a safe command like ping to verify execution without harm.

Execute [[commands/execute-sql-ping-via-xp_cmdshell]] to test:

```sql
DECLARE @result INT; EXEC @result = xp_cmdshell 'ping -n 1 127.0.0.1'; SELECT @result;
```

**Expected Output**: Ping response or success indicator from the command execution.

**Success Indicators**:
- Command execution confirmed (e.g., ping succeeds)
- No errors in SQL execution, indicating RCE capability

## Attack Chain Summary

### Key Achievements

1. Discovered and accessed unauthenticated WSDL service exposing test data
2. Exploited blind SQLi to gain database access
3. Escalated to critical RCE on production server via xp_cmdshell

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Server Software Component]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
