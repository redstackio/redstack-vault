---
tags:
  - lfi
  - libreoffice
  - file-craft
  - cve-2019-17400
type: procedure
tools:
  - '[[tools/LibreOffice]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[T1203.001]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 880c99ec-72cf-435d-81f3-1eacce399c0c
created_at: '2025-12-14T03:46:14.559Z'
updated_at: '2025-12-14T03:46:14.559Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1203.001]]'
---
# Craft-Malicious-Office-File-for-LibreOffice-LFI

## Summary

This procedure involves creating a specially crafted Office document that exploits a local file inclusion vulnerability in LibreOffice (CVE-2019-17400), enabling arbitrary local file access when processed by unoconv during thumbnail generation in environments like Slack.

## Description

The vulnerability stems from weaknesses in LibreOffice's handling of Office file structures and the unoconv library's conversion process, allowing malicious embeddings to trigger LFI. Attackers craft the file to include paths that reference sensitive local files, such as AWS metadata, upon processing. This is a preparation step for file upload attacks targeting preview features, requiring knowledge of Office file formats and the specific CVE. Expected outcome is a benign-appearing file that executes the exploit server-side without user interaction.

## Requirements

1. Access to an Office file editor (e.g., LibreOffice or hex editor for binary manipulation)
2. Understanding of CVE-2019-17400 details from vulnerability disclosures
3. Target environment using LibreOffice for file previews

## Defense

Defensive measures and detection strategies:

- Validate and sandbox file processing with restricted file system access
- Use updated LibreOffice versions post-CVE-2019-17400 patch
- Scan uploads for anomalous Office structures using antivirus or custom sigs

## Objectives

1. Generate a functional exploit file for LFI
2. Ensure compatibility with target processing pipeline
3. Minimize detection during upload

## Instructions

### Step 1: Analyze Vulnerability Path

**Context**: Review CVE-2019-17400 to identify exploitable elements in LibreOffice/unoconv, focusing on how crafted OLE objects or streams enable LFI.

Consult public PoC or disclosure for file structure modifications targeting local paths.

### Step 2: Modify Office File Structure

**Context**: Open a base Office template (e.g., .docx) and embed malicious content to exploit the conversion flaw.

Use a hex editor or Office macro tools to inject references to local files, such as `/proc/self/environ` or AWS metadata endpoints, leveraging unoconv's weak input sanitization.

### Step 3: Validate Crafted File

**Context**: Test the file locally with LibreOffice to ensure it triggers without crashing, confirming the LFI payload.

Process the file via command-line LibreOffice conversion and check for file read attempts in logs or outputs.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1203.001]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/LibreOffice]]

## Tags

- [[lfi]]
- [[tools/LibreOffice]]
- [[cve-2019-17400]]
