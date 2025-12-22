---
id: ed94d2de-e3c1-4068-bc25-44e4ce6940f6
name: msfdb
type: tool
verified: true
created_at: '2019-08-28T21:17:42.035403+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - metasploit
  - database
  - management
url: >-
  https://docs.metasploit.com/docs/using-metasploit/interacting-with-database.html
commands:
  - '[[commands/msfdb-init-database]]'
  - '[[commands/msfdb-start-service]]'
  - '[[commands/msfdb-stop-service]]'
  - '[[commands/msfdb-status-check]]'
  - '[[commands/msfdb-reinitialize-database]]'
validated: true
---

# msfdb

**Status**: Unverified

## Overview

msfdb is a command-line utility within the Metasploit Framework for managing the PostgreSQL database that stores Metasploit's data, such as hosts, services, vulnerabilities, and loot from penetration tests. It is essential for setting up and maintaining the database backend required for Metasploit's console (msfconsole) to function properly. Common use cases include initializing the database on first install, starting/stopping the service during testing sessions, and troubleshooting database issues.

## Description

msfdb handles the lifecycle of Metasploit's PostgreSQL database, including creation, configuration, and maintenance. It automates tasks like setting up the database schema, starting the PostgreSQL server, and ensuring compatibility with Metasploit modules. This tool is particularly useful in offensive security operations where persistent data storage is needed for tracking exploits, payloads, and session data across multiple engagements. It supports integration with tools like msfconsole for querying and managing penetration test results.

## Features

- Database initialization and schema setup for Metasploit
- Service start/stop/restart functionality for PostgreSQL
- Status checks to verify database connectivity and health
- Reinitialization for resetting corrupted or outdated databases
- Cross-platform support via Ruby-based scripting

## Installation

### Requirements

- Metasploit Framework installed (msfdb is bundled with it)
- PostgreSQL server (automatically handled by msfdb on supported platforms)
- Ruby 2.7+ (included in Metasploit)

### Install Commands

msfdb requires Metasploit to be installed first.

```bash
# On Kali Linux (pre-installed)
sudo apt update && sudo apt install metasploit-framework

# On Ubuntu
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall

# On Windows (via installer)
# Download from https://windows.metasploit.com/metasploitframework-latest.msi and run

# On macOS (via Homebrew)
brew install metasploit
```

After installation, run `msfdb init` to set up the database.

## Basic Usage

```bash
msfdb --help
```

This displays all available subcommands and options for database management.

### Common Options

| Option | Description |
|--------|-------------|
| `--help, -h` | Show help message and exit |
| `--version, -v` | Display msfdb version |
| `init` | Initialize the database (subcommand) |
| `start` | Start the PostgreSQL service (subcommand) |
| `stop` | Stop the PostgreSQL service (subcommand) |

## Examples

### Example 1: Basic Usage

Initialize the database on first use:

```bash
msfdb init
```

### Example 2: Advanced Usage

Start the database service and check status:

```bash
msfdb start
msfdb status
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] System Binary Proxy Execution (as it manages infrastructure for exploitation tools)
- [[System Services]] System Services (database service management)

### Tactics

- [[Privilege Escalation]] Privilege Escalation (enabling advanced Metasploit features)
- [[Persistence]] Persistence (maintaining database for ongoing operations)

## Detection

Indicators and methods for detecting this tool's usage:

- Process monitoring for `postgres` or `msfdb` executions
- Log entries in Metasploit or system journals showing database initialization
- Network listening on PostgreSQL default port (5432) from unexpected sources
- File system changes in Metasploit directories (~/.msf4/database/ or /opt/metasploit/)

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Metasploit Framework]]
- [[PostgreSQL]]

## References

- Official Metasploit Documentation: https://docs.metasploit.com/docs/using-metasploit/interacting-with-database.html
- Rapid7 GitHub Repository: https://github.com/rapid7/metasploit-framework
