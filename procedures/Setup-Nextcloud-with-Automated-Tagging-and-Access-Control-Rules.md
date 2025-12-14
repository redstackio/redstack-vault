---
id: proc-uuid-1
tags:
  - nextcloud
  - setup
  - access-control
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:28:58.706Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[File and Directory Discovery]]'
---
# Setup-Nextcloud-with-Automated-Tagging-and-Access-Control-Rules

## Summary

This procedure sets up a Nextcloud instance with the Files access control and automated tagging apps to enforce restrictions on files owned by admins, tagging them as 'Secret' and denying access to non-admin users, creating a controlled environment for testing bypasses.

## Description

The procedure involves installing Nextcloud on Ubuntu, enabling the necessary apps, creating a collaborative tag, and configuring rules to automatically tag files based on admin group membership and restrict access accordingly. This simulates a protected file storage scenario where sensitive data is isolated from unprivileged users. Prerequisites include a fresh Ubuntu 18.04 LTS install and admin access. Expected outcomes: Rules active, files tagged upon creation, direct access denied for non-admins.

## Requirements

1. Fresh Ubuntu 18.04 LTS server with internet access
2. Administrative privileges on the server
3. Snap package manager installed
4. Network access to download Nextcloud and apps

## Defense

Defensive measures and detection strategies:

- Regularly audit access control app configurations and test rules
- Monitor WebDAV logs for unusual SEARCH queries from unprivileged users
- Disable or restrict WebDAV SEARCH depth for shared folders
- Implement server-side permission checks in preview generation APIs

## Objectives

1. Establish a baseline protected environment in Nextcloud
2. Verify tagging and access denial for admin-owned files
3. Prepare for sharing and bypass testing

## Instructions

### Step 1: Install Nextcloud

**Context**: Install Nextcloud from Snap on Ubuntu to create the base instance.

No specific command; use `sudo snap install nextcloud` followed by initial setup via web interface (version 13.0.2snap1, revision 6916).

> Run the installation and complete admin account creation. Expected output: Nextcloud accessible at https://server-ip.

### Step 2: Enable Apps and Create Tag

**Context**: Install and enable Files access control v1.3.0 and Files automated tagging v1.3.0 apps, then create an invisible collaborative tag 'Secret' as admin.

No command; perform via Nextcloud admin web interface.

> Apps enabled, tag created. Expected output: Tags section shows 'Secret' tag.

### Step 3: Configure Tagging Rule

**Context**: Add a rule to automatically tag all files owned by 'admin' group members with 'Secret'.

No command; configure in Files automated tagging app settings.

> Rule saved. Expected output: New admin files receive 'Secret' tag.

### Step 4: Configure Access Control Rule

**Context**: Deny access to files with 'Secret' tag for users not in 'admin' group.

No command; set in Files access control app.

> Rule active. Expected output: Non-admin users cannot view tagged files directly.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/curl]]

## Tags

- nextcloud
- setup
- access-control
