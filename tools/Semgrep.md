---
url: 'https://semgrep.dev/'
tags:
  - static-analysis
  - code-scanning
  - vulnerability-detection
type: tool
verified: false
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.280Z'
id: bee1f567-ee90-4294-95d1-ba50ad269bc2
validated: true
submitted: true
---
# Semgrep

**Status**: Unverified

## Overview

Semgrep is an open-source static analysis tool for scanning source code to identify vulnerabilities, bugs, and compliance issues using lightweight semantic analysis and pattern matching.

## Description

Semgrep excels at discovering security flaws like CSRF in web applications by defining custom rules for patterns such as unprotected GET requests for state changes. It's commonly used in offensive security for pre-exploit analysis of leaked codebases and in defensive security for CI/CD pipelines. In this case, it identified the CSRF vulnerability in Elastic AppSearch by scanning for missing CSRF tokens on sensitive endpoints.

## Features

- Feature 1: Semantic code pattern matching beyond regex
- Feature 2: Support for multiple languages (Python, JavaScript, Java, etc.)
- Feature 3: Custom rule creation for specific vulnerability types like CSRF

## Installation

### Requirements

- Python 3.7+ or Node.js
- Git for rule repositories

### Install Commands

```bash
# Via pip (Python)
pip install semgrep

# Or via Homebrew (macOS)
brew install semgrep
```

## Basic Usage

```bash
semgrep --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output |
| `--config=URL` | Use rules from a config file or registry |

## Examples

### Example 1: Basic Usage

```bash
semgrep --config=auto path/to/codebase
```

Scan a directory for common vulnerabilities using auto-detected rules.

### Example 2: Advanced Usage

```bash
semgrep --config=p/csrf path/to/elastic/code --verbose
```

Scan for CSRF-specific rules from the public registry on the Elastic codebase.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]]

### Tactics

- [[Reconnaissance]]

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for semgrep binary executions in process logs
- Detection method 2: Network traffic to semgrep.dev for rule downloads

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://semgrep.dev/docs/
- Related resources: Semgrep Registry for security rules
