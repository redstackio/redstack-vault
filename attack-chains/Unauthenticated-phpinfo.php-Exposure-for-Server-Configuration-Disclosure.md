---
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
commands:
  - '[[commands/curl-access-endpoint]]'
platforms:
  - Web
  - Windows
  - PHP
complexity: medium
procedures:
  - '[[procedures/Initial-Web-Reconnaissance]]'
  - '[[procedures/Brute-Force-Directory-Discovery-with-Burp]]'
  - '[[procedures/Access-Exposed-phpinfo-File]]'
step_count: 3
techniques:
  - '[[File and Directory Discovery]]'
  - '[[Client Configurations]]'
description: >-
  Multi-stage reconnaissance chain exploiting an exposed phpinfo.php file to
  disclose sensitive server configuration details without authentication.
skill_level: intermediate
impact_level: high
id: b41d1d8e-8f2e-4771-af04-7ca54b3525e7
created_at: '2025-12-14T17:29:56.726Z'
updated_at: '2025-12-14T17:29:56.726Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
  - '[[Client Configurations]]'
---
# Unauthenticated phpinfo.php Exposure for Server Configuration Disclosure

## Overview

This attack chain demonstrates a reconnaissance workflow targeting a web application with an exposed phpinfo.php file. The vulnerability arises from a debugging file left accessible without authentication, allowing attackers to gather detailed server information such as OS version (Windows Server 2012 R2), PHP configuration, loaded extensions, and environment variables. This disclosure aids in further attack planning, like identifying exploitable extensions or OS-specific weaknesses. The chain involves initial access to the target, brute-forcing directories to locate the file, and direct access to extract information.

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
    A[Initial Access: Visit Target] --> B[Discovery: Brute-Force Directories]
    B --> C[Collection: Access phpinfo.php]
    C --> D[Objective: Information Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite-Intruder]]
- Web browser or [[commands/curl-access-endpoint]]

### Target Environment

- Web platform running PHP on Windows Server
- Exposed web directories without authentication
- Network access to the target domain (e.g., https://h2f54.n1.ips.mtn.co.ug)

### Initial Access Requirements

- No credentials required
- Direct internet access to the target
- No prior access needed

## Detailed Attack Procedures

### Step 1: Initial Web Reconnaissance
procedure: [[procedures/Initial-Web-Reconnaissance]]

**Objective**: Establish initial contact with the target domain to confirm accessibility and begin reconnaissance.

**Instructions**: Open a web browser and navigate to the target domain to verify the main site is live.

**Expected Output**: The target website loads successfully, indicating the server is responsive.

**Success Indicators**:
- Target domain (e.g., https://h2f54.n1.ips.mtn.co.ug) is accessible
- No immediate access restrictions observed

### Step 2: Brute-Force Directory Discovery with Burp
procedure: [[procedures/Brute-Force-Directory-Discovery-with-Burp]]

**Objective**: Identify hidden or sensitive directories, including potential exposure points like info.php or phpinfo.php.

**Instructions**: Configure Burp Suite Intruder to perform a brute-force scan on common directory paths. Use a wordlist of common web directories (e.g., /admin, /dashboard, /info) and send requests through the proxy.

**Expected Output**: Discovery of a responsive directory, such as /dashboard, leading to phpinfo.php.

**Success Indicators**:
- 200 OK responses for hidden paths
- Identification of /dashboard/phpinfo.php or similar

### Step 3: Access Exposed phpinfo.php
procedure: [[procedures/Access-Exposed-phpinfo-File]]

**Objective**: Directly access the exposed phpinfo.php file to extract server configuration details.

**Instructions**: Use a browser or [[commands/curl-access-endpoint]] to visit the full URL of the phpinfo.php file.

```bash
curl -s https://h2f54.n1.ips.mtn.co.ug/dashboard/phpinfo.php | grep -i "windows"
```

**Expected Output**: PHP info page displaying server OS, PHP version, extensions, and environment variables.

**Success Indicators**:
- Page loads without authentication prompt
- Sensitive details like "Windows Server 2012 R2" visible

## Attack Chain Summary

### Key Achievements

1. Confirmed target accessibility without barriers
2. Discovered exposed debugging file via brute-force
3. Disclosed critical server configuration for further exploitation planning

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]] File and Directory Discovery
- [[Client Configurations]] Gather Victim Host Information: Client Configurations

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01*
