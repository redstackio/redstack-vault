---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - default-browser
  - windows-10
type: procedure
tools: []
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Bypass User Account Control]]'
updated_at: '2025-12-14T17:29:44.569Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Bypass User Account Control]]'
---
# Set-Booby-Trapped-Browser-as-Default-on-Windows-10

## Summary

This procedure sets a tampered browser (e.g., IE) as the default on Windows 10 to ensure the hijacked protocol handlers are used during the ShellExecute trigger.

## Description

After tampering HKCU keys for a specific browser like IE (while default might be Edge), change defaults via settings to route URL opens through the booby-trapped handlers. This step is specific to Windows 10 where browser defaults affect protocol resolution.

## Requirements

1. Windows 10 with multiple browsers installed
2. Prior registry tampering for targeted browser
3. Access to system settings

## Defense

Defensive measures and detection strategies:

- Lock default app associations via GPO
- Monitor changes to default browser settings
- Use Edge/Chrome with protected mode enabled

## Objectives

1. Route URL handling to hijacked browser
2. Ensure compatibility with elevated ShellExecute
3. Validate default without triggering exploit

## Instructions

### Step 1: Access Default Apps Settings

**Context**: Navigate to change browser defaults.

**Instructions**: Open Windows Settings (Win+I) > Apps > Default apps > Web browser, select Internet Explorer (or targeted).

> For protocols: Scroll to "Choose default apps by protocol" and set HTTP/HTTPS to IE.

**Expected Output**: Confirmation in settings; test by opening a URL manually.

### Step 2: Verify Default

**Context**: Confirm the change takes effect.

**Instructions**: Open notepad and type a URL, or use run dialog (Win+R) with 'http://test.com'.

> Expected output: Opens in targeted browser, potentially triggering hijack if tested.
