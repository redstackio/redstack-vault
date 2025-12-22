---
id: 3d2aaa54-c646-48e5-8f71-08cd5c4be161
type: tool
verified: true
created_at: '2019-08-28T21:17:31.085744+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - visualization
  - analysis
  - graphing
  - osint
  - investigation
url: 'https://www.maltego.com/downloads'
validated: true
---

# casefile

**Status**: Unverified

## Overview

CaseFile is a free, open-source visualization and analysis tool designed for offline investigators and analysts. It functions as a lightweight version of Maltego, focusing on manual data entry, linking, and graph-based analysis without automated transforms or online queries. Ideal for building intelligence maps from team-sourced information during on-the-ground investigations.

## Description

CaseFile provides a graphical interface for quickly adding entities (such as persons, organizations, or IP addresses), creating relationships between them, and visualizing complex data connections in a graph format. It targets analysts working with non-programmatic, human-gathered intelligence, enabling the construction of investigative maps. Unlike full Maltego, it lacks transform execution but serves as an excellent free viewer for Maltego-generated graphs. Users can import/export graphs in formats like .gtm or .xml, making it suitable for collaborative offline analysis in security operations, OSINT, or forensic investigations.

## Features

- **Entity Management**: Manually add and categorize entities (e.g., domains, emails, phones) with custom properties.
- **Link Creation**: Draw directed or undirected relationships between entities to model connections.
- **Graph Visualization**: Interactive canvas for zooming, panning, and layout adjustments (e.g., organic, hierarchical).
- **Offline Operation**: No internet required; all data handled locally.
- **Export/Import**: Save graphs as images, PDFs, or Maltego-compatible files for sharing.
- **Search and Filter**: Query entities and edges within the graph for quick navigation.

## Installation

### Requirements

- Java Runtime Environment (JRE) 8 or higher.
- At least 2GB RAM for smooth performance with large graphs.
- Supported on Linux, Windows, and macOS.

### Install Commands

For Kali Linux or Ubuntu (via official .deb package):

```bash
# Download the latest .deb from official site
wget https://www.maltego.com/downloads/casefile.deb

# Install the package
dpkg -i casefile.deb

# Resolve dependencies if needed
apt-get install -f
```

For Windows: Download the .exe installer from the official site and run it.

For macOS: Download the .dmg and drag to Applications.

Note: CaseFile is pre-installed on some Kali Linux distributions under the Maltego suite.

## Basic Usage

```bash
[[commands/casefile-launch]]
```

This launches the CaseFile GUI. Once open:
1. Create a new graph via File > New.
2. Add entities using the palette (e.g., drag 'Person' icon to canvas).
3. Right-click entities to add properties or links.
4. Use the search bar to filter the graph.

### Common Options

CaseFile is primarily GUI-driven with limited CLI options. Launch parameters are minimal:

| Option | Description |
|--------|-------------|
| None (default) | Opens the main application window |
| -h, --help | Displays basic usage (if supported in version) |

## Examples

### Example 1: Basic Usage

Launch and create a simple graph:

```bash
casefile
```

In the GUI:
- Add an 'IP Address' entity.
- Add a 'Domain' entity.
- Link them with a 'Resolves To' relationship.
- Export as PNG via File > Export.

### Example 2: Advanced Usage

Open an existing Maltego graph:

```bash
casefile
```

In the GUI: File > Open > Select .gtm file. Analyze links manually without running transforms.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information (for manual OSINT graphing)
- [[Active Scanning]] Active Scanning (for visualizing scan results)

### Tactics

- [[Reconnaissance]] Reconnaissance (data correlation and mapping)

## Detection

CaseFile is a legitimate analysis tool, but its usage can be detected via:
- Process monitoring: Look for 'casefile.jar' or Java processes with graphing libraries.
- File artifacts: Presence of .gtm or .xml graph files in user directories.
- Network: Minimal, as it's offline; no outbound connections expected.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Maltego]] (Full version with transforms)
- [[tools/graphviz]] (Command-line graphing alternative)

## References

- Official Download: https://www.maltego.com/downloads
- Documentation: https://docs.maltego.com/
- GitHub Repository (community forks): https://github.com/search?q=casefile+maltego
