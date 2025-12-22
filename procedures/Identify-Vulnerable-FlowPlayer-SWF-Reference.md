---
id: proc-identify-swf
tags:
  - vulnerability-identification
  - flash
  - swf
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
  - '[[Hardware]]'
updated_at: '2025-12-14T03:47:18.644Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify Vulnerable FlowPlayer SWF Reference

## Summary

This procedure focuses on parsing cache manifest files or similar assets to locate references to outdated FlowPlayer SWF files, confirming vulnerability to Flash XSS via remote file inclusion.

## Description

Cache manifests like motd2.manifest list web app assets, including embeddable Flash content. Accessing http://templ4d2.pinion.gg/motd2.manifest reveals http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf. Version 3.2.15 is known vulnerable due to improper handling of the 'config' parameter with ExternalInterface.Call, allowing client-side RFI. This step requires verifying the version against CVE databases or prior knowledge. Outcomes include the exact SWF URL for exploitation.

## Requirements

1. Access to the manifest file URL
2. Knowledge of FlowPlayer vulnerabilities (e.g., version 3.2.15 flaws)
3. Browser to fetch and parse file contents

## Defense

Defensive measures and detection strategies:

- Update all Flash-based libraries to latest versions or migrate to HTML5
- Scan for outdated SWF files in asset inventories
- Block or monitor requests to known vulnerable SWF endpoints

## Objectives

1. Locate SWF references in asset lists
2. Confirm vulnerability based on version
3. Prepare for RFI exploitation

## Instructions

### Step 1: Access Cache Manifest

**Context**: Fetch the manifest file to review listed resources.

Navigate to http://templ4d2.pinion.gg/motd2.manifest in a browser.

> The file contents will display a list of assets, including SWF paths.

### Step 2: Verify SWF Vulnerability

**Context**: Cross-reference the SWF version with known issues.

Check the URL http://bin.pinion.gg/bin/flowplayer.commercial-3.2.15.swf for version 3.2.15.

> Confirm flaws in ExternalInterface.Call allowing RFI via 'config'.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Hardware

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[flash]]
- [[swf]]
