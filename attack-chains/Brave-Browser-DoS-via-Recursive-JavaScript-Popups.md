---
id: ac-brave-dos-recursive-popups
tags:
  - dos
  - browser
  - javascript
  - brave
  - popup
  - resource-consumption
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Windows
  - Web
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Malicious-HTML-for-Brave-DoS]]'
  - '[[procedures/Trigger-Recursive-Popups-in-Brave]]'
  - '[[procedures/Observe-and-Recover-from-Browser-Freeze]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.447Z'
description: >-
  A multi-stage attack chain exploiting a denial of service vulnerability in
  Brave browser through recursive JavaScript popups triggered by
  location.reload(), leading to uncontrolled resource consumption and browser
  freeze.
skill_level: beginner
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Endpoint Denial of Service]]'
---
# Brave Browser DoS via Recursive JavaScript Popups

Multi-stage attack chain demonstrating a complete denial of service workflow against Brave browser using malicious HTML with recursive JavaScript popups.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~1 minute |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Malicious Content] --> B[Trigger Recursive Popups]
    B --> C[Browser Freeze and Recovery]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in browser functionality)

### Target Environment

- Brave Browser version 0.11.6 or similar Chromium-based versions
- Platforms: Linux, Windows
- Web access to host the malicious HTML

### Initial Access Requirements

- User must open the malicious HTML in Brave browser
- No credentials or prior access needed; social engineering to trick user into visiting the page

## Detailed Attack Procedures

### Step 1: Access the Malicious HTML Content
procedure: [[procedures/Access-Malicious-HTML-for-Brave-DoS]]

**Objective**: Deliver and load the malicious HTML file containing the recursive popup JavaScript into the Brave browser.

**Instructions**: Host or provide the malicious HTML file (e.g., 'pop up dos.html') on a web server or as a local file. Direct the target to visit the URL or open the file in Brave browser.

**Expected Output**: The HTML page loads in Brave, initiating the JavaScript execution.

**Success Indicators**:
- Page loads without errors
- JavaScript begins executing (visible via developer tools if inspected)

### Step 2: Trigger Recursive Popups
procedure: [[procedures/Trigger-Recursive-Popups-in-Brave]]

**Objective**: Execute the JavaScript code that creates endless popup dialogs using location.reload(), overwhelming browser resources.

**Instructions**: Upon loading the HTML, the embedded JavaScript automatically runs, calling location.reload() in a loop to generate recursive popups. No manual input required beyond opening the page.

**Expected Output**: Continuous popup dialogs appear, each reloading the document and spawning more popups.

**Success Indicators**:
- Multiple popup windows or dialogs open rapidly
- Browser responsiveness begins to degrade

### Step 3: Observe Browser Freeze and Recovery
procedure: [[procedures/Observe-and-Recover-from-Browser-Freeze]]

**Objective**: Confirm the DoS impact by observing the browser hang and recover by terminating the process.

**Instructions**: Monitor the browser as popups consume resources, leading to a freeze. To recover, identify the Brave process ID (PID) using task manager (Windows) or `ps aux | grep brave` (Linux), then execute [[commands/kill-browser-process]] to terminate it.

```bash
ps aux | grep brave
kill -9 <PID>
```

**Expected Output**: Browser window freezes (only minimize button works); process termination confirms recovery with no output on success.

**Success Indicators**:
- Browser interface hangs, tabs cannot close with Ctrl+W
- Process kill restores system control

## Attack Chain Summary

### Key Achievements

1. Successful delivery of malicious HTML via web access or file open
2. Triggering of uncontrolled popup recursion leading to resource exhaustion
3. Demonstration of high-impact DoS requiring manual process termination

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Endpoint Denial of Service]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Impact]]

---
*Last updated: 2023-10-01T00:00:00Z*
