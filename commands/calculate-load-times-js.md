---
id: cmd-uuid-001
data: >-
  function calculate_load_times() { if (performance === undefined) {
  console.log('= Calculate Load Times: performance NOT supported'); return; }
  var resources = performance.getEntriesByType('resource'); if (resources ===
  undefined || resources.length <= 0) { console.log('= Calculate Load Times:
  there are NO `resource` performance records'); return; } console.log('=
  Calculate Load Times'); for (var i=0; i < resources.length; i++) { t =
  resources[i].responseEnd - resources[i].responseStart; console.log(t); } }
tags:
  - timing-measurement
type: command
output: Console logs of timing values (t) in milliseconds for each resource
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:50.090Z'
verified: false
validated: true
submitted: true
---
# calculate-load-times-js

## Command

```javascript
function calculate_load_times() { if (performance === undefined) { console.log('= Calculate Load Times: performance NOT supported'); return; } var resources = performance.getEntriesByType('resource'); if (resources === undefined || resources.length <= 0) { console.log('= Calculate Load Times: there are NO `resource` performance records'); return; } console.log('= Calculate Load Times'); for (var i=0; i < resources.length; i++) { t = resources[i].responseEnd - resources[i].responseStart; console.log(t); } }
```

## Description

This JavaScript function retrieves performance entries for loaded resources and logs the time delta between response start and end, used to measure load times in side-channel attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| performance.getEntriesByType('resource') | Fetches resource timing entries | Yes |
| responseEnd - responseStart | Computes duration in ms | Yes |

## Examples

### Basic Usage

```javascript
calculate_load_times();
```

### Advanced Usage

Embed in HTML and call on window.onload.

## Expected Output

Console logs like: "= Calculate Load Times" followed by numbers e.g., 45.2, 67.8 (ms per resource).

## Related

- [[Related Procedure: Host-Attacker-Webpage-for-Timing-Measurement]]
