---
tags:
  - idor
  - auth-bypass
  - android
  - mobile
  - attachment-download
  - http-interception
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
verified: false
platforms:
  - Android
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Intercept-App-Traffic-with-Burp-Suite]]'
  - '[[procedures/Send-and-Capture-Attachment-Request]]'
  - '[[procedures/Identify-Attachment-Download-Endpoint]]'
  - '[[procedures/Modify-ID-for-IDOR-Exploitation]]'
  - '[[procedures/Bypass-Authentication-to-Download-Attachments]]'
step_count: 5
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:47.799Z'
description: >-
  Multi-stage attack exploiting Insecure Direct Object Reference (IDOR) and
  authentication bypass in the BCM Messenger Android app to download any user's
  private attachments without authorization.
skill_level: intermediate
impact_level: high
id: 4c2be937-fcf9-4779-b4b0-9d0ca589cc83
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# IDOR and Auth Bypass in BCM Messenger Attachments for Unauthorized File Downloads

Multi-stage attack chain demonstrating exploitation of an Insecure Direct Object Reference (IDOR) vulnerability combined with authentication bypass in the BCM Messenger Android app's attachment download endpoint. By intercepting traffic, modifying predictable numeric IDs, and removing authorization headers, an attacker can download sensitive media from private conversations belonging to any user.

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
    A[Intercept App Traffic] --> B[Send and Capture Attachment]
    B --> C[Identify Download Endpoint]
    C --> D[Modify ID for IDOR]
    D --> E[Bypass Auth and Download]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Android device running BCM Messenger app
- Web endpoint: ameim.bs2dl.yy.com (attachments service)
- No specific ports required; uses HTTPS (443)
- Network access: Attacker must be able to proxy traffic from their Android device

### Initial Access Requirements

- Installed BCM Messenger app on attacker's and victim's Android devices
- Accounts on the app for sending/receiving attachments
- Rooted or proxy-configured Android device for traffic interception
- No prior credentials needed beyond app login for initial capture

## Detailed Attack Procedures

### Step 1: Intercept App Traffic with Burp Suite
procedure: [[procedures/Intercept-App-Traffic-with-Burp-Suite]]

**Objective**: Set up traffic interception to monitor HTTP requests from the BCM Messenger Android app.

**Instructions**: Configure Burp Suite as a proxy on the attacker's machine and set the Android device's Wi-Fi proxy to point to Burp's listener (default: 127.0.0.1:8080). Install Burp's CA certificate on the Android device to handle HTTPS traffic.

**Expected Output**: All app traffic visible in Burp's Proxy history.

**Success Indicators**:
- App requests appear in Burp without errors
- HTTPS interception works for the app's endpoints

### Step 2: Send and Capture Attachment Request
procedure: [[procedures/Send-and-Capture-Attachment-Request]]

**Objective**: Upload and send an attachment between accounts to generate a traceable request.

**Instructions**: Use the BCM Messenger app to send an attachment (e.g., image) from the victim's account to the attacker's account. Monitor the upload request in Burp Proxy to note the generated numeric ID (e.g., 938540538).

**Expected Output**: HTTP POST request to upload endpoint, followed by a response containing the attachment ID.

**Success Indicators**:
- Attachment sent successfully in app
- ID captured in Burp (e.g., /attachments/938540538)

### Step 3: Identify Attachment Download Endpoint
procedure: [[procedures/Identify-Attachment-Download-Endpoint]]

**Objective**: Locate the download request in intercepted traffic to understand the endpoint structure.

**Instructions**: In Burp Proxy history, filter for GET requests to /attachments/{ID}. Note headers like X-Signal-Agent: OWA and Host: ameim.bs2dl.yy.com.

**Expected Output**: GET /attachments/938540538 request logged with response serving the file.

**Success Indicators**:
- Download endpoint identified
- Request format confirmed (GET /attachments/{numeric ID})

### Step 4: Modify ID for IDOR Exploitation
procedure: [[procedures/Modify-ID-for-IDOR-Exploitation]]

**Objective**: Alter the ID parameter to access attachments from other users via predictable numbering.

**Instructions**: Send the captured request to Burp Repeater, change the ID (e.g., from 938540538 to 359912920), and replay. Brute-force nearby IDs if needed to find valid ones.

**Expected Output**: Server responds with a different attachment file.

**Success Indicators**:
- Unauthorized attachment downloaded
- No 404 or access denied errors

### Step 5: Bypass Authentication to Download Attachments
procedure: [[procedures/Bypass-Authentication-to-Download-Attachments]]

**Objective**: Remove authorization to enable anonymous access to any attachment.

**Instructions**: In Burp Repeater, delete the Authorization header from the modified request and replay. The endpoint serves the file without requiring credentials.

**Expected Output**: Attachment content returned without authentication.

**Success Indicators**:
- Download succeeds without Authorization header
- Sensitive files from private chats accessible anonymously

## Attack Chain Summary

### Key Achievements

1. Intercepted and analyzed app traffic to discover vulnerable endpoint
2. Exploited IDOR by modifying predictable numeric IDs to access other users' attachments
3. Bypassed authentication entirely, allowing anonymous file downloads

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access

---
*Last updated: 2023-10-01T00:00:00Z*
