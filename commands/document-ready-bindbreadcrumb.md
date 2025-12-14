---
id: cmd-doc-ready-bind
data: '$(document).ready(function(){ bindBreadCrumb(); });'
tags:
  - dom-trigger
type: command
output: Executes bindBreadCrumb() to build breadcrumb
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.717Z'
verified: false
validated: true
submitted: true
---
# document-ready-bindbreadcrumb

## Command

```javascript
$(document).ready(function(){ bindBreadCrumb(); });
```

## Description

Triggers the bindBreadCrumb function after the document loads, initiating the vulnerable breadcrumb construction process.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Automatically fires on DOM ready | No |

## Examples

### Basic Usage

```javascript
$(document).ready(function(){ bindBreadCrumb(); });
```

### Advanced Usage

```javascript
// Integrated in page script
$(document).ready(function(){ 
    bindBreadCrumb(); 
    // Additional init
});
```

## Expected Output

bindBreadCrumb() executes, processing referrer and appending elements if conditions met.

## Related

- [[Related Procedure: Load-Target-Page-to-Trigger-Breadcrumb-Building]]
