---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - recon
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T05:32:13.468Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-File-Upload-Endpoint

## Summary

This procedure involves reconnaissance to locate file upload endpoints in a web application, focusing on identifying vulnerable upload functionalities without proper validation, as seen in the Starbucks job portal.

## Description

In web applications, file upload features are common entry points for attacks. This procedure details inspecting network traffic and application behavior to pinpoint the exact endpoint, parameters, and any initial validation mechanisms. For the target ecjobsdc.starbucks.com.cn, the upload is handled via an ASP.NET endpoint lacking strict extension checks, allowing preparation for malicious uploads.

## Requirements

1. Access to the target web application over HTTP/HTTPS
2. Web browser with developer tools or a proxy like Burp Suite
3. Basic knowledge of HTTP requests and form handling

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor upload requests
- Log all file upload attempts and scan for anomalous extensions
- Use client-side and server-side validation with allowlists for file types

## Objectives

1. Discover the upload endpoint URL and parameters
2. Understand the request format (e.g., multipart/form-data)
3. Identify potential bypass opportunities like extension manipulation

## Instructions

### Step 1: Monitor Application Interactions

**Context**: Use browser developer tools to capture network requests during normal file upload attempts.

Navigate to the job portal upload form and attempt a benign upload while intercepting traffic.

**Expected Output**: Captured POST request to /recruitjob/hxpublic_v6/hxinterface6.aspx?_hxcategory=hx_filebox_upload_file with parameter hxwebfileboxcontrol_upload_file_inputbox.

### Step 2: Analyze Request Structure

**Context**: Examine the Content-Type and form-data boundaries to understand how to replicate the request.

Review headers like Content-Type: multipart/form-data; boundary=----WebKitFormBoundary... and filename handling.

**Expected Output**: Insight into modifiable elements like filename suffix for bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web-vuln]]
