---
id: proc-setup-nextcloud-local
tags:
  - setup
  - nextcloud
  - local-instance
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - PHP
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T00:11:09.462Z'
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
# Setup-Nextcloud-Instance-Locally

## Summary

This procedure sets up a local Nextcloud 27.0.0.8 instance to test the Deck app self-XSS vulnerability, providing a controlled environment for manual HTML injection testing.

## Description

The procedure involves downloading, installing, and configuring Nextcloud on localhost. It requires a web server like Apache or Nginx with PHP support. Once running, enable the Deck app to access card comments. This setup replicates the vulnerable environment discovered through manual testing, allowing injection of HTML payloads without affecting production systems.

## Requirements

1. Local machine with PHP 7.4+ and a web server (e.g., Apache)
2. Database like MySQL or SQLite for Nextcloud
3. Internet access for initial download
4. Administrative privileges on the local system

## Defense

Defensive measures and detection strategies:

- Use containerization (e.g., Docker) to isolate test environments
- Monitor local network traffic for anomalous requests during setup
- Apply Nextcloud security updates post-testing to patch known issues

## Objectives

1. Establish a functional local Nextcloud instance
2. Enable the Deck app for vulnerability testing
3. Ensure accessibility via web browser for manual exploitation

## Instructions

### Step 1: Download and Install Nextcloud

**Context**: Obtain the specific vulnerable version and set up the base installation.

Download Nextcloud 27.0.0.8 from the official archive and extract it to your web server's document root (e.g., /var/www/html/nextcloud).

Configure the web server to point to the directory and set up the database.

**Expected Output**: Installation wizard loads at http://localhost/nextcloud.

### Step 2: Complete Initial Configuration

**Context**: Run the setup wizard to create an admin account and configure basics.

Access http://localhost/nextcloud, create an admin user, and select storage/database options.

**Expected Output**: Dashboard accessible after login.

### Step 3: Install and Enable Deck App

**Context**: Add the Deck app to enable card and comment functionality.

From the apps section, search for and install the Deck app, then enable it.

**Expected Output**: Deck appears in the main menu.

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
- [[nextcloud]]
- [[local-instance]]
