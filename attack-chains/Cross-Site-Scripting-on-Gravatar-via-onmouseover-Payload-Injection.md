---
tags:
  - xss
  - gravatar
  - javascript
  - onmouseover
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
complexity: low
procedures:
  - '[[procedures/Create-Local-HTML-File-with-XSS-Payload-for-Gravatar]]'
  - '[[procedures/Load-Injected-HTML-in-Firefox-to-Simulate-Gravatar-Page]]'
  - '[[procedures/Trigger-XSS-by-Hovering-over-JSON-XML-Links]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
description: >-
  A multi-step proof-of-concept demonstrating XSS vulnerability in Gravatar by
  injecting malicious JavaScript into HTML elements, leading to arbitrary code
  execution on hover.
skill_level: beginner
impact_level: high
id: b70ee9bd-86ae-43e4-8fc6-98c177efbd41
created_at: '2025-12-14T03:15:35.936Z'
updated_at: '2025-12-14T03:15:35.936Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Cross-Site Scripting on Gravatar via onmouseover Payload Injection

## Overview

This attack chain exploits a Cross-Site Scripting (XSS) vulnerability in the Gravatar service, where insufficient input sanitization allows injection of malicious JavaScript into HTML attributes across various directories and parameters. The proof-of-concept involves creating a local HTML file with an injected payload mimicking a Gravatar page, loading it in a browser, and triggering execution by hovering over affected elements like 'JSON' or 'XML' links. This enables arbitrary JavaScript execution in the victim's browser, potentially leading to theft of cookies, session tokens, or other malicious actions. The vulnerability affects 171 instances, with high severity impact on user sessions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Payload Injection] --> B[Local Simulation] --> C[Trigger Execution]
    C --> D[Arbitrary JS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Firefox or Mozilla browser

### Target Environment

- Web platform
- Gravatar service (simulated locally)
- No specific ports or services required beyond local file access

### Initial Access Requirements

- Local machine with text editor and browser
- Access to Pastebin for payload source
- No network credentials or prior access needed; simulates client-side execution

## Detailed Attack Procedures

### Step 1: Payload Preparation
procedure: [[procedures/Create-Local-HTML-File-with-XSS-Payload-for-Gravatar]]

**Objective**: Inject a malicious onmouseover JavaScript payload into an HTML file that mimics a vulnerable Gravatar page to prepare for local testing.

**Instructions**: Use a text editor to create an HTML file incorporating the payload from the provided source, embedding attributes like 'onmouseover='prompt(916137)'bad="' into elements.

**Expected Output**: A local HTML file ready for browser loading, containing injected script in various directories/parameters simulation.

**Success Indicators**:
- HTML file created without syntax errors
- Payload visible in file inspection

### Step 2: Local Page Simulation
procedure: [[procedures/Load-Injected-HTML-in-Firefox-to-Simulate-Gravatar-Page]]

**Objective**: Render the injected HTML locally in a browser to simulate the vulnerable Gravatar environment without needing remote access.

**Instructions**: Open the created HTML file directly in Firefox or Mozilla browser to load and display the page with embedded malicious content.

**Expected Output**: Browser displays a Gravatar-like page with elements such as JSON/XML links, ready for interaction; no errors in console.

**Success Indicators**:
- Page loads successfully
- Injected elements (e.g., links) are visible and hoverable

### Step 3: Execution Trigger
procedure: [[procedures/Trigger-XSS-by-Hovering-over-JSON-XML-Links]]

**Objective**: Execute the injected JavaScript by interacting with affected elements, demonstrating arbitrary code execution.

**Instructions**: Hover the mouse cursor over links like 'JSON' or 'XML' on the loaded page to fire the onmouseover event.

**Expected Output**: Alert box pops up displaying '916137', confirming script execution in the browser context.

**Success Indicators**:
- Alert triggered on hover
- No browser crashes; script runs in victim context

## Attack Chain Summary

### Key Achievements

1. Successful injection of XSS payload into local HTML simulating Gravatar
2. Rendering of vulnerable page in browser without remote exploitation
3. Demonstration of high-impact JS execution via simple user interaction (hover)

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---
*Last updated: 2023-10-01*
