---
tags:
  - xss
  - stored-xss
  - wordpress
  - plugin-vulnerability
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Inject-Malicious-Payload-into-Stream-Plugin-Activity-Log]]'
  - '[[procedures/Trigger-Stored-XSS-in-WordPress-Admin-Dashboard]]'
step_count: 2
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T00:11:09.224Z'
description: >-
  Unauthenticated stored XSS in the Stream WordPress plugin allowing JavaScript
  injection through unsanitized wp_redirect logs from plugin-editor.php, leading
  to admin-privileged code execution in the dashboard.
skill_level: intermediate
impact_level: high
id: d48679d4-1146-47dc-8048-ebb62a54cdc0
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Stored XSS in Stream WordPress Plugin via Unsanitized Activity Logs

Multi-stage attack chain demonstrating a complete attack workflow for exploiting a stored XSS vulnerability in the Stream WordPress plugin on a target site like newsroom.uber.com.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 2 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access: Inject Payload] --> B[Execution: Trigger XSS]
    B --> C[Privilege Escalation: Admin JS Execution]
    C --> D[Objective: Site Compromise]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- WordPress site with Stream plugin version 1.4.9 or vulnerable equivalent
- Access to wp-login.php and admin dashboard (for triggering)
- No authentication required for injection

### Initial Access Requirements

- Network access to the target WordPress site (e.g., https://newsroom.uber.com)
- No credentials needed for payload injection
- Administrative access to view the Stream tab for exploitation

## Detailed Attack Procedures

### Step 1: Initial Access
procedure: [[procedures/Inject-Malicious-Payload-into-Stream-Plugin-Activity-Log]]

**Objective**: Inject unsanitized JavaScript payload into the Stream plugin's activity log via a crafted Referer header in a wp_redirect event.

**Instructions**: Use [[commands/curl-inject-xss-referer]] to send a POST request to wp-login.php with action=postpass and a malicious Referer header simulating a redirect from plugin-editor.php:

```bash
curl -v -H 'Referer: /hello?plugin-editor.php&file=aaa%3cscript%3ealert(%27stored%20xss%27);%3c/script%3e' --data 'post-password=foo' 'https://newsroom.uber.com/wp-login.php?action=postpass'
```

**Expected Output**: HTTP 302 redirect response, with verbose output showing the request details; the payload is logged in the Stream plugin's database without sanitization.

**Success Indicators**:
- 302 redirect status in curl output
- Payload stored in database (verifiable by querying Stream's activity log table if accessible)

### Step 2: Execution
procedure: [[procedures/Trigger-Stored-XSS-in-WordPress-Admin-Dashboard]]

**Objective**: Trigger the stored XSS by viewing the unsanitized log entry in the admin dashboard, executing JavaScript with administrator privileges.

**Instructions**: Log in as an administrator and navigate to the Stream tab in the WordPress dashboard. The injected payload will render and execute automatically upon display of the activity log.

**Expected Output**: JavaScript alert popup displaying 'stored xss' or execution of the injected code, potentially allowing further actions like site defacement or PHP file modifications.

**Success Indicators**:
- Alert or JS execution observed in browser
- Ability to run arbitrary JS in admin context, confirmed by inspecting console or further payload testing

## Attack Chain Summary

### Key Achievements

1. Unauthenticated payload injection into WordPress activity logs
2. Execution of admin-privileged JavaScript via stored XSS
3. Potential for full site compromise, including content control and server-side PHP edits

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
