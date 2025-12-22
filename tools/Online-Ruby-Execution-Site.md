---
id: tool-online-ruby-site
url: ''
tags:
  - rce
  - ruby
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:27.847Z'
validated: true
submitted: true
---
# Online-Ruby-Execution-Site

**Status**: Unverified

## Overview

Online Ruby execution sites are web-based platforms that allow users to write, run, and debug Ruby code snippets in a browser without local installation. In security testing, they are used to identify and exploit server-side code execution vulnerabilities, particularly when lacking sandboxing.

## Description

These tools provide an interactive code editor, execution engine, and output console for Ruby. Common use cases in offensive security include testing for RCE by submitting code that invokes system calls. Features often include syntax highlighting, error reporting, and shareable sessions, but vulnerable instances may execute code with host privileges, enabling shell access.

## Features

- Feature 1: Browser-based Ruby REPL for instant code execution
- Feature 2: Output console displaying stdout/stderr from server-side runs
- Feature 3: No setup required, accessible via public web URL

## Installation

### Requirements

- Web browser (e.g., Chrome, Firefox)
- Internet connection

### Install Commands

```bash
# No installation needed; access via web browser
```

## Basic Usage

```bash
# Navigate to site (e.g., search "online ruby runner"), paste code, click Run
```

### Common Options

| Option | Description |
|--------|-------------|
| Run/Execute | Triggers server-side code execution |
| Clear | Resets the editor and output |

## Examples

### Example 1: Basic Usage

```bash
# Paste: puts "Hello Ruby"
# Click Run → Output: Hello Ruby
```

### Example 2: Advanced Usage

```bash
# Paste RCE code and execute to run shell commands
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Web logs showing repeated code submissions with system calls
- Unusual server resource usage from Ruby executions
- Output logs containing shell command results

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Replit]]
- [[tools/JDoodle]]

## References

- Generic online Ruby runners (e.g., replit.com/languages/ruby)
- HackerOne report for vulnerability context
