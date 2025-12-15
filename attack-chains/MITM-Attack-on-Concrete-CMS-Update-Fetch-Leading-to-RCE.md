---
id: ac-concrete-mitm-rce-001
tags:
  - mitm
  - rce
  - concrete-cms
  - http-downgrade
  - proxy-tampering
  - zip-upload
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Login-as-Administrator-in-Concrete-CMS]]'
  - '[[procedures/Configure-Arbitrary-Proxy-in-Concrete-CMS]]'
  - '[[procedures/Tamper-with-Update-JSON-via-Proxy-Rules]]'
  - '[[procedures/Host-Malicious-ZIP-File-on-Attacker-Server]]'
  - '[[procedures/Trigger-Tampered-Update-Download-and-Unzip]]'
  - '[[procedures/Access-Unzipped-Malicious-PHP-Payload]]'
  - '[[procedures/Predict-Update-Directory-Using-CCM-Token]]'
step_count: 7
techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Remote File Copy]]'
  - '[[Python]]'
updated_at: '2025-12-14T17:23:24.142Z'
description: >-
  A multi-stage attack exploiting HTTP downgrade and arbitrary proxy
  configuration in Concrete CMS to perform a man-in-the-middle attack, tamper
  with update JSON, and achieve remote code execution via malicious ZIP upload.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
  - '[[Remote File Copy]]'
  - '[[Python]]'
---
# MITM Attack on Concrete CMS Update Fetch Leading to RCE

Multi-stage attack chain demonstrating a complete attack workflow exploiting vulnerabilities in Concrete CMS update mechanism.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 7 |
| Execution Time | ~10 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Admin Login] --> B[Proxy Config]
    B --> C[JSON Tampering]
    C --> D[Malicious ZIP Host]
    D --> E[Trigger Update]
    E --> F[Payload Access]
    F --> G[Directory Prediction]
    G --> H[RCE Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#9b59b6
    style F fill:#27ae60
    style G fill:#27ae60
    style H fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Concrete CMS (formerly concrete5) version 8.5.x or similar
- Web server with PHP
- Writable 'updates' directory
- Port 8000 open for attacker server

### Initial Access Requirements

- Administrator credentials for Concrete CMS
- Network access to the target instance
- Ability to configure outgoing proxy (admin privileges)

## Detailed Attack Procedures

### Step 1: Admin Login
procedure: [[procedures/Login-as-Administrator-in-Concrete-CMS]]

**Objective**: Gain authenticated access to the admin dashboard to enable proxy configuration and update checks.

**Instructions**: Navigate to the Concrete CMS login page and authenticate using administrator credentials.

**Expected Output**: Successful login redirect to the admin dashboard.

**Success Indicators**:
- Access to dashboard settings
- Ability to view update section

### Step 2: Configure Proxy
procedure: [[procedures/Configure-Arbitrary-Proxy-in-Concrete-CMS]]

**Objective**: Set up an attacker-controlled proxy to intercept HTTP traffic to the update server.

**Instructions**: In the admin dashboard, locate the outgoing proxy settings and configure it to point to a local Burp Suite instance, such as 127.0.0.1:8080.

**Expected Output**: Proxy configuration saved and active for outgoing requests.

**Success Indicators**:
- Proxy settings updated without errors
- Subsequent requests routed through proxy

### Step 3: Tamper with JSON
procedure: [[procedures/Tamper-with-Update-JSON-via-Proxy-Rules]]

**Objective**: Intercept and modify the update JSON response to redirect the download to a malicious ZIP file.

**Instructions**: Use Burp Suite to set up Match and Replace rules: Replace the current version in the request (e.g., '8.5.4' to '8'), modify the response's 'direct_download_url' to the attacker's server (e.g., http://192.168.1.170:8000/test.zip), and update the 'version' field to a higher value like '8.6'.

**Expected Output**: Tampered JSON response indicating a new update available.

**Success Indicators**:
- Intercepted request/response modified successfully
- JSON parseable with malicious URL

### Step 4: Host Malicious ZIP
procedure: [[procedures/Host-Malicious-ZIP-File-on-Attacker-Server]]

**Objective**: Prepare and serve the malicious ZIP containing the PHP payload for download.

**Instructions**: Create a ZIP file 'test.zip' containing 'poc.php' (e.g., a simple PHP shell) and host it on an attacker-controlled web server at http://192.168.1.170:8000/test.zip.

**Expected Output**: ZIP file accessible via HTTP GET request.

**Success Indicators**:
- Server logs show file serving
- Direct access to ZIP confirms availability

### Step 5: Trigger Update
procedure: [[procedures/Trigger-Tampered-Update-Download-and-Unzip]]

**Objective**: Initiate the update process to download and unzip the malicious ZIP into the updates directory.

**Instructions**: In the admin dashboard, perform an update check; the proxy will tamper the response, showing a new update. Click download to fetch and unzip the ZIP, placing files in a timestamp-based subdirectory.

**Expected Output**: ZIP downloaded and unzipped into /updates/<timestamp>/.

**Success Indicators**:
- Update process completes without errors
- New directory created in updates folder

### Step 6: Access Payload
procedure: [[procedures/Access-Unzipped-Malicious-PHP-Payload]]

**Objective**: Directly access the unzipped PHP file to execute the payload.

**Instructions**: If the exact timestamp is known, navigate to http://target/updates/<timestamp>/poc.php to trigger RCE.

**Expected Output**: PHP payload executes, e.g., command output or shell access.

**Success Indicators**:
- HTTP response from PHP file
- RCE commands execute successfully

### Step 7: Predict Directory
procedure: [[procedures/Predict-Update-Directory-Using-CCM-Token]]

**Objective**: Locate the exact update directory using predictable timestamp from ccm_token.

**Instructions**: Make an unauthenticated request to retrieve ccm_token (time-based), approximate the timestamp with [[commands/php-time]] or nearby values, and brute-force 2-3 directories like /updates/1600080000/.

**Expected Output**: Identification of the correct directory containing poc.php.

**Success Indicators**:
- ccm_token retrieved
- Directory found via minimal brute-force

## Attack Chain Summary

### Key Achievements

1. Successful MITM interception without CA installation
2. Tampering of update JSON to inject malicious download
3. Achievement of RCE via unzipped PHP payload in predictable location

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle
- [[Remote File Copy]] Ingress Tool Transfer
- [[Python]] PHP

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

---
*Last updated: 2023-10-01T00:00:00Z*
