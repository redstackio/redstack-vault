---
id: proc-review-ee-image-lib
tags:
  - code-review
  - vulnerability-discovery
  - php
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
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:26:06.057Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Review-ExpressionEngine-Image-Library-Source

## Summary

This procedure involves auditing the source code of ExpressionEngine's Image library to identify potential security flaws in image processing functions, particularly those interacting with external tools via PHP's exec function.

## Description

In ExpressionEngine, the Image library (Image_lib.php) handles image manipulation using libraries like ImageMagick and NetPBM. Inherited from CodeIgniter, it processes source and destination file paths. By reviewing the code, attackers or researchers can uncover unsanitized inputs leading to command injection. This is crucial for vulnerability discovery in legacy CMS installations. Expected outcomes include mapping function flows and spotting insecure exec usages. Prerequisites: Access to the source code repository or installed files.

## Requirements

1. Access to ExpressionEngine source code (e.g., ./system/ee/legacy/libraries/Image_lib.php)
2. Basic PHP and CodeIgniter knowledge
3. Text editor or IDE for code navigation

## Defense

Defensive measures and detection strategies:

- Implement code scanning tools like SonarQube or Semgrep to flag unsanitized exec calls
- Enforce secure coding standards requiring escapeshellarg for shell commands
- Regular code audits and dependency updates to match secure frameworks like CodeIgniter

## Objectives

1. Understand image processing workflow in ExpressionEngine
2. Identify parameters derived from user-controlled inputs like filenames
3. Document potential injection vectors for further analysis

## Instructions

### Step 1: Locate and Open Source File

**Context**: Begin by accessing the core Image library file to examine its structure and dependencies.

Navigate to the file and open it in an editor. Note that it extends CodeIgniter's Image_lib class.

### Step 2: Analyze Image Processing Functions

**Context**: Focus on functions that invoke external image processing tools, tracing parameter flows.

Review image_process_imagemagick and image_process_netpbm. Trace how full_src_path and full_dst_path are constructed from uploaded or specified image details.

### Step 3: Document Inheritance and Comparisons

**Context**: Compare with upstream CodeIgniter to highlight deviations.

Check the official CodeIgniter repo (e.g., line 892 in Image_lib.php) for proper escaping, confirming ExpressionEngine's lack thereof.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- code-review
- php
- expressionengine
