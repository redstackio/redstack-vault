---
tags:
  - setup
  - nextcloud
  - server
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
techniques: []
updated_at: '2025-12-14T03:15:53.555Z'
sub_techniques: []
id: a4c94d8e-63ef-43d7-8f1b-9607cccb71ac
validated: true
mitre_tactics:
  - '[[Initial Access]]'
---
# Setup-Nextcloud-Server-and-Users

## Summary

This procedure sets up a Nextcloud server instance, creates an administrator account, registers a regular user, and installs the Nextcloud Talk application to prepare for exploiting XSS in group conversations.

## Description

The setup involves installing Nextcloud on a server environment, configuring initial accounts, and enabling the Talk app, which is essential for the vulnerability demonstration. This creates the backend infrastructure where malicious group names can be injected. The target environment is a self-hosted Nextcloud server accessible via web browser. Prerequisites include server hosting capabilities (e.g., LAMP stack) and basic web administration skills. Expected outcomes include a running server with Talk enabled and two functional user accounts.

## Requirements

1. Server environment with PHP, MySQL, and Apache/Nginx (e.g., Ubuntu VM)
2. Domain or IP for server access
3. Administrative privileges on the server
4. Web browser for interface interaction

## Defense

Defensive measures and detection strategies:

- Use official Nextcloud installation guides and verify checksums to prevent tampered setups
- Enable server-side logging for user account creations and app installations
- Implement role-based access control to limit admin actions

## Objectives

1. Establish a functional Nextcloud server
2. Create admin and user accounts for testing
3. Install and enable Nextcloud Talk for conversation features

## Instructions

### Step 1: Install Nextcloud Server

**Context**: Deploy the Nextcloud application on the server to create the base environment.

No specific command; use the web installer or manual setup via official docs. Download from nextcloud.com, extract to web root, and run the installer.

> Access the server IP in a browser, follow the setup wizard to configure database and admin account.

### Step 2: Create Administrator Account

**Context**: Register the initial admin user during or after installation.

During the setup wizard, provide admin username and password.

> Successful login to the web interface as admin confirms setup.

### Step 3: Create User Account

**Context**: Add a regular user for the victim role in the attack.

Log in as admin, navigate to Users section, and create a new user with email and password.

> User appears in the users list and can log in independently.

### Step 4: Install Nextcloud Talk

**Context**: Enable the Talk app to support group conversations and calls.

As admin, go to Apps, search for "Talk", install and enable it.

> Talk icon appears in the top menu, confirming activation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[setup]]
- [[nextcloud]]
- [[Server]]
