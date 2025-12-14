---
id: proc-mirror-sync
tags:
  - mirroring
  - synchronization
  - uber
  - archive.uber.com
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:08.181Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Wait-for-Uber-PyPI-Mirror-Synchronization

## Summary

This procedure involves monitoring and waiting for Uber's automated PyPI mirroring process to sync the malicious package, generating an HTML page that unsafely renders the XSS payload as clickable links.

## Description

Uber's archive.uber.com periodically mirrors packages from PyPI, fetching metadata and rendering fields like home_page and download_url directly into <a href> tags without URI validation or escaping. This step is passive, relying on the target's infrastructure. Once synced, the page becomes a persistent XSS vector. No direct interaction is needed beyond initial upload; timing depends on Uber's sync schedule, typically minutes to hours.

## Requirements

1. Package already uploaded to PyPI
2. Knowledge of target mirror URL structure
3. Browser for verification

## Defense

Defensive measures and detection strategies:

- Implement URL sanitization in mirroring scripts to strip or validate schemes
- Use HTML entity encoding for metadata in generated pages
- Log and alert on new mirrored packages with suspicious metadata

## Objectives

1. Leverage automated mirroring for payload propagation
2. Create persistent XSS entry point on mirror site
3. Exploit lack of sanitization in HTML generation

## Instructions

### Step 1: Monitor PyPI Status

**Context**: Confirm package visibility on PyPI before checking mirror.

Visit https://pypi.org/project/ignore-me/ to verify upload.

> Ensure metadata shows the injected fields.

### Step 2: Check Mirror Page

**Context**: Poll the Uber mirror URL until the package appears.

Navigate to http://archive.uber.com/pypi/simple/ignore-me-1.0/ and refresh periodically.

> Once loaded, inspect source for <a href='Javascript:alert(0)'> links confirming unsafe rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- mirroring
- synchronization
- passive
