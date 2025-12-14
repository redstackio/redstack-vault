---
tags:
  - information-disclosure
  - wayback-machine
  - simplenote
  - privacy-leak
  - reconnaissance
type: procedure
tools:
  - '[[tools/web.archive.org]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Search Engines]]'
updated_at: '2025-12-14T17:25:12.967Z'
sub_techniques: []
id: 9f5955a6-0308-4a15-9dd8-ebfb70ee3701
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Engines]]'
---
# Discover-Archived-Private-Notes-Using-Wayback-Machine

## Summary

This procedure outlines how to search the Wayback Machine (web.archive.org) for archived snapshots of private Simplenote notes, revealing sensitive information that was intended to be restricted to shared recipients but became publicly accessible due to lack of crawling protections.

## Description

Simplenote, a service by Automattic, allows users to create and share private notes via URLs like http://simp.ly/p/* or http://app.simplenote.com/. These notes are meant for limited sharing, but without measures like robots.txt or IP blocking, the Wayback Machine crawls and archives them. An attacker can search for these URLs on web.archive.org to access recent snapshots (e.g., from December 31, 2020) containing emails, passwords, or other confidential data. The procedure targets web-based reconnaissance to exploit this misconfiguration, leading to information disclosure and privacy violations.

## Requirements

1. Internet access to web.archive.org
2. Basic web browsing knowledge
3. No special credentials or tools beyond a standard browser

## Defense

Defensive measures and detection strategies:

- Implement robots.txt to disallow crawling of private endpoints (e.g., Disallow: /p/*)
- Block web.archive.org user agents or IPs in server configurations
- Monitor for unauthorized archiving by periodically searching web.archive.org for sensitive URLs
- Educate users on the risks of sharing sensitive data via web-based note services

## Objectives

1. Locate archived private Simplenote notes
2. Extract sensitive information from exposed content
3. Demonstrate the impact of inadequate crawling protections

## Instructions

### Step 1: Search for Simplenote Endpoints

**Context**: Begin by querying the Wayback Machine for known Simplenote URL patterns to identify archived private notes.

No specific command required; use the web interface.

Navigate to http://web.archive.org and enter search terms like "http://app.simplenote.com/" or "http://simp.ly/p/" in the URL bar.

> This will display a calendar of available snapshots. Focus on recent dates to find current or near-current private notes.

### Step 2: Review and Access Snapshots

**Context**: Examine the archived pages for private note contents, verifying the presence of sensitive data.

Click on snapshot links to load the archived pages.

> Successful access shows the full text of private notes, potentially including emails, passwords, or shared confidential information. Validate by checking for non-public indicators like personal details not intended for broad sharing.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Search Engines]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/web.archive.org]]

## Tags

- information-disclosure
- wayback-machine
- simplenote
- privacy-leak
- reconnaissance
