---
id: cisco-sx80-auth-bypass-rce
tags:
  - cisco
  - telepresence
  - default-credentials
  - auth-bypass
  - rce
  - video-conferencing
type: attack_chain
tools:
  - '[[tools/ipinfo-io]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Hardware
  - Network
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Exposed-Cisco-TelePresence-Device]]'
  - '[[procedures/Bypass-Authentication-with-Default-Credentials-on-Cisco-SX80]]'
  - '[[procedures/Access-Device-Configuration-for-Full-Control]]'
  - '[[procedures/Achieve-RCE-via-Startup-Scripts-on-Cisco-SX80]]'
step_count: 4
techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T17:31:31.085Z'
description: >-
  Multi-stage attack exploiting an exposed Cisco TelePresence SX80 device with
  default credentials to achieve authentication bypass and remote code
  execution, compromising video conferencing systems in sensitive environments.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Valid Accounts]]'
  - '[[Default Accounts]]'
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
---
# Authentication Bypass and RCE on Cisco TelePresence SX80 via Default Credentials

Multi-stage attack chain demonstrating exploitation of an exposed Cisco TelePresence SX80 video conferencing device using default credentials to bypass authentication and achieve remote code execution, potentially allowing device compromise, data interception, and persistent backdoor access in training and briefing environments.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Reconnaissance: Identify Device] --> B[Initial Access: Auth Bypass]
    B --> C[Privilege Escalation: Gain Control]
    C --> D[Execution: RCE via Scripts]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/ipinfo-io]]

### Target Environment

- Cisco TelePresence SX80 hardware device
- Exposed web interface on port 443 (HTTPS)
- Networked in a scope-associated ASN

### Initial Access Requirements

- Public or internal network access to the device's IP address
- Knowledge of default credentials (e.g., admin / blank or known defaults per Cisco documentation)
- No prior access needed beyond reachability

## Detailed Attack Procedures

### Step 1: Identify Exposed Device
procedure: [[procedures/Identify-Exposed-Cisco-TelePresence-Device]]

**Objective**: Locate and confirm the Cisco TelePresence SX80 device within the target scope using IP reconnaissance.

**Instructions**: Use [[tools/ipinfo-io]] to query the IP address and verify ASN ownership.

Navigate to https://ipinfo.io and input the target's IP to retrieve details.

**Expected Output**: Confirmation of device association with in-scope ASN (e.g., ID: ██████) and identification as a Cisco TelePresence SX80 at https://█████.

**Success Indicators**:
- ASN matches target scope
- Device type confirmed as SX80

### Step 2: Bypass Authentication
procedure: [[procedures/Bypass-Authentication-with-Default-Credentials-on-Cisco-SX80]]

**Objective**: Gain initial access to the web interface using unchanged default credentials.

**Instructions**: Access the web interface at https://███████ and attempt login with default credentials such as `█████████` / ████.

Enter the credentials in the login form to authenticate as user ███.

**Expected Output**: Successful login to the administrative dashboard.

**Success Indicators**:
- Login prompt accepted without errors
- Access to user dashboard granted

### Step 3: Gain Full Control
procedure: [[procedures/Access-Device-Configuration-for-Full-Control]]

**Objective**: Escalate to full administrative control over device configurations and connections.

**Instructions**: Post-login, navigate through the interface to access configuration menus, including connection controls and system settings.

Explore sections like system administration and endpoint management.

**Expected Output**: Ability to view and modify device settings, such as call controls and network configurations.

**Success Indicators**:
- Configuration panels accessible and editable
- Administrative privileges confirmed

### Step 4: Achieve RCE
procedure: [[procedures/Achieve-RCE-via-Startup-Scripts-on-Cisco-SX80]]

**Objective**: Execute arbitrary code by uploading custom startup scripts, establishing persistent compromise.

**Instructions**: From the authenticated session, navigate to https://██████████/web/scripts and upload a custom script for execution on startup.

Select the upload option and provide the script file containing desired code (e.g., shell commands for data exfiltration).

**Expected Output**: Script uploaded successfully and executed on device reboot or trigger, allowing command execution.

**Success Indicators**:
- Script addition confirmed in interface
- Code execution verifiable via logs or callbacks

## Attack Chain Summary

### Key Achievements

1. Identified exposed SX80 device in scope via IP lookup.
2. Bypassed authentication using default credentials for admin access.
3. Gained full control over video conferencing configurations.
4. Achieved RCE through unrestricted script uploads, enabling backdoor persistence.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Valid Accounts]] Valid Accounts
- [[Default Accounts]] Default Accounts
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Command-Line Interface]] Command and Scripting Interpreter

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
