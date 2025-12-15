---
tags:
  - setup
  - nextcloud
  - configuration
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:24:45.122Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 629f42df-cdc4-4b99-9121-04be0c7ec0c6
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Set-Up-Nextcloud-Instance-with-Default-Settings

## Summary

This procedure outlines the installation and configuration of a clean Nextcloud server instance using default settings, ensuring the 'Search global and public address book for users' functionality is enabled to replicate the vulnerable environment.

## Description

Nextcloud is a self-hosted file sync and share platform. In default configurations, the global address book search is active, which interacts with an external lookup server. This setup is necessary to demonstrate the privacy leak when paired with the Android client. The procedure assumes a Linux server with PHP and web server (e.g., Apache) installed. No custom modifications are made to preserve the default behavior where the server treats missing 'lookup' parameters as true.

## Requirements

1. Linux server with PHP 7.4+ and MySQL/MariaDB
2. Web server like Apache or Nginx
3. Internet access for downloading Nextcloud
4. Administrative privileges on the server

## Defense

Defensive measures and detection strategies:

- Disable global address book search in Nextcloud admin settings if not needed
- Monitor outbound traffic from Nextcloud server to external endpoints
- Use network segmentation to block unnecessary external queries

## Objectives

1. Establish a functional Nextcloud server
2. Verify default global search is enabled
3. Prepare environment for client testing

## Instructions

### Step 1: Install Dependencies

**Context**: Ensure the server has required software for Nextcloud.

Download and install Nextcloud from the official site, then configure the web server to point to the installation directory. Enable the sharing module in the admin panel.

### Step 2: Configure Default Settings

**Context**: Activate the vulnerable feature without alterations.

In the Nextcloud admin settings under Sharing, confirm 'Search global and public address book for users' is checked (default). No API changes are needed.

### Step 3: Verify Setup

**Context**: Test basic functionality.

Access the web interface and attempt a share operation to ensure the server is responsive.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[nextcloud]]
- [[configuration]]
