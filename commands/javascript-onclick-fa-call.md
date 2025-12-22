---
data: >-
  onClick:function(){Fa('self-promotion','live','live_dashboard'), (0,
  de.xw)(m)}
tags:
  - frontend-analysis
type: command
executor: javascript
platforms:
  - Web
id: 6ef2caa0-320b-4d54-8a96-c68ea05dabdc
created_at: '2025-12-14T17:28:36.438Z'
updated_at: '2025-12-14T17:28:36.438Z'
verified: false
validated: true
submitted: true
---
# javascript-onclick-fa-call

## Command

```javascript
onClick:function(){Fa('self-promotion','live','live_dashboard'), (0, de.xw)(m)}
```

## Description

JavaScript event handler that triggers an analytics call to Fa() with parameters indicating live shopping promotion, discovered in TikTok frontend code.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| 'self-promotion' | Event category for self-promotion actions | Yes |
| 'live' | Event action for live status | Yes |
| 'live_dashboard' | Event label for dashboard navigation | Yes |

## Examples

### Basic Usage

```javascript
onClick:function(){Fa('self-promotion','live','live_dashboard'), (0, de.xw)(m)}
```

### Advanced Usage

Embed in HTML element: <button onClick="...">Live Ads</button>

## Expected Output

Triggers Fa() analytics event; no direct output, but logs event for live dashboard interaction.

## Related

- [[Related Procedure]]
