---
tags:
  - reconnaissance
  - domain-discovery
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
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:24:08.087Z'
sub_techniques: []
id: e88f735f-881f-4311-9ebb-96f89ba78bfa
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Discover-and-Identify-reverb-twitter-com-Endpoint

## Summary

This procedure involves researching Twitter's Bug Bounty Program to discover the reverb.twitter.com domain and identify the unauthenticated /api/actions/saveImage.php endpoint, which lacks input validation.

## Description

During reconnaissance on Twitter's infrastructure, the reverb.twitter.com domain (also reverb.guru) is identified as a backend for the Twitter Reverb application, which generates data visualizations. Probing reveals the saveImage.php endpoint accepts POST requests with 'image', 'filename', and 'extension' parameters without authentication, allowing file creation in /var/www/html/view/data/image/. This sets the stage for exploitation via directory traversal and unrestricted uploads.

## Requirements

1. Access to Twitter Bug Bounty Program documentation or public sources
2. Tools for domain enumeration (e.g., browser, curl)
3. Public internet access

## Defense

Defensive measures and detection strategies:

- Implement domain scoping in bug bounty programs to limit exposure
- Use web application firewalls (WAF) to block reconnaissance probes
- Monitor for unusual API endpoint accesses in logs

## Objectives

1. Identify backend domains associated with Twitter services
2. Confirm unauthenticated endpoints for further testing
3. Map the application's file handling behavior

## Instructions

### Step 1: Research Twitter Bug Bounty

**Context**: Review public reports and program details to find references to reverb.twitter.com.

No specific command; use search engines or HackerOne to identify the domain as a visualization backend.

> Expected: Documentation confirming reverb.twitter.com handles TwitterReverb app data.

### Step 2: Probe for Endpoints

**Context**: Test for API endpoints without authentication.

Use curl to send a basic POST:

```bash
curl -X POST https://reverb.twitter.com/api/actions/saveImage.php -d "image=test&filename=test&extension=png" -v
```

> The -v flag shows headers; expect 200 OK without auth challenges.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Reconnaissance]]
- [[web-app]]
