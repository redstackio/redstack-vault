---
id: tool-create-git
url: 'https://www.npmjs.com/package/create-git'
tags:
  - npm
  - git
  - rce
type: tool
verified: false
platforms:
  - Node.js
  - JavaScript
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:19.627Z'
validated: true
submitted: true
---
# create-git

**Status**: Unverified

## Overview

create-git is an NPM module designed for programmatically creating Git repositories in Node.js applications, handling initialization, commits, and remote setup. In vulnerable versions, it enables RCE through command injection, commonly used in security testing to demonstrate supply chain risks in third-party dependencies.

## Description

The tool automates Git repository creation via JavaScript, invoking shell commands through child_process.exec() without input sanitization. This makes it exploitable for injecting arbitrary commands via parameters like remoteOrigin. It was the subject of HackerOne report #694471, where the fix involved safer execution APIs. Use in offensive security to test Node.js apps for deserialization flaws.

## Features

- Feature 1: Automatic Git repo initialization and first commit
- Feature 2: Remote origin addition and template ignoring
- Feature 3: Options for ignoring existing repos and custom commit messages

## Installation

### Requirements

- Node.js 10+ installed
- NPM package manager

### Install Commands

```bash
npm install create-git
```

## Basic Usage

```javascript
const createGit = require('create-git');
createGit({});
```

### Common Options

| Option | Description |
|--------|-------------|
| ignoreExisting | Skip if repo exists (boolean) |
| initialCommitMessage | Commit message string |
| remoteOrigin | Remote URL string (vulnerable to injection) |
| ignoreTemplates | Array of ignored templates |

## Examples

### Example 1: Basic Usage

```javascript
const createGit = require('create-git');
createGit({ initialCommitMessage: 'Hello World' });
```

### Example 2: Advanced Usage

```javascript
const createGit = require('create-git');
createGit({
  remoteOrigin: 'https://github.com/user/repo.git',
  ignoreTemplates: ['Node']
});
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor NPM installs for create-git in vulnerable versions (< fixed release)
- Log child_process.exec() calls with git commands containing user inputs
- Scan Node.js apps for direct concatenation of inputs into shell executions

## Related Procedures

- [[procedures/Exploit-Command-Injection-in-create-git]]

## Related Tools

- [[tools/child_process-exec]]

## References

- NPM page: https://www.npmjs.com/package/create-git
- HackerOne Report: https://hackerone.com/reports/694471
