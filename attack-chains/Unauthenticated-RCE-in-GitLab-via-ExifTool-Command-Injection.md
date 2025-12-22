---
tags:
  - rce
  - gitlab
  - exiftool
  - command-injection
  - vulnerability-exploitation
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Discover-Outdated-GitLab-Server]]'
  - '[[procedures/Exploit-ExifTool-RCE-Vulnerability]]'
step_count: 2
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
description: >-
  An unauthenticated remote code execution attack exploiting a command injection
  vulnerability in an outdated GitLab server's ExifTool integration, allowing
  full server compromise.
skill_level: intermediate
impact_level: high
id: 8622e55d-5fa8-43df-9f97-7aa829110d37
created_at: '2025-12-14T17:23:50.211Z'
updated_at: '2025-12-14T17:23:50.211Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Unauthenticated RCE in GitLab via ExifTool Command Injection

## Overview

This attack chain demonstrates the exploitation of an unauthenticated remote code execution (RCE) vulnerability in an outdated GitLab server hosted at https://169.38.86.185/ (edst.ibm.com). The flaw originates from a command injection vulnerability in the ExifTool component integrated with GitLab. Through reconnaissance, the outdated version is identified, and a public exploit is used to inject commands, leading to full server compromise without authentication. The vulnerability was reported via HackerOne (Report #1379130) and remediated by IBM.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Discover Vulnerable GitLab] --> B[Execution: Exploit ExifTool RCE]
    B --> C[Compromise: Full Server Control]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or reconnaissance tools like [[tools/nmap]] for initial scanning (optional for verification).

### Target Environment

- GitLab server running an outdated version (pre-14.1.2 or similar, vulnerable to ExifTool command injection).
- Exposed web interface on port 80/443.
- No authentication required for exploitation.

### Initial Access Requirements

- Internet access to the target URL (https://169.38.86.185/).
- No credentials or prior access needed.
- Public exploit availability (e.g., from GitHub or Exploit-DB).

## Detailed Attack Procedures

### Step 1: Discover Outdated GitLab Server
procedure: [[procedures/Discover-Outdated-GitLab-Server]]

**Objective**: Identify the GitLab instance and confirm its outdated version susceptible to ExifTool RCE.

**Instructions**: Access the target URL https://169.38.86.185/ in a web browser to observe the GitLab login or dashboard, indicating it's a GitLab instance. Manually inspect the page source or use browser developer tools to check for version indicators (e.g., meta tags or JavaScript comments revealing GitLab version <14.1.2). Alternatively, query public sources like Shodan or check GitLab's powered-by headers via curl to confirm vulnerability.

**Expected Output**: Confirmation of GitLab version and presence of ExifTool integration.

**Success Indicators**:
- GitLab interface visible without authentication.
- Version identified as vulnerable (e.g., via /help or API endpoints).

### Step 2: Exploit ExifTool RCE Vulnerability
procedure: [[procedures/Exploit-ExifTool-RCE-Vulnerability]]

**Objective**: Inject commands via the ExifTool flaw to execute arbitrary code and gain server control.

**Instructions**: Locate the upload or metadata processing endpoint in GitLab (e.g., via file upload features that use ExifTool for image processing). Use a public exploit script (e.g., Python-based from Exploit-DB) to craft a malicious file or payload that triggers command injection. Send the payload to the vulnerable endpoint, such as by uploading a manipulated image with shell metacharacters in EXIF data (e.g., `; id > /tmp/pwned.txt`). Monitor for command execution by attempting to read back output or reverse shell connection.

**Expected Output**: Successful command execution, such as file creation or shell access on the server.

**Success Indicators**:
- Arbitrary command output visible (e.g., `id` command reveals user context).
- Reverse shell established or persistent access gained.

## Attack Chain Summary

### Key Achievements

1. Identified vulnerable GitLab instance without authentication.
2. Exploited ExifTool command injection for RCE.
3. Achieved full server compromise, enabling data exfiltration or persistence.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01*
