---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - setup
  - weblate
  - permissions
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:01.927Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Weblate-Instance-with-Removed-Permissions

## Summary

This procedure configures a local Weblate 2.15-dev instance by installing the software, creating a test project, removing all permissions from the Guest group, and restarting the server to simulate the vulnerable environment where API access controls are bypassed.

## Description

In the context of testing the Weblate API vulnerability, this setup creates a Django-based translation management system running on port 8000. A test project ('testproject') and component ('testcomponent') with English (Canada) translations are added. Removing Guest group permissions ensures UI denial for anonymous users, highlighting the API's failure to enforce the same controls. This is essential for reproducing the improper access control issue reported in HackerOne #232994.

## Requirements

1. Local machine with Python 3.6+ and pip installed
2. Access to Docker or virtual environment for Weblate installation
3. Administrative privileges to manage the Weblate database and permissions
4. Network interface allowing binding to port 8000

## Defense

Defensive measures and detection strategies:

- Enforce consistent permission checks across UI and API layers in Django views
- Implement API authentication middleware to require tokens for all endpoints
- Monitor API logs for anonymous access patterns to sensitive resources

## Objectives

1. Establish a reproducible vulnerable Weblate environment
2. Verify permission removal affects only UI, not API
3. Prepare for anonymous API testing

## Instructions

### Step 1: Install and Run Weblate

**Context**: Download and start the development version of Weblate to create the base instance.

Follow the official Weblate documentation to install 2.15-dev using pip or Docker, then run the server with `python manage.py runserver 0.0.0.0:8000`.

> Ensure the server binds to all interfaces for remote testing if needed.

### Step 2: Create Test Project and Component

**Context**: Add a sample project to test access controls.

Use the admin interface (http://localhost:8000/admin/) to create a project named 'testproject' and a component 'testcomponent' with a sample translation file for 'en_CA'.

> Upload a basic .po file containing dummy translations to simulate sensitive data.

### Step 3: Remove Guest Permissions

**Context**: Strip access from anonymous users to trigger the bypass condition.

In the admin panel, navigate to Groups > Guest, and remove all project-related permissions (e.g., view, download).

> Restart the server with `python manage.py runserver` to apply changes.

### Step 4: Verify Setup

**Context**: Confirm the instance is running and permissions are cleared.

Access http://localhost:8000/admin/ to check Guest group has no permissions assigned.

> Expected: Server logs show no errors; test project exists but is inaccessible via UI for guests.

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
- [[weblate]]
- [[permissions]]
