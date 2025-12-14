---
id: cmd-settimeout-iframe
data: >-
  setTimeout(function(){ ifr = document.querySelector('iframe'); ifr.style="";
  ifr.removeAttribute("sandbox"); console.log(ifr); },4000)
tags:
  - iframe-manip
  - sandbox-bypass
type: command
output: Console log of iframe; sandbox removed
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.022Z'
verified: false
validated: true
submitted: true
---
# SetTimeout Manipulate Iframe

## Command

```javascript
setTimeout(function(){ ifr = document.querySelector('iframe'); ifr.style=""; ifr.removeAttribute("sandbox"); console.log(ifr); },4000)
```

## Description

After 4s, selects iframe, clears style, removes sandbox, logs it.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ifr | Selected iframe | Yes |

## Examples

### Basic Usage

```javascript
// Run in console or script
```

## Expected Output

Iframe object logged; attributes modified.

## Related

- [[Related Procedure: Setup ClickJacking]]
