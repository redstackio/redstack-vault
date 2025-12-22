---
type: procedure
description: >-
  Visualize the results of an Amass DNS enumeration scan using D3 to generate an
  interactive HTML graph of discovered assets.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Network Information]]'
sub_techniques: []
tags:
  - reconnaissance
  - dns
  - visualization
  - amass
commands:
  - '[[commands/amass-viz-d3-output-directory]]'
tools:
  - '[[tools/amass]]'
platforms:
  - Linux
  - macOS
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Visualize-Amass-DNS-Scan-Results-with-D3

## Summary

This procedure outlines how to generate a D3-based visualization of assets discovered during a previous Amass DNS enumeration scan. It creates an interactive HTML file that maps relationships between subdomains, IP addresses, and other network elements, aiding in the analysis of the target's attack surface.

## Description

Amass is a comprehensive tool for passive and active reconnaissance, particularly effective for DNS-based asset discovery. After running an enumeration scan, the visualization subcommand processes the output database and generates a graph using D3.js, which is ideal for programmatically rendering complex graphing data from graph databases into a web-viewable format. This procedure assumes a prior Amass scan has been completed, producing an output directory with files like indexes.bolt and amass.json. The resulting amass_d3.html can be opened in any modern web browser to explore the visualized data interactively, helping identify clusters of assets and potential entry points.

## Requirements

1. Amass tool installed ([[tools/amass]])
2. An existing output directory from a prior Amass enumeration scan, containing the BoltDB file (indexes.bolt) and JSON export
3. Bash-compatible environment (Linux or macOS)
4. Web browser for viewing the generated HTML

## Defense

Defensive measures and detection strategies:

- Monitor for execution of the 'amass' binary via endpoint detection and response (EDR) tools
- Analyze DNS query patterns for high-volume enumeration attempts from reconnaissance tools
- Inspect local file systems for creation of visualization files like amass_d3.html in temporary directories
- Enable logging of process creation and network connections to detect tool usage during reconnaissance phases

## Objectives

1. Generate an interactive visual representation of enumerated DNS assets
2. Facilitate analysis of asset relationships for identifying attack paths
3. Verify the completeness of prior scan data through graphical inspection

## Instructions

### Step 1: Prepare the Output Directory

**Context**: Ensure the directory from your previous Amass scan is accessible and contains the necessary files. This step verifies prerequisites and sets up the environment for visualization.

Navigate to the output directory and list its contents to confirm the presence of indexes.bolt and amass.json.

```bash
ls $_OUTPUT_DIRECTORY
```

> Expected: Files such as amass.json, amass.log, amass.txt, and indexes.bolt should be present. If missing, rerun the Amass enumeration to generate them.

### Step 2: Generate D3 Visualization

**Context**: Execute the visualization command to process the scan data and create the D3 graph. This step reads the graph database and exports an HTML file for browser-based viewing, providing a clear view of asset interconnections.

**Command** ([[commands/amass-viz-d3-output-directory]]):

```bash
amass viz -d3 -dir $_OUTPUT_DIRECTORY
```

> This command uses the -d3 flag to specify D3.js output and -dir to point to the scan directory. It processes the data without additional network activity, making it suitable for offline analysis. Upon success, an amass_d3.html file is created in the directory.

### Step 3: View and Analyze the Visualization

**Context**: Open the generated HTML file to interact with the graph. This step allows manual exploration of the data, such as zooming into subdomain clusters or tracing IP relationships.

Open the file in a web browser:

```bash
xdg-open $_OUTPUT_DIRECTORY/amass_d3.html  # On Linux
open $_OUTPUT_DIRECTORY/amass_d3.html      # On macOS
```

> Expected: An interactive graph loads, displaying nodes for domains, IPs, and ASNs with edges representing relationships. Use browser tools to inspect for patterns like wildcard subdomains or shared infrastructure.
