---
type: command
executor: bash
data: amass viz -d3 -dir $_OUTPUT_DIRECTORY
output: >-
  Creates amass_d3.html in the specified directory. Example directory listing:
  amass_d3.html  amass.json  amass.log  amass.txt  indexes.bolt
tags:
  - reconnaissance
  - dns
  - visualization
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# amass-viz-d3-output-directory

## Command

```bash
amass viz -d3 -dir $_OUTPUT_DIRECTORY
```

## Description

This command generates a D3.js-based interactive visualization from an existing Amass scan output directory. It processes the graph database to create an HTML file mapping discovered DNS assets, useful for reconnaissance analysis after enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d3 | Specifies D3.js as the visualization format (interactive web graph) | Yes |
| -dir $_OUTPUT_DIRECTORY | Path to the directory containing Amass scan outputs (e.g., indexes.bolt, amass.json) | Yes |

## Examples

### Basic Usage

```bash
amass viz -d3 -dir ./owasp.org/
```

### Advanced Usage

If combining with other formats, note that -d3 is specific; for Graphviz, use -gviz instead, but this command focuses on D3.

```bash
amass viz -d3 -dir /path/to/scan/output
```

## Expected Output

The command runs silently or with minimal output, creating amass_d3.html in $_OUTPUT_DIRECTORY. A successful directory listing after execution:

```
amass_d3.html  amass.json  amass.log  amass.txt  indexes.bolt
```

Open amass_d3.html in a browser to view the graph showing asset relationships.

## Related

- [[procedures/Visualize-Amass-DNS-Scan-Results-with-D3]]
- [[tools/amass]]
