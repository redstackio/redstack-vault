---
tags:
  - web-server
  - apache
  - hosting
type: procedure
tools:
  - '[[tools/Apache]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/analyze-apache-logs-for-snapchat-requests]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
updated_at: '2025-12-14T04:38:49.729Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
id: ff8447d2-eb55-4059-96b0-7815b3845f6a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Set Up Apache Server on Taken Over Subdomain

## Summary

This procedure configures an Apache web server as a backend for the taken-over Fastly subdomain to host proof-of-concept content and log incoming requests from Snapchat clients.

## Description

After takeover, the Fastly service routes traffic to an Apache instance. The server hosts static files like /takeover.html and logs access to monitor exploitation. This setup allows serving arbitrary unauthenticated content to clients querying CDN paths.

## Requirements

1. Control over a server with Apache installed.
2. Fastly backend configuration pointing to the Apache host.
3. Log access permissions.

## Defense

Defensive measures and detection strategies:

- Monitor CDN traffic for anomalous backends.
- Rate-limit unauthenticated CDN endpoints.
- Alert on unexpected server responses from subdomains.

## Objectives

1. Host demonstration content on the subdomain.
2. Capture and analyze client requests.
3. Verify active use by target applications.

## Instructions

### Step 1: Configure Apache

**Context**: Install and set up Apache to serve content.

**Command** (Basic Setup):
```bash
sudo apt update && sudo apt install apache2
sudo systemctl start apache2
```

> Create /var/www/html/takeover.html with proof-of-concept text.

### Step 2: Analyze Logs

**Context**: Filter logs for Snapchat client requests using [[commands/analyze-apache-logs-for-snapchat-requests]].

**Command** ([[commands/analyze-apache-logs-for-snapchat-requests]]):
```bash
cat /var/log/apache2/access.log | grep -v server-status | grep snapchat -i
```

> Expected output: Entries like '23.235.39.33 - - [02/Aug/2016:18:28:25 +0000] "GET /bq/story_blob?..." 404 ... "Snapchat/9.21.1.1"'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Sub-Techniques

- None

## Commands Used

- [[commands/analyze-apache-logs-for-snapchat-requests]]

## Tools Used

- [[tools/Apache]]

## Tags

- [[web-server]]
- [[tools/Apache]]
- [[hosting]]
