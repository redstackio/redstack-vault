---
id: 4d332c81-5082-41c4-a2a7-4398dd532702
type: tool
verified: true
created_at: '2019-08-28T21:17:23.807701+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - phishing
  - social-engineering
  - red-team
  - awareness-training
url: 'https://github.com/securestate/king-phisher'
validated: true
---

# King Phisher

**Status**: Unverified

## Overview

King Phisher is an open-source tool designed for simulating real-world phishing attacks to test and promote user awareness in security training and red team exercises. It allows security professionals to create, manage, and track phishing campaigns, including email templates, landing pages, and credential harvesting.

## Description

King Phisher consists of a server component for hosting campaigns and a client for administration. It supports features like SMTP integration for sending emails, database storage for captured data, and web-based interfaces for victims. Commonly used in penetration testing to evaluate employee susceptibility to phishing without risking real harm.

## Features

- Feature 1: Campaign management with customizable email templates and landing pages
- Feature 2: Real-time tracking of email opens, clicks, and credential submissions
- Feature 3: Integration with external SMTP servers for realistic email delivery
- Feature 4: Reporting and analytics for awareness training debriefs
- Feature 5: Support for multi-stage phishing lures and credential harvesting

## Installation

### Requirements

- Python 3.6+
- PostgreSQL database
- Git
- pip and virtualenv

### Install Commands

```bash
# Clone the repository
git clone https://github.com/securestate/king-phisher.git
cd king-phisher

# Create virtual environment
virtualenv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Install King Phisher
pip install .

# Set up database (example for PostgreSQL)
createdb king_phisher
psql -d king_phisher -f server/database/schema.sql
```

For Windows, use similar steps with appropriate path separators and activation.

## Basic Usage

```bash
king-phisher-server --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-c, --config` | Specify configuration file path |
| `--host` | Server bind address |
| `--port` | Server port |

## Examples

### Example 1: Basic Usage

Start the server:

```bash
king-phisher-server
```

Launch the client:

```bash
king-phisher-client --username admin --password password
```

### Example 2: Advanced Usage

Start server with custom config:

```bash
king-phisher-server --config /path/to/config.ini --host 0.0.0.0 --port 8443
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]] Phishing
- [[T1566.001]] Spearphishing Attachment
- [[T1566.002]] Spearphishing Link

### Tactics

- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual outbound SMTP traffic from internal servers
- Detection method 2: Web server logs showing requests to non-standard phishing domains
- Detection method 3: Database connections to PostgreSQL instances with King Phisher schemas
- Detection method 4: Process monitoring for king-phisher-server or client executables

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Gophish]]
- [[tools/SET]]

## References

- Official GitHub: https://github.com/securestate/king-phisher
- Documentation: https://docs.kingphisher.com
- Related resources: OWASP Phishing Awareness Guide
