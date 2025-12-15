---
id: proc-uuid-4
name: Trigger PDF Regeneration to Execute SSRF
tags:
  - ssrf
  - exfiltration
  - aws
  - credentials
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
updated_at: '2025-12-14T17:28:28.640Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Credentials In Files]]'
---
# Trigger PDF Regeneration to Execute SSRF

## Summary

This procedure refreshes the generated PDF URL after payload injection, causing the FAST server to re-process the tainted session data, execute the injected JavaScript server-side, and fetch AWS metadata via SSRF. The credentials are then visible in the PDF content or network traces.

## Description

PDF generation in FAST involves server-side rendering of HTML/JS from the saved session. Refreshing forces re-fetch of data, executing the iframe src to the metadata service. The response (JSON with AccessKeyId, etc.) embeds in the PDF, allowing exfiltration. Monitor with Burp or browser dev tools.

## Requirements

1. Modified session saved via /api/save/
2. Original PDF URL with session ID
3. Tools to inspect PDF content or network (Burp, browser inspector)

## Defense

Defensive measures and detection strategies:

- Isolate app servers from metadata services using VPC security groups
- Audit PDF generation logs for internal URL requests
- Implement content security policies (CSP) to block iframe src to internal endpoints

## Objectives

1. Force server-side re-execution of injected code
2. Observe SSRF request and credential leak
3. Validate impact by extracting AWS tokens

## Instructions

### Step 1: Refresh PDF URL

**Context**: Reload to trigger regeneration and script execution.

In browser, refresh https://target.example.com/print/checklist/fast_session_XXXXXX.pdf.

> Server re-queries /api/save/ data, processes JS, makes SSRF request.

### Step 2: Inspect Output for Credentials

**Context**: Check rendered PDF or intercepted traffic for metadata response.

View PDF source or Burp Repeater/Proxy for the iframe fetch to 169.254.169.254.

> Expect JSON: {"AccessKeyId": "...", "SecretAccessKey": "...", "Token": "..."}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Credentials In Files]] Credentials In Files

### Sub-Techniques

-

## Commands Used

-

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- ssrf
- exfiltration
- aws
- credentials
