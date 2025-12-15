---
tags:
  - folder-prediction
  - source-code-analysis
  - expressionengine
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - PHP
techniques:
  - '[[File and Directory Discovery]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9af31a14-c9d3-4c14-b2eb-929f37be234a
created_at: '2025-12-14T17:23:36.812Z'
updated_at: '2025-12-14T17:23:36.812Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Predict-Temporary-Folder-for-Uploaded-File

## Summary

This procedure involves analyzing ExpressionEngine's source code to predict the temporary folder name and path where an uploaded file is stored, leveraging the exposed naming algorithm for targeted access without brute-forcing.

## Description

ExpressionEngine's upload function uses a predictable algorithm for temporary storage, often based on timestamps, hashes, or session data visible in the codebase (e.g., in system/expressionengine/libraries/Upload.php). An attacker reviews the source to replicate the logic, calculating the exact folder (e.g., tmp_ followed by Unix timestamp). This enables precise location of uploaded files in web-accessible dirs, facilitating RCE. Requires source code access; outcomes include full path to malicious file.

## Requirements

1. Access to ExpressionEngine source code (via download, leak, or server file access)
2. Knowledge of upload timing (e.g., exact timestamp of upload submission)
3. Basic understanding of PHP naming conventions in the CMS

## Defense

Defensive measures and detection strategies:

- Obfuscate or randomize temporary folder names with secure tokens
- Restrict source code exposure and use code obfuscation
- Log and alert on anomalous access to temp directories
- Place system folders outside web root to prevent direct access

## Objectives

1. Reverse-engineer the temp folder generation algorithm
2. Compute the exact path based on upload variables
3. Locate the uploaded file without extensive enumeration

## Instructions

### Step 1: Review Source Code

**Context**: Identify the upload handler and naming logic in the codebase.

Download or access the ExpressionEngine files, focusing on the import channel field upload function (e.g., search for 'upload' in system/expressionengine/controllers/cp/channel.php or libraries).

Locate the temp dir creation, often like $temp_dir = 'tmp_' . time() . '/';

### Step 2: Replicate Algorithm

**Context**: Use the logic to predict based on known inputs.

Note the upload time (e.g., current Unix timestamp via browser dev tools). Apply the algorithm: if it's tmp_[timestamp]_[hash], compute manually or with a calculator.

Example prediction: For timestamp 1696152000, folder = /system/expressionengine/cache/tmp_1696152000/

### Step 3: Validate Prediction

**Context**: Confirm the path structure matches server layout.

If partial access to server dirs is possible (e.g., via another feature), list dirs to verify pattern; otherwise, proceed to access attempt.

**Expected Output**: Full predicted path like /var/www/system/tmp/predicted_folder/malicious.php

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[File and Directory Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[source-analysis]]
- [[prediction]]
- [[Discovery]]
