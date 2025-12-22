---
tags:
  - setup
  - concrete-cms
  - installation
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
updated_at: '2025-12-14T03:16:02.523Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e487bb9d-5754-4282-8588-ae66136623be
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Install-and-Setup-Concrete-CMS-8-5-2

## Summary

This procedure outlines the installation of Concrete CMS version 8.5.2, a vulnerable version containing the stored XSS flaw, to prepare an environment for exploitation testing.

## Description

Concrete CMS 8.5.2 is a PHP-based content management system. This procedure involves downloading the specific version, setting up a local web server with PHP and a database (e.g., MySQL), and completing the installation wizard. It is essential for replicating the vulnerability in a controlled environment. Prerequisites include a LAMP/WAMP stack or equivalent. Expected outcome is a fully functional CMS instance ready for admin access.

## Requirements

1. PHP 7.x environment with MySQL database
2. Web server (Apache/Nginx)
3. Download access to Concrete CMS 8.5.2 archive
4. Basic knowledge of server configuration

## Defense

Defensive measures and detection strategies:

- Use updated CMS versions (post-8.5.2) with patched vulnerabilities
- Monitor for unauthorized installations in production environments
- Implement web application firewalls (WAF) to block anomalous setup traffic

## Objectives

1. Establish a vulnerable CMS instance for testing
2. Verify basic functionality before exploitation
3. Ensure admin access is possible

## Instructions

### Step 1: Download Concrete CMS 8.5.2

**Context**: Obtain the vulnerable version from official archives or mirrors.

**Action**:

- Visit the Concrete CMS download page or archive.
- Download the ZIP/TAR for version 8.5.2.

> Extract the archive to your web server root (e.g., /var/www/html/concrete).

### Step 2: Configure Database and Server

**Context**: Set up the necessary backend for the CMS.

**Action**:

- Create a MySQL database and user.
- Edit configuration files if needed (e.g., php.ini for extensions).
- Start the web server and ensure PHP is enabled.

> Access http://localhost/concrete to begin the setup wizard.

### Step 3: Run Installation Wizard

**Context**: Complete the interactive setup to initialize the CMS.

**Action**:

- Follow the wizard: Enter database details, site name, admin credentials.
- Agree to terms and finalize installation.

> Upon completion, the dashboard should load at /index.php/dashboard.

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
- [[installation]]
