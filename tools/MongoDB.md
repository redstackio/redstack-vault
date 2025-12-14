---
url: 'https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/'
tags:
  - database
  - backend
type: tool
verified: false
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:30.222Z'
id: 1a595656-46a3-4fcf-be68-3243523cec78
validated: true
submitted: true
---
# MongoDB

**Status**: Unverified

## Overview

MongoDB is a NoSQL document database used as the backend for data storage in the meemo app during vulnerability reproduction.

## Description

Provides persistent storage for app data; in this context, required for meemo's operations alongside LDAP auth. Installed via Ubuntu packages.

## Features

- Feature 1: Schema-less document storage
- Feature 2: High availability with replication
- Feature 3: Horizontal scaling via sharding

## Installation

### Requirements

- Ubuntu 18.04+ or compatible
- Administrative access

### Install Commands

```bash
# Add MongoDB repo and install
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
```

## Basic Usage

```bash
mongod --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help |
| --port | Specify port |

## Examples

### Example 1: Basic Usage

```bash
sudo systemctl start mongod
```

### Example 2: Advanced Usage

```bash
mongod --dbpath /data/db --port 27017
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Port 27017 listening
- Process 'mongod' running
- Logs in /var/log/mongodb

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/node]]
- [[tools/ldapjstestserver]]

## References

- Official documentation: https://docs.mongodb.com/manual/
