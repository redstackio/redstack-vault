---
id: ac-php-session-dos-001
tags:
  - php
  - dos
  - null-pointer-dereference
  - session-upload-progress
  - vulnerability
type: attack_chain
tools:
  - '[[tools/PHP-Built-in-Web-Server]]'
  - '[[tools/fsockopen]]'
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Setup-Vulnerable-PHP-Server]]'
  - '[[procedures/Prepare-Malformed-Multipart-Request-PoC]]'
  - '[[procedures/Trigger-PHP-Crash-with-PoC]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T05:32:09.961Z'
description: >-
  A multi-stage attack chain exploiting a null pointer dereference in PHP's
  session upload progress handling to cause a remote denial-of-service by
  crashing the PHP process.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
---
# Remote DoS via Null Pointer Dereference in PHP Session Upload Progress

Multi-stage attack chain demonstrating a complete denial-of-service workflow against vulnerable PHP versions (5.4 through 7) by exploiting improper handling of session upload progress data.

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
    A[Setup Vulnerable Server] --> B[Prepare PoC Request]
    B --> C[Trigger Crash]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PHP-Built-in-Web-Server]]
- [[tools/fsockopen]]

### Target Environment

- PHP versions 5.4 through 7
- Web platform with session.upload_progress enabled
- Linux OS for testing
- Port 8000 open

### Initial Access Requirements

- Local or remote access to start a PHP server
- No credentials required
- Network access to the target PHP endpoint

## Detailed Attack Procedures

### Step 1: Setup Vulnerable PHP Server
procedure: [[procedures/Setup-Vulnerable-PHP-Server]]

**Objective**: Configure and start a PHP built-in web server with the vulnerable session.upload_progress.cleanup disabled to mimic a production-like environment prone to the null pointer dereference.

**Instructions**: Create a web directory and start the server using [[commands/php-start-builtin-server]]:

```bash
php -S localhost:8000 -t /www/web/ -d session.upload_progress.cleanup=0
```

Ensure an index.php file exists in /www/web/ to handle requests.

**Expected Output**: Server startup message indicating the development server is listening on http://localhost:8000.

**Success Indicators**:
- Server logs show successful bind to port 8000
- No errors in PHP configuration

### Step 2: Prepare Malformed Multipart Request PoC
procedure: [[procedures/Prepare-Malformed-Multipart-Request-PoC]]

**Objective**: Craft a PHP script that generates a malformed POST request lacking file start events to leave upload progress data uninitialized.

**Instructions**: Write the poc.php script using fsockopen to construct the HTTP POST with multipart/form-data, including PHP_SESSION_UPLOAD_PROGRESS but no file data. Use boundary ---------------------------2020 for the multipart sections.

**Expected Output**: A valid poc.php file ready for execution.

**Success Indicators**:
- Script file created without syntax errors
- Request structure matches the vulnerability trigger (no MULTIPART_EVENT_FILE_START)

### Step 3: Trigger PHP Crash with PoC
procedure: [[procedures/Trigger-PHP-Crash-with-PoC]]

**Objective**: Send the crafted request to the vulnerable server, causing a null pointer dereference in session.c and crashing the PHP process for DoS.

**Instructions**: Execute the PoC script using [[commands/php-execute-poc]]:

```bash
php poc.php
```

The script connects via fsockopen to localhost:8000 and sends the POST request.

**Expected Output**: Partial or error response dumped from the server, followed by a segmentation fault in server logs indicating PHP process crash.

**Success Indicators**:
- Server process terminates remotely
- Logs show null pointer dereference in php_session_rfc1867_callback

## Attack Chain Summary

### Key Achievements

1. Successfully configured a vulnerable PHP environment without custom code.
2. Crafted a request exploiting uninitialized progress->data leading to SEPARATE_ARRAY null dereference.
3. Achieved remote DoS crashing PHP-FPM or CLI processes.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Privilege Escalation]]

---
*Last updated: 2023-10-01T00:00:00Z*
