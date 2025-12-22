---
tags:
  - ssrf
  - ios
  - nextcloud
  - file-disclosure
  - javascript-execution
type: attack_chain
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
verified: false
platforms:
  - iOS
  - Mobile
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Upload-Proof-of-Concept-File-to-Nextcloud-iOS]]'
  - '[[procedures/Discover-Application-Path-via-JavaScript-in-Uploaded-HTML]]'
  - '[[procedures/Access-Manipulated-HTML-to-Reveal-App-Path]]'
  - '[[procedures/Upload-HTML-with-Iframe-for-Local-File-SSRF]]'
  - '[[procedures/Access-HTML-to-Disclose-Local-File-Content]]'
step_count: 5
techniques:
  - '[[JavaScript]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:24:40.126Z'
description: >-
  A multi-stage attack exploiting SSRF in the Nextcloud iOS app's local storage
  feature to disclose arbitrary local files by uploading HTML files that execute
  JavaScript and load file:// resources.
skill_level: intermediate
impact_level: high
id: ee23a406-d373-4392-a8fb-80ed76b99e96
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Data from Local System]]'
---
# SSRF via Manipulated HTML Uploads in Nextcloud iOS App for Local File Disclosure

Multi-stage attack chain demonstrating exploitation of a Server-Side Request Forgery (SSRF) vulnerability in the local storage feature of the Nextcloud iOS mobile app. The attack allows arbitrary local file disclosure using the file:// protocol by uploading manipulated HTML files that execute JavaScript to reveal the application path and embed iframes to load sensitive local files, which are then viewed through the app's file viewer. This leads to exposure of any local documents or system files on the device.

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
    A[Upload Proof File] --> B[Upload HTML to Discover Path]
    B --> C[Access HTML to Reveal Path]
    C --> D[Upload Iframe HTML for SSRF]
    D --> E[Access HTML to Disclose Local File]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#f39c12
    style D fill:#3498db
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- Nextcloud iOS mobile app installed on an iOS device
- Access to the app's local storage upload feature

### Target Environment

- iOS platform
- Nextcloud iOS app (vulnerable version with unsanitized file upload and viewing)
- Local file system access via file:// protocol
- No specific ports or network services required; attack is client-side on the device

### Initial Access Requirements

- Valid user account in Nextcloud app for file upload
- Physical or authorized access to the iOS device
- No prior network position needed; exploits local app behavior

## Detailed Attack Procedures

### Step 1: Upload Proof of Concept File
procedure: [[procedures/Upload-Proof-of-Concept-File-to-Nextcloud-iOS]]

**Objective**: Demonstrate basic interaction with the local storage by uploading a simple text file to confirm upload capability.

**Instructions**: Use the Nextcloud iOS app to upload a text file named 'ssrfpoc.txt' containing the content 'test ssrf'. This serves as a target file for later SSRF exploitation.

**Expected Output**: File successfully uploaded and visible in the app's local storage viewer.

**Success Indicators**:
- File 'ssrfpoc.txt' appears in the file list
- Content 'test ssrf' can be viewed without errors

### Step 2: Discover Application Path
procedure: [[procedures/Discover-Application-Path-via-JavaScript-in-Uploaded-HTML]]

**Objective**: Upload a manipulated file disguised as a common type but containing HTML with JavaScript to execute and disclose the current application path.

**Instructions**: Create a file (e.g., originally a .txt or .doc) and modify its content to HTML format, embedding the payload `<svg/onload=document.write(document.location)>`. Change the extension to .html if needed, then upload it via the app's local storage feature.

**Expected Output**: File uploaded successfully, ready for viewing to trigger the JavaScript.

**Success Indicators**:
- Manipulated HTML file listed in storage
- No upload rejection due to content type

### Step 3: Reveal Application Path
procedure: [[procedures/Access-Manipulated-HTML-to-Reveal-App-Path]]

**Objective**: View the uploaded HTML file in the app to execute the JavaScript payload and obtain the full application path for subsequent SSRF targeting.

**Instructions**: Open the uploaded HTML file using the app's built-in file viewer. The JavaScript will automatically execute, writing the current document location (app path) to the page.

**Expected Output**: The viewer displays the application path, e.g., 'file:///private/var/mobile/Containers/Data/Application/[APP-ID]/Documents/'.

**Success Indicators**:
- JavaScript executes without blocking
- Full local path to the app's directory is visible in the viewer

### Step 4: Upload Iframe for SSRF
procedure: [[procedures/Upload-HTML-with-Iframe-for-Local-File-SSRF]]

**Objective**: Upload a second manipulated HTML file containing an iframe that references the proof file using the discovered path and file:// protocol to enable SSRF-based local file loading.

**Instructions**: Prepare another file as HTML with the payload `<iframe src="file://[DISCOVERED-PATH]/ssrfpoc.txt" width="400" height="400"></iframe>`, replacing [DISCOVERED-PATH] with the path from Step 3. Upload it to local storage.

**Expected Output**: HTML file uploaded and listed, with no sanitization errors.

**Success Indicators**:
- File upload completes
- Iframe payload is intact in the file content

### Step 5: Disclose Local File Content
procedure: [[procedures/Access-HTML-to-Disclose-Local-File-Content]]

**Objective**: View the second HTML file to trigger the iframe, loading and displaying the content of the target local file via SSRF.

**Instructions**: Open the uploaded iframe HTML file in the app's viewer. The iframe will fetch and render the 'ssrfpoc.txt' content from the local path.

**Expected Output**: The iframe displays 'test ssrf' from the proof file, confirming successful local file disclosure.

**Success Indicators**:
- Iframe loads without protocol blocking
- Content of 'ssrfpoc.txt' is visible within the iframe
- No app crashes or security prompts

## Attack Chain Summary

### Key Achievements

1. Confirmed local file upload capability in Nextcloud iOS app
2. Bypassed content sanitization to execute JavaScript in uploaded HTML
3. Discovered sensitive application path via client-side execution
4. Exploited SSRF with file:// iframes to read arbitrary local files
5. Achieved disclosure of local documents, enabling broader data exposure on the device

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Data from Local System]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
