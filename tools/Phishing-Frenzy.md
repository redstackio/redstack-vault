---
id: c9f38ecf-3969-4008-9d59-88a67d0c59c7
type: tool
verified: true
created_at: '2019-08-28T21:17:36.208285Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - phishing
  - framework
  - ruby-on-rails
  - social-engineering
url: 'https://github.com/undergroundwires/Phishing-Frenzy'
validated: true
---

# Phishing-Frenzy

**Status**: Unverified

## Overview

Phishing Frenzy is a Ruby on Rails-based framework designed for creating, managing, and executing phishing campaigns in security testing and red team operations. It allows users to clone legitimate websites, generate phishing pages, send targeted emails, and track victim interactions such as clicks and credential submissions. Commonly used for simulating phishing attacks to train defenders or assess organizational awareness.

## Description

Built on Ruby on Rails, Phishing Frenzy provides a web-based admin interface for campaign management. Key capabilities include site cloning via templates, email template customization, SMTP integration for sending phishing emails, and real-time analytics for opens, clicks, and captures. It supports integration with external tools like ngrok for tunneling and databases for storing results. Ideal for penetration testers needing a customizable phishing platform without relying on commercial tools.

## Features

- Feature 1: Easy site generation from GitHub templates or local clones
- Feature 2: Built-in email sending with SMTP support and personalization
- Feature 3: Real-time dashboard for tracking campaign metrics and captured data
- Feature 4: Exportable results in CSV/JSON for analysis
- Feature 5: Modular design for custom payloads and post-capture actions

## Installation

### Requirements

- Ruby 2.7+ and Rails 6.0+
- Bundler 2.0+
- Database (SQLite for dev, PostgreSQL/MySQL for prod)
- SMTP server access for email sending

### Install Commands

```bash
# Clone the repository
git clone https://github.com/undergroundwires/Phishing-Frenzy.git
cd Phishing-Frenzy

# Install dependencies
bundle install

# Setup database
rails db:create db:migrate

# Optional: Configure SMTP in config/initializers/smtp.rb
```

For Kali Linux/Ubuntu:
```bash
sudo apt update
sudo apt install ruby-full build-essential zlib1g-dev
# Then follow the clone and bundle steps above
```

## Basic Usage

```bash
rails server
```

Access the admin interface at http://localhost:3000/admin to create campaigns.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -v, --verbose | Verbose output during generation/sending |
| --environment production | Run in production mode |

## Examples

### Example 1: Basic Usage

Start the server and generate a site:
```bash
rails server &
rails generate phishing:site demo --template https://github.com/example/login-page.git
```

### Example 2: Advanced Usage

Create and launch a campaign:
```bash
rails phishing:campaign:create --name test --target-list targets.csv --site demo --smtp smtp.gmail.com:587:user:pass
rails phishing:campaign:send test
rails phishing:results:view --campaign test
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

- Detection method 1: Unusual outbound SMTP traffic from development servers
- Detection method 2: Web server logs showing cloned site requests or credential POSTs
- Detection method 3: Network monitoring for phishing domain resolutions or email patterns
- Detection method 4: Rails/Puma process signatures on non-standard ports

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
- [[tools/Ngrok]]

## References

- Official GitHub: https://github.com/undergroundwires/Phishing-Frenzy
- Rails Documentation: https://guides.rubyonrails.org/
- Phishing Best Practices: https://www.phishme.com/

Related Commands:
- [[commands/phishing-frenzy-start-server]]
- [[commands/phishing-frenzy-generate-site]]
- [[commands/phishing-frenzy-create-campaign]]
- [[commands/phishing-frenzy-view-results]]
