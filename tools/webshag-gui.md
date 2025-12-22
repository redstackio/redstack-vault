---
id: 379c876d-7ac2-48e1-8ad4-d6a7d1bd71dd
type: tool
verified: true
created_at: '2019-08-28T21:17:41.495074+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web-scanning
  - crawling
  - fuzzing
  - reconnaissance
url: 'https://github.com/1N3/WebShag'
commands:
  - '[[commands/webshag-gui-launch-basic]]'
  - '[[commands/webshag-gui-launch-with-proxy]]'
validated: true
---

# webshag-gui

**Status**: Unverified

## Overview

webshag-gui is the graphical user interface for Webshag, a multi-threaded, multi-platform web server audit tool written in Python. It provides functionalities for website crawling, URL scanning, and file fuzzing, making it useful for reconnaissance and vulnerability assessment in web applications. Commonly used in penetration testing to map web server structures and identify potential entry points.

## Description

Webshag-gui allows users to perform web audits through an intuitive interface, supporting HTTP and HTTPS protocols, proxy configurations, and HTTP authentication (Basic and Digest). It includes innovative features for IDS evasion, such as using different random proxies per request to complicate request correlation. The tool is particularly effective for discovering hidden directories, files, and parameters on web servers without requiring extensive manual effort.

## Features

- **Website Crawling**: Multi-threaded spidering to map site structure and discover links.
- **URL Scanning**: Automated scanning of URLs for common vulnerabilities and misconfigurations.
- **File Fuzzing**: Dictionary-based fuzzing to uncover sensitive files and directories.
- **Proxy Support**: Integration with proxies for anonymized scanning.
- **Authentication Handling**: Support for Basic and Digest HTTP authentication.
- **IDS Evasion**: Random proxy rotation and other techniques to bypass intrusion detection systems.

## Installation

### Requirements

- Python 2.7 (note: legacy tool, may require Python 2 environment)
- Git
- Libraries: urllib, threading (standard library)

### Install Commands

```bash
# Clone the repository
sudo apt update && sudo apt install git python2.7 -y
git clone https://github.com/1N3/WebShag.git
cd WebShag

# No formal setup.py; run directly
python2.7 WebShag-gui.py
```

For Kali Linux: The tool is not pre-installed but can be installed via the above git clone method. On Ubuntu, ensure Python 2.7 is available (may need to install from deadsnakes PPA if not present).

## Basic Usage

```bash
python2.7 WebShag-gui.py
```

This launches the GUI interface where users can input target URLs, configure threads, proxies, and authentication, then initiate crawling or fuzzing scans.

### Common Options

The GUI handles most options interactively, but launch can be customized if scriptable:

| Option | Description |
|--------|-------------|
| No CLI flags for GUI launch | All configuration done via interface |
| Proxy config in GUI | Set HTTP proxy host/port |
| Auth in GUI | Enter username/password for Basic/Digest |

## Examples

### Example 1: Basic Launch

```bash
cd /path/to/WebShag
python2.7 WebShag-gui.py
```

In the GUI, enter a target URL like http://example.com, set thread count to 10, and start crawling to map the site.

### Example 2: Launch and Configure Proxy (via GUI post-launch)

Launch as above, then in the GUI settings, enable proxy and input details like 127.0.0.1:8080 for Burp Suite integration.

## Related Commands

- [[commands/webshag-gui-launch-basic]]
- [[commands/webshag-gui-launch-with-proxy]]

## References

- Official GitHub: https://github.com/1N3/WebShag
- Original project documentation in repository README
