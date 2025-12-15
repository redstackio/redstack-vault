---
url: >-
  https://www.hitachivantara.com/en-us/products/pentaho-platform/report-designer.html
tags:
  - pentaho
  - report-design
  - rce
type: tool
verified: false
platforms:
  - Java
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.314Z'
id: 2072320a-a817-4d45-a04c-34f24e582770
validated: true
submitted: true
---
# Pentaho-Report-Designer

**Status**: Unverified

## Overview

Pentaho Report Designer is a graphical tool for creating and editing PRPT report files used in Pentaho BI Server, commonly leveraged in security testing to embed malicious scripts for exploitation.

## Description

This Java-based IDE allows designing reports with support for scripting languages like BeanShell, JavaScript, and Java. In offensive security, it's used to craft reports that execute arbitrary code when processed by the server, targeting vulnerable BI deployments.

## Features

- Feature 1: Drag-and-drop report element design
- Feature 2: Integration of formulas and scripts (BeanShell, JS, Java)
- Feature 3: Export to PRPT format for server compatibility

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher
- Approximately 500MB disk space

### Install Commands

```bash
# Download from official site and extract
wget https://downloads.hitachivantara.com/.../pentaho-report-designer.zip
unzip pentaho-report-designer.zip
cd report-designer
./report-designer.sh
```

## Basic Usage

```bash
./report-designer.sh
```

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show help message |
| `-v, --verbose` | Verbose output during design |

## Examples

### Example 1: Basic Usage

```bash
./report-designer.sh
```
Launch the designer to create a new blank report.

### Example 2: Advanced Usage

```bash
./report-designer.sh --open malicious.prpt
```
Open an existing PRPT file for editing embedded scripts.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]] JavaScript
- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Tactics

- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of report-designer directories or processes on attacker systems
- Network traffic to Pentaho downloads or related domains
- Analysis of PRPT files for designer metadata

## Related Procedures


## Related Tools

- [[Related Tool 1]]
- [[Related Tool 2]]

## References

- Official documentation: https://help.hitachivantara.com/Documentation/Pentaho/9.2/...
- Related resources: Pentaho community forums
