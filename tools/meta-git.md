---
id: 123e4567-e89b-12d3-a456-426614174014
name: meta-git
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:20.152Z'
platforms:
  - Linux
  - Node.js
tags:
  - git-plugin
  - vulnerable
url: 'https://www.npmjs.com/package/meta-git'
validated: true
submitted: true
---

# meta-git

**Status**: Unverified

## Overview

meta-git is a Node.js module for git operations within the meta framework, vulnerable to RCE in version 1.1.2 due to unsanitized shell command formatting.

## Description

This tool provides git clone and update functionalities but insecurely formats user input into shell commands, allowing command injection. Used in attacks to execute arbitrary code via malicious repository names.

## Features

- Feature 1: Git clone integration for Node.js apps
- Feature 2: Update mechanisms for meta projects
- Feature 3: Shell-based execution (vulnerable point)

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm i meta-git -g
```

## Basic Usage

```bash
meta-git --help
```

### Common Options

| Option | Description |
|--------|-------------|
| clone | Clone a repository |
| update | Update git resources |

## Examples

### Example 1: Basic Usage

```bash
meta-git clone repo-url
```

### Example 2: Advanced Usage

```bash
meta-git clone 'malicious||command'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Unix Shell]]
- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Look for meta-git processes spawning shell commands
- Audit npm logs for installation of version 1.1.2

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[Related Tool: git]]

## References

- Official documentation: https://www.npmjs.com/package/meta-git
- Vulnerability report: https://hackerone.com/reports/728040
