---
url: 'https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.8.0/angular.min.js'
tags:
  - javascript
  - framework
type: tool
platforms:
  - Web
description: >-
  JavaScript framework used for building web applications, exploited here for
  CSP bypass via sandbox escapes.
id: ab9b8095-0418-4a47-b447-7b105f8ee40e
created_at: '2025-12-13T23:56:20.387Z'
updated_at: '2025-12-13T23:56:20.387Z'
verified: false
validated: true
submitted: true
---
# AngularJS

**Status**: Unverified

## Overview

AngularJS is a structural framework for dynamic web apps, used in this exploit to bypass CSP by loading in iframes and using directives like ng-on-error.

## Description

Version 1.8.0 allows sandbox escapes when loaded in srcdoc with ng-csp, enabling arbitrary JS execution.

## Features

- Data binding
- Directives like ng-on-error
- CSP compatibility modes

## Installation

### Requirements

- Web browser

### Install Commands

Load via script tag: <script src="https://cdnjs.cloudflare.com/ajax/libs/angular.js/1.8.0/angular.min.js"></script>

## Basic Usage

Include in HTML with ng-app.

### Common Options

| Option | Description |
|--------|-------------|
| ng-on-error | Execute on error |

## Examples

### Example 1: Basic Usage

<script src="//code.angularjs.org/1.8.0/angular.js"></script>

### Example 2: Advanced Usage

Use in srcdoc for exploit.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Monitor for AngularJS loads in iframes
- CSP violation logs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Browser]]

## References

- AngularJS documentation
