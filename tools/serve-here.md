---
url: 'https://www.npmjs.com/package/serve-here'
tags:
  - web-server
  - static-server
  - vulnerable
type: tool
verified: false
platforms:
  - Linux
  - Node.js
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:11.869Z'
id: 8bdd43b8-9384-462a-94b1-c7975d91f93d
validated: true
submitted: true
---
# serve-here

**Status**: Unverified

## Overview

serve-here is a lightweight Node.js package for serving static files from the current directory as a simple HTTP web server. It's used in development but vulnerable to directory traversal in version 3.2.0, allowing arbitrary file reads.

## Description

This tool provides a CLI binary 'here' to quickly spin up a server without configuration. Features include port binding and basic serving. In security contexts, it's exploited for path traversal via unsanitized URL paths, enabling info disclosure on misconfigured hosts.

## Features

- Feature 1: Instant server startup from current directory
- Feature 2: Customizable port and host binding
- Feature 3: Simple static file delivery (vulnerable to traversal)

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install -g serve-here@3.2.0
```

## Basic Usage

```bash
here --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-p, --port` | Specify port |
| `-h, --host` | Bind to host |

## Examples

### Example 1: Basic Usage

```bash
here -p 8081
```

### Example 2: Advanced Usage

```bash
here -p 8081 --host 0.0.0.0
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for 'node' running serve-here scripts
- Port scans for ephemeral HTTP servers on ports like 8080/8081
- Log analysis for traversal attempts in access logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/http-server]]
- [[tools/Node.js]]

## References

- Official documentation: https://www.npmjs.com/package/serve-here
- Related resources: HackerOne report #296254
