---
tags:
  - xxe
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 25a6850f-1d4b-4ca9-916a-44c3ddca60e6
created_at: '2025-12-13T09:00:27.581Z'
updated_at: '2025-12-13T09:00:27.581Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Vulnerable Upload Feature

## Summary

This procedure involves identifying file upload features in web applications, specifically targeting SVG uploads that may be vulnerable to XXE due to improper XML parsing.

## Description

In web applications like Moneybird, file upload endpoints can parse SVG files as XML. This procedure tests for the presence of such features and confirms if they process uploads without secure XML parsing, setting the stage for XXE exploitation. The target environment is a web platform, and success is measured by confirming upload functionality.

## Requirements

1. Access to the web application (e.g., user account)
2. Browser or HTTP client for testing
3. Knowledge of the upload endpoint URL

## Defense

Defensive measures and detection strategies:

- Implement secure XML parsers that disable external entity resolution
- Monitor upload logs for suspicious file types or contents

## Objectives

1. Locate and confirm SVG upload functionality
2. Verify server-side processing of uploaded files
3. Identify potential for XML injection

## Instructions

### Step 1: Access Upload Interface

**Context**: Navigate to the file upload section in the application.

Log in to the Moneybird application and locate the SVG upload feature.

> Expected: Access to upload form.

### Step 2: Test with Benign File

**Context**: Upload a non-malicious SVG to confirm processing.

Create a simple SVG and upload it via the interface.

> Expected: Successful upload without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[recon]]
