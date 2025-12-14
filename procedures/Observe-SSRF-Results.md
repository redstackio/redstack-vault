---
id: proc-slack-observe-results
tags:
  - ssrf
  - observation
  - banner-grab
  - scanning
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/php-redirect-ipv6-internal]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T03:46:14.467Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Observe-SSRF-Results

## Summary

This procedure analyzes the responses from invoked slash commands to capture internal service banners and perform port scanning via repeated SSRF triggers.

## Description

Post-invocation, the Slack response reveals internal data like SSH or SMTP banners, confirming the SSRF. Adjust PHP redirects for different ports to scan internals. Target: Slack responses. Outcomes: Service versions and potential further access points identified.

## Requirements

1. Successful slash command invocation
2. Access to modify PHP script for port variations
3. Logging on attacker server for request verification

## Defense

Defensive measures and detection strategies:

- Sanitize and filter SSRF responses before returning to users
- Monitor for anomalous internal connections from Slack IPs
- Implement content security policies on responses

## Objectives

1. Extract and interpret internal service information
2. Conduct port scanning through multiple invocations
3. Assess impact for further exploitation

## Instructions

### Step 1: Review Initial Response

**Context**: Check for SSH banner on port 22.

Examine the slash command output in Slack for text like "SSH-2.0-OpenSSH".

> Banner confirms access to [::]:22.

### Step 2: Modify for Other Ports

**Context**: Scan additional services like SMTP.

Update index.php with [[commands/php-redirect-ipv6-internal]] adjusted to http://[::]:25/, re-invoke /yourslash, and observe.

```php
<?php header("Location: http://[::]:25/"); ?>
```

> Response shows SMTP greeting, e.g., "220 smtp.example.com ESMTP".

### Step 3: Log and Analyze

**Context**: Document findings for reconnaissance.

Record banners and ports; repeat for other targets (e.g., 80, 443) to map internals.

> Comprehensive scan results compiled.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/php-redirect-ipv6-internal]]

## Tools Used


## Tags

- [[ssrf]]
- [[observation]]
- [[banner-grab]]
- [[scanning]]
