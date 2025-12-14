---
id: ac-brave-ios-blob-url-spoofing
name: URL Spoofing via history.replaceState with Blob URL in iOS Brave Browser
tags:
  - url-spoofing
  - browser-vulnerability
  - blob-url
  - history-api
  - same-origin-policy
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - iOS
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-HTML-for-Blob-URL-Replacement]]'
  - '[[procedures/Host-HTML-on-Local-Server]]'
  - '[[procedures/Visit-Page-in-iOS-Brave-to-Trigger-Spoofing]]'
step_count: 3
techniques:
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T17:24:39.951Z'
description: >-
  Demonstrates a vulnerability in iOS Brave browser allowing
  history.replaceState to replace the displayed URL with a blob URL, potentially
  enabling UI spoofing and user confusion about the page origin.
skill_level: beginner
impact_level: low
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
---
# URL Spoofing via history.replaceState with Blob URL in iOS Brave Browser

Multi-stage attack chain demonstrating a browser vulnerability in iOS Brave version 1.3.1 that allows manipulation of the address bar URL using history.replaceState with a blob URL, violating same-origin policy expectations and enabling potential UI spoofing.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Low |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Malicious HTML] --> B[Host Locally]
    B --> C[Load in iOS Brave]
    C --> D[URL Spoofed to Blob]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Local web server (e.g., Python's http.server)

### Target Environment

- iOS device with Brave browser version 1.3.1 (or vulnerable version)
- Local network access for hosting

### Initial Access Requirements

- Physical access to iOS device or remote control
- No credentials required; targets browser directly

## Detailed Attack Procedures

### Step 1: Create Malicious HTML
procedure: [[procedures/Create-HTML-for-Blob-URL-Replacement]]

**Objective**: Generate an HTML file with JavaScript that uses history.replaceState to swap the URL to a blob format upon loading.

**Instructions**: Create a file named `blob.html` containing the script that executes on page load to replace the state with a blob URL.

**Expected Output**: An HTML file ready for hosting.

**Success Indicators**:
- HTML file created with the specified script
- Script syntax verified (no errors in code editor)

### Step 2: Host HTML on Local Server
procedure: [[procedures/Host-HTML-on-Local-Server]]

**Objective**: Serve the HTML file locally to make it accessible via HTTP for browser loading.

**Instructions**: Use a simple local server to host the file at an IP like http://192.168.1.111/blob.html. For example, navigate to the directory and run a Python HTTP server.

**Expected Output**: Server running and file accessible at the local URL.

**Success Indicators**:
- Server logs show listening on port 80 or 8000
- File loads correctly when accessed from another browser

### Step 3: Visit Page in iOS Brave to Trigger Spoofing
procedure: [[procedures/Visit-Page-in-iOS-Brave-to-Trigger-Spoofing]]

**Objective**: Load the hosted page in the vulnerable iOS Brave browser to trigger the URL replacement and observe the spoofing.

**Instructions**: Open iOS Brave version 1.3.1 and navigate to the hosted URL (e.g., http://192.168.1.111/blob.html). The script should execute automatically, changing the address bar to a blob URL like blob:http://192.168.1.111/xxxx.

**Expected Output**: Address bar displays the blob URL instead of the original HTTP URL.

**Success Indicators**:
- Blob URL appears in the address bar
- No errors in browser console; page loads without crashing

## Attack Chain Summary

### Key Achievements

1. Successful creation of a proof-of-concept HTML exploiting history.replaceState.
2. Local hosting without issues, simulating a malicious site.
3. Demonstration of URL spoofing in iOS Brave, highlighting same-origin policy bypass.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution

### MITRE ATT&CK Tactics

- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
