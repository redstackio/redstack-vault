---
id: ac-starbucks-wsdl-sqli-rce
tags:
  - sql-injection
  - rce
  - unauthenticated-access
  - wsdl
  - soap
  - mssql
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Windows
  - Microsoft SQL Server
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Browsable-WSDL-Service]]'
  - '[[procedures/Access-Unauthenticated-WSDL-Functions]]'
  - '[[procedures/Exploit-Blind-SQL-Injection]]'
  - '[[procedures/Execute-RCE-via-xp_cmdshell]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Web Shell]]'
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T03:15:10.109Z'
description: >-
  Multi-stage attack exploiting an unauthenticated WSDL service on a Starbucks
  API endpoint to access sensitive data via blind SQL injection, escalating to
  remote code execution on a production Microsoft SQL Server.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Web Shell]]'
  - '[[Windows Command Shell]]'
---
# Unauthenticated WSDL Access Leading to Blind SQL Injection and RCE on Starbucks API

The attacker identifies a browsable WSDL service on a non-standard port under the starbucks.com.cn domain, enabling unauthenticated access to API functions that expose user lists, passwords, and personal information from a test database. This access reveals a blind SQL injection vulnerability, allowing database enumeration and escalation to command execution using the xp_cmdshell extended stored procedure on the Microsoft SQL Server backend. The attack culminates in remote code execution on a production server, demonstrated harmlessly with a ping command, highlighting a critical security flaw despite the test data context.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Discover WSDL Service] --> B[Access Sensitive Data]
    B --> C[Exploit SQL Injection]
    C --> D[Execute RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or SOAP client for WSDL access
- SQL injection tool (e.g., sqlmap) for exploitation

### Target Environment

- Web platform with SOAP/WSDL API on non-standard port
- Microsoft SQL Server backend
- Network access to starbucks.com.cn domain

### Initial Access Requirements

- Public internet access to the API endpoint
- No credentials required due to unauthenticated service

## Detailed Attack Procedures

### Step 1: Discover Browsable WSDL Service
procedure: [[procedures/Discover-Browsable-WSDL-Service]]

**Objective**: Identify the exposed WSDL service on the target domain to map the API attack surface.

**Instructions**: Navigate to the suspected API endpoint on the non-standard port using a web browser to locate the WSDL file, which describes available SOAP functions.

**Expected Output**: WSDL XML document listing service operations, confirming browsable access.

**Success Indicators**:
- WSDL file accessible without authentication
- Service functions visible in the XML

### Step 2: Access Unauthenticated WSDL Functions
procedure: [[procedures/Access-Unauthenticated-WSDL-Functions]]

**Objective**: Invoke API functions to extract sensitive data from the test database without authentication.

**Instructions**: Use a SOAP client or browser to call functions exposed in the WSDL, such as those for listing users and passwords, targeting the unauthenticated endpoint.

**Expected Output**: Lists of users, hashed passwords, and personal information from the test database.

**Success Indicators**:
- Data retrieval without login prompts
- Exposure of PII from test environment

### Step 3: Exploit Blind SQL Injection
procedure: [[procedures/Exploit-Blind-SQL-Injection]]

**Objective**: Leverage input vulnerabilities in the SOAP service to inject SQL payloads and enumerate the database.

**Instructions**: Identify injectable parameters in SOAP requests (e.g., user IDs or search fields) and craft blind SQLi payloads to extract database schema, users, and data via conditional responses.

**Expected Output**: Database contents inferred from true/false responses, including schema details and user data.

**Success Indicators**:
- Boolean-based responses confirming injection success
- Database enumeration without direct output

### Step 4: Execute RCE via xp_cmdshell
procedure: [[procedures/Execute-RCE-via-xp_cmdshell]]

**Objective**: Escalate SQL injection to command execution on the server using xp_cmdshell.

**Instructions**: Through the blind SQLi, enable xp_cmdshell if needed and invoke it with a command like ping to demonstrate RCE, monitoring network traffic for confirmation.

**Expected Output**: Network ping response from the production server IP.

**Success Indicators**:
- Ping reply received, proving command execution
- No errors in SQL invocation

## Attack Chain Summary

### Key Achievements

1. Discovered and accessed unauthenticated WSDL service exposing test data
2. Exploited blind SQLi to access underlying database
3. Achieved RCE on production server via xp_cmdshell

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Web Shell]]
- [[Windows Command Shell]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
