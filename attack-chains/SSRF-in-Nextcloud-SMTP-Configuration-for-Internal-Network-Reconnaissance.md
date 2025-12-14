---
id: ac-nextcloud-ssrf-recon-001
tags:
  - ssrf
  - nextcloud
  - reconnaissance
  - smtp
  - internal-network
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Nextcloud
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Access-Nextcloud-Admin-SMTP-Settings]]'
  - '[[procedures/Probe-Different-Network-Segment-via-SMTP]]'
  - '[[procedures/Probe-Non-Existent-IP-via-SMTP]]'
  - '[[procedures/Probe-Existing-Host-Default-SMTP-Port]]'
  - '[[procedures/Probe-Existing-Host-Non-Open-Port-via-SMTP]]'
step_count: 5
techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.089Z'
description: >-
  An authenticated administrator exploits a Server-Side Request Forgery (SSRF)
  vulnerability in Nextcloud's SMTP email configuration to perform internal
  network reconnaissance, revealing host existence, network segments, and open
  ports.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
  - '[[Exploit Public-Facing Application]]'
---
# SSRF in Nextcloud SMTP Configuration for Internal Network Reconnaissance

Multi-stage attack chain demonstrating how an authenticated Nextcloud administrator can exploit an SSRF vulnerability in the SMTP email configuration to conduct internal network reconnaissance. By inputting various internal IP addresses into the SMTP server field, the attacker observes distinct error messages and success indicators that reveal whether hosts exist, their network segment relative to the server, and specific port openness. This can expose sensitive infrastructure details in shared hosting or corporate environments, aiding further attacks.

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
    A[Access Admin Settings] --> B[Probe Network Segments]
    B --> C[Probe Non-Existent Hosts]
    C --> D[Probe Existing Hosts - Default Port]
    D --> E[Probe Ports on Existing Hosts]
    E --> F[Reconnaissance Complete]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#3498db
    style F fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Web browser (e.g., Chrome or Firefox)

### Target Environment

- Nextcloud instance (version vulnerable to CVE or similar, e.g., pre-patch for this issue)
- Authenticated administrator access
- Internal network access to target IPs (e.g., 172.17.x.x range)
- Services/ports: SMTP (25), SSH (22)

### Initial Access Requirements

- Valid admin credentials for Nextcloud
- Direct access to the Nextcloud web interface (e.g., https://target.nextcloud.com/settings/admin/additional)
- No prior network access beyond admin login; exploits server-side requests

## Detailed Attack Procedures

### Step 1: Access Admin Settings
procedure: [[procedures/Access-Nextcloud-Admin-SMTP-Settings]]

**Objective**: Gain access to the SMTP configuration interface to begin probing.

**Instructions**: Log in as an administrator and navigate to the admin settings page. Select SMTP as the email mode to enable the server address field for input.

**Expected Output**: SMTP configuration form visible, with fields for server address and port.

**Success Indicators**:
- Admin settings page loads successfully
- SMTP mode selected without errors

### Step 2: Probe Different Network Segment
procedure: [[procedures/Probe-Different-Network-Segment-via-SMTP]]

**Objective**: Determine if a target IP is on a different network segment from the Nextcloud server.

**Instructions**: Enter an IP from a suspected different segment (e.g., 172.17.1.0) into the SMTP server address field and attempt to send a test email.

**Expected Output**: Error message indicating the address is not on the same network segment.

**Success Indicators**:
- Specific hint about network segment mismatch
- No connection success

### Step 3: Probe Non-Existent IP
procedure: [[procedures/Probe-Non-Existent-IP-via-SMTP]]

**Objective**: Confirm if a host does not exist or has no open ports.

**Instructions**: Input a non-existent or closed IP (e.g., 172.17.0.0) into the SMTP server address field and trigger the test email.

**Expected Output**: Hint indicating the address does not exist or lacks open ports.

**Success Indicators**:
- Error revealing host non-existence
- No successful connection

### Step 4: Probe Existing Host Default SMTP Port
procedure: [[procedures/Probe-Existing-Host-Default-SMTP-Port]]

**Objective**: Verify the existence of a host and openness of the default SMTP port (25).

**Instructions**: Enter an existing internal host IP (e.g., 172.17.0.1) with port left empty (defaults to 25) and send the test email.

**Expected Output**: Test email sends successfully.

**Success Indicators**:
- Successful email transmission
- Confirmation of host and port accessibility

### Step 5: Probe Existing Host Non-Open Port
procedure: [[procedures/Probe-Existing-Host-Non-Open-Port-via-SMTP]]

**Objective**: Check if a specific non-standard port is open on an existing host.

**Instructions**: Use the same existing IP (e.g., 172.17.0.1) but specify a non-open port like 22 (SSH) in the port field and attempt the test.

**Expected Output**: Hint that the address exists but the port is not accessible.

**Success Indicators**:
- Error distinguishing host existence from port closure
- Partial reconnaissance success

## Attack Chain Summary

### Key Achievements

1. Revealed network topology, including segment separation
2. Identified non-existent hosts and closed ports
3. Confirmed existing internal hosts and open SMTP ports
4. Mapped port status on live hosts, exposing potential services like SSH

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### MITRE ATT&CK Tactics

- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
