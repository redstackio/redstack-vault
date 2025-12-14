---
tags:
  - recon
  - tomcat
  - file-upload
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Windows
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:37.073Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 3d615087-7b71-4580-8f1c-517f35c0e353
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Write-Enabled Default Servlet in Tomcat

## Summary

This procedure identifies if Apache Tomcat's default servlet is configured to allow writes (readonly=false), which is a prerequisite for file upload exploits on case-insensitive file systems like Windows.

## Description

The default servlet in Tomcat handles static content and, when write-enabled, permits HTTP PUT requests for file uploads. This configuration is vulnerable on case-insensitive systems where extension checks can be bypassed. The procedure involves probing the server with a test upload to confirm writability, targeting the root webapp path. Expected outcomes include successful file persistence, indicating the vulnerability setup.

## Requirements

1. Network access to the Tomcat server (port 8080 default)
2. HTTP client capable of PUT requests (e.g., curl)
3. Knowledge of the target URL path

## Defense

Defensive measures and detection strategies:

- Set default servlet to readonly=true in server.xml or web.xml
- Monitor HTTP PUT requests in access logs for anomalous uploads
- Use web application firewalls (WAF) to block unexpected PUT methods

## Objectives

1. Confirm write-enabled servlet configuration
2. Validate case-insensitive file system behavior
3. Establish baseline for further exploitation

## Instructions

### Step 1: Probe for Write Access

**Context**: Send a test PUT request to upload a harmless file and check server response.

Execute a PUT request using curl:

```bash
curl -X PUT -d "test content" http://target:8080/test.txt
```

> This command uploads a simple text file. A successful response (201 or 204) confirms write access; failure indicates readonly mode or restrictions.

### Step 2: Verify File Persistence

**Context**: Download the uploaded file to ensure it was stored correctly.

Execute a GET request:

```bash
curl http://target:8080/test.txt
```

> Expected output: The content "test content" returned, proving the file exists and is accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[tomcat]]
