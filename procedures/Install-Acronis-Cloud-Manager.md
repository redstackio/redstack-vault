---
id: proc-install-acronis-001
tags:
  - setup
  - acronis
  - installation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T03:16:25.461Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Install-Acronis-Cloud-Manager

## Summary

This procedure installs the Acronis Cloud Manager console and web portal on a Windows system, creating a local environment vulnerable to XSS in Swagger UI for testing purposes.

## Description

Acronis Cloud Manager is a backup and management solution. This setup replicates the environment where an outdated dom-purify library in Swagger UI allows XSS via the 'url' parameter. The procedure involves downloading the free trial, unzipping, and installing per official guides, ensuring the web portal runs on port 16080 connected to a database.

## Requirements

1. Windows OS with administrative privileges
2. Internet access for download
3. At least 4GB RAM and 10GB disk space

## Defense

Defensive measures and detection strategies:

- Keep Acronis Cloud Manager updated to patch dom-purify vulnerabilities
- Disable or restrict access to Swagger UI in production
- Implement Content Security Policy (CSP) to block inline JavaScript

## Objectives

1. Establish a functional local Acronis environment
2. Enable web portal access for vulnerability testing
3. Prepare for database integration

## Instructions

### Step 1: Download Acronis Cloud Manager

**Context**: Obtain the installer from the official Acronis website.

Visit https://www.acronis.com/en-us/products/cloud-manager/ and download the free trial ZIP file.

### Step 2: Unzip and Install

**Context**: Extract and run the installer on Windows.

Unzip the downloaded file to a directory, then execute the setup wizard. Follow the guide at https://dl.acronis.com/u/rc/GSG_AcronisCloudManager_5.0_EN-US.pdf for console and web portal installation, configuring the portal to bind to localhost:16080.

### Step 3: Verify Installation

**Context**: Confirm the components are running.

Launch the Acronis console and access https://localhost:16080 in a browser to ensure the admin portal loads.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- acronis
- installation
