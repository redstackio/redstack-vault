---
tags:
  - xss
  - nextcloud
  - setup
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:26.440Z'
sub_techniques: []
id: 8db659ee-e8ad-44b6-b439-d958ef9b2432
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Accessing Nextcloud Setup Configuration

## Summary

This procedure involves navigating to the initial setup page of a fresh Nextcloud 18.0.1 installation to access the database configuration form, setting the stage for vulnerability exploitation.

## Description

In a new Nextcloud deployment, the setup configuration page is the entry point for configuring database connections, including MySQL parameters. This page is publicly accessible without authentication and serves as the target for reflected XSS due to improper input handling. The procedure assumes a local or direct network access to an uninstalled instance running on PHP with MySQL services.

## Requirements

1. Web browser with JavaScript enabled
2. Direct access to the Nextcloud web interface (e.g., http://localhost/nextcloud)
3. Fresh, uninstalled Nextcloud 18.0.1 instance

## Defense

Defensive measures and detection strategies:

- Ensure Nextcloud is updated beyond version 18.0.1 to include input sanitization fixes
- Monitor setup logs for anomalous access patterns during installation
- Implement web application firewall (WAF) rules to block script tag injections

## Objectives

1. Load the vulnerable setup form
2. Verify accessibility of input fields
3. Prepare for payload injection

## Instructions

### Step 1: Navigate to Setup Page

**Context**: Open the browser and direct it to the Nextcloud root to trigger the setup interface.

No command required; use browser navigation to http://target/nextcloud (replace with actual host).

> The setup page should load, displaying the configuration form. If it redirects or shows an error, confirm the instance is uninstalled.

### Step 2: Verify Form Fields

**Context**: Inspect the page to ensure database fields are present.

Use browser developer tools (F12) to view the HTML form elements, confirming the 'mysql Username' input exists.

> Expected: Input fields for host, username, password, and database name are visible and editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- nextcloud
- setup
