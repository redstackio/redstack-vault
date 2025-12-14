---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - xss
  - trigger
  - media-list
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.939Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-WordPress-Media-List

## Summary

This procedure triggers the stored XSS by viewing the WordPress media library as an administrator, executing the JavaScript payload from the malicious filename.

## Description

Once uploaded, the filename is output unescaped in the media list table via echo wp_basename($file) in <p class="filename">, allowing HTML/JS injection. Also triggers on attachment pages (?attachment_id=ID) in vulnerable themes. Leads to alert() or more advanced payloads like cookie theft.

## Requirements

1. Admin or viewer access to dashboard
2. Uploaded malicious attachment
3. Vulnerable WordPress core (pre-esc_html fix)

## Defense

Defensive measures and detection strategies:

- Update to patched WordPress version
- Use security plugins to escape outputs
- Monitor JS errors or unexpected alerts in browser console

## Objectives

1. Load media list to execute payload
2. Compromise viewer session (e.g., steal admin cookies)
3. Demonstrate impact on attachment pages

## Instructions

### Step 1: Access Media List

**Context**: Log in as admin and navigate to view the unescaped filename.

**Command** (Browser navigation):
No command; go to https://wordpress.site/wp-admin/upload.php (list mode default).

> Filename renders as <p class="filename">ccc'><img src=x onerror=alert('xss') onload=alert('xss')></p>, executing on load. Expected: JS alert pops. For attachment page: https://wordpress.site/?attachment_id=POST_ID.

### Step 2: Verify Execution

**Context**: Check browser console for errors or use dev tools to inspect payload.

> Success if alert fires; extend payload for exfil (e.g., fetch to attacker server).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- wordpress
- media
