---
id: cmd-wayback-navigate
data: |-
  # Browser-based navigation to Wayback Machine
  Visit: https://web.archive.org/web/*/https://api.planet.com/
tags:
  - recon
type: command
output: null
executor: browser
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.323Z'
verified: false
validated: true
submitted: true
---
# wayback-url-navigate

## Command

Browser navigation (no CLI):

Visit https://web.archive.org/web/*/https://api.planet.com/ to access the snapshot calendar.

## Description

This is a browser-based action to load the Wayback Machine's capture history for a specific URL, displaying available historical snapshots for inspection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL wildcard | Target domain with * for captures (e.g., web/*/https://api.planet.com/) | Yes |

## Examples

### Basic Usage

Open browser and navigate to https://web.archive.org/web/*/https://api.planet.com/.

### Advanced Usage

Append query params if needed, e.g., https://web.archive.org/web/*/https://api.planet.com/* for subpaths.

## Expected Output

A calendar interface with capture dates; clicking loads archived pages.

## Related

- [[Related Procedure: Access-Wayback-Machine-Snapshots]]
