---
id: ac-slack-ssrf-slash-ipv6-bypass
tags:
  - ssrf
  - slack
  - ipv6
  - slash-commands
  - internal-scanning
  - bypass
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Create-Custom-Slack-App]]'
  - '[[procedures/Configure-Slash-Command-SSRF]]'
  - '[[procedures/Save-Slack-App-Configuration]]'
  - '[[procedures/Invoke-Slack-Slash-Command]]'
  - '[[procedures/Observe-SSRF-Results]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:46:14.481Z'
description: >-
  Multi-stage attack exploiting SSRF in Slack's custom slash commands to access
  internal IPv6 services like SSH and SMTP, bypassing prior mitigations.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
---
# SSRF in Slack Slash Commands Bypassing IPv6 Protections for Internal Service Access

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery (SSRF) vulnerability in Slack's api.slack.com via custom slash commands. This bypasses protections from previous reports (#61312 and #356765) by using IPv6 localhost redirects to access internal services, enabling port scanning and banner disclosure for services like SSH on port 22 and SMTP on port 25.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Create Custom App] --> B[Configure SSRF URL]
    B --> C[Save Configuration]
    C --> D[Invoke Slash Command]
    D --> E[Observe Internal Access]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for api.slack.com access
- Attacker-controlled server hosting PHP (e.g., Apache with PHP)

### Target Environment

- Slack workspace with app creation permissions
- Internal services on IPv6 localhost (e.g., SSH on [::]:22, SMTP on [::]:25)
- Network access to api.slack.com

### Initial Access Requirements

- Valid Slack account with permissions to create custom apps
- Control over a public domain/server for hosting redirect script
- No prior internal access needed; exploits external-facing Slack API

## Detailed Attack Procedures

### Step 1: Create Custom Slack App
procedure: [[procedures/Create-Custom-Slack-App]]

**Objective**: Set up a custom Slack application to enable slash command configuration for SSRF exploitation.

**Instructions**: Access api.slack.com in a web browser, log in with your Slack account, and create a new app by selecting 'From scratch'. Provide an app name and select your workspace. Navigate to the 'Slash Commands' feature and add a new command with a custom name like /yourslash.

**Expected Output**: New Slack app created with slash command feature enabled.

**Success Indicators**:
- App dashboard visible on api.slack.com
- Slash command section available for configuration

### Step 2: Configure Slash Command for SSRF
procedure: [[procedures/Configure-Slash-Command-SSRF]]

**Objective**: Point the slash command to an attacker-controlled URL that redirects to internal IPv6 services, setting up the SSRF payload.

**Instructions**: In the slash command settings, set the 'Request URL' to your attacker-controlled domain, e.g., https://attacker.com/index.php. Ensure index.php contains the PHP redirect script using [[commands/php-redirect-ipv6-internal]] to target http://[::]:22/ for SSH or adjust port for other services like http://[::]:25/ for SMTP.

```php
<?php header("Location: http://[::]:22/"); ?>
```

Upload and verify the PHP file on your server.

**Expected Output**: Slash command URL configured to attacker domain.

**Success Indicators**:
- URL field shows attacker.com/index.php
- PHP script accessible and redirects when fetched directly

### Step 3: Save Slack App Configuration
procedure: [[procedures/Save-Slack-App-Configuration]]

**Objective**: Activate the malicious slash command by finalizing app settings.

**Instructions**: Review all app configurations, ensure the slash command is enabled, and click 'Save Changes' on the api.slack.com dashboard. Install the app to your workspace if prompted.

**Expected Output**: Configuration saved; slash command active in workspace.

**Success Indicators**:
- No errors on save
- App installed in Slack workspace

### Step 4: Invoke Slack Slash Command
procedure: [[procedures/Invoke-Slack-Slash-Command]]

**Objective**: Trigger the SSRF by invoking the slash command, causing Slack's server to fetch the redirect URL and access internal services.

**Instructions**: In your Slack workspace, type /yourslash in any channel and send the message. Slack's backend will request the configured URL, follow the PHP redirect to the internal IPv6 address, and proxy the response.

**Expected Output**: Slash command response appears in Slack chat.

**Success Indicators**:
- Command invokes without errors
- Response loads (may show internal banner or error)

### Step 5: Observe SSRF Results
procedure: [[procedures/Observe-SSRF-Results]]

**Objective**: Capture and analyze the disclosed internal service information to confirm exploitation and scan further ports.

**Instructions**: Review the slash command response in Slack for service banners (e.g., SSH version on port 22). Repeat invocations with modified PHP redirects for other ports like 25 (SMTP) to perform internal port scanning.

**Expected Output**: Banners such as "SSH-2.0-OpenSSH_8.2p1" or SMTP responses.

**Success Indicators**:
- Internal service data visible in Slack response
- Ability to probe multiple ports via repeated invocations

## Attack Chain Summary

### Key Achievements

1. Bypassed IPv6 localhost protections in Slack slash commands
2. Accessed internal services (SSH, SMTP) via SSRF redirects
3. Enabled reconnaissance and potential further internal pivoting

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Network Service Scanning]] Network Service Scanning

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Discovery]] Discovery

---
*Last updated: 2023-10-01T00:00:00Z*
