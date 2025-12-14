---
tags:
  - dos
  - brave-browser
  - javascript
  - client-side
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Web Browser
submitted: true
complexity: low
created_at: '2024-01-01T00:00:00Z'
procedures:
  - '[[procedures/Brave-Browser-window.close-DoS-Exploitation]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.791Z'
description: >-
  A client-side denial of service attack exploiting Brave browser's improper
  handling of window.close() from dynamically generated events, leading to
  unexpected window closure.
skill_level: novice
impact_level: medium
id: 30c3376c-e85a-415c-bd35-e49d9ce7162a
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[Endpoint Denial of Service]]'
---
# Brave Browser Denial of Service via Malicious window.close() JavaScript

Multi-stage attack chain demonstrating a complete client-side denial of service workflow targeting the Brave browser on Linux.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Novice |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious HTML] --> B[Load in Brave Browser]
    B --> C[Trigger window.close()]
    C --> D[DoS Achieved]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in browser capabilities)

### Target Environment

- Brave browser (latest version) on Linux
- Local file system access to create and open HTML files
- No network access required

### Initial Access Requirements

- Physical or remote access to a Linux machine with Brave installed
- User-level permissions to run the browser
- No prior credentials or network position needed

## Detailed Attack Procedures

### Step 1: Create Malicious HTML File
procedure: [[procedures/Brave-Browser-window.close-DoS-Exploitation]]

**Objective**: Generate an HTML file containing a malicious link that invokes window.close(self) without validation.

**Instructions**: Create the POC HTML file using a text editor or command line. The file includes a link with `href="javascript:window.close(self);"`.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Brave Window Object DoS Test POC</title>
</head>
<body>
    <p>Click the link below to test the vulnerability:</p>
    <a href="javascript:window.close(self);">Brave Window Object DoS Test POC</a>
</body>
</html>
```

Save this as `poc.html`.

**Expected Output**: A valid HTML file ready for loading in the browser.

**Success Indicators**:
- HTML file created without errors
- File contains the malicious JavaScript link

### Step 2: Load HTML File in Brave Browser
procedure: [[procedures/Brave-Browser-window.close-DoS-Exploitation]]

**Objective**: Open the malicious HTML in the vulnerable Brave browser on Linux to prepare for exploitation.

**Instructions**: Launch Brave and navigate to the local file. Use the file URI or drag-and-drop the file into the browser.

For command-line opening (optional):

```bash
brave-browser file:///path/to/poc.html
```

The page will display with the clickable link labeled "Brave Window Object DoS Test POC".

**Expected Output**: Browser window loads the HTML page showing the test link.

**Success Indicators**:
- Page loads without errors
- Malicious link is visible and clickable
- No immediate closure occurs

### Step 3: Trigger the Vulnerability
procedure: [[procedures/Brave-Browser-window.close-DoS-Exploitation]]

**Objective**: Execute the JavaScript to close the browser window, causing denial of service.

**Instructions**: Click the provided link on the loaded page. This invokes `window.close(self)`, which Brave fails to validate, closing the current window unexpectedly.

**Expected Output**: The browser window closes immediately upon click, disrupting the user's session.

**Success Indicators**:
- Window closes without user confirmation
- Browsing session is interrupted (DoS achieved)
- Behavior does not replicate in Firefox or Chrome

## Attack Chain Summary

### Key Achievements

1. Successful creation of a portable malicious HTML POC
2. Exploitation of Brave's design flaw in window.close() handling
3. Demonstration of client-side DoS without requiring network or elevated privileges

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[Endpoint Denial of Service]] Endpoint Denial of Service

### MITRE ATT&CK Tactics

- [[Execution]] Execution
- [[Impact]] Impact

---
*Last updated: 2024-01-01T00:00:00Z*
