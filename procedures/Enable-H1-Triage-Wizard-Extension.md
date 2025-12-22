---
tags:
  - chrome-extension
  - installation
type: procedure
tools:
  - '[[tools/H1-Triage-Wizard-Chrome-Extension]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Chrome Browser Extension
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Execution through Module Load]]'
updated_at: '2025-12-14T00:11:09.497Z'
sub_techniques: []
id: a91a2349-1cea-4aa4-b4db-6557b40327c4
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Execution through Module Load]]'
---
# Enable-H1-Triage-Wizard-Extension

## Summary

This procedure installs and activates the H1 Triage Wizard Chrome Extension, a browser tool for triaging HackerOne reports, enabling the demonstration of HTML injection vulnerabilities.

## Description

The H1 Triage Wizard is a Chrome extension designed to assist in reviewing HackerOne vulnerability reports. In this attack scenario, enabling the extension is the first step to access its triage questionnaire feature, which lacks input sanitization and allows HTML injection leading to stored XSS. This procedure assumes a standard Chrome installation and requires no prior access beyond the Chrome Web Store.

## Requirements

1. Google Chrome browser version 80 or later
2. Internet access to the Chrome Web Store
3. No administrative privileges needed for user-level extension installation

## Defense

Defensive measures and detection strategies:

- Disable or review third-party extensions regularly using chrome://extensions/
- Use enterprise policies to restrict extension installations
- Monitor browser console for unexpected script executions

## Objectives

1. Prepare the browser environment for extension-based attacks
2. Ensure the extension is active for HackerOne domains
3. Validate extension readiness without triggering alerts

## Instructions

### Step 1: Install the Extension

**Context**: Locate and add the H1 Triage Wizard from the official Chrome Web Store.

Search for "H1 Triage Wizard" in the Chrome Web Store, click "Add to Chrome", and confirm the installation.

> The extension installs silently and appears in the extensions menu.

### Step 2: Activate the Extension

**Context**: Enable the extension to make its features available on HackerOne pages.

Navigate to chrome://extensions/, find H1 Triage Wizard, and toggle it on if not already enabled.

> Success is indicated by the extension icon in the toolbar and no errors in the extensions page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Execution through Module Load]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/H1-Triage-Wizard-Chrome-Extension]]

## Tags

- chrome-extension
- installation
