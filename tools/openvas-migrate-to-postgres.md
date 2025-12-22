---
id: 729a99f7-8759-49be-9de6-5e42125aec24
type: tool
verified: true
created_at: '2019-08-28T21:17:37.622069+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - vulnerability-scanning
  - migration
  - database
  - openvas
  - gvm
url: >-
  https://greenbone.github.io/docs/latest/22.4/source-build/html/chapter-migrate.html
validated: true
---

# openvas-migrate-to-postgres

**Status**: Unverified

## Overview

The openvas-migrate-to-postgres tool is a utility for migrating OpenVAS (now part of Greenbone Vulnerability Manager - GVM) data from legacy database backends like SQLite or MySQL to PostgreSQL. This migration enhances performance, scalability, and reliability for large-scale vulnerability scanning and management operations in security testing environments.

## Description

OpenVAS is an open-source vulnerability scanner framework that provides comprehensive scanning capabilities, backed by a feed of over 50,000 Network Vulnerability Tests (NVTs). The migration tool facilitates transitioning the backend database to PostgreSQL, which is recommended for production deployments due to better handling of concurrent operations and larger datasets. It preserves all scan configurations, results, and user data during the process. This tool is particularly useful for red teams and security operations centers upgrading their scanning infrastructure.

## Features

- Feature 1: Supports migration from SQLite, MySQL, or other SQL backends to PostgreSQL.
- Feature 2: Data integrity checks and schema validation during transfer.
- Feature 3: Verbose logging and error handling for troubleshooting migrations.
- Feature 4: Integration with GVM services for seamless post-migration setup.

## Installation

### Requirements

- PostgreSQL server (version 9.6 or later) installed and running.
- OpenVAS/GVM source code or packages.
- Python 3 with required libraries (e.g., psycopg2 for Postgres, pymysql for MySQL).
- Administrative access to source and target databases.

### Install Commands

```bash
# On Kali Linux or Ubuntu (assuming GVM is installed via source)
sudo apt update
sudo apt install postgresql postgresql-contrib

# Clone and build GVM if not already installed
git clone https://github.com/greenbone/gvmd.git
cd gvmd
mkdir build && cd build
cmake ..
make
sudo make install

# The migration tool is typically included in gvmd utilities
sudo ln -s /usr/local/sbin/openvas-migrate-to-postgres /usr/bin/openvas-migrate-to-postgres
```

For containerized setups, use the official Greenbone Community Edition Docker images with Postgres backend.

## Basic Usage

```bash
openvas-migrate-to-postgres --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and usage |
| -v, --verbose | Enable detailed logging |
| --dry-run | Simulate migration without committing changes |

## Examples

### Example 1: Basic Usage

Migrate from default SQLite to local Postgres:

```bash
openvas-migrate-to-postgres --source sqlite:///var/lib/openvas/mgr/data-objects.sqlite --target postgres://gvmd:password@localhost/gvmd
```

### Example 2: Advanced Usage

Migrate from MySQL with verbose output:

```bash
openvas-migrate-to-postgres --source mysql://openvas:pass@192.168.1.10/openvas --target postgres://gvmd:password@db-server/gvmd --verbose --dry-run
```

After migration, restart GVM services and update configuration to point to the new database.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for vulnerability assessment post-migration)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Log entries in GVM or Postgres logs showing migration scripts execution.
- Detection method 2: Database schema changes or connection spikes during migration periods.
- Detection method 3: File system artifacts like temporary migration logs in /var/lib/openvas/.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/openvas]]
- [[tools/gvm]]
- [[tools/postgresql]]

## References

- Official Greenbone Documentation: https://greenbone.github.io/docs/
- GVM Migration Guide: https://greenbone.github.io/docs/latest/22.4/source-build/html/chapter-migrate.html
- OpenVAS Community Forum for troubleshooting.
