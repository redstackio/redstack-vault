---
id: 3d8f7e67-6a15-48c4-923b-def185cb676b
type: tool
verified: true
description: >-
  Open-source collaboration framework for managing security assessment data,
  enabling information sharing and report generation during penetration tests.
url: 'https://dradisframework.com/'
created_at: '2019-08-28T21:17:23.058212+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - collaboration
  - reporting
  - pentest
validated: true
---

# dradis

**Status**: Unverified

## Overview

Dradis is an open-source framework designed for effective information sharing during security assessments, particularly penetration testing and red team operations. It acts as a centralized web-based repository to track progress, store findings, manage notes, and generate reports, facilitating collaboration among team members.

## Description

Dradis provides a self-contained Ruby on Rails web application that serves as a knowledge base for security engagements. It allows teams to organize data hierarchically (e.g., by host or issue), attach evidence, integrate with tools like Nessus or Burp Suite via plugins, and automate report creation. Commonly used in offensive security to streamline workflows from reconnaissance to debriefing, reducing email chains and scattered documentation.

## Features

- Feature 1: Hierarchical node structure for organizing findings by target, issue type, or phase.
- Feature 2: Support for file attachments, including screenshots, logs, and exploit outputs.
- Feature 3: Plugin ecosystem for importing data from tools (e.g., Metasploit, Nmap) and exporting reports in multiple formats (HTML, PDF, Word).
- Feature 4: User authentication and role-based access for team collaboration.
- Feature 5: Customizable templates for professional report generation.

## Installation

### Requirements

- Ruby 2.7+ and Rails 6+
- PostgreSQL or MySQL database
- Bundler and Git
- At least 2GB RAM for server operation

### Install Commands

For Ubuntu/Kali Linux (recommended):

```bash
# Install dependencies
sudo apt update && sudo apt install -y ruby-dev build-essential libpq-dev postgresql

# Install PostgreSQL and create database
sudo service postgresql start
sudo -u postgres createdb dradis

# Clone and install Dradis
git clone https://github.com/dradis/dradis-ce.git
cd dradis-ce
bundle install

# Set up database
bundle exec rake db:setup

# Start the server (see related command)
```

For Docker (cross-platform):

```bash
docker pull dradis/dradis-ce
mkdir -p ~/dradis-plugins
# Mount volume for plugins and run
```

On Windows/macOS, use Docker or WSL for best compatibility.

## Basic Usage

```bash
dradis-ctl start
```

Access the web interface at http://localhost:3000 and log in with default credentials (admin/dradis) to create projects and add nodes.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help for dradis-ctl commands |
| `-v, --version` | Display Dradis version |
| `--config` | Specify custom configuration file |

## Examples

### Example 1: Basic Usage

Start the server and access the UI:

```bash
dradis-ctl start
# Then browse to http://localhost:3000
```

### Example 2: Advanced Usage

Upload evidence via CLI while server runs:

```bash
dradis upload evidence.txt -n 1
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- N/A (Dradis is a reporting and collaboration tool, not directly tied to ATT&CK techniques; used post-exploitation for documentation).

### Tactics

- [[Command and Control]] (Original File Creation - for report generation in command and control phases).

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Running processes like "ruby" or "rails server" on non-standard ports (e.g., 3000) during assessments.
- Detection method 2: Network traffic to localhost:3000 or plugin integrations pulling data from scanners.
- Detection method 3: File artifacts like dradis.log or exported reports in team shares.

## Related Commands

- [[commands/dradis-start-server]]
- [[commands/dradis-upload-evidence]]
- [[commands/dradis-export-report]]

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Nessus]] (for evidence import)
- [[tools/Burp-Suite]] (for plugin integration)

## References

- Official documentation: https://docs.dradisframework.com/
- GitHub repository: https://github.com/dradis/dradis-ce
- Community plugins: https://github.com/dradis/dradis-plugins
