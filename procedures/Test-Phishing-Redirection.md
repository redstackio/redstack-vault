---
id: proc-uuid2-placeholder
tags:
  - phishing
  - url-masking
  - redirection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Phishing]]'
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:28:04.857Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Phishing]]'
  - '[[T1566.002]]'
---
# Test-Phishing-Redirection

## Summary

This procedure tests the URL masking HTML in the Brave browser to verify the phishing effectiveness, confirming that the status bar displays a spoofed legitimate URL while the actual click redirects to a malicious site.

## Description

Targeting the Brave browser's link handling (Chromium-based with Muon 2.0.19, libchromiumcontent 54.0.2840.100), this procedure involves loading the crafted HTML and interacting with the link to observe the discrepancy between visual cues and actual navigation. It simulates an attack where users are deceived into visiting unintended sites, such as from google.com appearance to datarift.blogspot.in. Prerequisites: The crafted HTML file and Brave browser on Windows. Outcomes include validation of the vulnerability for informative reporting, noting similarities in Firefox and Chrome.

## Requirements

1. Crafted `click.html` file from prior procedure
2. Brave browser installed on Windows
3. Local file access or internet for hosted version

## Defense

Defensive measures and detection strategies:

- Train users to always check the address bar post-click
- Implement browser policies to disable or warn on status bar manipulations
- Use antivirus/web filters to block known malicious domains like datarift.blogspot.in
- Log and alert on unexpected redirects in enterprise environments

## Objectives

1. Verify status bar spoofing on link hover
2. Confirm redirection to malicious site on click
3. Assess phishing impact without actual harm

## Instructions

### Step 1: Load the HTML in Browser

**Context**: Open the file to prepare for interaction testing.

Navigate to the local `click.html` file via file explorer (double-click) or enter the hosted URL (e.g., http://hackies.in/click.html) in Brave's address bar.

> Expected output: Page loads showing the link text "Click here for Google" without errors.

### Step 2: Hover and Click to Test Masking

**Context**: Interact with the link to observe and confirm the deception.

Hover the mouse over the link; check the browser's status bar (bottom-left) for `http://google.com`. Then click the link and verify the address bar changes to `datarift.blogspot.in`.

> Expected output: Status bar shows spoofed URL on hover; page redirects to malicious site on click, demonstrating the vulnerability.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Phishing]] Phishing
- [[T1566.002]] Spearphishing Link

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[url-masking]]
- [[browser-testing]]
