---
id: proc-identify-version-001
tags:
  - reconnaissance
  - wordpress
  - vulnerability
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Software]]'
updated_at: '2025-12-14T03:15:47.261Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Software]]'
---
# Identify-Vulnerable-Plugin-Versions

## Summary

This procedure confirms whether an identified WordPress plugin version is vulnerable by comparing it against known release notes and security advisories, focusing on outdated versions like Yoast SEO v2.1.1.

## Description

Attackers use this to validate reconnaissance findings by checking plugin changelogs or official documentation for security patches. In the context of Uber's people.uber.com, v2.1.1 was found to lack fixes for XSS issues. The target is WordPress installations; outcomes include flagging exploitable versions. Requires internet access for documentation lookup.

## Requirements

1. Extracted plugin version from source code
2. Access to WordPress plugin repositories or changelogs
3. Basic knowledge of version comparison

## Defense

Defensive measures and detection strategies:

- Regularly update plugins to latest versions
- Disable version disclosure in plugin outputs
- Monitor for reconnaissance scans via web logs

## Objectives

1. Compare plugin version to patched releases
2. Determine vulnerability status
3. Document potential risks

## Instructions

### Step 1: Check Plugin Changelog

**Context**: Visit the official plugin page to review version history and identify if the current version predates security fixes.

For Yoast SEO, browse https://yoast.com/wordpress/plugins/seo/ and note that v2.1.1 (from 2013) is vulnerable to XSS before later patches.

> Expected output: Confirmation that v2.1.1 has known issues, such as improper sanitization leading to XSS.

### Step 2: Cross-Reference with Security Resources

**Context**: Use internal notes or quick searches to flag the version.

Manually note: Yoast v2.1.1 matches vulnerable releases documented in public DBs.

> Successful execution yields a list of associated risks, like arbitrary JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Software]] Software

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[wordpress]]
- [[vulnerability]]
