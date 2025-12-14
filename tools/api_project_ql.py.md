---
id: tool-api_project_ql.py
url: null
tags:
  - mock-script
  - python
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:14.538Z'
validated: true
submitted: true
---
# api_project_ql.py

**Status**: Unverified

## Overview

A custom Python Flask script that mocks GitLab's GraphQL API for bulk imports, responding with attacker-controlled import_source and template_name to enable command injection payloads.

## Description

The script simulates project queries, setting import_source to paths with shell metacharacters (e.g., '/tmp/ggg;echo lala|tee /tmp/1234;#') and import_type to 'project_entity'. It's configured with PROJECT_PATH, PROJECT_ID, and optional Burp proxy.

## Features

- Feature 1: GraphQL endpoint simulation
- Feature 2: Customizable payload injection
- Feature 3: JSON response formatting for GitLab compatibility

## Installation

### Requirements

- Python 3, Flask

### Install Commands

```bash
# Download from source (HackerOne or custom)
git clone <repo> or wget script
pip install flask
```

## Basic Usage

```bash
FLASK_APP=api_project_ql.py flask run
```

### Common Options

| Option | Description |
|--------|-------------|
| Edit PROJECT_PATH | Set to mock project path | N/A |
| Edit import_source | Inject payload | N/A |

## Examples

### Example 1: Basic Usage

Configure payload, run server, query /api/graphql.

### Example 2: Advanced Usage

Add proxy: Edit script with proxies dict for Burp.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]] Unix Shell

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Local Flask processes with GraphQL routes
- Responses containing shell metacharacters
- Unsolicited API calls from imports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/fake_server.py]]
- [[tools/Flask]]

## References

- Custom script from HackerOne report #1609965
