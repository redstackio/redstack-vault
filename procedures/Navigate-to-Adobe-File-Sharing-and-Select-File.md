---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - web
  - initial-access
  - adobe
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:15:53.015Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate to Adobe File Sharing and Select File

## Summary

This procedure accesses the Adobe Acrobat cloud file sending interface and selects a file to initiate the sharing process, serving as the entry point for injecting a stored XSS payload.

## Description

In the context of exploiting a stored XSS vulnerability in Adobe's file sharing feature, this step involves navigating to https://cloud.acrobat.com/send and choosing a file. This sets up the form where the malicious description can later be injected. The target environment is any modern web browser with access to Adobe services. Expected outcomes include the file being loaded into the sharing interface without errors, preparing for anonymous link configuration.

## Requirements

1. Web browser with JavaScript enabled
2. Internet connection to access Adobe cloud services
3. Optional: Local file to share (any type, e.g., PDF)

## Defense

Defensive measures and detection strategies:

- Implement web application firewall (WAF) rules to monitor access patterns to sharing endpoints
- Require authentication for file sharing interfaces to limit anonymous abuse

## Objectives

1. Gain access to the vulnerable file sending form
2. Prepare a file for sharing to enable payload injection
3. Establish initial foothold in the sharing workflow

## Instructions

### Step 1: Access the Sharing Page

**Context**: Open the browser and load the Adobe file sending interface to begin the attack setup.

Navigate to https://cloud.acrobat.com/send in your web browser.

> This loads the send file page where files can be selected and shared.

### Step 2: Select a File

**Context**: Choose a file to make the sharing request appear legitimate.

Click the file upload or select button and choose a local file (e.g., a PDF document).

> The file is added to the sharing queue, displaying its name and size on the page.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- web
- initial-access
