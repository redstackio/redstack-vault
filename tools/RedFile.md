---
id: 6864774d-fa8b-4afc-a2a3-5103e50c6100
type: tool
verified: true
created_at: '2019-08-28T21:17:36.275703+00:00'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
  - macOS
tags:
  - redteam
  - payload-delivery
  - flask
  - wsgi
url: 'https://github.com/example/redfile'
commands:
  - '[[commands/redfile-start-server]]'
  - '[[commands/redfile-generate-payload-config]]'
validated: true
---

# RedFile

**Status**: Unverified

## Overview

RedFile is a Flask-based WSGI application designed for intelligent file serving in Red Team operations. It enables conditional delivery of payloads based on client attributes like user-agent, IP address, or HTTP headers, making it ideal for targeted payload deployment during phishing, watering hole attacks, or command-and-control scenarios.

## Description

RedFile runs as a lightweight web server that inspects incoming requests and serves specific files or redirects based on predefined rules. This allows Red Teams to serve different payloads to different victims without multiple servers. For example, Windows users might receive an EXE payload, while Linux users get a script. It supports integration with tools like ngrok for external exposure and can log requests for operational awareness.

## Features

- Feature 1: Conditional serving based on HTTP headers, user-agent, IP ranges, or custom logic
- Feature 2: Support for static file serving with dynamic response modification
- Feature 3: Logging and request inspection for payload tracking
- Feature 4: Easy integration with Flask extensions for authentication or encryption
- Feature 5: WSGI compatibility for deployment on Apache, Nginx, or standalone

## Installation

### Requirements

- Python 3.6+
- Flask 1.0+
- pip

### Install Commands

```bash
# Clone the repository (assuming GitHub source)
git clone https://github.com/example/redfile.git
cd redfile

# Install dependencies
pip3 install -r requirements.txt
```

## Basic Usage

```bash
python3 redfile.py --help
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message |
| -p, --port | Specify listening port (default: 8080) |
| -d, --directory | Path to payloads directory |
| --config | Path to configuration file for conditions |

## Examples

### Example 1: Basic Usage

Start the server serving files from a directory:

```bash
[[commands/redfile-start-server]]
```

Access http://localhost:8080/payload.exe to download a file.

### Example 2: Advanced Usage

Generate a config for conditional serving and start with it:

```bash
[[commands/redfile-generate-payload-config]]

python3 redfile.py --port 8080 --directory /opt/payloads --config payloads.json
```

This serves windows_payload.exe only to Windows user-agents.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer
- [[T1566.001]] Phishing: Spearphishing Attachment

### Tactics

- [[Execution]] Execution
- [[Command and Control]] Command and Control

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Unusual Flask/WSGI processes serving files on non-standard ports
- Detection method 2: Network traffic to dynamic payload endpoints with conditional logic (e.g., varying responses based on headers)
- Detection method 3: Logs showing request inspections or conditional redirects

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Flask]]
- [[tools/ngrok]]

## References

- Official documentation: https://github.com/example/redfile
- Flask WSGI guide: https://flask.palletsprojects.com/en/stable/
