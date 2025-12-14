---
id: uuid-1234-5678-9abc-def2
tags:
  - directory-exploration
  - endpoint-discovery
  - web
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
updated_at: '2025-12-14T17:23:54.686Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Explore Leaked Directories to Identify Endpoints

## Summary

This procedure entails navigating through exposed directories from a directory listing to locate specific endpoints, such as PHP scripts handling sensitive operations like password hashing, setting the stage for vulnerability testing.

## Description

Building on directory listing discovery, this step involves manual exploration of leaked paths on the target server. In the Ubiquiti case, delving into /tools/ revealed ntpasswd.php, a utility for converting passwords to NT/LM hashes using system commands. This exposes potential injection points due to unsanitized inputs. Prerequisites include prior identification of the listing; outcomes are pinpointing exploitable endpoints.

## Requirements

1. Access to exposed directories from Step 1
2. Web browser for navigation
3. Basic understanding of web file structures

## Defense

Defensive measures and detection strategies:

- Restrict directory permissions to prevent listing exposure
- Use robots.txt or .htaccess to block sensitive paths
- Log and alert on deep directory traversals

## Objectives

1. Locate PHP endpoints with user input handling
2. Understand endpoint functionality (e.g., password processing)
3. Prepare for targeted fuzzing

## Instructions

### Step 1: Navigate to Exposed Directories

**Context**: Click into directories like /tools/ from the root listing.

Manually browse to http://tw.corp.ubnt.com/tools/.

> Expect to see files including ntpasswd.php; review descriptions for hashing features.

### Step 2: Inspect Endpoint Details

**Context**: Access the endpoint to confirm input parameters.

Load http://tw.corp.ubnt.com/tools/ntpasswd.php and note form fields for password input.

> Verify it accepts clear text and outputs hashes, indicating backend command execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[directory-exploration]]
- [[endpoint-discovery]]
