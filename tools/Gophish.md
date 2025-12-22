---
id: 664f7616-faab-4f3a-bc66-fe41df981177
name: Gophish
type: tool
verified: true
created_at: '2019-08-28T21:17:26.391592+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - phishing
  - social-engineering
  - awareness-training
url: 'https://getgophish.com/'
validated: true
---

# Gophish

**Status**: Unverified

## Overview

Gophish is an open-source phishing toolkit designed for penetration testers, security teams, and organizations conducting security awareness training. It allows users to create and launch phishing campaigns, track user interactions, and simulate real-world phishing attacks to educate employees on recognizing and avoiding phishing attempts.

## Description

Gophish provides a user-friendly web-based interface for managing phishing simulations. Key capabilities include designing email templates, creating realistic landing pages, sending emails via SMTP integration, and monitoring clicks, submissions, and other interactions in real-time. It supports importing user lists from CSV files, scheduling campaigns, and generating reports on campaign effectiveness. Commonly used in red team exercises to test phishing defenses and in blue team training to improve awareness. The tool runs as a self-contained binary with an embedded web server, making it easy to deploy on various platforms without complex dependencies.

## Features

- **Campaign Management**: Create, launch, and track phishing campaigns with customizable timelines.
- **Email Templates**: Built-in editor for HTML emails with dynamic content like user names and links.
- **Landing Pages**: Host fake websites to capture credentials or simulate malware downloads.
- **Tracking Pixels**: Monitor email opens and link clicks without requiring external trackers.
- **User Import/Export**: Bulk import targets from CSV and export results for analysis.
- **API Access**: RESTful API for automation and integration with other tools.
- **Reporting**: Generate statistics on success rates, per-user interactions, and overall campaign metrics.

## Installation

### Requirements

- Go 1.8 or later (for building from source, optional).
- SMTP server access for sending emails (e.g., Gmail, Office 365, or self-hosted).
- Ports 3333 (admin) and 80/443 (phishing server) available.

### Install Commands

For Linux (Kali/Ubuntu):

```bash
# Download the latest release from GitHub
wget https://github.com/gophish/gophish/releases/download/v0.12.1/gophish-v0.12.1-linux-64bit.zip

# Unzip the archive
unzip gophish-v0.12.1-linux-64bit.zip

# Make the binary executable
chmod +x gophish

# On first run, it will generate self-signed certificates in the config.json
```

For Windows:

Download the Windows ZIP from the releases page, extract, and run `gophish.exe` from Command Prompt.

For macOS:

Similar to Linux; download the Darwin ZIP, unzip, and run `./gophish`.

Building from source (optional):

```bash
go install github.com/gophish/gophish@latest
```

## Basic Usage

```bash
./gophish
```

This starts the admin server on https://127.0.0.1:3333 (default credentials: admin/gophish). Access the web UI to configure and launch campaigns.

### Common Options

| Option | Description |
|--------|-------------|
| `-admin https://0.0.0.0:3333` | Set admin server listen address and protocol |
| `-phish https://0.0.0.0:80` | Set phishing server listen address |
| `-dev` | Enable development mode (disables security checks) |
| `-config /path/to/config.json` | Use custom config file |

## Examples

### Example 1: Basic Usage

Start Gophish with default settings:

```bash
./gophish
```

Navigate to https://localhost:3333, log in, and create your first campaign.

### Example 2: Advanced Usage

Start with custom ports and external access:

```bash
./gophish -admin https://0.0.0.0:8443 -phish https://0.0.0.0:8080
```

This binds the admin interface to port 8443 and phishing server to 8080 for remote access (use firewall rules to restrict).

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

- Unusual outbound SMTP traffic from internal servers.
- DNS queries or connections to newly registered domains mimicking legitimate ones.
- Web server logs showing requests to non-standard phishing paths (e.g., /track, /submit).
- Network traffic on non-standard ports (e.g., 3333 for admin).
- File artifacts like gophish binary or config.json with self-signed certs.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/SET]] (Social-Engineer Toolkit)
- [[tools/King-Phisher]]

## References

- Official Documentation: https://docs.getgophish.com/
- GitHub Repository: https://github.com/gophish/gophish
- User Guide: https://getgophish.com/documentation
