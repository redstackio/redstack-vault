---
id: 816b988b-8283-47f4-9364-4f98a0daf6ce
name: dirb
type: tool
verified: true
created_at: '2019-08-28T21:17:40.424414+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - brute-force
  - web-applications
  - directory-enumeration
url: 'https://github.com/v0re/dirb'
commands:
  - '[[commands/dirb-directory-brute-force]]'
validated: true
---

# dirb

**Status**: Unverified

## Overview

DIRB is a multi-threaded web application content scanner used for brute-forcing directories and files on web servers. It performs dictionary-based attacks using wordlists to identify hidden or existing content, analyzing HTTP responses for codes and sizes to distinguish valid discoveries. Commonly used in web reconnaissance during penetration testing to map the attack surface.

## Description

DIRB launches requests against a target web server for each entry in a provided wordlist, appending potential directory or file names to the base URL. It supports HTTP and HTTPS protocols and can filter results based on response codes (e.g., 200 for success, 403 for forbidden). For advanced usage, integrate with comprehensive wordlists like those from SecLists. DIRB focuses on content discovery rather than vulnerability scanning, making it ideal for initial enumeration in web application assessments. It handles extensions like .php, .html, and supports non-recursive scans to avoid deep crawling.

## Features

- Dictionary-based brute-forcing with customizable wordlists
- Multi-threaded scanning for efficiency
- Response code and size analysis to identify valid content
- Support for URL extensions and non-recursive modes
- Integration with proxy tools for traffic interception
- Customizable timeouts, threads, and redirect handling

## Installation

### Requirements

- Linux/Unix-based system (e.g., Kali, Ubuntu)
- Access to wordlists (install SecLists separately for advanced lists)
- Network connectivity to target web servers

### Install Commands

```bash
# On Kali Linux (pre-installed)
# No action needed

# On Ubuntu/Debian
sudo apt update
sudo apt install dirb

# Verify installation
which dirb
dirb --help
```

## Basic Usage

```bash
dirb http://example.com /usr/share/wordlists/dirb/common.txt
```

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and options |
| -r | Non-recursive scan (do not follow into discovered directories) |
| -X <extensions> | Append file extensions (e.g., -X .php,.html) |
| -t <threads> | Number of concurrent threads (default: 100) |
| -N | Do not follow HTTP redirects |
| -P <proxy> | Use proxy server (e.g., -P 127.0.0.1:8080) |
| -w <wordlist> | Path to custom wordlist |

## Examples

### Example 1: Basic Usage

Perform a non-recursive directory scan on a target using the default common wordlist.

```bash
dirb http://10.10.10.10 /usr/share/wordlists/dirb/common.txt -r
```

### Example 2: Advanced Usage

Scan an HTTPS target with specific extensions, increased threads, and proxy support.

```bash
dirb https://target.com /usr/share/wordlists/dirb/big.txt -X .php,.html,.txt -t 200 -P 127.0.0.1:8080
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[File and Directory Discovery]] File and Directory Discovery

### Tactics

- [[Discovery]] Discovery

## Detection

Indicators and methods for detecting this tool's usage:

- Sudden increase in HTTP GET requests from a single source IP targeting sequential or dictionary-like paths
- Requests with default DIRB user-agent (e.g., "DIRB v2.22    By The Dark Raver")
- High-volume probing of common directories (e.g., /admin, /backup) without legitimate navigation patterns
- Log analysis for 404/403 responses in bursts, followed by 200s on hidden paths
- Network monitoring for non-standard port usage or proxy chaining

## Related Procedures

No related procedures documented yet.

## Related Tools

- [[tools/Gobuster]]
- [[tools/ffuf]]

## References

- [Official GitHub Repository](https://github.com/v0re/dirb)
- [SecLists Wordlists](https://github.com/danielmiessler/SecLists)
- [Kali Linux Tools Documentation](https://www.kali.org/tools/dirb/)
