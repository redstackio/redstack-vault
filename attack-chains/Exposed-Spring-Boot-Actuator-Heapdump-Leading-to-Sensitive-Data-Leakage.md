---
tags:
  - spring-boot
  - actuator
  - heapdump
  - data-leak
  - misconfiguration
  - credential-access
type: attack_chain
tools:
  - '[[tools/Eclipse-Memory-Analyzer]]'
  - '[[tools/VisualVM]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Java
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Spring-Boot-Actuator-Heapdump-Endpoint]]'
  - '[[procedures/Download-Heap-Dump-File]]'
  - '[[procedures/Analyze-Heap-Dump-with-Memory-Tools]]'
  - '[[procedures/Extract-Sensitive-Information-from-Heap-Dump]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:47.366Z'
description: >-
  Multi-stage attack exploiting misconfigured Spring Boot actuator endpoints to
  download and analyze heap dumps, revealing sensitive customer data,
  credentials, and secrets.
id: 43aec05c-5ebd-4c18-8822-3553a725c007
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Exposed Spring Boot Actuator Heapdump Leading to Sensitive Data Leakage

Multi-stage attack chain demonstrating exploitation of misconfigured Spring Boot applications to access and analyze heap dumps for sensitive information leakage.

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
    A[Access Endpoint] --> B[Download Heapdump]
    B --> C[Analyze Dump]
    C --> D[Extract Secrets]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Eclipse-Memory-Analyzer]]
- [[tools/VisualVM]]
- Web browser or [[commands/curl-download]]

### Target Environment

- Web platform with Spring Boot Java application
- Exposed actuator endpoints (e.g., /actuator/heapdump)
- No authentication on endpoints

### Initial Access Requirements

- Public network access to target domains
- No credentials needed due to misconfiguration
- Knowledge of target URLs (e.g., via reconnaissance)

## Detailed Attack Procedures

### Step 1: Access the Actuator Heapdump Endpoint
procedure: [[procedures/Access-Spring-Boot-Actuator-Heapdump-Endpoint]]

**Objective**: Identify and navigate to the exposed heapdump endpoint to initiate the download process.

**Instructions**: Use a web browser or [[commands/curl-access-endpoint]] to directly access the actuator endpoint on target domains.

```bash
curl -O https://my.stripo.email/cabinet/stripeapi/actuator/heapdump
```

**Expected Output**: The server responds with a downloadable heap dump file, typically a large .hprof binary file.

**Success Indicators**:
- Endpoint returns a 200 OK status without authentication prompt
- File download begins immediately

### Step 2: Download the Heap Dump File
procedure: [[procedures/Download-Heap-Dump-File]]

**Objective**: Retrieve the full memory dump containing in-memory server data.

**Instructions**: If not already downloaded via the access step, use [[commands/curl-download]] to fetch the file explicitly.

```bash
curl -O https://plugins.stripo.email/actuator/heapdump
```

**Expected Output**: A complete heap dump file (e.g., heapdump.hprof) saved locally, often several GB in size.

**Success Indicators**:
- File downloaded successfully without errors
- File size indicates substantial memory content

### Step 3: Open and Analyze the Downloaded Heap Dump File
procedure: [[procedures/Analyze-Heap-Dump-with-Memory-Tools]]

**Objective**: Load the heap dump into analysis tools to inspect its structure and contents.

**Instructions**: Launch [[tools/Eclipse-Memory-Analyzer]] or [[tools/VisualVM]] and import the downloaded file.

For Eclipse MAT:

```bash
# No specific command; use GUI to open file
```

**Expected Output**: Tool displays heap contents, including object graphs, threads, and string data.

**Success Indicators**:
- File loads without corruption errors
- Overview shows classes, instances, and memory usage

### Step 4: Search for and Extract Sensitive Information
procedure: [[procedures/Extract-Sensitive-Information-from-Heap-Dump]]

**Objective**: Query the dump for credentials, secrets, and other exploitable data to enable further attacks.

**Instructions**: Within the analysis tool, use search functions to find strings like passwords, API keys, or JWT tokens.

In Eclipse MAT, use the search bar for terms like "secret" or "password".

**Expected Output**: List of extracted strings, including customer PII, database credentials, and source code snippets.

**Success Indicators**:
- Sensitive data (e.g., JWT secrets, admin passwords) located and exportable
- Potential for account takeover or data exfiltration confirmed

## Attack Chain Summary

### Key Achievements

1. Unauthorized access to server memory via public endpoint
2. Extraction of sensitive credentials and PII from heap dump
3. Enablement of downstream exploits like account takeovers and payment fraud

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
