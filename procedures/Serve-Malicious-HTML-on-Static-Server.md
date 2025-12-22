---
id: proc-serve-og-xss
tags:
  - web-server
  - poc-hosting
type: procedure
tools:
  - '[[tools/static-server]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Node.js
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Web Protocols]]'
updated_at: '2025-12-14T03:16:20.512Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Web Protocols]]'
---
# Serve-Malicious-HTML-on-Static-Server

## Summary

This procedure hosts the malicious HTML and JS files on a local static server to mimic an attacker-controlled website, making it available for scraping by metascraper.

## Description

The attacker needs to serve the files over HTTP on port 8080. This step uses a simple static server tool. In a real attack, this could be any web host. Expected outcome: The URL http://127.0.0.1:8080/article.html is accessible with the malicious OG metadata.

## Requirements

1. Static server tool installed (e.g., via npm or Python's http.server)
2. Files article.html and malware.js in the server root
3. Port 8080 available

## Defense

Defensive measures and detection strategies:

- Block or scan hosted content for script injections in meta tags
- Use CSP headers on scraping targets to prevent inline script execution
- Log and alert on unusual meta property contents

## Objectives

1. Expose malicious page for HTTP fetching
2. Ensure JS file is servable at the same origin
3. Validate accessibility before proceeding

## Instructions

### Step 1: Prepare Directory and Start Server

**Context**: Place files in root and launch the static server on port 8080.

No specific command; use a tool like Python's http.server or npm http-server:

```bash
# Using Python (if available)
python -m http.server 8080

# Or install and use http-server via npm
npm install -g http-server
http-server -p 8080
```

> Server starts, serving files at http://127.0.0.1:8080. Verify by curling the URL or browsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Web Protocols]] Web Protocols

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/static-server]]

## Tags

- [[web-server]]
- [[poc-hosting]]
