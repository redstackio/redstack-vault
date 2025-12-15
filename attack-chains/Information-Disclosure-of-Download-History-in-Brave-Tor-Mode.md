---
id: ac-brave-tor-disclosure-001
tags:
  - brave
  - tor
  - browser
  - information-disclosure
  - privacy-leak
type: attack_chain
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web Browser
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Launch-Brave-Tor-Mode]]'
  - '[[procedures/Navigate-Privileged-URIs-Tor]]'
  - '[[procedures/Download-File-Normal-Mode]]'
  - '[[procedures/View-Leaked-Downloads-Tor]]'
  - '[[procedures/Test-Brave-URI-Navigation-Tor]]'
step_count: 5
techniques:
  - '[[Data from Local System]]'
  - '[[Data from Information Repositories]]'
updated_at: '2025-12-14T17:24:56.309Z'
description: >-
  Demonstrates inconsistent privacy protections in Brave's Tor mode, allowing
  access to privileged chrome:// URIs that leak download history from normal
  browsing sessions into the Tor context.
skill_level: beginner
impact_level: medium
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
  - '[[Data from Information Repositories]]'
---
# Information Disclosure of Download History in Brave Tor Mode

Multi-stage demonstration of a privacy vulnerability in Brave browser's Tor mode, where certain privileged chrome:// and brave:// URIs remain accessible, leading to the unintended disclosure of download history from normal browsing sessions.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Launch Tor Mode] --> B[Navigate Privileged URIs]
    B --> C[Download in Normal Mode]
    C --> D[Access Downloads in Tor]
    D --> E[Test URI Navigation]
    E --> F[Data Disclosure]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Brave Browser (version 1.29.81 or similar)

### Target Environment

- Web Browser platform
- Brave with Tor integration
- No specific services or ports required; local browser instance

### Initial Access Requirements

- Local access to Brave browser
- No network credentials needed; operates within browser sessions
- Prior installation of Brave required

## Detailed Attack Procedures

### Step 1: Launch Brave in Tor Mode
procedure: [[procedures/Launch-Brave-Tor-Mode]]

**Objective**: Initiate a private Tor browsing session to establish the privacy context.

**Instructions**: Open Brave browser and enable Tor mode to create an isolated window.

**Expected Output**: A new Tor-enabled private window opens, routing traffic through Tor.

**Success Indicators**:
- Tor window active with onion routing indicator
- Normal browsing history isolated

### Step 2: Navigate to Privileged URIs in Tor Mode
procedure: [[procedures/Navigate-Privileged-URIs-Tor]]

**Objective**: Test accessibility of chrome:// and brave:// URIs within the Tor session to identify inconsistencies.

**Instructions**: In the Tor window, enter URIs like `chrome://downloads`, `brave://inspect/#devices`, or `brave://device-log/` in the address bar.

**Expected Output**: Some URIs load directly (e.g., chrome://downloads), while others (e.g., chrome://history) redirect to a normal window.

**Success Indicators**:
- chrome://downloads accessible without redirect
- Confirmation of inconsistent blocking

### Step 3: Download a File in Normal Mode
procedure: [[procedures/Download-File-Normal-Mode]]

**Objective**: Create download history in a standard Brave session to prepare for leakage testing.

**Instructions**: Switch to a normal (non-Tor) Brave window, navigate to a test URL such as `https://docs.oracle.com/javase/tutorialJWS/samples/deployment/dynamictree_webstartJWSProject/dynamictree_webstart.jnlp`, and initiate a download, saving the file locally.

**Expected Output**: File downloads successfully, appearing in the browser's download manager.

**Success Indicators**:
- Download entry visible in normal session's chrome://downloads
- File saved to local path with source URL recorded

### Step 4: View Leaked Downloads in Tor Mode
procedure: [[procedures/View-Leaked-Downloads-Tor]]

**Objective**: Access the global download history from within the Tor session to demonstrate disclosure.

**Instructions**: Return to the Tor window and navigate to `chrome://downloads`.

**Expected Output**: The page displays download entries from the normal session, including file names (e.g., dynamictree_webstart.jnlp) and source URLs.

**Success Indicators**:
- Normal session downloads visible in Tor context
- Potential confusion or unintended data visibility confirmed

### Step 5: Test Brave URI Navigation in Tor Mode
procedure: [[procedures/Test-Brave-URI-Navigation-Tor]]

**Objective**: Verify navigation to brave:// URIs via drag-and-drop or paste to exploit potential protocol handling flaws.

**Instructions**: In the Tor window, drag or paste a brave:// URI (e.g., brave://inspect/#devices) from another context into the address bar.

**Expected Output**: The URI loads successfully within the Tor session, bypassing expected privacy redirects.

**Success Indicators**:
- URI navigation succeeds without redirect to normal browser
- Additional privileged data potentially accessible

## Attack Chain Summary

### Key Achievements

1. Successful launch of Tor mode for privacy isolation
2. Identification of accessible privileged URIs in Tor context
3. Disclosure of normal session download history (file names and URLs) in Tor
4. Confirmation of inconsistent privacy protections via URI navigation tests
5. Demonstration of potential user confusion in privacy-focused sessions

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Data from Local System]] Data from Local System
- [[Data from Information Repositories]] Data from Information Repositories

### MITRE ATT&CK Tactics

- [[Collection]] Collection

---
*Last updated: 2023-10-01T00:00:00Z*
