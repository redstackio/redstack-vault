---
id: 646ad461-0056-49a0-a7ab-1f20c5640bd0
name: xsser
type: tool
verified: true
created_at: '2019-08-28T21:17:38.526300+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - macOS
tags:
  - xss
  - web
  - exploitation
  - testing
url: 'https://github.com/epsylon/xsser'
commands:
  - '[[commands/xsser-basic-xss-detection]]'
  - '[[commands/xsser-crawl-and-inject]]'
  - '[[commands/xsser-bypass-filter]]'
validated: true
---

# xsser

**Status**: Unverified

## Overview

xsser (Cross Site Scripter) is an open-source Python-based framework designed for automated detection, exploitation, and reporting of Cross-Site Scripting (XSS) vulnerabilities in web applications. It is commonly used in penetration testing to identify reflected, stored, and DOM-based XSS flaws, with built-in support for filter evasion techniques.

## Description

xsser automates the process of injecting various XSS payloads into web forms, URLs, and headers, then analyzes responses for successful execution. It supports crawling websites to discover injection points, applying heuristics for bypassing Web Application Firewalls (WAFs) and input sanitization, and generating detailed reports. The tool is particularly useful for offensive security operations targeting client-side vulnerabilities in modern web apps, including single-page applications (SPAs).

## Features

- Feature 1: Over 600 predefined XSS payloads covering common vectors and evasions.
- Feature 2: Website crawling to automatically find and test forms, query parameters, and headers.
- Feature 3: Heuristic engine for filter bypass (e.g., encoding, case manipulation, null bytes).
- Feature 4: Plugin support for custom payloads and reporting formats (HTML, XML).
- Feature 5: Multi-threading for faster scanning of large sites.

## Installation

### Requirements

- Python 2.7 or 3.x
- Git
- pip

### Install Commands

```bash
# Clone from GitHub
sudo apt update && sudo apt install git python3-pip -y
git clone https://github.com/epsylon/xsser.git
cd xsser

# Install dependencies
pip3 install -r requirements.txt

# For Kali Linux (pre-built package available)
sudo apt install xsser
```

For Ubuntu/Debian, the above git clone method works. On macOS, use Homebrew to install dependencies first: `brew install python git`.

## Basic Usage

```bash
xsser.py -h
```

This displays the full help menu with options for URLs, payloads, crawling, and more.

### Common Options

| Option | Description |
|--------|-------------|
| -u, --url | Target URL for testing |
| -p, --payload | Specific payload number or custom string |
| --crawl | Enable site crawling |
| --auto | Automatic payload selection and testing |
| --heuristic | Apply bypass heuristics (1-20) |
| -r, --report | Generate report in specified format |

## Examples

### Example 1: Basic Usage

See [[commands/xsser-basic-xss-detection]] for testing a single URL with a basic payload.

### Example 2: Advanced Usage

See [[commands/xsser-crawl-and-inject]] for automated crawling and testing.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript (for XSS payload execution)
- [[Drive-by Compromise]] Drive-by Compromise (via exploited XSS)

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection (data exfiltration via XSS)

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Network logs showing repeated requests with encoded JavaScript payloads (e.g., <script>alert(1)</script> variations).
- Detection method 2: WAF alerts on heuristic bypass attempts like case-mixed tags or null byte injections.
- Detection method 3: Python process monitoring for 'xsser.py' execution on assessment machines.
- Detection method 4: Browser console logs or error pages reflecting suspicious payloads during scans.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Burp-Suite]] (for manual XSS testing)
- [[tools/sqlmap]] (for combined XSS/SQLi testing)

## References

- Official GitHub: https://github.com/epsylon/xsser
- Documentation: Included in the repo README
- Related resources: OWASP XSS Prevention Cheat Sheet
