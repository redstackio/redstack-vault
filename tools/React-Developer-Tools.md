---
url: >-
  https://chrome.google.com/webstore/detail/react-developer-tools/fmkadmapgofadopljbjfkapdkoienihi?hl=en
tags:
  - react
  - debugging
type: tool
platforms:
  - Web
description: Chrome extension for inspecting React components and props.
id: 3a2c5a4d-35d3-4e3e-8bb7-e65b73912466
created_at: '2025-12-11T06:10:17.561Z'
updated_at: '2025-12-11T06:10:17.561Z'
verified: false
validated: true
submitted: true
---
# React Developer Tools

**Status**: Unverified

## Overview

React Developer Tools is a browser extension for debugging React applications by inspecting component hierarchies and props.

## Description

Essential for jumping to code generating React components in apps like Steam Chat.

## Features

- Component tree inspection
- Props and state viewing
- Source code navigation

## Installation

### Requirements

- Google Chrome

### Install Commands

Install from Chrome Web Store.

## Basic Usage

```bash
# Open in DevTools tab
```

### Common Options

| Option | Description |
|--------|-------------|
| Components | View tree |
| Profiler | Performance |

## Examples

### Example 1: Basic Usage

Inspect React components in Steam Chat.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Active Scanning]]

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

- https://reactjs.org/blog/2015/09/02/new-react-developer-tools.html
