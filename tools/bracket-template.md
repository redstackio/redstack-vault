---
url: 'https://www.npmjs.com/package/bracket-template'
tags:
  - template
  - xss
  - vulnerable
type: tool
platforms:
  - Node.js
description: Node.js templating engine vulnerable to XSS in version 1.1.5.
id: 978c8319-4572-4992-adf5-76874431b34d
created_at: '2025-12-14T03:16:37.160Z'
updated_at: '2025-12-14T03:16:37.160Z'
verified: false
validated: true
submitted: true
---
# bracket-template

**Status**: Unverified

## Overview

bracket-template is a lightweight templating engine for Node.js, vulnerable to reflected XSS when unsanitized inputs are used in interpolations like [[= n ]].

## Description

It compiles templates with bracket syntax but fails to escape hex sequences (\xHH), allowing injection. Used in the sample app to render GET params; alternatives include EJS or Pug for safer options.

## Features

- Feature 1: Bracket-based syntax for logic and output
- Feature 2: Compile-time optimization
- Feature 3: Escaping for standard HTML (but not hex)

## Installation

### Requirements

- Node.js and npm

### Install Commands

```bash
npm install bracket-template@1.1.5
```

## Basic Usage

```bash
# In JS
const bt = require('bracket-template');
const tpl = '[[= name ]]';
const render = bt.compile(tpl);
console.log(render({name: '<script>alert(1)</script>'}));
```

### Common Options

| Option | Description |
|--------|-------------|
| `compile` | Pre-compile templates |
| `escape` | Built-in HTML escaping (limited) |

## Examples

### Example 1: Basic Usage

```bash
# Vulnerable render
let html = bt.compile(`<strong>Hello [[= n ]]</strong>`)({n: input});
```

### Example 2: Advanced Usage

```bash
# With logic
let tpl = `[[ if (n) { ]]<p>[[= n ]]</p>[[ } ]]`;
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Presence in package.json
- Template files with [[ ]] syntax
- Logs showing unescaped outputs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Node.js]]

## References

- npm page: https://www.npmjs.com/package/bracket-template
