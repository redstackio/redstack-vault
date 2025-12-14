---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
tags:
  - xss
  - stored-xss
  - wordpress
  - xmlrpc
  - attachment-upload
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
  - PHP
  - WordPress
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Prepare-XMLRPC-Payload-for-Malicious-Attachment]]'
  - '[[procedures/Upload-Malicious-Attachment-via-XMLRPC]]'
  - '[[procedures/Trigger-XSS-in-WordPress-Media-List]]'
step_count: 3
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.951Z'
description: >-
  A multi-stage attack exploiting a stored XSS vulnerability in WordPress core
  by uploading an attachment with a malicious filename via XMLRPC, leading to
  JavaScript execution when admins view the media list or attachment pages.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# WordPress Stored XSS via Malicious Attachment Filename

Multi-stage attack chain demonstrating exploitation of a stored XSS vulnerability in WordPress core through unescaped attachment filenames in the media list and attachment pages.

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
    A[Prepare Payload] --> B[Upload Attachment]
    B --> C[Trigger XSS]
    C --> D[Execute JavaScript]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- WordPress installation (core vulnerable versions, e.g., pre-4.2.5)
- XMLRPC enabled
- Authenticated access to wp.newPost() via XMLRPC (e.g., contributor or higher role)
- Web browser for triggering

### Initial Access Requirements

- Valid WordPress credentials for XMLRPC API
- Network access to the WordPress site
- No prior admin access needed, but admin viewing triggers escalation

## Detailed Attack Procedures

### Step 1: Prepare Payload
procedure: [[procedures/Prepare-XMLRPC-Payload-for-Malicious-Attachment]]

**Objective**: Create an XML file with a wp.newPost() payload that sets a malicious filename containing an XSS payload as an attachment.

**Instructions**: Generate the XML payload file named xss.xml with the specified parameters, embedding the XSS in the file parameter.

**Expected Output**: A valid XML file ready for submission.

**Success Indicators**:
- XML file created without syntax errors
- Payload includes <img src=x onerror=alert('xss') onload=alert('xss')> in filename

### Step 2: Upload Attachment
procedure: [[procedures/Upload-Malicious-Attachment-via-XMLRPC]]

**Objective**: Send the XMLRPC request to create the attachment post with the malicious filename.

**Instructions**: Use [[commands/curl-xmlrpc-post-attachment]] to POST the XML to /xmlrpc.php:

```bash
curl 'https://wordpress.site/xmlrpc.php' --data-binary "\`cat xss.xml\`" -H 'Content-type: application/xml'
```

**Expected Output**: XMLRPC response confirming post creation, e.g., <int>123</int> for post ID.

**Success Indicators**:
- HTTP 200 response
- Attachment created in media library with malicious filename

### Step 3: Trigger XSS
procedure: [[procedures/Trigger-XSS-in-WordPress-Media-List]]

**Objective**: View the media list or attachment page as an admin to execute the stored XSS payload.

**Instructions**: Log in as administrator and navigate to Dashboard > Media in list mode.

**Expected Output**: JavaScript alert('xss') triggered on page load due to unescaped filename in <p class="filename">.

**Success Indicators**:
- Alert box appears
- Potential session compromise if payload exfiltrates cookies

## Attack Chain Summary

### Key Achievements

1. Successful upload of attachment with XSS payload via XMLRPC
2. Storage of malicious filename without escaping in WordPress core
3. Arbitrary JavaScript execution on admin dashboard views, enabling account compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]

### MITRE ATT&CK Tactics

- [[Execution]]

---

*Last updated: 2023-10-01T00:00:00Z*
