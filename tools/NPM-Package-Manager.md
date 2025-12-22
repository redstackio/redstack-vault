---
url: 'https://www.npmjs.com/'
tags:
  - package-manager
  - setup
type: tool
verified: false
platforms:
  - Node.js
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.047Z'
id: 64d92944-caa3-4a51-880b-7de618c85fe0
validated: true
submitted: true
---
# NPM-Package-Manager

**Status**: Unverified

## Overview

npm is the default package manager for Node.js, used to install, share, and manage code dependencies like the vulnerable query-mysql module in security testing.

## Description

npm handles dependency resolution, versioning, and installation from the npm registry. In offensive security, it's used to deploy vulnerable components for local exploitation demos, such as SQLi in third-party modules.

## Features

- Feature 1: Install packages globally or locally
- Feature 2: Manage package.json dependencies
- Feature 3: Run scripts and audits for vulns

## Installation

### Requirements

- Node.js installed

### Install Commands

```bash
# npm comes with Node.js
node -v  # Verify
npm -v   # Should show 5.5.1 or later
```

## Basic Usage

```bash
npm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -g, --global | Install globally |
| --save | Add to package.json |
| -v, --version | Show version |

## Examples

### Example 1: Basic Usage

```bash
npm install query-mysql
```

### Example 2: Advanced Usage

```bash
npm audit  # Check for vulns
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- npm install logs in CI/CD
- node_modules directory creation
- Network traffic to registry.npmjs.org

## Related Procedures

- [[procedures/Install-query-mysql-Module]]

## Related Tools

- [[Yarn]]
- [[pnpm]]

## References

- Official documentation: https://docs.npmjs.com
- Related resources: Node.js security best practices
