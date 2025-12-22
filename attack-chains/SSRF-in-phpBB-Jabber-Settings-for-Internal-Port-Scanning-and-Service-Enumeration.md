---
id: ac-phpbb-ssrf-jabber-portscan
tags:
  - ssrf
  - phpbb
  - port-scanning
  - service-enumeration
  - jabber
type: attack_chain
tools:
  - '[[tools/sshd]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-SSRF-in-phpBB-Jabber-Settings]]'
step_count: 5
techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:18.804Z'
description: >-
  Authenticated administrator exploits SSRF in phpBB's Jabber settings to scan
  internal ports and enumerate services like SSH and MySQL on localhost or
  internal network.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in phpBB Jabber Settings for Internal Port Scanning and Service Enumeration

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery (SSRF) vulnerability in the phpBB 3.3.1 Administrator Control Panel's Jabber settings. An authenticated administrator can manipulate the 'jabber server' and 'Jabber port' parameters to force the server to connect to arbitrary internal hosts and ports, such as localhost (127.0.0.1). This enables port scanning, service enumeration (e.g., detecting open SSH or MySQL services and extracting version information from error messages), and potential further interactions with restricted internal resources. The attack requires admin privileges but reveals sensitive internal network details without direct access.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 5 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Access Admin Panel] --> B[Configure Jabber Settings]
    B --> C[Submit and Trigger SSRF]
    C --> D[Observe Error Responses]
    D --> E[Enumerate Multiple Ports]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/sshd]] (for demonstrating SSH service detection)

### Target Environment

- phpBB 3.3.1 running on a web server (e.g., Apache with PHP on Linux)
- Jabber (XMPP) feature available in Admin Control Panel
- Open internal services like SSH on port 2222 or MySQL for enumeration
- Network access to the phpBB instance

### Initial Access Requirements

- Valid administrator credentials for phpBB
- Direct access to the web interface (no network position restrictions beyond reaching the app)
- No prior access needed beyond authentication

## Detailed Attack Procedures

### Step 1: Access the Jabber Settings in the Admin Control Panel
procedure: [[procedures/Exploit-SSRF-in-phpBB-Jabber-Settings]]

**Objective**: Gain entry to the vulnerable configuration panel to prepare for SSRF exploitation.

**Instructions**: Log in to the phpBB Administrator Control Panel using admin credentials. Navigate to the 'Jabber settings' section under the messaging or integration options.

**Expected Output**: The Jabber settings form loads, displaying fields for 'Jabber server' and 'Jabber port'.

**Success Indicators**:
- Admin panel accessible without errors
- Jabber settings form visible

### Step 2: Set the Jabber Server and Port Parameters
procedure: [[procedures/Exploit-SSRF-in-phpBB-Jabber-Settings]]

**Objective**: Input arbitrary internal host and port values to target localhost or internal services.

**Instructions**: In the 'Jabber server' field, enter '127.0.0.1' (localhost). In the 'Jabber port' field, specify a target port, such as 2222 for an SSH demo service.

**Expected Output**: Form fields populated with the malicious inputs.

**Success Indicators**:
- Inputs accepted without client-side validation errors
- Form ready for submission

### Step 3: Enable Jabber and Submit the Form
procedure: [[procedures/Exploit-SSRF-in-phpBB-Jabber-Settings]]

**Objective**: Trigger the server-side connection attempt, exploiting the SSRF.

**Instructions**: Select the 'Enabled' radio button for the Jabber feature and click 'Submit' to process the form and initiate the connection to the specified host and port.

**Expected Output**: Form submission redirects or reloads, with the server attempting the connection.

**Success Indicators**:
- No immediate form rejection
- Page processes without HTTP errors

### Step 4: Observe the Response for Error Messages
procedure: [[procedures/Exploit-SSRF-in-phpBB-Jabber-Settings]]

**Objective**: Analyze error responses to detect open ports and extract service details.

**Instructions**: Review the post-submission page for error messages. For closed ports, expect 'Connection refused'; for open services like SSH or MySQL, look for 'Could not authorize on Jabber server' or leaked version information.

**Expected Output**: Specific error strings revealing connection status, e.g., SSH version details if [[tools/sshd]] is running on port 2222.

**Success Indicators**:
- 'Connection refused' for closed ports
- Service-specific errors (e.g., authentication failures or version banners) for open ports

### Step 5: Repeat for Different Ports to Enumerate Services
procedure: [[procedures/Exploit-SSRF-in-phpBB-Jabber-Settings]]

**Objective**: Perform systematic port scanning to map internal services and gather enumeration data.

**Instructions**: Iterate the process by changing the 'Jabber port' value (e.g., 22 for SSH, 3306 for MySQL) and resubmitting the form multiple times, noting response differences to identify open services and versions.

**Expected Output**: Varied error messages across ports, enabling a map of open internal services.

**Success Indicators**:
- Multiple ports tested with distinct responses
- Service types and versions inferred from errors (e.g., MySQL version in connection errors)

## Attack Chain Summary

### Key Achievements

1. Successful SSRF exploitation to connect to localhost/internal hosts
2. Port scanning revealing open services like SSH and MySQL
3. Service enumeration extracting version information from error leaks

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
