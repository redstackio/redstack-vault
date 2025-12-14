---
id: n4o5p6q7-r8s9-0123-nopq-456789012345
name: react-schema-form
type: tool
verified: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.287Z'
platforms:
  - Web
tags:
  - form
  - xss
url: 'https://networknt.github.io/react-schema-form/'
validated: true
submitted: true
---

# react-schema-form

**Status**: Unverified

## Overview

react-schema-form is a React component for generating forms from JSON schemas, vulnerable to XSS when using notevil for condition evaluation in browser contexts.

## Description

It dynamically renders forms and evaluates user-supplied conditions, allowing sandbox escapes to inject scripts. Used in web apps for dynamic UIs; exploitable via demo for PoC.

## Features

- Feature 1: JSON schema to form generation
- Feature 2: Dynamic condition evaluation
- Feature 3: Radio, text, and other input types

## Installation

### Requirements

- React environment

### Install Commands

```bash
npm install react-schema-form
```

## Basic Usage

```javascript
import ReactSchemaForm from 'react-schema-form';
```

### Common Options

| Option | Description |
|--------|-------------|
| schema | JSON schema input |
| form | Form configuration array |

## Examples

### Example 1: Basic Usage

Load demo and input schema/form JSON.

### Example 2: Advanced Usage

Configure with malicious condition for XSS test.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Tactics

- [[Collection]] Collection

## Detection

Indicators and methods for detecting this tool's usage:

- DOM elements with class 'rsf' or schema-form
- Network requests to form rendering endpoints

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/notevil]]

## References

- https://networknt.github.io/react-schema-form/
