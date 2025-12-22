---
tags:
  - setup
  - wordpress
  - infogram
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:14.262Z'
sub_techniques: []
id: 1fca4d5d-077a-4e82-bb42-0cd752dedfcd
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install WordPress and Infogram Plugin

## Summary

This procedure sets up a vulnerable WordPress environment by installing version 4.5 and the Infogram plugin version 1.5.1, enabling the exploitation of stored XSS through the plugin's embedding feature.

## Description

The procedure involves downloading and configuring WordPress 4.5, then installing the specific vulnerable version of the Infogram plugin. This creates the target environment where the project name from Infogram is fetched and displayed without proper sanitization in a popup. Prerequisites include a web server (e.g., Apache with PHP) and MySQL for WordPress. Expected outcomes include a functional WordPress site with the plugin active, ready for embedding Infogram content.

## Requirements

1. Web server with PHP 5.6+ and MySQL 5.5+
2. Internet access to download WordPress and the plugin
3. Administrative privileges on the hosting environment

## Defense

Defensive measures and detection strategies:

- Keep WordPress core and plugins updated to patch known vulnerabilities
- Enable Content Security Policy (CSP) to restrict inline JavaScript execution
- Monitor plugin installations and review third-party integrations for sanitization issues

## Objectives

1. Establish a WordPress instance vulnerable to Infogram plugin XSS
2. Activate the plugin to expose the embedding interface
3. Prepare for payload injection via external service

## Instructions

### Step 1: Download and Install WordPress

**Context**: Obtain and set up the base WordPress application.

Navigate to wordpress.org/download and select version 4.5. Extract the files to your web server root (e.g., /var/www/html). Create a database in MySQL and run the installer via browser at http://localhost/wp-admin/install.php, providing database credentials.

### Step 2: Install Infogram Plugin

**Context**: Add the vulnerable plugin to enable Infogram integration.

Log in to the WordPress admin at http://localhost/wp-admin. Go to Plugins > Add New, search for "Infogram", upload or install version 1.5.1 specifically (avoid auto-updates). Activate the plugin from the Plugins list.

> Verify activation by checking for the 'Add from Infogram' button in the post editor.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- setup
- wordpress
- infogram
