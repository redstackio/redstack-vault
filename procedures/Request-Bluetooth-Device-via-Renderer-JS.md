---
id: proc-002
tags:
  - bluetooth
  - javascript
  - access-bypass
  - renderer
type: procedure
tools:
  - '[[tools/Developer-Tools]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/request-bluetooth-device]]'
verified: false
platforms:
  - Desktop
  - Electron
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:29.158Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploitation for Client Execution]]'
  - '[[JavaScript]]'
---
# Request-Bluetooth-Device-via-Renderer-JS

## Summary

This procedure executes JavaScript in the Electron app's renderer process developer console to request access to a nearby Bluetooth device using the acceptAllDevices option, bypassing permission checks and granting unauthorized read/write access.

## Description

In vulnerable Electron versions, the Web Bluetooth API's requestDevice method with acceptAllDevices: true allows the renderer to directly access any nearby Bluetooth device without triggering user permission prompts or errors. This exploits the lack of isolation between renderer and system resources. The procedure assumes the vulnerable app is running and developer tools are accessible. Successful execution returns a BluetoothDevice object, enabling further interactions like reading GATT characteristics.

## Requirements

1. Running vulnerable Electron app with renderer loaded
2. Developer tools enabled (Ctrl+Shift+I on Windows/Linux, Cmd+Option+I on macOS)
3. Nearby Bluetooth devices in discoverable mode
4. No browser or Electron policies blocking console execution

## Defense

Defensive measures and detection strategies:

- Patch Electron to versions that deny Bluetooth requests from renderers without explicit permissions
- Use Electron's --enable-blink-features=WebBluetoothBlockNewlyCreatedConnections flag
- Implement sandboxing for renderers and monitor console logs for bluetooth.requestDevice calls
- Educate users to avoid loading untrusted content in Electron apps

## Objectives

1. Bypass access controls to obtain BluetoothDevice object
2. Demonstrate unauthorized access to device services
3. Highlight risks of untrusted renderer content

## Instructions

### Step 1: Open Developer Tools

**Context**: Access the console in the renderer process to execute JavaScript.

**Instructions**: In the running Electron app window, open the developer tools.

```javascript
// No command needed; use Ctrl+Shift+I to open
```

> Opens the Chromium DevTools panel with Console tab active. Expected output: DevTools interface loads.

### Step 2: Execute Bluetooth Request Command

**Context**: Run the JavaScript command to request device access, exploiting the vulnerability.

**Command** ([[commands/request-bluetooth-device]]):
```javascript
await navigator.bluetooth.requestDevice({acceptAllDevices: true})
```

> This asynchronous command requests a Bluetooth device, accepting all nearby ones without filters. In vulnerable versions, it returns a Promise resolving to a BluetoothDevice object (e.g., { id: 'xx:xx:xx:xx:xx:xx', name: 'Device Name' }). In patched versions, it throws a DOMException: 'User activation is required' or permission error.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploitation for Client Execution]] Exploitation for Client Execution
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/request-bluetooth-device]]

## Tools Used

- [[tools/Developer-Tools]]

## Tags

- bluetooth
- javascript
- access-bypass
- renderer
