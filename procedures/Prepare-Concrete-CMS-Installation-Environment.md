---
id: proc-prepare-concrete-cms-env
tags:
  - setup
  - installation
  - concrete-cms
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.153Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Prepare-Concrete-CMS-Installation-Environment

## Summary

This procedure sets up a local environment for Concrete CMS installation, including downloading and extracting the archive, to prepare for vulnerability testing during the setup phase.

## Description

In the context of exploiting web application vulnerabilities like reflected XSS, preparing the installation environment involves simulating a fresh Concrete CMS deployment on a local web server. This targets the installation wizard where configuration inputs are processed. Expected outcomes include a functional installer accessible via browser, enabling subsequent payload injection without prior access requirements beyond local setup.

## Requirements

1. Local machine with internet access to download the Concrete CMS archive
2. Installed Apache web server with PHP 5.6+ support
3. Running MySQL server (version 5.5+) with a valid database user and password

## Defense

Defensive measures and detection strategies:

- Run installations in isolated environments (e.g., VMs) to prevent payload execution in production
- Monitor web server logs for unusual archive downloads or extraction patterns
- Use input sanitization in installers to block early-stage exploits

## Objectives

1. Establish a testable Concrete CMS installation instance
2. Ensure web server serves the extracted files correctly
3. Verify prerequisites like PHP and MySQL are operational

## Instructions

### Step 1: Download Concrete CMS Archive

**Context**: Obtain the vulnerable version (8.2.1) from the official source to replicate the exact environment.

No command required; manually download from https://www.concretecms.org/download/ and save as concrete5-8.2.1.zip.

> Download the file and confirm integrity via file size or checksum if available.

### Step 2: Extract Archive to Web Root

**Context**: Place the files in a directory served by Apache to access the installer.

Manually unzip the archive into /var/www/html/concrete/ (or equivalent local path).

> Ensure permissions allow web server execution (e.g., chmod 755 on directories).

### Step 3: Verify Local Server Access

**Context**: Confirm the setup by accessing the base URL in a browser.

Navigate to http://localhost/concrete/ in your web browser.

> Expected: Directory listing or default page loads without errors.

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
- [[concrete-cms]]
