---
id: proc-slack-phishing-upload
tags:
  - phishing
  - credential-theft
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/slack-upload-binary-html-redirect]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[T1566.001]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:24:27.321Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[T1566.001]]'
  - '[[JavaScript]]'
---
# Upload-Phishing-HTML-for-Credential-Theft

## Summary

This procedure uploads an HTML file mimicking a Slack login page, disguised with binary prefix, to host phishing content via public links for stealing credentials.

## Description

Similar to initial upload but with HTML form that posts credentials to an attacker server; shared links trick users into submitting data, enabling theft or further attacks.

## Requirements

1. Slack token and channel access
2. Attacker-controlled server for credential collection

## Defense

- Content security policies on file previews
- User training on suspicious links
- Monitor for fake login pages in shares

## Objectives

1. Host convincing phishing page
2. Capture submitted credentials
3. Distribute via public links

## Instructions

### Step 1: Craft Phishing HTML

**Context**: Create HTML with fake Slack login form posting to evil.com.

Include binary prefix to bypass sanitization.

### Step 2: Upload and Share

**Context**: Use upload command, then generate public link.

**Command** ([[commands/slack-upload-binary-html-redirect]]):
```bash
curl -X POST https://upload.slack.com/api/files.uploadAsync \
  # (similar to initial upload but with phishing HTML content)
```

> Response includes file ID; create link like https://slack.com/files-pri/T1ARLSGBS-F1AVC33M5/login?pub_secret=e80f120635.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[T1566.001]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/slack-upload-binary-html-redirect]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- phishing
- slack
