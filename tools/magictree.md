---
id: 0fac1c24-7f56-4af5-af42-644cc9200517
name: MagicTree
type: tool
verified: true
created_at: '2019-08-28T21:17:42.313290+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - productivity
  - pentesting
  - data-management
  - reporting
url: 'http://www.gremwell.com/software/magictree'
validated: true
---

# MagicTree

**Status**: Unverified

## Overview

MagicTree is a penetration testing productivity tool designed to streamline data management during security assessments. It allows testers to consolidate findings from various scans, execute external commands, perform queries on collected data, and generate professional reports—all within a intuitive tree-based interface. Commonly used in red team operations for organizing reconnaissance, exploitation, and post-exploitation data.

## Description

MagicTree stores pentest data in a hierarchical tree structure, making it easy to navigate and correlate information from multiple sources. Users can import results from tools like Nmap, Nessus, or Burp Suite, run ad-hoc commands against nodes (e.g., SSH to a host), query data using a simple SQL-like language, and automate report generation. It's particularly valuable for long engagements where managing spreadsheets or notes becomes cumbersome, as it centralizes everything in one application. The tool supports both GUI and limited CLI operations, running on Perl for cross-platform compatibility.

## Features

- **Data Consolidation**: Import and merge data from XML, CSV, or custom formats into a unified tree.
- **External Command Execution**: Run tools like Nmap or Metasploit directly from tree nodes with context-aware parameters.
- **Querying**: Use MagicQL (MagicTree Query Language) to search and filter data across the tree.
- **Report Generation**: Export customized reports in HTML, PDF, or Word formats with templates.
- **Visualization**: Interactive tree view with color-coding for hosts, services, and vulnerabilities.
- **Collaboration**: Share project files (.mtr) for team-based pentesting workflows.

## Installation

### Requirements

- Perl 5.10 or later
- GTK+ libraries for GUI (on Linux)
- Approximately 50MB disk space
- Internet access for initial download

### Install Commands

On Kali Linux (pre-built package available):

```bash
sudo apt update
sudo apt install magictree
```

On Ubuntu:

```bash
sudo apt update
sudo apt install perl libgtk2-perl
# Download and extract MagicTree from official site
wget http://www.gremwell.com/sites/default/files/MagicTree.zip
unzip MagicTree.zip
cd MagicTree
perl magictree.pl
```

On Windows:

Download the Windows executable from the official website and run the installer. No additional dependencies required.

On macOS:

Use Homebrew to install Perl and GTK, then download and run the Perl script similar to Ubuntu.

```bash
brew install perl gtk+
# Download and run as above
```

## Basic Usage

```bash
magictree
```

This launches the GUI. Create a new project via File > New, or open an existing .mtr file.

### Common Options

| Option | Description |
|--------|-------------|
| -h, --help | Show help message and available flags |
| -v, --version | Display MagicTree version |
| --silent | Run in non-interactive mode for scripting |

## Examples

### Example 1: Basic Usage

```bash
magictree
```

Launches the GUI for manual data entry and management.

### Example 2: Advanced Usage

```bash
magictree -import nmap.xml -project myproject.mtr
```

Imports Nmap results into a project file from the command line.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for organizing recon data)
- [[Windows Management Instrumentation]] Windows Management Instrumentation (for command execution in Windows environments)

### Tactics

- [[Impact]] Impact (report generation for assessment impact)
- [[Discovery]] Discovery (data querying and consolidation)

## Detection

- Process monitoring for 'magictree' or 'magictree.pl' executions.
- File system watches for .mtr project files or frequent XML imports.
- Network logs for external command executions initiated from the tool (e.g., Nmap scans).
- GUI process detection on endpoints during assessments.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/dradis]] (Alternative collaboration platform)
- [[tools/KeepNote]] (Note-taking for pentests)

## References

- Official Documentation: http://www.gremwell.com/software/magictree
- User Guide: Included in the download or available online
- Community Forums: Various pentest blogs and GitHub discussions
