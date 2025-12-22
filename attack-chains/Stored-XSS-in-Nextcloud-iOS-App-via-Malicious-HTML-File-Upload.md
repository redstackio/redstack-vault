---
tags:
  - xss
  - stored-xss
  - nextcloud
  - ios
  - mobile
  - file-upload
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - iOS
  - Web
submitted: true
complexity: medium
created_at: '2024-09-18T00:00:00Z'
procedures:
  - '[[procedures/Upload-Malicious-HTML-File-to-Nextcloud]]'
  - '[[procedures/Share-Malicious-File-with-Victim]]'
  - '[[procedures/Trigger-XSS-Execution-in-iOS-App]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T03:16:25.159Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in the Nextcloud
  iOS app by uploading and sharing a malicious HTML file that executes
  JavaScript when opened by the victim.
skill_level: intermediate
impact_level: high
id: a6fda906-9a8a-4540-b484-13e2f0613062
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Stored XSS in Nextcloud iOS App via Malicious HTML File Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting improper HTML rendering in the Nextcloud iOS app.

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
    A[Upload Malicious HTML] --> B[Share File with Victim]
    B --> C[Victim Opens in iOS App]
    C --> D[JavaScript Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses built-in Nextcloud web interface and sharing features)

### Target Environment

- Nextcloud server with file upload and sharing enabled
- Nextcloud iOS app installed on victim's device
- Web browser for uploading files

### Initial Access Requirements

- Valid Nextcloud account with upload permissions
- Ability to share files with target users
- No prior network access beyond standard Nextcloud login

## Detailed Attack Procedures

### Step 1: Upload Malicious HTML File
procedure: [[procedures/Upload-Malicious-HTML-File-to-Nextcloud]]

**Objective**: Upload an HTML file containing a JavaScript payload to the Nextcloud server, which will be stored and later rendered unsafely in the iOS app.

**Instructions**: Create an HTML file with an embedded XSS payload, such as an anchor tag linking to a data URI that decodes to JavaScript code. For example, use a payload like `<a href="data:text/html;base64,PHNjcmlwdD5hbGVydCgiWFNTIik8L3NjcmlwdD4=">hack</a>`, which base64-decodes to an HTML snippet with `<script>alert("XSS")</script>`. Then, log in to the Nextcloud web interface, navigate to the file upload section, and upload the file.

**Expected Output**: The file appears in your Nextcloud file list without rendering the HTML on the web interface.

**Success Indicators**:
- File uploaded successfully
- No immediate JavaScript execution on web or Android clients

### Step 2: Share the Malicious File with the Victim
procedure: [[procedures/Share-Malicious-File-with-Victim]]

**Objective**: Distribute the uploaded malicious HTML file to the target user via Nextcloud's sharing feature, setting up the conditions for XSS execution.

**Instructions**: In the Nextcloud web interface, select the uploaded HTML file, use the sharing options to generate a share link or directly share with the victim's Nextcloud account. Ensure the share permissions allow the victim to view and open the file in the app.

**Expected Output**: Share link or notification sent to the victim, confirming access.

**Success Indicators**:
- Victim receives the share notification
- File is accessible via the victim's Nextcloud account

### Step 3: Trigger XSS Execution in iOS App
procedure: [[procedures/Trigger-XSS-Execution-in-iOS-App]]

**Objective**: Induce the victim to open the shared file in the Nextcloud iOS app, causing the app to render the HTML and execute the embedded JavaScript.

**Instructions**: The victim must open the shared file using the Nextcloud iOS app. Upon opening, the app's file viewer renders the HTML content without sanitization, executing the JavaScript payload, such as displaying an alert or rendering a fake login form to capture credentials.

**Expected Output**: JavaScript executes in the app's context, e.g., alert popup or form submission to attacker-controlled endpoint.

**Success Indicators**:
- Alert or other payload effects observed in the iOS app
- Potential credential theft if fake form is used

## Attack Chain Summary

### Key Achievements

1. Successful storage of malicious HTML in Nextcloud without detection on web/Android
2. Delivery of the payload via legitimate sharing features
3. Arbitrary JavaScript execution in the victim's iOS app context, enabling phishing or data exfiltration

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2024-09-18T00:00:00Z*
