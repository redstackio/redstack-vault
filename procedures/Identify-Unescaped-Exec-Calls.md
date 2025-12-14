---
id: proc-identify-unescaped-exec
tags:
  - command-injection
  - code-audit
  - exec
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:26:06.053Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Identify-Unescaped-Exec-Calls

## Summary

This procedure details searching for and analyzing PHP exec function calls in the Image library that lack proper shell escaping, enabling the identification of command injection vulnerabilities.

## Description

PHP's exec function executes system commands, but without escaping arguments like filenames, attackers can inject malicious payloads. In ExpressionEngine's Image_lib.php, functions image_process_imagemagick and image_process_netpbm pass full_src_path and full_dst_path directly to exec at lines 590, 604, 608, and 691. This procedure guides reviewers in locating these issues, assessing impact (e.g., RCE if paths are user-controlled), and recommending fixes like escapeshellarg. Target: Legacy PHP web applications using external image processors.

## Requirements

1. Source code access to Image_lib.php
2. Knowledge of PHP shell functions and injection techniques
3. Ability to grep or search for 'exec(' patterns

## Defense

Defensive measures and detection strategies:

- Use static analysis tools (e.g., PHPStan) to detect unsafe exec usages
- Log all exec calls for anomaly detection (e.g., unexpected commands)
- Sanitize all user inputs before path construction

## Objectives

1. Locate all exec invocations in image processing
2. Verify absence of escaping on path parameters
3. Quantify risk based on control over filenames

## Instructions

### Step 1: Search for Exec Functions

**Context**: Systematically find all exec calls to narrow focus.

Use search tools in your editor to find 'exec(' within Image_lib.php, prioritizing image_process_* functions.

### Step 2: Trace Parameter Sources

**Context**: Determine if parameters like full_src_path are derived from controllable inputs.

Follow variable assignments backward; confirm they stem from upload filenames or user-specified paths.

### Step 3: Check for Escaping

**Context**: Validate sanitization to confirm vulnerability.

Inspect call sites at lines 590, 604, 608, 691; note direct concatenation without escapeshellarg or similar.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Software

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- command-injection
- php-exec
- vulnerability-scan
