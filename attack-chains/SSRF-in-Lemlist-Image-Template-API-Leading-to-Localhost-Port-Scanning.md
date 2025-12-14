---
tags:
  - ssrf
  - port-scanning
  - localhost
  - headless-chrome
  - redirection
type: attack_chain
tools:
  - '[[tools/PHP-Built-in-Server]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/php-built-in-server-host]]'
platforms:
  - Web
  - Linux
complexity: medium
procedures:
  - '[[procedures/Prepare-SSRF-Exploitation-Files]]'
  - '[[procedures/Host-Attack-Files-on-Attacker-Server]]'
  - '[[procedures/Trigger-SSRF-via-Lemlist-Endpoint]]'
  - '[[procedures/Observe-Port-Scan-Results]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
description: >-
  Exploits an SSRF vulnerability in the Lemlist img.lemlist.com API to perform
  localhost port scanning using a redirection script and JavaScript-based PoC in
  headless Chrome.
skill_level: intermediate
impact_level: high
id: 320c80f4-c7e0-4109-a631-4851029e8ead
created_at: '2025-12-14T04:08:55.355Z'
updated_at: '2025-12-14T04:08:55.355Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Network Service Scanning]]'
---
# SSRF in Lemlist Image Template API Leading to Localhost Port Scanning

Multi-stage attack chain demonstrating a complete SSRF exploitation workflow to scan localhost ports via headless Chrome screenshots.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Files] --> B[Host Server]
    B --> C[Trigger SSRF]
    C --> D[Observe Results]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/PHP-Built-in-Server]]

### Target Environment

- Web application using Lemlist img.lemlist.com API
- Headless Chrome for screenshot rendering
- Network access to the vulnerable endpoint

### Initial Access Requirements

- Public access to https://img.lemlist.com/api/image-templates
- Attacker-controlled domain for hosting files
- No credentials required

## Detailed Attack Procedures

### Step 1: Prepare Exploitation Files
procedure: [[procedures/Prepare-SSRF-Exploitation-Files]]

**Objective**: Create the redirection script and port scanning HTML to exploit SSRF in headless Chrome.

**Instructions**: Develop stealer.php for permanent redirection and PoC.html for JavaScript-based port scanning via iframes.

**Expected Output**: Functional PHP script and HTML file ready for hosting.

**Success Indicators**:
- Files created without syntax errors
- Redirection tested locally

### Step 2: Host Attack Files
procedure: [[procedures/Host-Attack-Files-on-Attacker-Server]]

**Objective**: Serve the exploitation files from an attacker-controlled server.

**Instructions**: Place files in a directory and start the server using [[commands/php-built-in-server-host]]:

```bash
php -S 0.0.0.0:80
```

**Expected Output**: Server started on http://0.0.0.0:80.

**Success Indicators**:
- Server accessible over HTTP
- Files load correctly in browser

### Step 3: Trigger SSRF Vulnerability
procedure: [[procedures/Trigger-SSRF-via-Lemlist-Endpoint]]

**Objective**: Send a malicious email parameter to the vulnerable API to initiate the SSRF and load the PoC.

**Instructions**: Access the endpoint with the attacker's URL in the email parameter, triggering fetch and redirection to PoC.html for port scanning.

**Expected Output**: Headless Chrome loads the PoC and executes JavaScript to scan ports.

**Success Indicators**:
- API request accepted without validation
- Redirection to localhost ports attempted

### Step 4: Observe Port Scan Results
procedure: [[procedures/Observe-Port-Scan-Results]]

**Objective**: Capture and analyze the results of the port scan from the executed PoC.

**Instructions**: Monitor the PoC execution in headless Chrome, adjusting timeouts for reliable detection of open ports via onload events.

**Expected Output**: Array of open ports identified through screenshot or logs.

**Success Indicators**:
- Open ports detected (e.g., via multiple onload fires)
- Screenshots reveal local service details

## Attack Chain Summary

### Key Achievements

1. Bypassed URL validation in email parameter for SSRF
2. Achieved localhost port scanning in headless environment
3. Enabled potential data leakage via screenshots

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Network Service Scanning]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Reconnaissance]]

---
*Last updated: 2023-10-01*
