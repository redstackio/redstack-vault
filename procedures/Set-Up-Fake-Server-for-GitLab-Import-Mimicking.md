---
tags:
  - gitlab
  - fake-server
  - api-mimic
type: procedure
tools:
  - '[[tools/fake_server.py]]'
  - '[[tools/Flask]]'
  - '[[tools/Browser-Console]]'
  - '[[tools/Digest::SHA2]]'
  - '[[tools/Git]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - GitLab.com
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 65b21459-8d49-4121-bbbe-975ff69ced52
created_at: '2025-12-11T03:47:59.553Z'
updated_at: '2025-12-11T03:47:59.553Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Set Up Fake Server for GitLab Import Mimicking

## Summary

This procedure sets up a fake Flask server to mimic GitLab's import API, injecting a malicious 'file://' URL to exploit the repository import vulnerability.

## Description

The fake server responds to import requests by providing a crafted 'httpUrlToRepo' with the 'file://' protocol, tricking GitLab into fetching local repositories. This targets the improper validation in Gitlab::UrlBlocker, allowing access to any repository path on the server.

## Requirements

1. Python environment with Flask installed
2. Calculated repository path from project ID
3. Local machine to run the server

## Defense

Defensive measures and detection strategies:

- Implement schema restrictions in URL validation
- Monitor for anomalous import requests in GitLab

## Objectives

1. Create a server that fakes GitLab API responses
2. Inject malicious URL for local file access
3. Enable the import exploit chain

## Instructions

### Step 1: Download and Edit Script

**Context**: Obtain and modify fake_server.py with the target path.

Edit line 99 to include the hashed path, e.g., 'file:///var/opt/gitlab/git-data/repositories/@hashed/b1/74/b174103b399555239923697fbe124faa61de4d441bd5c5678275eb0a5a27a562.git'.

### Step 2: Run the Fake Server

**Context**: Start the Flask application to handle requests.

**Command** ([[commands/flask-run-fake-server]]):
```bash
FLASK_APP=fake_server.py FLASK_ENV=development flask run
```

> This starts the server on port 5000, ready to mimic the import process.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/flask-run-fake-server]]

## Tools Used

- [[tools/fake_server.py]]
- [[tools/Flask]]

## Tags

- #gitlab
- [[commands/flask-run-fake-server]]
- #api-mimic
