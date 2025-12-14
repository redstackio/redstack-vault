---
id: uuid-1234-5678-9abc-def0
tags:
  - command-injection
  - rce
  - directory-listing
  - php
  - web-vulnerability
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-Enabled-Directory-Listing-on-Target]]'
  - '[[procedures/Explore-Leaked-Directories-to-Identify-Endpoints]]'
  - '[[procedures/Fuzz-Endpoint-for-Command-Injection-Vulnerability]]'
step_count: 3
techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:54.709Z'
description: >-
  A multi-stage reconnaissance and exploitation chain targeting a PHP-based
  password hashing tool, resulting in remote code execution via command
  injection.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Unix Shell]]'
---
# Command Injection in NTPasswd PHP Endpoint Leading to Remote Code Execution

Multi-stage attack chain demonstrating reconnaissance, endpoint discovery, and exploitation of a command injection vulnerability in a PHP-based password hashing tool on a corporate web server.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Directory Listing Discovery] --> B[Discovery: Explore Leaked Files] --> C[Exploitation: Fuzz for Command Injection]
    C --> D[RCE Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Firefox or Chrome)
- Fuzzing tool like Burp Suite or manual input via curl

### Target Environment

- Web platform with PHP backend
- Exposed web server (e.g., http://tw.corp.ubnt.com/)
- No authentication required for initial access

### Initial Access Requirements

- Direct network access to the target host
- No credentials needed
- Public-facing web application

## Detailed Attack Procedures

### Step 1: Discover Enabled Directory Listing
procedure: [[procedures/Discover-Enabled-Directory-Listing-on-Target]]

**Objective**: Identify if the target web server has directory listing enabled, exposing sensitive files and directories.

**Instructions**: Navigate to the root of the target host using a web browser. Observe the directory listing contents for any exposed files or subdirectories.

**Expected Output**: A web page displaying a list of files and directories, such as /tools/, /admin/, or configuration files.

**Success Indicators**:
- Directory listing page loads without a default index file
- Sensitive directories like /tools/ are visible

### Step 2: Explore Leaked Directories to Identify Endpoints
procedure: [[procedures/Explore-Leaked-Directories-to-Identify-Endpoints]]

**Objective**: Examine exposed directories to locate vulnerable endpoints, specifically those handling user input like password processing.

**Instructions**: Click into exposed directories from the listing, such as /tools/, and review file names and descriptions. Look for PHP scripts related to system utilities, like ntpasswd.php for password hashing.

**Expected Output**: Identification of /tools/ntpasswd.php, described as a tool to convert clear text passwords into NT and LM hashes.

**Success Indicators**:
- Endpoint /tools/ntpasswd.php found with input fields for passwords
- Confirmation of functionality via GET/POST parameters

### Step 3: Fuzz Endpoint for Command Injection Vulnerability
procedure: [[procedures/Fuzz-Endpoint-for-Command-Injection-Vulnerability]]

**Objective**: Test the identified endpoint for command injection by fuzzing input fields to inject and execute arbitrary commands.

**Instructions**: Use a browser or curl to send payloads to the password input parameter in /tools/ntpasswd.php. Start with simple tests like appending `; id` to the password value and observe for command output in responses.

For example, using curl:

```bash
curl "http://tw.corp.ubnt.com/tools/ntpasswd.php?password=pass;id"
```

Escalate to more complex payloads if initial tests succeed, confirming RCE.

**Expected Output**: Server response includes output from injected commands, such as user ID or system information, indicating successful injection.

**Success Indicators**:
- Unexpected command output in HTTP response
- Arbitrary command execution confirmed (e.g., file read or shell access)

## Attack Chain Summary

### Key Achievements

1. Exposed directory listing revealing internal tools
2. Discovery of vulnerable PHP endpoint for password hashing
3. Exploitation of command injection for remote code execution

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Unix Shell]] Unix Shell

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
