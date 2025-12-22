---
id: uuid-1234-5678-9abc-def1
tags:
  - directory-listing
  - reconnaissance
  - web
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
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:23:54.698Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Discover Enabled Directory Listing on Target

## Summary

This procedure involves accessing the root URL of a target web server to check for enabled directory listing, which can expose sensitive files and directories for further reconnaissance.

## Description

Directory listing is a web server configuration (common in Apache or Nginx) that displays the contents of a directory when no index file is present. In this scenario, targeting a corporate internal site like tw.corp.ubnt.com, the researcher browsed to the root and observed exposed directories containing tools and configurations. This step is foundational for identifying misconfigurations that lead to vulnerability discovery. Expected outcomes include visibility into file structures, enabling targeted exploration.

## Requirements

1. Direct HTTP access to the target host (no firewall blocking)
2. Web browser or HTTP client like curl
3. No authentication barriers

## Defense

Defensive measures and detection strategies:

- Disable directory listing in web server configs (e.g., Options -Indexes in Apache)
- Monitor access logs for root directory requests without specific files
- Implement web application firewall (WAF) rules to block anomalous browsing patterns

## Objectives

1. Confirm exposure of directory contents
2. Identify potential sensitive directories like /tools/
3. Gather initial attack surface information

## Instructions

### Step 1: Access Target Root URL

**Context**: Use a browser to load the target's base URL and inspect for listing.

No specific command; manually navigate to http://tw.corp.ubnt.com/ in a browser.

> The page should display a directory index with files and folders if enabled. Look for items like ntpasswd.php or other PHP scripts.

### Step 2: Document Exposed Content

**Context**: Screenshot or note the listed items for reference in subsequent steps.

Manually review and list directories such as /tools/.

> Success is indicated by visible file listings without 403/404 errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[directory-listing]]
- [[Reconnaissance]]
