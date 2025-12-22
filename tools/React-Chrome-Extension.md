---
url: >-
  https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en
tags:
  - react
  - debugging
type: tool
platforms:
  - Web
description: Chrome extension for inspecting React applications.
id: 8dca10e5-a427-4a17-8f87-c5fd77bbf376
created_at: '2025-12-14T00:11:25.272Z'
updated_at: '2025-12-14T00:11:25.272Z'
verified: false
validated: true
submitted: true
---
# React Chrome Extension

**Status**: Unverified

## Overview

This extension allows inspecting React components, props, and jumping to source code in React-based apps like Steam chat.

## Description

Used to analyze React hierarchies and identify unsafe props.

## Features

- Component tree inspection
- Prop and state viewing
- Source code navigation

## Installation

### Requirements

- Google Chrome

### Install Commands

Install from Chrome Web Store.

## Basic Usage

```bash
# Enable in DevTools tab
```

### Common Options

| Option | Description |
|--------|-------------|
| Components | View tree |
| Profiler | Performance |

## Examples

### Example 1: Basic Usage

Inspect Steam chat components.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Gather Victim Network Information]]

### Tactics

- [[Discovery]]

## Detection

Indicators and methods for detecting this tool's usage:

- Extension installation logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Chrome-DevTools]]

## References

- Official extension page
