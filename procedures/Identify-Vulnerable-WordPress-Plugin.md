---
tags:
  - recon
  - wordpress
  - plugin-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - WordPress
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 2dbed3eb-e86c-4d3a-8dcb-75d6dc67d389
created_at: '2025-12-14T00:11:25.152Z'
updated_at: '2025-12-14T00:11:25.152Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable WordPress Plugin

## Summary

This procedure involves reconnaissance to detect outdated and vulnerable plugins like Formidable Forms on a WordPress site, setting the stage for further exploitation.

## Description

In this attack scenario, the target is a WordPress installation with public-facing forms. The procedure scans for plugin versions and cross-references with known vulnerabilities, such as those in Formidable Forms that enable XSS and data exposure. Expected outcomes include confirmation of exploitability without authentication.

## Requirements

1. Network access to the target website
2. Knowledge of common WordPress plugin structures
3. Access to vulnerability databases like CVE or advisory links

## Defense

Defensive measures and detection strategies:

- Regularly update plugins to patched versions
- Monitor for unusual plugin version queries or scans

## Objectives

1. Detect presence of Formidable Forms plugin
2. Confirm outdated version vulnerable to XSS
3. Identify potential attack vectors

## Instructions

### Step 1: Scan for Plugins

**Context**: Inspect the site's source code or use browser tools to identify installed plugins.

> View page source and search for plugin-specific paths like /wp-content/plugins/formidable/.

### Step 2: Check Version Against Vulnerabilities

**Context**: Compare detected version with known issues.

> Reference advisories like https://klikki.fi/adv/formidable.html to confirm root cause.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- recon
- wordpress
