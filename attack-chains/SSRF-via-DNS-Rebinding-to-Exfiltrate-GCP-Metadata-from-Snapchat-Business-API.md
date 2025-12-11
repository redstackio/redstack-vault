---
id: 7bd805f7-cf91-4c9f-8a50-1d8c333f7424
name: SSRF via DNS Rebinding to Exfiltrate GCP Metadata from Snapchat Business API
type: attack_chain
description: >-
  Multi-stage attack exploiting SSRF in Snapchat's media import endpoint using
  DNS rebinding to access and exfiltrate sensitive GCP metadata.
verified: false
submitted: true
step_count: 6
created_at: '2025-12-11T06:10:15.626Z'
updated_at: '2025-12-11T06:10:15.626Z'
procedures:
  - '[[procedures/Access-Snapchat-Business-Creative-Import]]'
  - '[[procedures/Set-Up-Timing-and-Logging-Server]]'
  - '[[procedures/Host-Malicious-HTML-with-DNS-Rebinding-JavaScript]]'
  - '[[procedures/Trigger-SSRF-by-Submitting-Malicious-URL]]'
  - '[[procedures/Perform-DNS-Rebinding-Switch]]'
  - '[[procedures/Exfiltrate-GCP-Metadata-via-JavaScript]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Unsecured Credentials]]'
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
  - '[[Collection]]'
tags:
  - ssrf
  - dns-rebinding
  - gcp
  - metadata-exfil
  - cloud
platforms:
  - Web
  - GCP
tools:
  - '[[tools/Flask]]'
  - '[[tools/flask_cors]]'
  - '[[tools/XMLHttpRequest]]'
commands:
  - '[[commands/flask-app-run]]'
  - '[[commands/flask-sleep]]'
  - '[[commands/flask-print-log]]'
  - '[[commands/flask-set-log-level]]'
complexity: high
skill_level: advanced
impact_level: high
validated: true
mitre_tactics:
  - '[[TA0001]]'
  - '[[TA0007]]'
  - '[[TA0009]]'
mitre_techniques:
  - '[[T1190]]'
  - '[[T1552]]'
---

# SSRF via DNS Rebinding to Exfiltrate GCP Metadata from Snapchat Business API

Multi-stage attack chain demonstrating a complete attack workflow exploiting an SSRF vulnerability in Snapchat's business API to fetch internal GCP metadata via DNS rebinding.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 6 |
| Execution Time | ~10 minutes |
| Skill Level | Advanced |
| Complexity | High |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access to Snapchat] --> B[Setup Timing Server]
    B --> C[Host Malicious HTML]
    C --> D[Trigger SSRF]
    D --> E[DNS Rebinding]
    E --> F[Exfiltrate Metadata]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#8e44ad
    style F fill:#2c3e50
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Flask]]
- [[tools/flask_cors]]
- [[tools/XMLHttpRequest]]

### Target Environment

- Web platform with access to business.snapchat.com
- Cloud (GCP) environment for metadata service
- Ports: 5000, 80
- Services: Google Metadata Service, Google Compute Engine

### Initial Access Requirements

- Valid Snapchat business account credentials
- Publicly accessible host for timing server
- Control over DNS records for rebinding domain

## Detailed Attack Procedures

### Step 1: Initial Access - [[procedures/Access-Snapchat-Business-Creative-Import]]

**Procedure**: [[procedures/Access-Snapchat-Business-Creative-Import]]

**Objective**: Gain access to the vulnerable media import functionality in Snapchat's business portal.

**Expected Output**: Successful navigation to the import endpoint ready for URL submission.

**Success Indicators**:
- Logged into business.snapchat.com
- Creative import interface loaded

### Step 2: Setup Server - [[procedures/Set-Up-Timing-and-Logging-Server]]

**Procedure**: [[procedures/Set-Up-Timing-and-Logging-Server]]

**Objective**: Create a server to handle timing delays and logging for the DNS rebinding attack.

**Expected Output**: Flask server running on port 5000, responding to routes with delays and logging.

First, set up the Flask app and run it using [[commands/flask-app-run]]:

```python
app.run(host='0.0.0.0')
```

Configure logging with [[commands/flask-set-log-level]]:

```python
log.setLevel(logging.ERROR)
```

Implement sleep in routes using [[commands/flask-sleep]]:

```python
sleep(3)
```

Log messages with [[commands/flask-print-log]]:

```python
print request.args['msg']
```

**Success Indicators**:
- Server accessible at ssh.█████:5000
- Routes '/' and '/log' functional

### Step 3: Host Malicious Payload - [[procedures/Host-Malicious-HTML-with-DNS-Rebinding-JavaScript]]

**Procedure**: [[procedures/Host-Malicious-HTML-with-DNS-Rebinding-JavaScript]]

**Objective**: Prepare and host an HTML file with JavaScript that performs DNS rebinding and fetches metadata.

**Expected Output**: HTML file hosted on attacker-controlled domain, JavaScript ready to execute rebinding and exfiltration.

**Success Indicators**:
- JavaScript logs to timing server
- Fetches from metadata endpoints like /computeMetadata/v1beta1/project/attributes/ssh-keys

### Step 4: Trigger Vulnerability - [[procedures/Trigger-SSRF-by-Submitting-Malicious-URL]]

**Procedure**: [[procedures/Trigger-SSRF-by-Submitting-Malicious-URL]]

**Objective**: Submit the malicious URL to the SSRF-vulnerable endpoint to force server-side fetch.

**Expected Output**: Server fetches the provided URL, loading the malicious HTML.

**Success Indicators**:
- Request to /api/v1/media/import with URL http://demon.███████/ssrf.html succeeds

### Step 5: Rebind DNS - [[procedures/Perform-DNS-Rebinding-Switch]]

**Procedure**: [[procedures/Perform-DNS-Rebinding-Switch]]

**Objective**: Switch DNS records to rebind the domain to the internal metadata IP.

**Expected Output**: Domain resolves to 169.254.169.254 after switch.

**Success Indicators**:
- DNS update propagates within 3 minutes
- JavaScript executes against internal IP

### Step 6: Data Exfiltration - [[procedures/Exfiltrate-GCP-Metadata-via-JavaScript]]

**Procedure**: [[procedures/Exfiltrate-GCP-Metadata-via-JavaScript]]

**Objective**: Use the rebound connection to fetch and log sensitive metadata.

**Expected Output**: Exfiltrated data such as SSH keys, service accounts, and hostnames logged to the timing server.

**Success Indicators**:
- Logs show data from endpoints like /computeMetadata/v1/instance/service-accounts/
- Ability to mint tokens from service accounts

## Attack Chain Summary

### Key Achievements

1. Successful SSRF trigger via media import
2. DNS rebinding to internal GCP metadata
3. Exfiltration of sensitive cloud credentials and data

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Unsecured Credentials]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]
- [[Collection]]

---

*Last updated: [TIMESTAMP]*
