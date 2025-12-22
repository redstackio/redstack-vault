---
tags:
  - rce
  - deserialization
  - django
  - pickle
  - cache
type: attack_chain
tools:
  - '[[tools/sqlite3]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
  - Python
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Django-Project-with-DatabaseCache]]'
  - '[[procedures/Inject-Malicious-Payload-into-Cache]]'
  - '[[procedures/Trigger-Deserialization-for-RCE]]'
step_count: 4
techniques:
  - '[[Python]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:23:24.682Z'
description: >-
  A multi-stage attack exploiting Django's DatabaseCache backend to inject and
  deserialize malicious pickled data, leading to remote code execution on the
  server.
skill_level: intermediate
impact_level: high
id: ba71a8a6-c45b-405a-9bb3-94e11bc074e1
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Python]]'
  - '[[Exploitation for Client Execution]]'
---
# Django Cache Deserialization RCE via Malicious Payload Injection

Multi-stage attack chain demonstrating exploitation of Django's cache backends using Python's pickle module for remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Django Environment] --> B[Inject Malicious Payload]
    B --> C[Trigger Cache Fetch]
    C --> D[RCE Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sqlite3]]

### Target Environment

- Django application using DatabaseCache or RedisCache backend
- SQLite database for cache storage (PoC setup)
- Access to the database file (e.g., db.sqlite3)

### Initial Access Requirements

- Local or remote access to the Django project's database
- Ability to modify cache storage (e.g., via SQL injection or file access)
- Network access to trigger cache fetch via web requests

## Detailed Attack Procedures

### Step 1: Setup Django Environment
procedure: [[procedures/Setup-Django-Project-with-DatabaseCache]]

**Objective**: Prepare a vulnerable Django application with caching enabled to create an exploitable cache entry.

**Instructions**: Create a new Django project, configure DatabaseCache in settings.py, and generate an initial cache entry by accessing a page.

**Expected Output**: A running Django server with a populated cache table containing pickled data.

**Success Indicators**:
- Cache table 'my_cache_table' exists in the database
- Accessing a page creates a new cache entry (verifiable via query)

### Step 2: Inject Malicious Payload into Cache
procedure: [[procedures/Inject-Malicious-Payload-into-Cache]]

**Objective**: Modify an existing cache entry with a base64-encoded pickled payload that executes arbitrary code upon deserialization.

**Instructions**: Use sqlite3 to query the cache table, identify a target row, and update its 'value' field with the malicious payload.

**Expected Output**: Updated cache row with the injected payload (1 row affected).

**Success Indicators**:
- Query shows the modified 'value' column
- No errors during UPDATE execution

### Step 3: Trigger Deserialization for RCE
procedure: [[procedures/Trigger-Deserialization-for-RCE]]

**Objective**: Force the Django application to fetch and deserialize the malicious cache entry, executing the payload.

**Instructions**: Reload the cached page in a browser to trigger FetchFromCacheMiddleware, which loads and unpickles the data.

**Expected Output**: Command execution (e.g., 'whoami' output) in server logs or console.

**Success Indicators**:
- Server-side command runs successfully
- Logs show output from the executed command (e.g., username)

### Step 4: Observe and Verify Execution

**Objective**: Confirm RCE by checking server logs for payload execution.

**Instructions**: Monitor the Django development server console or logs for the results of the deserialized command.

**Expected Output**: Output from os.system('whoami'), such as the current user.

**Success Indicators**:
- Arbitrary code executes on the server
- Potential full compromise if escalated

## Attack Chain Summary

### Key Achievements

1. Successful setup of vulnerable Django caching environment
2. Injection of RCE payload via direct database manipulation
3. Triggering deserialization to achieve remote code execution
4. Demonstration of full server compromise potential

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Python]]
- [[Exploitation for Client Execution]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
