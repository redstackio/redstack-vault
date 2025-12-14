---
url: null
tags:
  - fake-server
  - github-mock
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.951Z'
id: 0274b77c-da15-4b22-ba2a-4a3260a03666
validated: true
submitted: true
---
# Dummy-GitHub-Server

**Status**: Unverified

## Overview

A custom or scripted server mimicking GitHub's API to host fake repositories with malicious data, used for testing import vulnerabilities like XSS in label colors.

## Description

In this attack, the dummy server responds to GitLab's import requests with repository metadata including scoped labels containing XSS payloads. It's typically a Node.js/ Python script or tool like json-server configured to emulate /repos/{repo}/labels endpoint.

## Features

- Feature 1: Mocks GitHub API endpoints for repos and labels
- Feature 2: Serves custom JSON with injected payloads (e.g., malicious color strings)
- Feature 3: Runs on custom port (e.g., 11211) for isolated testing

## Installation

### Requirements

- Node.js or Python runtime
- Port 11211 available

### Install Commands

```bash
# Example with json-server (npm install -g json-server)
# Create db.json with repo/label data
json-server --watch db.json --port 11211
```

## Basic Usage

```bash
tool-name --port 11211 --data malicious-labels.json
```

### Common Options

| Option | Description |
|--------|-------------|
| `--port` | Listen port |
| `--host` | Bind IP |
| `--data` | JSON file with mock data |

## Examples

### Example 1: Basic Usage

```bash
json-server --port 11211 db.json
```

### Example 2: Advanced Usage

```bash
# db.json: {"labels": [{"name":"yvvdwf::label-name","color":">...<script>..."}]}
json-server --host 0.0.0.0 --port 11211 db.json
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Encrypted Channel]]

### Tactics

- [[Execution]]
- [[Impact]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual inbound traffic to non-standard ports (11211)
- DNS queries or connections to attacker-controlled IPs
- API responses with malformed data during imports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[json-server]]
- [[WireMock]]

## References

- Related resources: GitHub API documentation for endpoint emulation
