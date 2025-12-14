---
id: ac-uuid-1234
tags:
  - information-disclosure
  - phpinfo
  - reconnaissance
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite-Intruder]]'
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Linux
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Discover-and-Access-Exposed-phpinfo-File]]'
step_count: 3
techniques:
  - '[[Active Scanning]]'
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:09.598Z'
description: >-
  Multi-stage reconnaissance attack discovering and exploiting an exposed
  phpinfo() file on a U.S. Department of Defense web server to disclose
  sensitive configuration details including OS, PHP settings, and environment
  variables.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
  - '[[Gather Victim Host Information]]'
---
# Unauthenticated phpinfo() Exposure Leading to Server Configuration Disclosure on DoD Web Server

Multi-stage attack chain demonstrating reconnaissance via directory enumeration to identify and access an exposed phpinfo() file, revealing sensitive server details on a U.S. Department of Defense web server.

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
    A[Initial Access to Target] --> B[Directory Enumeration]
    B --> C[Access Exposed Endpoint]
    C --> D[Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite-Intruder]]

### Target Environment

- Web platform with PHP on Linux
- No specific ports required beyond standard HTTP/HTTPS (80/443)
- Publicly accessible web server

### Initial Access Requirements

- Network access to the target domain
- No credentials needed
- Browser or proxy tool for interception

## Detailed Attack Procedures

### Step 1: Initial Access to Target
procedure: [[procedures/Discover-and-Access-Exposed-phpinfo-File]]

**Objective**: Establish connection to the target web server to begin reconnaissance.

**Instructions**: Open a web browser and navigate to the target scope URL, such as https://██████████, to confirm accessibility and observe the main page response.

**Expected Output**: The main landing page loads without errors, indicating the server is reachable.

**Success Indicators**:
- Target domain resolves and serves content
- No immediate access restrictions observed

### Step 2: Directory Enumeration
procedure: [[procedures/Discover-and-Access-Exposed-phpinfo-File]]

**Objective**: Use automated fuzzing to identify hidden or sensitive directories and files, specifically uncovering the /info.php endpoint.

**Instructions**: Configure Burp Suite Intruder to perform directory brute-forcing. Intercept a request to the target root, send it to Intruder, and use a wordlist (e.g., common directories like 'info', 'phpinfo') for payload positions in the path. Launch the attack to scan for 200 OK responses.

**Expected Output**: Identification of /info.php as a valid endpoint returning PHP info output.

**Success Indicators**:
- Discovery of /info.php with a successful HTTP response
- No 404 errors for the enumerated path

### Step 3: Access Exposed Endpoint
procedure: [[procedures/Discover-and-Access-Exposed-phpinfo-File]]

**Objective**: Directly access the discovered phpinfo() file to extract sensitive configuration data without authentication.

**Instructions**: In the browser, navigate to https://████████/info.php. The page loads immediately, displaying detailed phpinfo() output including OS kernel (Linux 3.10.0-1160.80.1.el7.x86_64), PHP version, loaded extensions, and environment variables.

**Expected Output**: Comprehensive server information dump, such as PHP configuration directives, module lists, and system paths.

**Success Indicators**:
- Unauthenticated access granted
- Sensitive details like OS version and env vars visible

## Attack Chain Summary

### Key Achievements

1. Successful directory enumeration revealing hidden debugging file
2. Unauthenticated disclosure of server OS, PHP config, and extensions
3. Potential intelligence for further attacks like targeted exploitation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Active Scanning]] Active Scanning
- [[Gather Victim Host Information]] Gather Victim Host Information

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---

*Last updated: 2023-10-01T00:00:00Z*
