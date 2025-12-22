---
tags:
  - xss
  - stored-xss
  - nodejs
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/npm]]'
  - '[[tools/nodejs]]'
  - '[[tools/Firefox-ESR]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Install-http-file-server-Module]]'
  - '[[procedures/Create-Malicious-Filename-for-XSS]]'
  - '[[procedures/Run-http-file-server]]'
  - '[[procedures/Access-Directory-Listing]]'
  - '[[procedures/Trigger-XSS-Payload]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:31.320Z'
description: >-
  Demonstrates exploitation of a stored XSS vulnerability in the
  http-file-server Node.js module by injecting a malicious JavaScript payload
  into a filename, leading to arbitrary code execution in the client's browser
  upon interaction with the directory listing.
skill_level: intermediate
impact_level: high
id: 2f4dd015-dc97-41d1-9087-d63fbe1eab72
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Stored XSS in http-file-server via Malicious Filename Injection

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in the http-file-server Node.js module (version 0.2.6), where unsanitized filenames in directory listings allow injection of JavaScript payloads. The attacker creates a file with a malicious name, serves the directory, and triggers the payload in a victim's browser, potentially leading to session hijacking or data theft.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Install Server] --> B[Create Malicious File]
    B --> C[Run Server]
    C --> D[Access Listing]
    D --> E[Trigger XSS]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/npm]]
- [[tools/nodejs]]
- [[tools/Firefox-ESR]]

### Target Environment

- Linux OS
- Node.js runtime installed
- Port 8080 available

### Initial Access Requirements

- Local access to a Linux machine with npm and Node.js
- No network restrictions for localhost access
- Browser for demonstration

## Detailed Attack Procedures

### Step 1: Install http-file-server Module
procedure: [[procedures/Install-http-file-server-Module]]

**Objective**: Set up the vulnerable http-file-server module for serving directories.

**Instructions**: Install the module globally using [[commands/npm-install-global-http-file-server]] to make the server command available system-wide.

```bash
npm install -g http-file-server
```

**Expected Output**: Installation logs ending with a success message indicating the package is installed.

**Success Indicators**:
- 'http-file-server' command is available in PATH
- No errors during npm installation

### Step 2: Create Malicious Filename for XSS
procedure: [[procedures/Create-Malicious-Filename-for-XSS]]

**Objective**: Inject a stored XSS payload into a filename to exploit the lack of sanitization in directory listings.

**Instructions**: In the target directory (e.g., ~/Desktop/), create an empty file with a name containing the XSS payload, such as '" onmouseover=alert(1) "'. Use touch or any editor to create it.

```bash
touch '~/Desktop/" onmouseover=alert(1) "'
```

**Expected Output**: File created successfully without errors.

**Success Indicators**:
- File exists in the directory with the malicious name
- Filename includes quotes and event handler for injection

### Step 3: Run http-file-server
procedure: [[procedures/Run-http-file-server]]

**Objective**: Start the vulnerable server to expose the directory listing with unsanitized filenames.

**Instructions**: Navigate to the target directory and execute [[commands/http-file-server-run]] or the alternative [[commands/nodejs-run-http-file-server]].

```bash
cd ~/Desktop/
http-file-server
```

Or alternatively:

```bash
nodejs /usr/lib/node_modules/http-file-server/http-file-server.js
```

**Expected Output**: Server startup message, e.g., "Server running at http://localhost:8080".

**Success Indicators**:
- Server listens on port 8080
- No startup errors

### Step 4: Access Directory Listing
procedure: [[procedures/Access-Directory-Listing]]

**Objective**: View the served directory in a browser to load the unsanitized HTML listing.

**Instructions**: Open a browser and navigate to the server's URL. Use [[tools/Firefox-ESR]] for demonstration.

No command needed; manually enter http://localhost:8080/ in the browser address bar.

**Expected Output**: Directory listing page displaying filenames, including the malicious one, without HTML escaping.

**Success Indicators**:
- Page loads showing file list
- Malicious filename appears in the HTML source unescaped

### Step 5: Trigger XSS Payload
procedure: [[procedures/Trigger-XSS-Payload]]

**Objective**: Execute the injected JavaScript by interacting with the malicious filename in the browser.

**Instructions**: In the directory listing, hover the mouse over the malicious filename to trigger the onmouseover event.

No command needed; perform the mouse hover action in the browser.

**Expected Output**: Alert box pops up displaying "1" due to alert(1).

**Success Indicators**:
- JavaScript alert executes
- Arbitrary code runs in the browser context

## Attack Chain Summary

### Key Achievements

1. Successful installation and execution of the vulnerable server
2. Injection of XSS payload via filename, bypassing sanitization
3. Client-side JavaScript execution upon user interaction, demonstrating potential for further attacks like data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]

---
*Last updated: 2023-10-01T00:00:00Z*
