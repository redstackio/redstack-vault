---
id: 3c7418ba-b014-410c-9856-06e8f4273198
type: tool
verified: true
created_at: '2019-08-28T21:17:33.105969+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - web
  - brute-force
  - reconnaissance
  - directory-enumeration
url: 'https://sourceforge.net/projects/dirbuster/'
validated: true
---

# dirbuster

**Status**: Unverified

## Overview

DirBuster is a multi-threaded Java application designed for brute forcing directories and file names on web and application servers. It is commonly used in penetration testing to uncover hidden content on servers that appear to be in a default state but contain undisclosed pages, directories, or applications.

## Description

DirBuster excels at discovering hidden web resources by systematically testing potential paths against a target server. Unlike basic tools, it uses crowdsourced wordlists generated from real-world web crawling, making it highly effective for finding developer-used paths. It supports nine built-in wordlists for directories, files, and extensions, and offers a pure brute force mode for exhaustive enumeration when wordlists are insufficient. The tool handles multi-threading for speed and can filter results by HTTP status codes, recursion depth, and extensions.

## Features

- Feature 1: Multi-threaded scanning for faster enumeration of large wordlists.
- Feature 2: Nine pre-built wordlists derived from actual internet usage patterns.
- Feature 3: Pure brute force option with customizable character sets and lengths.
- Feature 4: Support for URL encoding, case sensitivity, and recursive scanning.
- Feature 5: Filtering by response codes (e.g., 200, 403) to focus on interesting finds.

## Installation

### Requirements

- Java Runtime Environment (JRE) 1.6 or higher.
- Sufficient memory for large wordlists (recommend 512MB+).

### Install Commands

```bash
# Download the JAR file from SourceForge
wget https://sourceforge.net/projects/dirbuster/files/dirbuster_1_0_RC1.jar/download -O dirbuster.jar

# Or on macOS/Windows, download manually from the project page
```

DirBuster is a standalone JAR file; no compilation is needed. Place the JAR in a directory and ensure Java is in your PATH.

## Basic Usage

```bash
java -jar dirbuster.jar
```

This launches the GUI interface for interactive configuration.

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Specify target URL |
| -w, --wordlist | Path to custom wordlist |
| -e, --extensions | File extensions to append (e.g., .php,.jsp) |
| -t, --threads | Number of threads (default: 10) |
| -f | Enable brute force mode |

## Examples

### Example 1: Basic Usage

```bash
java -jar dirbuster.jar -u http://example.com
```

Launches GUI scan against the target.

### Example 2: Advanced Usage

```bash
java -jar dirbuster.jar -u http://example.com -w directories.txt -e .php,.html -t 20
```

Runs a CLI-like scan with custom wordlist, extensions, and increased threads.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of HTTP requests from a single IP to sequential paths (e.g., /admin, /backup) with varying extensions.
- Detection method 2: Java process (java.exe) with network connections to web servers and console output mentioning DirBuster.
- Detection method 3: Web server logs showing 404/403 responses in patterns matching common wordlists.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Gobuster]]
- [[tools/ffuf]]

## References

- Official SourceForge project: https://sourceforge.net/projects/dirbuster/
- OWASP Web Security Testing Guide (archived reference)
- GitHub forks for updates: https://github.com/topics/dirbuster
