---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567893
tags:
  - reconnaissance
  - path-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[System Information Discovery]]'
updated_at: '2025-12-14T17:23:32.360Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[System Information Discovery]]'
---
# Download-and-Analyze-ownCloud-Config-Report

## Summary

This procedure retrieves and parses the ownCloud configuration report to extract critical server paths, such as the data directory and PHP interpreter, essential for payload placement and execution chaining.

## Description

The config report in ownCloud provides diagnostic information including filesystem paths and environment details. In a LAMP setup, it reveals the datadirectory (e.g., /var/www/owncloud/data) for file uploads and the PHP binary path (e.g., /usr/bin/php). This reconnaissance step is key to constructing the exploitable AV path without direct server access.

## Requirements

1. Admin access to ownCloud settings
2. Text editor or viewer to analyze the downloaded report
3. Understanding of LAMP path conventions

## Defense

Defensive measures and detection strategies:

- Restrict config report access to trusted admins only
- Audit downloads of sensitive reports via access logs
- Obfuscate or remove unnecessary path details from reports

## Objectives

1. Obtain datadirectory path for file uploads
2. Identify PHP interpreter location
3. Gather environment details for exploitation

## Instructions

### Step 1: Access General Settings

**Context**: Locate the config report download option.

In the admin dashboard, go to Settings > General and find the "Download config report" button.

> Click to initiate download. Expected output: A .txt or .php file containing configuration data.

### Step 2: Analyze Report Content

**Context**: Extract relevant paths from the report sections.

Open the file and search for "datadirectory" in the config section and PHP path in the environment structure.

> Note paths like datadirectory => '/var/www/owncloud/data/' and PHP binary at /usr/bin/php. Verify against expected LAMP setup.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[System Information Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- reconnaissance
- path-discovery
