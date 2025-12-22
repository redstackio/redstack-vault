---
tags:
  - dos
  - mattermost
  - logging
  - resource-exhaustion
  - web
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/make-run-server]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Setup-Mattermost-Test-Environment]]'
  - '[[procedures/Trigger-DoS-via-Large-Slash-Command-Payload]]'
  - '[[procedures/Trigger-DoS-via-Large-Authentication-Cookie]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
description: >-
  A multi-vector denial-of-service attack exploiting uncontrolled logging of
  large inputs in Mattermost, causing server hangs at DEBUG, INFO, or WARN log
  levels.
skill_level: intermediate
impact_level: high
id: 18ab0cdd-6088-414d-a787-0a3bc7472e78
created_at: '2025-12-14T17:26:48.161Z'
updated_at: '2025-12-14T17:26:48.161Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
---
# Mattermost DoS via Oversized Payloads in Slash Commands and Cookies

## Overview

This attack chain exploits a vulnerability in Mattermost where large inputs exceeding 64KB in slash commands or authentication cookies are logged to the console without size limits, causing the server to hang during logging operations. The attack affects all users and teams, requiring a server restart to recover. It was discovered by setting up a development environment, intercepting API requests with Burp Suite, and injecting oversized payloads. Vectors include authenticated slash commands at DEBUG level and unauthenticated cookie manipulation at INFO or WARN levels, leading to complete denial of service.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Setup Environment] --> B[Trigger Slash Command DoS]
    B --> C[Trigger Cookie DoS]
    C --> D[Server Hang and Recovery]

    style A fill:#3498db
    style B fill:#f39c12
    style C fill:#e74c3c
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Mattermost server (development or production)
- Enabled console logging
- Access to a web browser and proxy tool
- Network access to the Mattermost instance

### Initial Access Requirements

- Administrative access for setup (development environment)
- User authentication for slash command vector
- No authentication required for cookie vector on GET requests

## Detailed Attack Procedures

### Step 1: Environment Setup

procedure: [[procedures/Setup-Mattermost-Test-Environment]]

**Objective**: Prepare a testable Mattermost instance with console logging enabled to facilitate payload injection and observation of DoS effects.

**Instructions**: Follow the developer setup guide to install Mattermost on Windows WSL, create a test server and team, and enable DEBUG-level console logging in server settings.

**Expected Output**: A running Mattermost server with console output visible, ready for API interception.

**Success Indicators**:
- Server starts successfully without errors
- Console logs appear at DEBUG level
- Test team and channel accessible

### Step 2: Slash Command Payload Exploitation

procedure: [[procedures/Trigger-DoS-via-Large-Slash-Command-Payload]]

**Objective**: Intercept a slash command request, inflate the payload beyond 64KB, and send it to trigger logging-induced server hang.

**Instructions**: Configure Burp Suite as a proxy, execute a non-existent slash command in a channel to capture the POST request to /api/v4/commands/execute, forward it to Repeater, replace the 'command' field with a string exceeding 66,000 characters (e.g., repeated '0's), and replay the request.

**Expected Output**: Server processes the request but hangs during logging, becoming unresponsive to all subsequent requests.

**Success Indicators**:
- Modified request sent successfully
- Server logs show the large payload before hanging
- All users experience service denial

### Step 3: Cookie-Based DoS Exploitation and Recovery

procedure: [[procedures/Trigger-DoS-via-Large-Authentication-Cookie]]

**Objective**: Exploit cookie logging vectors at lower log levels without authentication, then recover the server.

**Instructions**: Using Burp Suite, craft POST or GET requests to any endpoint with an oversized MMAUTHTOKEN cookie (>64KB), send them to trigger hang at INFO (POST) or WARN (GET) levels. Restart the server using [[commands/make-run-server]] to recover.

**Expected Output**: Server hangs on cookie logging; post-restart, service resumes normally.

**Success Indicators**:
- Requests with large cookies cause immediate unresponsiveness
- No authentication needed for GET vector
- Server restarts and logs normalize

## Attack Chain Summary

### Key Achievements

1. Achieved full DoS on Mattermost server via slash command at DEBUG level
2. Demonstrated unauthenticated DoS via cookie at WARN level
3. Highlighted logging as a vector for resource exhaustion without input validation

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---
*Last updated: 2023-10-01*
