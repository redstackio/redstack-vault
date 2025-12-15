---
tags:
  - setup
  - installation
  - acronis
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:28:58.852Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9e9db960-f1c6-4cf5-86d7-81776ac024ad
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-Acronis-Cloud-Manager

## Summary

This procedure outlines the installation of Acronis Cloud Manager on a local Windows machine, including the console and web portal, to set up a testable environment for vulnerability assessment.

## Description

Acronis Cloud Manager is a service provider platform for managing cyber protection services. To replicate the vulnerable setup, download the free trial, unzip the installer, and follow the official guide to install the console and web portal directly on Windows. This creates a local instance accessible via HTTPS on port 16080, allowing access to the Swagger UI for testing. The setup requires administrative privileges and prepares the environment for database integration and vulnerability exploitation.

## Requirements

1. Windows machine with administrative access
2. Internet connection for downloading the trial from https://www.acronis.com/en-us/products/cloud-manager/
3. Unzipping tool for the installer package

## Defense

Defensive measures and detection strategies:

- Restrict downloads and installations to trusted sources only
- Monitor for unauthorized software installations on endpoints
- Use endpoint detection tools to flag unusual installer executions

## Objectives

1. Establish a local Acronis Cloud Manager instance
2. Verify web portal accessibility on localhost:16080
3. Prepare for subsequent database and vulnerability testing

## Instructions

### Step 1: Download the Installer

**Context**: Obtain the Acronis Cloud Manager free trial package to begin setup.

Visit https://www.acronis.com/en-us/products/cloud-manager/ and download the free trial. Unzip the downloaded file to access the installer.

### Step 2: Run Installation

**Context**: Install the console and web portal components following the official guide.

Launch the installer and follow the steps in the guide at https://dl.acronis.com/u/rc/GSG_AcronisCloudManager_5.0_EN-US.pdf. Select options for console and web portal installation on the local Windows system.

> Ensure HTTPS is enabled and the web portal binds to port 16080.

### Step 3: Verify Installation

**Context**: Confirm the installation by accessing the web portal.

Open a browser and navigate to https://localhost:16080 to ensure the portal loads without errors.

**Expected Output**: Acronis Cloud Manager web interface displays successfully.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[acronis]]
- [[windows]]
