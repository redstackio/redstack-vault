---
id: 97dfea0b-5e8d-4c74-9371-363cb320a1d6
type: tool
verified: true
created_at: '2019-08-28T21:17:27.881222+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - osint
  - reconnaissance
  - web-interface
url: 'https://github.com/i3visio/osrframework'
validated: true
---

# OSRFramework Server

**Status**: Unverified

## Overview

OSRFramework Server is a web-based interface for the OSRFramework suite, a collection of Python libraries and tools designed for Open Source Intelligence (OSINT) tasks. It enables users to perform reconnaissance activities such as username availability checks, DNS lookups, information leak searches, deep web queries, and regular expression-based extractions through a graphical web UI. This tool is particularly useful for security researchers, red teams, and investigators needing an accessible frontend for OSINT workflows without relying on command-line interfaces.

## Description

OSRFramework provides modular libraries that integrate with various OSINT applications. The server component (osrframework_server.py) launches a local web server, allowing users to interact with these libraries via a browser. Key capabilities include querying social media platforms for usernames, resolving domains, searching for data leaks, and extracting patterns from web content. It supports ad-hoc integrations like Maltego transforms for visual representations and can be extended with custom scripts. The server facilitates collaborative OSINT sessions by hosting the interface on a network-accessible host.

## Features

- **Web Interface**: Browser-based access to OSINT tools without terminal dependency.
- **Modular Queries**: Supports username checks (e.g., usufy), email searches (e.g., mailfy), phone number lookups, and more.
- **Integration Support**: Compatible with Maltego for graphical transforms and OSRFConsole for CLI fallback.
- **Customization**: Allows configuration of query sources, rate limiting, and output formats (JSON, CSV).
- **Local Hosting**: Runs as a lightweight Flask or similar server for secure, local deployments.

## Installation

### Requirements

- Python 3.6+ with pip
- Git for cloning the repository
- Dependencies: requests, beautifulsoup4, lxml (installed via setup.py)

### Install Commands

```bash
# Clone the repository
git clone https://github.com/i3visio/osrframework.git
cd osrframework

# Install dependencies
pip install -r requirements.txt
# Or run setup
python setup.py install
```

For Kali Linux or Ubuntu, OSRFramework may be available via apt:
```bash
sudo apt update
sudo apt install osrframework
```

On Windows or macOS, use virtual environments:
```bash
python -m venv osrf_env
source osrf_env/bin/activate  # Linux/macOS
# or osrf_env\Scripts\activate  # Windows
pip install osrframework
```

## Basic Usage

```bash
python osrframework_server.py --host 127.0.0.1 --port 5000
```

This starts the server on localhost port 5000. Access via http://127.0.0.1:5000 in a browser. Use --host 0.0.0.0 for network access.

### Common Options

| Option | Description |
|--------|-------------|
| `--host` | IP address to bind the server (default: 127.0.0.1) |
| `--port` | Port to listen on (default: 5000) |
| `--debug` | Enable debug mode for development |
| `--config` | Path to custom configuration file |

## Examples

### Example 1: Basic Local Server

```bash
python osrframework_server.py
```

Starts the default server. Navigate to http://localhost:5000 to use the OSINT dashboard for username or domain queries.

### Example 2: Network-Accessible Server

```bash
python osrframework_server.py --host 0.0.0.0 --port 8080 --debug
```

Allows access from other machines on the network at http://<your-ip>:8080. Useful for team-based OSINT operations.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information
- [[Gather Victim Identity Information]] Gather Victim Identity Information

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to common OSINT endpoints (e.g., social media APIs, whois servers).
- Python processes running osrframework_server.py or related modules.
- Web server logs showing queries from the OSRFramework interface.
- Installed packages via pip list | grep osrframework.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Maltego]] (For graphical transforms)
- [[tools/theHarvester]] (Alternative OSINT reconnaissance tool)

## References

- Official GitHub: https://github.com/i3visio/osrframework
- Documentation: https://github.com/i3visio/osrframework/wiki
- PyPI: https://pypi.org/project/osrframework/
