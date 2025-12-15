---
url: 'https://beefproject.com/'
tags:
  - beef
  - browser-exploitation
  - web
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:12.955Z'
id: c6448ad3-38bd-4deb-a137-d8af43c11fb8
validated: true
submitted: true
---
# BeEF

**Status**: Unverified

## Overview

BeEF (Browser Exploitation Framework) is an open-source tool for exploiting web browser vulnerabilities, primarily used to hook and control victim browsers after initial compromise like clickjacking, enabling actions such as keylogging, phishing, or network reconnaissance.

## Description

BeEF operates by injecting a JavaScript hook into the victim's browser, allowing the attacker to send commands via a web interface. In clickjacking scenarios, it's integrated into the POC to gain persistent control post-click, facilitating data exfiltration or further attacks. It's commonly used in penetration testing for demonstrating browser-based risks.

## Features

- Feature 1: Browser hooking via JavaScript injection
- Feature 2: Command modules for keystroke capture, plugin enumeration, and social engineering
- Feature 3: RESTful API for automation and integration with other tools

## Installation

### Requirements

- Ruby (2.7+)
- Bundler
- Node.js for some modules

### Install Commands

```bash
# Clone repository
git clone https://github.com/beefproject/beef.git

# Install dependencies
cd beef
bundle install

# Start BeEF
./beef
```

## Basic Usage

```bash
./beef -h
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-x` | Enable XSS extensions |
| `-P PORT` | Specify hook port |

## Examples

### Example 1: Basic Usage

```bash
./beef
```

> Starts the framework on http://localhost:3000/ui/panel. Access hooked browsers via the web UI.

### Example 2: Advanced Usage

```bash
./beef -P 8080
```

> Runs on custom port for integration with clickjacking POC by updating hook URL to http://attacker-ip:8080/hook.js.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Adversary-in-the-Middle]]

### Tactics

- [[Execution]]
- [[Collection]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for unusual JavaScript loads from external domains (e.g., hook.js)
- Detection method 2: Browser console logs showing BeEF commands or network requests to attacker IPs

## Related Procedures


## Related Tools

- [[Metasploit]]
- [[Burp Suite]]

## References

- Official documentation: https://beefproject.com/
- Related resources: GitHub repository
