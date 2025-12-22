---
tags:
  - setup
  - nextcloud
  - testing
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b3859dad-e5c0-45a8-b3b6-295f4abb9f17
created_at: '2025-12-14T03:47:18.614Z'
updated_at: '2025-12-14T03:47:18.614Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Nextcloud-Test-Instance

## Summary

This procedure sets up a local test instance of Nextcloud Server to safely replicate and test the SVG logo endpoint vulnerability without affecting production environments.

## Description

Nextcloud is a PHP-based file sharing platform with a vulnerable SVG logo generation endpoint. This setup involves installing Nextcloud on a local server or VM, configuring it for web access, and verifying the endpoint availability. It requires basic server administration skills and is essential for isolated vulnerability testing to avoid legal or operational risks.

## Requirements

1. Local server or VM with PHP, Apache/Nginx, and MySQL
2. Internet access for Nextcloud download
3. Administrative privileges on the test machine

## Defense

Defensive measures and detection strategies:

- Use isolated environments (VMs) for testing to prevent accidental exposure
- Monitor server logs for unusual installations or access patterns

## Objectives

1. Deploy a functional Nextcloud instance
2. Ensure the SVG endpoint is accessible
3. Prepare for payload injection testing

## Instructions

### Step 1: Install Nextcloud

**Context**: Download and install Nextcloud on your local server.

Follow official installation guide: Download from nextcloud.com/install, extract to web root, run installer via browser.

> Configure database and admin account during setup.

### Step 2: Verify Endpoint Access

**Context**: Confirm the vulnerable endpoint responds.

Use Web Browser to visit http://localhost/nextcloud/index.php/svg/core/logo/logo?color=red.

> Expected: A red-tinted SVG logo renders without errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- [[setup]]
- [[nextcloud]]
- [[testing]]
