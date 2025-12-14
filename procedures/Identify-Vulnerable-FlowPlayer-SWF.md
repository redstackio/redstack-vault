---
id: proc-uuid-identify-swf
tags:
  - vulnerability-identification
  - flash
  - flowplayer
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Flash
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:17.690Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Identify-Vulnerable-FlowPlayer-SWF

## Summary

This procedure verifies the version and known vulnerabilities of a FlowPlayer SWF file identified during reconnaissance, confirming susceptibility to XSS via remote file inclusion in the 'config' parameter.

## Description

Outdated Flash components like FlowPlayer 3.2.15 are prone to RFI attacks where the SWF loads external configuration files without validation, allowing JavaScript injection via ExternalInterface. This step involves accessing the SWF endpoint and cross-referencing with vulnerability reports (e.g., GitHub issues) to assess exploitability. Prerequisites include the SWF URL from prior recon.

## Requirements

1. SWF URL from manifest (e.g., http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf)
2. Access to vulnerability databases or GitHub
3. Browser with Flash support for testing

## Defense

Defensive measures and detection strategies:

- Update all Flash/SWF files to latest versions or remove Flash entirely
- Implement content security policies (CSP) blocking external loads
- Monitor SWF accesses for anomalous query parameters

## Objectives

1. Confirm SWF version as vulnerable (3.2.15)
2. Document RFI via 'config' parameter
3. Prepare for payload hosting

## Instructions

### Step 1: Access and Inspect SWF

**Context**: Retrieve the SWF file to check its version.

Visit http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf in a browser or use curl to download.

> Look for version strings in file metadata or headers.

### Step 2: Research Vulnerability

**Context**: Validate known issues with the version.

Search for "FlowPlayer 3.2.15 XSS" on GitHub or CVE databases.

> Expected: Confirmation of RFI allowing JS execution without host validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[vulnerability-scanning]]
- [[flash-xss]]
