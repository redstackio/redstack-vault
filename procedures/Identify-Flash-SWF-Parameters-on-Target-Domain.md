---
tags:
  - recon
  - flash
  - swf
  - xss
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - Flash (SWF)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:47:18.438Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 86bbe0b3-255e-49d4-b667-16173ae882a3
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify Flash SWF Parameters on Target Domain

## Summary

This procedure involves inspecting a web application's source and network traffic to identify embedded Flash SWF files and their configurable parameters, focusing on those that allow HTML insertion for potential XSS exploitation.

## Description

In the context of legacy web applications like Imgur, Flash components such as swfupload.swf are used for file uploads. These often accept parameters like buttonText without proper sanitization, enabling reflected XSS. The procedure requires browser developer tools to examine page resources and confirm parameter behavior on the target domain (e.g., imgur.com).

## Requirements

1. Web browser with developer tools (e.g., Chrome DevTools)
2. Public access to the target website
3. Basic knowledge of Flash parameters and URL encoding

## Defense

Defensive measures and detection strategies:

- Migrate away from Flash to modern HTML5/JavaScript uploaders
- Implement Content Security Policy (CSP) to restrict script execution
- Sanitize all SWF parameters server-side

## Objectives

1. Locate vulnerable SWF files on the main domain
2. Document injectable parameters like buttonText
3. Prepare for payload injection

## Instructions

### Step 1: Inspect Target Page for SWF Resources

**Context**: Load the upload page and use network tab to identify Flash files.

Navigate to the Imgur upload interface and open DevTools > Network. Filter for SWF files to find https://imgur.com/include/flash/swfupload.swf.

**Expected Output**: SWF URL confirmed in network requests.

### Step 2: Analyze SWF Parameters

**Context**: Review how the SWF is embedded and what parameters it accepts.

Examine the embedding script or direct URL construction. Note parameters: buttonText (HTML insertion), buttonTextStyle (styling), buttonDisabled, buttonImageURL, buttonAction, buttonCursor.

**Expected Output**: List of customizable parameters without sanitization.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[flash]]
