---
id: proc-wordpress-version-recon
tags:
  - reconnaissance
  - wordpress
  - version-detection
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-generator-header]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T17:32:10.974Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Reconnaissance-of-WordPress-Version

## Summary

This procedure identifies the WordPress version on a target website to confirm vulnerabilities like those in 4.6.2, enabling further exploitation such as information disclosure or XSS.

## Description

In an attack scenario targeting public websites like Nextcloud's, reconnaissance involves checking HTTP headers, source code, or using online tools to detect the CMS version. For WordPress 4.6.2, this reveals exposure to CVEs in WPVulnDB, including REST API leaks and theme upload flaws. Prerequisites include public access to the site; outcomes include version confirmation for targeted attacks.

## Requirements

1. Internet access to the target URL
2. Basic knowledge of HTTP headers and vulnerability databases like WPVulnDB
3. Tools like curl or browser inspector

## Defense

Defensive measures and detection strategies:

- Update WordPress regularly to patch known vulnerabilities
- Remove version info from generator meta tags and headers
- Monitor for unusual reconnaissance traffic via WAF logs

## Objectives

1. Confirm WordPress 4.6.2 or similar outdated version
2. Cross-reference with WPVulnDB for exploitable issues
3. Prepare for targeted exploitation

## Instructions

### Step 1: Check HTTP Headers for Generator

**Context**: WordPress often exposes its version in the X-Generator header.

**Command** ([[commands/curl-generator-header]]):
```bash
curl -I https://target.com | grep -i generator
```

> This command fetches headers and filters for the generator string, e.g., "WordPress 4.6.2". Expected output: Version confirmation if present.

### Step 2: Inspect Source Code

**Context**: View page source for meta generator tag.

**Command** ([[commands/curl-page-source]]):
```bash
curl -s https://target.com | grep -i 'generator.*wordpress'
```

> Extracts the meta tag like <meta name="generator" content="WordPress 4.6.2">. Success if version matches vulnerable one.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used

- [[commands/curl-generator-header]]
- [[commands/curl-page-source]]

## Tools Used


## Tags

- [[Reconnaissance]]
- [[wordpress]]
