---
id: proc-configure-mock-gitlab-api
tags:
  - mock-api
  - flask
  - payload-injection
type: procedure
tools:
  - '[[tools/api_project_ql.py]]'
  - '[[tools/Flask]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/flask-run-api-script]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:24:14.618Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Configure-Mock-GitLab-API-Server

## Summary

This procedure configures a Flask-based mock GitLab API server to simulate GraphQL responses, injecting a malicious import_source with shell metacharacters (e.g., ';echo lala|tee /tmp/1234;#') to exploit the command injection in BulkImports.

## Description

The mock server responds to GitLab's import queries, setting import_source to a path that breaks out of the gzip command ('gzip -dc #{@archive_path} | wc -c') via shell injection. Avoid '>' due to JSON escaping; use tee for output. Optional Burp proxy for request interception.

## Requirements

1. Python 3 with Flask installed
2. GitLab project details (ID, path) for mock responses
3. Local network for server hosting

## Defense

Defensive measures and detection strategies:

- Validate all external API endpoints in import sources
- Use allowlists for import origins
- Monitor for anomalous GraphQL queries or unexpected payloads

## Objectives

1. Simulate malicious import source control
2. Deliver shell injection payload
3. Enable RCE during validation

## Instructions

### Step 1: Download and Edit Script

**Context**: Prepare the mock server script with payload.

**Instructions**: Download api_project_ql.py, set PROJECT_PATH='/group/project', PROJECT_ID=1, import_source='/tmp/ggg;echo lala|tee /tmp/1234;#', template_name='project_entity'. Add Burp proxy if needed: proxies={'http':'http://127.0.0.1:8080'}.

### Step 2: Run the Server

**Context**: Start the Flask app on port 5000.

**Command** ([[commands/flask-run-api-script]]):
```bash
FLASK_APP=api_project_ql.py flask run
```

> Server binds to 127.0.0.1:5000; test with curl to /api/graphql endpoint.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Unix Shell]] Unix Shell

### Sub-Techniques


## Commands Used

- [[commands/flask-run-api-script]]

## Tools Used

- [[tools/api_project_ql.py]]
- [[tools/Flask]]

## Tags

- mock-api
- payload-injection
