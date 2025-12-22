---
id: 1d83a9ae-b348-4783-a70e-268874146dbe
name: Invoke-PSImage
type: tool
verified: true
created_at: '2019-08-28T21:17:25.997638+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - steganography
  - powershell
  - evasion
  - payload-delivery
url: 'https://github.com/JoelGryct/Invoke-PSImage'
validated: true
---

# Invoke-PSImage

**Status**: Unverified

## Overview

Invoke-PSImage is a PowerShell-based steganography tool designed to hide PowerShell scripts within the pixels of PNG image files. It allows red teams and penetration testers to conceal payloads for evasion and delivery in scenarios like phishing or file transfer restrictions, generating one-liners for extraction and execution.

## Description

The tool provides two main functions: ConvertTo-HiddenPSImage for embedding scripts into images and Get-HiddenPSImage for extracting them. This enables the creation of seemingly innocuous image files that contain executable code, useful for bypassing basic content filters or hiding malicious payloads in visual media. It modifies pixel values without altering the image's appearance significantly, making it suitable for offensive security operations involving data exfiltration or command execution evasion.

## Features

- Feature 1: Embed PowerShell scripts into PNG files using least significant bit (LSB) steganography
- Feature 2: Generate extraction one-liners for direct execution on target systems
- Feature 3: Preserve image integrity and visual quality post-embedding
- Feature 4: Support for verbose output and error handling during operations

## Installation

### Requirements

- PowerShell 2.0 or later (Windows environments)
- .NET Framework (standard on Windows)
- Access to GitHub for downloading the script

### Install Commands

```powershell
# Clone the repository or download the script
Invoke-WebRequest -Uri https://raw.githubusercontent.com/JoelGryct/Invoke-PSImage/master/Invoke-PSImage.ps1 -OutFile Invoke-PSImage.ps1

# Load the script into the current PowerShell session
dot-source .\Invoke-PSImage.ps1
```

On Kali Linux or other non-Windows systems, use PowerShell Core:

```bash
# Install PowerShell if needed
sudo apt install powershell

# Then run the PowerShell commands above
```

## Basic Usage

```powershell
Get-Help ConvertTo-HiddenPSImage -Full
Get-Help Get-HiddenPSImage -Full
```

### Common Options

| Option | Description |
|--------|-------------|
| -Verbose | Enable detailed output during embedding or extraction |
| -ImagePath | Specify the input PNG image file |
| -ScriptPath | Specify the PowerShell script to embed |
| -OutFile | Specify the output file for the modified image |

## Examples

### Example 1: Basic Usage

Embed a script:

```powershell
ConvertTo-HiddenPSImage -ImagePath cover.png -ScriptPath payload.ps1 -OutFile hidden.png
```

Extract and execute:

```powershell
Get-HiddenPSImage -ImagePath hidden.png | IEX
```

### Example 2: Advanced Usage

Embed with verbose logging:

```powershell
ConvertTo-HiddenPSImage -ImagePath cover.png -ScriptPath payload.ps1 -OutFile hidden.png -Verbose
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Obfuscated Files or Information]] Obfuscated Files or Information
- [[PowerShell]] PowerShell

### Tactics

- [[Defense Evasion]] Defense Evasion
- [[Execution]] Execution

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor PowerShell execution logs for calls to ConvertTo-HiddenPSImage or Get-HiddenPSImage
- Detection method 2: Analyze PNG files for anomalous pixel value patterns indicative of LSB steganography
- Detection method 3: Network logs showing downloads of the Invoke-PSImage script from GitHub
- Detection method 4: File integrity checks on images revealing hidden data via steganography tools like Stegdetect

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/PowerSploit]]
- [[tools/Invoke-Obfuscation]]

## References

- Official GitHub Repository: https://github.com/JoelGryct/Invoke-PSImage
- PowerShell Steganography Techniques: Various offensive security blogs and resources
