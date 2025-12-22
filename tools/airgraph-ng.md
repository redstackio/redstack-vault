---
id: 8a047496-fa76-4ba2-a1e3-7459595ff405
type: tool
verified: true
created_at: '2019-08-28T21:17:17.792763+00:00'
updated_at: '2023-05-29T16:48:53.029709+00:00'
platforms:
  - Linux
tags:
  - wireless
  - wifi
  - reconnaissance
  - visualization
url: 'https://www.aircrack-ng.org/doku.php?id=airgraph-ng'
validated: true
---

# airgraph-ng

**Status**: Unverified

## Overview

airgraph-ng is a visualization tool within the aircrack-ng suite designed to generate Graphviz-compatible dot files from wireless capture data produced by airodump-ng. It is primarily used in wireless security testing to create visual representations of WiFi networks, helping analysts understand client-access point relationships and probe behaviors. Common use cases include post-capture analysis during WiFi penetration testing, reconnaissance visualization, and educational demonstrations of wireless attack surfaces.

## Description

airgraph-ng processes CSV output files from airodump-ng (or compatible capture files) to produce two types of graphs: CAPR (Client Access Point Relationship) graphs, which illustrate connections between clients and access points, and CPG (Common Probe Graph) graphs, which highlight ESSIDs probed by devices. These graphs are output as .dot files that can be rendered into images using Graphviz tools like dot. The tool is lightweight, script-based, and integrates seamlessly with other aircrack-ng components for offline analysis of captured wireless traffic. It does not perform live captures but excels at making complex wireless data more interpretable through visualization.

## Features

- **CAPR Graph Generation**: Creates directed graphs showing client devices connected to specific access points, useful for mapping network topology.
- **CPG Graph Generation**: Produces graphs centered on probed ESSIDs, revealing devices that have attempted to connect to hidden or specific networks.
- **Input Flexibility**: Supports airodump-ng CSV files or pcap captures as input.
- **Output Compatibility**: Generates standard Graphviz .dot files for easy rendering to PNG, SVG, or other formats.
- **Lightweight Processing**: No real-time requirements; ideal for offline analysis of large capture datasets.

## Installation

### Requirements

- Linux environment with aircrack-ng suite installed (includes dependencies like Graphviz for rendering).
- Perl (airgraph-ng is a Perl script).
- Graphviz package for rendering dot files to images.

### Install Commands

```bash
# On Kali Linux (pre-installed in aircrack-ng suite)
sudo apt update && sudo apt install aircrack-ng graphviz

# On Ubuntu/Debian
sudo apt update && sudo apt install aircrack-ng graphviz

# On macOS (via Homebrew)
brew install aircrack-ng graphviz

# Manual build from source (if needed)
git clone https://github.com/aircrack-ng/aircrack-ng.git
cd aircrack-ng
make && sudo make install
graphviz # Install separately via package manager
```

## Basic Usage

```bash
airgraph-ng --help
```

### Common Options

| Option | Description |
|--------|-------------|
| `-i, --input <file>` | Specify the input CSV or cap file from airodump-ng |
| `-o, --output <dir>` | Directory to output the .dot graph files |
| `-t, --type <type>` | Graph type: `capr` for Client-AP relationships or `cpg` for Common Probe Graph |
| `-h, --help` | Display help message |
| `-v, --version` | Show version information |

## Examples

### Example 1: Basic Usage

Generate a CAPR graph from an airodump-ng CSV capture:

```bash
airgraph-ng -i capture.csv -o graphs -t capr
```

This creates a `capr.dot` file in the `graphs` directory.

### Example 2: Advanced Usage

Generate both graph types and render to PNG (requires Graphviz):

```bash
# Generate graphs
airgraph-ng -i capture.csv -o graphs -t capr
airgraph-ng -i capture.csv -o graphs -t cpg

# Render to image
dot -Tpng graphs/capr.dot -o capr.png
dot -Tpng graphs/cpg.dot -o cpg.png
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]] Active Scanning (for analyzing wireless reconnaissance data)
- [[Network Sniffing]] Network Sniffing (visualizing captured wireless traffic)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Presence of aircrack-ng binaries or Perl scripts in process lists (e.g., `ps aux | grep airgraph`).
- File system artifacts: .dot files in temporary directories or alongside .csv/.cap captures.
- Graphviz processes (dot) running post-airgraph-ng execution.
- Log entries for airodump-ng captures, as airgraph-ng depends on them.
- Network defenders can monitor for aircrack-ng suite installations via endpoint detection tools.

## Related Commands

- [[commands/airgraph-ng-generate-capr-graph]]
- [[commands/airgraph-ng-generate-cpg-graph]]

## Related Tools

- [[tools/airodump-ng]] (for capturing the input data)
- [[tools/graphviz]] (for rendering the output graphs)
- [[tools/aircrack-ng]] (parent suite)

## References

- Official Documentation: https://www.aircrack-ng.org/doku.php?id=airgraph-ng
- Aircrack-ng GitHub: https://github.com/aircrack-ng/aircrack-ng
- Graphviz Documentation: https://graphviz.org/documentation/
