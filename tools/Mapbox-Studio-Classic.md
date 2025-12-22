---
id: tool-uuid-1
url: 'https://www.mapbox.com/mapbox-studio/'
tags:
  - map-design
  - style-editor
  - deprecated
type: tool
verified: false
platforms:
  - Windows
  - macOS
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:30.235Z'
validated: true
submitted: true
---
---

# Mapbox-Studio-Classic

**Status**: Unverified

## Overview

Mapbox Studio Classic is a deprecated desktop application for creating, editing, and uploading custom vector tile map styles to Mapbox.com. It is commonly used in security testing for exploiting vulnerabilities in map attribution controls, such as injecting XSS payloads.

## Description

This tool provides a GUI for layering map data, styling elements, and setting metadata like attribution. In offensive operations, it allows crafting malicious styles that persist on Mapbox servers. Key features include TileJSON export, CartoCSS styling, and direct upload. It targets web mapping integrations like Mapbox.js.

## Features

- Feature 1: Visual style editor for maps with drag-and-drop layers
- Feature 2: Metadata controls including unsanitized attribution fields
- Feature 3: One-click upload to Mapbox account for persistence

## Installation

### Requirements

- Internet access
- Mapbox account
- Compatible OS (Windows 7+, macOS 10.9+, Ubuntu 14.04+)

### Install Commands

No CLI install; download GUI installer from https://www.mapbox.com/mapbox-studio/. Run the .exe/.dmg/.deb file and follow prompts.

## Basic Usage

Launch via desktop icon. Create new style, edit, save/upload.

### Common Options

| Option | Description |
|--------|-------------|
| New Style | Start blank project |
| Upload | Push to Mapbox.com |
| Export | Generate TileJSON |

## Examples

### Example 1: Basic Usage

Open app, select New Style, add layers, set attribution, upload.

### Example 2: Advanced Usage

Edit existing style, inject custom JS in metadata, preview, then upload with authentication.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]
- [[Remote File Copy]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Network traffic to Mapbox upload endpoints with anomalous payloads
- Deprecated tool usage in enterprise environments
- File system artifacts of installer

## Related Procedures


## Related Tools

- [[tools/Mapbox-Studio]] (modern web alternative)

## References

- Official documentation: https://docs.mapbox.com/help/glossary/studio-classic/
- Related resources: Mapbox API docs

