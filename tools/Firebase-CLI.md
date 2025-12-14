---
url: 'https://firebase.google.com/docs/cli'
tags:
  - cloud
  - hosting
  - deploy
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:31.335Z'
id: 094e81b2-e044-4d3b-8cce-e1621e2a162c
validated: true
submitted: true
---
# Firebase-CLI

**Status**: Unverified

## Overview

Firebase CLI is a command-line interface for managing Firebase projects, including deploying to Hosting, used here to quickly host malicious pages on free subdomains.

## Description

In security testing, it's abused for ingress of payloads via static hosting. Supports init, deploy, and auth; integrates with NodeJS.

## Features

- Feature 1: Easy deployment of static assets
- Feature 2: Project management and emulators
- Feature 3: Authentication via Google account

## Installation

### Requirements

- NodeJS >= 12

### Install Commands

```bash
npm install -g firebase-tools
firebase login
```

## Basic Usage

```bash
firebase --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-P, --project` | Specify project ID |
| `--only` | Deploy specific service |

## Examples

### Example 1: Basic Usage

```bash
firebase deploy
```

### Example 2: Advanced Usage

```bash
firebase deploy --only hosting -P my-project
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- firebase-tools process
- API calls to firebase.googleapis.com
- Deploy logs in Firebase console

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/NodeJS]]

## References

- Official documentation: https://firebase.google.com/docs/hosting/quickstart
