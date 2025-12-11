---
data: 'history.pushState(''/'',''/'',location.pathname +''?monitor&state=''+ st)'
tags:
  - javascript
  - history
type: command
executor: javascript
platforms:
  - Web
id: b5b3c0d8-6886-4a11-a308-2bb36c4bb19d
created_at: '2025-12-11T06:10:22.323Z'
updated_at: '2025-12-11T06:10:22.323Z'
verified: false
validated: true
submitted: true
---
# history-pushstate-monitor

## Command

```javascript
history.pushState('/','/',location.pathname +'?monitor&state='+ st)
```

## Description

Updates the browser history with monitoring parameters including state.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```javascript
history.pushState('/','/',location.pathname +'?monitor&state=state123')
```

## Expected Output

Updated URL.

## Related

- [[procedures/Prepare-Malicious-OAuth-State-and-Page]]
