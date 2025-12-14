---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Prepare-Malicious-Google-Drive-URL
tags:
  - ssrf
  - google-drive
  - url-crafting
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-prepare-gdrive-url]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:56.356Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Malicious-Google-Drive-URL

## Summary

This procedure involves creating and hosting a malicious file on Google Drive that redirects or proxies requests to internal endpoints, setting up the payload for an SSRF attack in applications like Shopify that fetch external URLs.

## Description

In the context of Shopify's Google Drive integration, the application fetches content from provided Google Drive URLs during file processing. By uploading an HTML file with JavaScript or meta redirects pointing to internal services like AWS metadata (169.254.169.254), an attacker can trick the server into making unauthorized internal requests. Prerequisites include a Google account for uploading files and ensuring the file is publicly shareable. Expected outcomes include a valid URL that triggers SSRF when processed by the target application.

## Requirements

1. Google Drive account with upload permissions
2. Basic knowledge of HTML redirects (e.g., <meta http-equiv="refresh" content="0; url=http://169.254.169.254/latest/meta-data/">)
3. Access to [[tools/curl]] for testing URL validity

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed URL domains in file integrations (e.g., block non-Google domains or internal IPs)
- Use network segmentation to prevent backend servers from accessing metadata services via SSRF
- Monitor API logs for unusual URL patterns or fetches to localhost/internal IPs

## Objectives

1. Generate a shareable Google Drive URL hosting malicious redirect content
2. Ensure the URL is fetchable without authentication
3. Test that the redirect targets sensitive internal endpoints like AWS metadata

## Instructions

### Step 1: Create and Upload Malicious File

**Context**: Prepare an HTML file that redirects to the AWS metadata service upon being fetched.

**Command** ([[commands/curl-prepare-gdrive-url]]):
```bash
curl -I "https://drive.google.com/uc?id=YOUR_FILE_ID&export=download"
```

> This command tests if the uploaded file is accessible. First, manually create the HTML file locally with redirect content, upload it to Google Drive, set sharing to 'Anyone with the link', and replace YOUR_FILE_ID with the actual ID from the share link. Expected output: HTTP 200 with content disposition for download.

### Step 2: Verify Redirect Functionality

**Context**: Confirm the file's redirect works when fetched, simulating server behavior.

**Command** ([[commands/curl-prepare-gdrive-url]]):
```bash
curl -L "https://drive.google.com/uc?id=YOUR_FILE_ID&export=download" -o test.html && cat test.html
```

> Fetch the file content and inspect it. The output should show the HTML with the embedded redirect to http://169.254.169.254. If the redirect is JavaScript-based, ensure it's executable in a server context.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-prepare-gdrive-url]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- google-drive
- url-crafting
