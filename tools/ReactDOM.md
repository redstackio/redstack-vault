---
id: tool-uuid-4
url: 'https://reactjs.org/'
tags:
  - dom
  - rendering
type: tool
verified: false
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.803Z'
validated: true
submitted: true
---
---

# ReactDOM

**Status**: Unverified

## Overview

ReactDOM provides DOM-specific methods to render React components to the browser, essential for displaying the vulnerable Markdown output.

## Description

Handles mounting React elements to HTML, where the unsanitized href in the rendered anchor enables XSS.

## Features

- Feature 1: render() for mounting components
- Feature 2: hydrate() for server-side rendering
- Feature 3: unmountComponentAtNode() for cleanup

## Installation

### Requirements

- React installed

### Install Commands

```bash
npm install react-dom
```

## Basic Usage

```javascript
import ReactDOM from 'react-dom';
```

### Common Options

| Option | Description |
|--------|-------------|
| `render` | Render to DOM |

## Examples

### Example 1: Basic Usage

```javascript
ReactDOM.render(<div>Hello</div>, root);
```

### Example 2: Advanced Usage

```javascript
ReactDOM.render(component, document.getElementById('root'));
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[JavaScript]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Source code search for ReactDOM imports

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/React]]

## References

- Official documentation: https://reactjs.org/docs/react-dom.html

