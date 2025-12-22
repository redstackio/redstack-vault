---
id: 7acb7f52-136f-47d9-9ad4-c81433c248a3
type: tool
verified: true
created_at: '2019-08-28T21:17:32.878021+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - phishing
  - social-engineering
  - campaign-management
url: 'https://github.com/RSRC01/FiercePhish'
commands:
  - '[[commands/fiercephish-start-server]]'
  - '[[commands/fiercephish-create-campaign]]'
  - '[[commands/fiercephish-schedule-emails]]'
  - '[[commands/fiercephish-manage-sessions]]'
validated: true
---

# FiercePhish

**Status**: Unverified

## Overview

FiercePhish is an open-source phishing framework designed for managing comprehensive phishing engagements. It enables security professionals to create, track, and execute phishing campaigns, including email scheduling, landing page hosting, and real-time session monitoring. Commonly used in red team operations for simulating phishing attacks to test organizational awareness and defenses.

## Description

FiercePhish provides a centralized platform for phishing simulations, allowing users to set up multiple campaigns with customizable email templates, track recipient interactions, and harvest credentials from phishing pages. Built on Ruby on Rails, it includes features for database management of campaigns, integration with SMTP servers for email delivery, and a web-based dashboard for monitoring. It supports both automated and manual phishing workflows, making it suitable for training exercises, penetration testing, and security awareness programs.

## Features

- Feature 1: Campaign management with separate tracking for multiple phishing scenarios.
- Feature 2: Email scheduling and templating for realistic phishing simulations.
- Feature 3: Real-time session monitoring and credential capture from landing pages.
- Feature 4: Integration with external tools for payload delivery and reporting.
- Feature 5: Web-based admin interface for easy configuration and analytics.

## Installation

### Requirements

- Ruby 2.5+ and Rails 5.2+
- PostgreSQL or SQLite for database
- Bundler for dependency management
- Git for cloning the repository

### Install Commands

```bash
# Clone the repository
git clone https://github.com/RSRC01/FiercePhish.git
cd FiercePhish

# Install dependencies
bundle install

# Set up database
rails db:create
rails db:migrate

# For production, configure SMTP and web server (e.g., Puma or Passenger)
```

On Kali Linux or Ubuntu, ensure Ruby and development libraries are installed:
```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
```

## Basic Usage

```bash
# Start the Rails server
rails server -b 0.0.0.0 -p 3000
```
Access the web interface at http://localhost:3000 to configure campaigns.

### Common Options

| Option | Description |
|--------|-------------|
| `-b` | Bind address for the server (e.g., 0.0.0.0 for external access) |
| `-p` | Port to listen on (default 3000) |
| `-e` | Environment (development, production) |
| `--help` | Show Rails server help |

## Examples

### Example 1: Basic Usage

Start the server in development mode:
```bash
rails server
```
This launches the dashboard for creating campaigns.

### Example 2: Advanced Usage

Start in production mode with custom port and bind:
```bash
RAILS_ENV=production rails server -b 0.0.0.0 -p 8080
```
Configure SMTP in config files for email sending.

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

- Detection method 1: Unusual outbound SMTP traffic from non-standard ports or high-volume email sends.
- Detection method 2: Web server logs showing access to phishing landing pages or credential submission endpoints.
- Detection method 3: Network monitoring for Ruby/Rails processes hosting suspicious web content.
- Detection method 4: Endpoint detection of Ruby installations and bundle activity in unexpected locations.

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
- [[tools/King-Phisher]]
- [[tools/SET]]

## References

- Official GitHub Repository: https://github.com/RSRC01/FiercePhish
- Documentation: Included in repo README and Rails guides
- Related Resources: OWASP Phishing Awareness Project
