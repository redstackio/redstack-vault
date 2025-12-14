---
id: cmd-import-react-001
data: >-
  import React from 'react'; import AutolinkerWrapper from
  'react-autolinker-wrapper';
tags:
  - import
  - react
type: command
output: No output; modules imported successfully.
executor: javascript
platforms:
  - Web
  - Node.js
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.625Z'
verified: false
validated: true
submitted: true
---
# import-react-and-autolinkerwrapper

## Command

```javascript
import React from 'react';
import AutolinkerWrapper from 'react-autolinker-wrapper';
```

## Description

Imports the React library and the vulnerable react-autolinker-wrapper component for use in a JavaScript or React application setup.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | Direct import statements | Yes |

## Examples

### Basic Usage

```javascript
import React from 'react';
import AutolinkerWrapper from 'react-autolinker-wrapper';
```

### Advanced Usage

In a full module:

```javascript
import React from 'react';
import AutolinkerWrapper from 'react-autolinker-wrapper';
// Additional imports as needed
```

## Expected Output

Successful import with no module resolution errors; available for use in component definitions.

## Related

- [[commands/define-react-app-component]]
