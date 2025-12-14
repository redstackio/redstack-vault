---
id: tool-001
url: 'https://github.com/search?q=r57+shell&type=code'
tags:
  - web-shell
  - php
  - rce
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.248Z'
validated: true
submitted: true
---
# r57-PHP-Web-Shell

**Status**: Unverified

## Overview

r57 is a popular PHP web shell used in penetration testing to gain remote command execution on compromised web servers. It provides a web-based interface for file management, command execution, and server evaluation, commonly employed to demonstrate file upload vulnerabilities.

## Description

This tool is a single PHP file containing functions for executing system commands, browsing directories, uploading/downloading files, and evaluating PHP code. In offensive security, it's uploaded via vulnerable endpoints to establish persistence and control. For Stripo exploits, it's disguised as .jpg or .txt to bypass filters, then accessed via browser for interaction (e.g., /shell.jpg?cmd=ls).

## Features

- Feature 1: Command execution via GET/POST parameters (e.g., system($_GET['cmd']))
- Feature 2: File upload/download and directory traversal
- Feature 3: Server info disclosure and safe mode bypass attempts

## Installation

### Requirements

- PHP-enabled environment for testing (not needed for upload)
- Text editor for modification

### Install Commands

No installation; download the .php file from public repos and customize.

```bash
# Download example (use wget or curl from a test repo)
wget https://raw.githubusercontent.com/example/r57.php
```

## Basic Usage

Upload to target server, then access via browser:

```
http://target.com/uploads/shell.jpg?cmd=whoami
```

### Common Options

| Option | Description |
|--------|-------------|
| `cmd` | Execute system command |
| No options | Default interface for file ops |

## Examples

### Example 1: Basic Usage

Access uploaded shell:

```bash
# Browser or curl: curl "http://target.com/shell.jpg?cmd=ls -la"
```

### Example 2: Advanced Usage

Upload file through shell interface (after accessing the web UI).

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Server Software Component]]
- [[Windows Command Shell]]

### Tactics

- [[Execution]]
- [[Lateral Movement]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Scan web directories for .php files with system() calls or base64-encoded payloads
- Detection method 2: Monitor HTTP requests for ?cmd= parameters or anomalous file uploads

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: Various GitHub repos for testing
- Related resources: OWASP Web Shell cheatsheet
