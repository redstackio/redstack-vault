---
tags:
  - directory-listing
  - information-disclosure
  - reconnaissance
  - nextcloud
type: attack_chain
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-directory-listing]]'
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Access-Exposed-Directories-via-Listing]]'
step_count: 1
techniques:
  - '[[File and Directory Discovery]]'
description: >-
  A reconnaissance attack chain exploiting enabled directory listing on a
  Nextcloud web server to expose file structures, assets, and server details.
skill_level: beginner
impact_level: medium
id: a858d2b3-d190-4627-8076-ba95ac50cdda
created_at: '2025-12-14T17:26:17.426Z'
updated_at: '2025-12-14T17:26:17.426Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Directory Listing Exposure in Nextcloud Web Server

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access to Web Server] --> B[Directory Enumeration]
    B --> C[Information Extraction]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser or [[commands/curl-directory-listing]]

### Target Environment

- Web platform with Nextcloud deployment
- Exposed HTTP/HTTPS ports (80/443)
- No authentication required for public paths

### Initial Access Requirements

- Public internet access to the target URL
- No credentials needed
- Direct network connectivity to the web server

## Detailed Attack Procedures

### Step 1: Enumerate Exposed Directories
procedure: [[procedures/Access-Exposed-Directories-via-Listing]]

**Objective**: Access common asset directories on the Nextcloud web server to check for enabled directory listing and extract file information.

**Instructions**: Navigate to or request the target directories using a web browser or command-line tool. Start with paths like /assets/, /css/, and /js/, which are typical for web applications.

Use [[commands/curl-directory-listing]] to fetch the /assets/ directory:

```bash
curl -i https://try.nextcloud.com/assets/
```

Repeat for /css/ and /js/:

```bash
curl -i https://try.nextcloud.com/css/
curl -i https://try.nextcloud.com/js/
```

**Expected Output**: HTTP 200 response with HTML content listing files (e.g., <pre> or <ul> tags showing file names) and server headers revealing technology stack, such as Apache version or Nextcloud details.

**Success Indicators**:
- Directory contents displayed instead of 403/404 error
- File names and sizes visible
- Server version or additional metadata in response headers

## Attack Chain Summary

### Key Achievements

1. Successful access to exposed directories without authentication
2. Exposure of non-public asset files and server configuration details
3. Gathered reconnaissance data for potential follow-on attacks, such as identifying vulnerable components

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Discovery]]

---
*Last updated: 2023-10-01*
