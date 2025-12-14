---
id: proc-capture-poc-acronis
tags:
  - poc-documentation
  - video-capture
  - vulnerability-reporting
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:29:28.526Z'
skill_level: beginner
impact_level: low
detection_risk: none
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Capture POC Video of Bypass

## Summary

This procedure documents the broken access control bypass by recording a video demonstration, useful for reporting vulnerabilities like the Acronis notary panel issue.

## Description

After exploiting the .html bypass, capture the process to provide evidence. This involves screen recording the failed auth attempt, successful bypass, and file viewing. No technical exploit execution here; it's evidentiary. Expected outcome: A clear video proving the vulnerability for platforms like HackerOne.

## Requirements

1. Screen recording tool (e.g., OBS Studio, QuickTime, or browser extension)
2. Completed prior bypass steps
3. Stable internet for target access

## Defense

Defensive measures and detection strategies:

- N/A (documentation step); focus on fixing the underlying vuln to prevent demos
- Monitor for unusual traffic patterns that might indicate testing

## Objectives

1. Visually demonstrate the access control failure
2. Provide verifiable proof for vulnerability reports
3. Aid in reproduction for remediation

## Instructions

### Step 1: Prepare Recording

**Context**: Set up the tool to capture browser and actions.

Launch screen recorder and select the browser window.

> Expected output: Recording started, ready to demo.

### Step 2: Record Failed Access

**Context**: Show the initial block to contrast with bypass.

Navigate to the panel URL without auth and capture the denial.

> Expected output: Video segment of error/redirect.

### Step 3: Record Bypass and File View

**Context**: Demonstrate the exploit and results.

Modify URL with .html, load, and scroll/inspect the static content.

> Expected output: Video showing successful file access.

### Step 4: Stop and Export

**Context**: Save the POC for attachment.

End recording and export as MP4 or similar.

> Expected output: Complete video file under 1MB for upload.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[poc-documentation]]
- [[video-capture]]
- [[vulnerability-reporting]]
