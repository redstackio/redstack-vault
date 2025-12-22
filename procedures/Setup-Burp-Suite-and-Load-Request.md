---
tags:
  - burp-suite
  - request-capture
  - web-testing
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:11.902Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 320f976a-09ef-49f9-8f42-cfc5f20525a5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
---

# Setup Burp Suite and Load Request

## Summary

This procedure sets up Burp Suite as a proxy and interception tool, navigates to the Repeater module, and loads a captured unauthenticated password change request for subsequent modification in an IDOR exploitation scenario.

## Description

In the context of testing web applications for vulnerabilities like IDOR, Burp Suite is used to intercept and manipulate HTTP traffic. This step prepares the environment by launching the tool, switching to Repeater for manual request editing, and inserting a pre-captured POST request to the password change endpoint. The request typically includes a Cookie header with UID2 parameter and body fields for userName and password. This is essential for unauthenticated testing where direct browser access might not suffice.

## Requirements

1. Burp Suite installed and licensed (Community or Professional edition)
2. Network access to the target DoD web application
3. A pre-captured HTTP request to the password change endpoint (e.g., from Proxy interception or report attachment)
4. Basic knowledge of HTTP requests and Burp interface

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or tool signatures in network logs
- Implement web application firewall (WAF) rules to detect request manipulation patterns
- Enforce client certificate pinning to prevent proxy interception

## Objectives

1. Prepare Burp Suite for request manipulation
2. Load the base password change request
3. Enable seamless transition to IDOR exploitation

## Instructions

### Step 1: Launch Burp Suite

**Context**: Start the Burp Suite application to enable proxy and interception capabilities for capturing and modifying web requests.

In Burp Suite, go to the Proxy tab and ensure the intercept is turned on if capturing live traffic. For this procedure, focus on the Repeater module.

> Launch Burp Suite and confirm the proxy listener is active on default port 8080.

### Step 2: Navigate to Repeater Tab

**Context**: Switch to the Repeater module, which allows sending and editing individual HTTP requests without full proxy setup.

Click on the Repeater tab in the Burp Suite interface.

> Repeater tab opens, ready for request input.

### Step 3: Paste Captured Request

**Context**: Insert the raw HTTP request into Repeater for inspection and modification.

Copy the captured POST request (e.g., from Proxy history or attachment) and paste it into the raw request pane in Repeater. The request should target the password change endpoint, with headers like Cookie: UID2=<current_id> and body: userName=<email>&password=<value>.

> Request loaded, displaying full HTTP structure for editing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[tools/Burp-Suite]]
- [[request-manipulation]]

