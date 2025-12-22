---
id: ac-phpbb-ssrf-portscan-001
tags:
  - ssrf
  - phpbb
  - port-scanning
  - service-enumeration
  - internal-recon
type: attack_chain
tools:
  - '[[tools/OpenSSH-Server-sshd]]'
tactics:
  - '[[Discovery]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-phpBB-Admin-Control-Panel]]'
  - '[[procedures/Configure-Jabber-Settings-for-SSRF]]'
  - '[[procedures/Submit-Jabber-Settings-to-Trigger-Connection]]'
  - '[[procedures/Analyze-SSRF-Response-for-Service-Detection]]'
  - '[[procedures/Iterate-SSRF-for-Port-Scanning]]'
step_count: 5
techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:29:10.157Z'
description: >-
  Authenticated administrator exploits SSRF vulnerability in phpBB's Jabber
  settings to scan localhost ports, enumerate internal services, and leak
  version information via error messages.
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in phpBB Jabber Settings for Localhost Port Scanning and Service Enumeration

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery (SSRF) vulnerability in the phpBB Administrator Control Panel's Jabber settings. An authenticated administrator can manipulate the 'jabber server' and 'Jabber port' parameters to force the server to connect to internal resources like localhost, enabling port scanning, service enumeration, and potential leakage of software versions through error messages. This allows reconnaissance of the host machine or internal network without direct access.

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
    A[Access Admin Panel] --> B[Configure Jabber to Localhost]
    B --> C[Submit Settings]
    C --> D[Observe Response]
    D --> E[Repeat for Scanning]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser for accessing the phpBB admin panel
- [[tools/OpenSSH-Server-sshd]] (for demo service on localhost)

### Target Environment

- phpBB 3.3.1 or vulnerable versions running on a web server (PHP-based)
- Required services/ports: Admin access to phpBB, internal services like SSH (port 2222) or MySQL for testing
- Network access requirements: Authenticated session as administrator

### Initial Access Requirements

- Valid administrator credentials for phpBB
- Direct access to the web application (no network position restrictions beyond login)
- No prior access needed beyond admin login

## Detailed Attack Procedures

### Step 1: Access the Administrator Control Panel
procedure: [[procedures/Access-phpBB-Admin-Control-Panel]]

**Objective**: Gain entry to the phpBB admin interface to reach the vulnerable Jabber settings.

**Instructions**: Log in to the phpBB forum as an administrator and navigate to the Admin Control Panel (ACP), then proceed to the Jabber configuration section.

**Expected Output**: Successful login and display of the ACP dashboard with access to settings panels.

**Success Indicators**:
- Admin dashboard loads without errors
- Jabber settings panel is accessible

### Step 2: Configure Jabber Server and Port for SSRF
procedure: [[procedures/Configure-Jabber-Settings-for-SSRF]]

**Objective**: Set the parameters to target internal localhost resources.

**Instructions**: In the Jabber settings form, enter '127.0.0.1' as the jabber server and specify a test port, such as 2222 for SSH or 3306 for MySQL.

**Expected Output**: Form fields populated with localhost IP and port values, ready for submission.

**Success Indicators**:
- Parameters accept localhost input without client-side validation errors
- Form is submittable

### Step 3: Enable and Submit Jabber Settings
procedure: [[procedures/Submit-Jabber-Settings-to-Trigger-Connection]]

**Objective**: Trigger the server-side connection attempt to the specified internal resource.

**Instructions**: Select the 'Enabled' radio button for the Jabber feature and submit the form to initiate the SSRF.

**Expected Output**: Form submission redirects or reloads the page, with the server attempting a connection to the localhost port.

**Success Indicators**:
- No immediate client-side blocks
- Page reloads after submission

### Step 4: Analyze Response for Port and Service Status
procedure: [[procedures/Analyze-SSRF-Response-for-Service-Detection]]

**Objective**: Interpret error messages to determine if the port is open and identify service details.

**Instructions**: Review the post-submission error or success message; look for 'Connection refused' for closed ports or service-specific responses like version leaks from debug-enabled services.

**Expected Output**: Error messages revealing connection status, e.g., 'Connection refused' for closed ports or 'Could not authorize on Jabber server' for open ports, potentially with version info.

**Success Indicators**:
- Specific error indicating open/closed port
- Service version or banner leaked in response

### Step 5: Repeat Configuration for Multiple Ports and IPs
procedure: [[procedures/Iterate-SSRF-for-Port-Scanning]]

**Objective**: Systematically scan multiple ports to map internal services.

**Instructions**: Modify the port value in the Jabber settings and resubmit repeatedly, targeting various ports on 127.0.0.1 or other internal IPs to enumerate services.

**Expected Output**: Cumulative results from multiple submissions showing open ports and inferred service types/versions.

**Success Indicators**:
- Multiple ports identified as open
- Internal network services enumerated

## Attack Chain Summary

### Key Achievements

1. Forced server connections to localhost without validation
2. Performed port scanning on internal interfaces
3. Enumerated services and leaked version information via errors

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Network Service Scanning]] Network Service Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Discovery]] Discovery

---

*Last updated: 2023-10-01T00:00:00Z*
