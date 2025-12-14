---
id: cmd-001
data: 'await navigator.bluetooth.requestDevice({acceptAllDevices: true})'
tags:
  - bluetooth
  - api-call
  - exploit
type: command
output: BluetoothDevice object or permission error
executor: javascript
platforms:
  - Desktop
  - Electron
  - Browser
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:29.142Z'
verified: false
validated: true
submitted: true
---
# request-bluetooth-device

## Command

```javascript
await navigator.bluetooth.requestDevice({acceptAllDevices: true})
```

## Description

This JavaScript command, executed in a browser or Electron renderer console, requests access to a Bluetooth Low Energy device using the Web Bluetooth API. The acceptAllDevices option bypasses device filters, accepting any nearby device. In vulnerable Electron environments, it succeeds without permission, granting access; otherwise, it requires user consent or fails.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| acceptAllDevices | Boolean flag to accept all nearby devices without selection UI | Yes |

## Examples

### Basic Usage

```javascript
await navigator.bluetooth.requestDevice({acceptAllDevices: true})
```

### Advanced Usage

```javascript
await navigator.bluetooth.requestDevice({
  acceptAllDevices: true,
  filters: [{ services: ['battery_service'] }]
})
```

> Adds optional filters for specific services, but acceptAllDevices overrides to accept any.

## Expected Output

In vulnerable setups: Promise resolves to a BluetoothDevice object, e.g., BluetoothDevice { id: 'xx:xx:xx:xx:xx:xx', name: 'Nearby Device', gatt: BluetoothRemoteGATTServer }. Allows further calls like device.gatt.connect(). In secure environments: Throws DOMException: 'The user did not respond to the permission request prompt in a reasonable time.' or similar error.

## Related

- [[Related Procedure|procedures/Request-Bluetooth-Device-via-Renderer-JS]]
