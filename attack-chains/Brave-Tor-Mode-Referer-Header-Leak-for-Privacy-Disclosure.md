---
tags:
  - information-disclosure
  - privacy-leak
  - browser
  - tor
  - referer
type: attack_chain
tools:
  - '[[tools/Brave-Browser]]'
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Browser
submitted: true
complexity: low
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Demonstrate-Brave-Tor-Referer-Leak]]'
step_count: 4
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:25:13.411Z'
description: >-
  Demonstrates an information disclosure vulnerability in Brave browser's Tor
  private window where the Referer header leaks the originating domain,
  compromising user privacy especially for .onion sites.
skill_level: beginner
impact_level: high
id: 16964755-a002-40d2-aed9-4de0becd0cdd
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Brave Tor Mode Referer Header Leak for Privacy Disclosure

Multi-stage demonstration of an information disclosure vulnerability in Brave browser's 'New Private Window with Tor' feature, where the Referer header is not properly stripped during navigation, leading to leaks of originating domains including sensitive .onion URLs in the Tor network. This can deanonymize users by revealing browsing history to external sites.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~2 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Launch Tor Private Window] --> B[Navigate to Controlled Page]
    B --> C[Trigger Cross-Origin Navigation]
    C --> D[Observe Leaked Referer]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Brave-Browser]]

### Target Environment

- Brave browser version 1.29.79 or similar with Tor integration
- Windows 10 or compatible OS
- Internet access for navigation

### Initial Access Requirements

- Local machine with Brave installed
- No special credentials needed
- Access to test sites like https://kirtikumarar.com and https://www.whatismybrowser.com

## Detailed Attack Procedures

### Step 1: Launch Tor Private Window
procedure: [[procedures/Demonstrate-Brave-Tor-Referer-Leak]]

**Objective**: Initialize the browser in Tor mode to route all traffic anonymously.

**Instructions**: Open Brave browser and select 'New Private Window with Tor' to ensure Tor connectivity is active. Verify Tor status in the browser interface.

**Expected Output**: Browser window opens with Tor onion icon and confirms connection to Tor network.

**Success Indicators**:
- Tor mode activated
- No direct IP leaks visible

### Step 2: Navigate to Controlled Exploit Page
procedure: [[procedures/Demonstrate-Brave-Tor-Referer-Leak]]

**Objective**: Load a page under attacker control to set up the referer source.

**Instructions**: In the Tor private window, navigate to https://kirtikumarar.com/referrer/top-page.html. This page contains a link that will trigger the navigation.

**Expected Output**: Page loads successfully, displaying a link to an external site.

**Success Indicators**:
- Page accessible via Tor
- Link to external site visible

### Step 3: Trigger Cross-Origin Navigation
procedure: [[procedures/Demonstrate-Brave-Tor-Referer-Leak]]

**Objective**: Initiate navigation to an external site to send the Referer header.

**Instructions**: Click on the link to https://www.whatismybrowser.com/ from the top-page.html. This action performs a cross-origin request.

**Expected Output**: External site loads, and upon inspection, the Referer header is populated.

**Success Indicators**:
- Navigation completes without errors
- External site reachable via Tor

### Step 4: Observe Leaked Referer Header
procedure: [[procedures/Demonstrate-Brave-Tor-Referer-Leak]]

**Objective**: Verify the information disclosure by checking the Referer value on the target site.

**Instructions**: On whatismybrowser.com, inspect the displayed headers or use browser dev tools to confirm the Referer shows 'https://kirtikumarar.com' instead of being blank or empty.

**Expected Output**: Referer header reveals the originating domain 'kirtikumarar.com'.

**Success Indicators**:
- Referer not blanked
- Source domain leaked, demonstrating privacy breach

## Attack Chain Summary

### Key Achievements

1. Successful reproduction of Referer leak in Tor mode
2. Confirmation of privacy impact for .onion sites
3. Highlight of browser's failure to enforce no-referrer policy

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Hardware]]

### MITRE ATT&CK Tactics

- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
