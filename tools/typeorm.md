---
url: 'https://www.npmjs.com/package/typeorm'
tags:
  - orm
  - database
type: tool
verified: false
platforms:
  - Node.js
  - MySQL
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:15.114Z'
id: 1b3a4345-4fc0-4b43-be4e-1903890d121a
validated: true
submitted: true
---
# typeorm

**Status**: Unverified

## Overview

TypeORM is an ORM for TypeScript and JavaScript, supporting MySQL and others, used here to demonstrate a SQL injection vulnerability in its query builder.

## Description

It simplifies database interactions but has a flaw in MysqlDriver.ts where function parameters aren't escaped, allowing injection. Version 0.2.14 is vulnerable; used for setup and exploitation in local Node.js apps.

## Features

- Feature 1: Entity-based querying
- Feature 2: Migration support
- Feature 3: Query builder with parameterization

## Installation

### Requirements

- Node.js v8+
- MySQL server

### Install Commands

```bash
npm install typeorm mysql2 reflect-metadata
```

## Basic Usage

```bash
typeorm --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `init` | Initialize project |
| `migration:run` | Run migrations |

## Examples

### Example 1: Basic Usage

```bash
typeorm init --name Test
```

### Example 2: Advanced Usage

```bash
typeorm entity:create src/entity/User
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploit Public-Facing Application]]

### Tactics

- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Dependency scans for vulnerable versions (0.2.14)
- Query logs showing unescaped functions

## Related Procedures

- [[procedures/Modify-Script-for-Injection]]

## Related Tools

- [[tools/Node.js]]

## References

- Official documentation: https://typeorm.io
