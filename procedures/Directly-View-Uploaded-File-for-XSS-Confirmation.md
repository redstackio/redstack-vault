---
tags:
  - xss-poc
  - file-view
  - sharepoint
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 93da818c-9768-415b-a7b1-1026636ca913
created_at: '2025-12-13T23:56:19.955Z'
updated_at: '2025-12-13T23:56:19.955Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Directly-View-Uploaded-File-for-XSS-Confirmation

## Summary

This procedure confirms the stored XSS by directly accessing the uploaded malicious file's URL, simulating a victim loading the asset independently of the blog post.

## Description

In SharePoint environments, uploaded files to blog photo lists can be accessed via direct URLs, bypassing post rendering but still executing embedded JavaScript due to poor sanitization. This PoC step verifies persistence and executability of the payload, highlighting risks for any user viewing shared assets. It requires login for access and demonstrates classic stored XSS impact.

## Requirements

1. Authenticated session (login credentials)
2. Known URL of the uploaded file (e.g., in /Blog/Lists/Photos/)
3. Web browser for direct navigation

## Defense

Defensive measures and detection strategies:

- Block direct access to uploaded files or serve them with no-sniff headers
- Validate and neutralize scripts in all file types (HTML, SVG) before storage
- Monitor access logs for direct file views from unauthorized users

## Objectives

1. Execute XSS payload via direct file load
2. Confirm vulnerability persistence outside post context
3. Validate PoC for reporting or remediation

## Instructions

### Step 1: Log In to Site

**Context**: Ensure authenticated access to protected file paths.

Navigate to https://████████/ _login/default.aspx?ReturnUrl=%2f _layouts%2f15%2fauthenticate.aspx%3fsource%3d%2fConference&source=/Conference and log in with credentials.

> Successful authentication grants access to profile and file lists.

### Step 2: Navigate to File URL

**Context**: Directly load the malicious file to trigger execution.

Go to https://██████/Profiles/My/alobaloss/Blog/Lists/Photos/evilsvgfile.svg (adjust path as needed for the uploaded file).

> The browser renders the file, executing the embedded JavaScript like alert('XSS').

### Step 3: Observe Payload Execution

**Context**: Verify the XSS alert or behavior.

Watch for the alert popup upon loading.

> Alert confirms successful stored XSS; no alert indicates potential mitigation or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-poc]]
- [[file-view]]
- [[Sharepoint]]
