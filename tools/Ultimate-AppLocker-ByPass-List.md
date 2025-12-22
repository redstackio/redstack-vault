---
id: f10ad428-704e-4a2d-8016-02c29a82b713
type: tool
verified: true
created_at: '2019-08-28T21:17:40Z'
updated_at: '2023-05-29T16:48:53Z'
platforms:
  - Windows
tags:
  - applocker
  - defense-evasion
  - bypass
url: 'https://github.com/api0cradle/UltimateAppLockerByPassList'
commands:
  - '[[commands/copy-executable-to-temp-and-execute]]'
  - '[[commands/regsvr32-signed-binary-proxy-execution]]'
  - '[[commands/mshta-javascript-execution-bypass]]'
validated: true
---

# Ultimate-AppLocker-ByPass-List

**Status**: Unverified

## Overview

The Ultimate AppLocker ByPass List is a comprehensive repository of techniques, paths, and methods to evade or bypass Microsoft AppLocker, an application control solution that restricts executable files, scripts, and other code based on rules. It is commonly used in red teaming and penetration testing to test the effectiveness of AppLocker policies in Windows environments.

## Description

This tool serves as a curated collection of known AppLocker bypass strategies, including writable paths for path rule evasion, verified exploits against default rules, and alternative execution methods like DLL hijacking or signed binary proxies. It helps security professionals identify weaknesses in AppLocker configurations without requiring custom tool development. The repository is maintained on GitHub and includes markdown files for easy reference during engagements.

## Features

- **Generic Bypasses**: Lists of commonly writable directories and paths (e.g., %TEMP%, user profiles) that can intercept or evade path-based rules.
- **Verified Bypasses**: Documented, tested methods against AppLocker's default publisher, path, and hash rules, including version-specific vulnerabilities.
- **DLL Execution Methods**: Techniques for loading DLLs via trusted binaries like rundll32, regsvr32, or odbcconf, often used for payload delivery.
- **Searchable Categories**: Organized by bypass type, Windows version, and AppLocker rule set for quick lookup.
- **Community Contributions**: Open-source format allowing updates for new Windows releases and patches.

## Installation

### Requirements

- Git installed on the system.
- A modern web browser or Markdown viewer for GitHub files.
- Windows environment for testing (optional, for validation).

### Install Commands

```bash
# Clone the repository
mkdir -p ~/security-tools && cd ~/security-tools
git clone https://github.com/api0cradle/UltimateAppLockerByPassList.git

# On Windows (using Git Bash or PowerShell)
git clone https://github.com/api0cradle/UltimateAppLockerByPassList.git
```

After cloning, navigate to the directory and open the Markdown files (e.g., Generic-AppLockerbypasses.md) in a text editor or browser.

## Basic Usage

```bash
# View the main lists
cat UltimateAppLockerByPassList/Generic-AppLockerbypasses.md
cat UltimateAppLockerByPassList/VerifiedAppLockerBypasses.md
cat UltimateAppLockerByPassList/DLL-Execution.md
```

Browse the repository online at the GitHub URL for rendered Markdown, or use it as a reference during testing to select appropriate bypasses based on the target's AppLocker configuration.

### Common Options

N/A - This is a static documentation repository, not an executable tool with CLI options.

## Examples

### Example 1: Basic Usage

During a red team engagement, query the VerifiedAppLockerBypasses.md file for Windows 10-specific techniques:

```bash
grep -i "windows 10" UltimateAppLockerByPassList/VerifiedAppLockerBypasses.md
```

This might reveal methods like using installutil.exe for .NET assembly execution.

### Example 2: Advanced Usage

Combine with local testing: Clone the repo, then test a path bypass by attempting to copy and run from a listed writable path, referencing the generic list for ideas.

```bash
# Example: Check writable paths from the list and test
ls %TEMP%
copy test.exe %TEMP%\test.exe
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Signed Binary Proxy Execution]] Signed Binary Proxy Execution (e.g., regsvr32, mshta)
- [[Registry Run Keys - Startup Folder]] PATH Interception (writable paths)
- [[Disable or Modify Tools]] Disable or Modify Tools (evading AppLocker rules)

### Tactics

- [[Execution]] Execution
- [[Defense Evasion]] Defense Evasion

## Detection

- Monitor for unusual executions of signed binaries like regsvr32.exe or mshta.exe with network arguments.
- Log file copies to sensitive paths like %TEMP% or %APPDATA%.
- AppLocker event logs (Event ID 8004/8006) for rule violations or evasions.
- Behavioral analytics for anomalous process chains (e.g., regsvr32 spawning cmd.exe).

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Powershell]]
- [[tools/Cmd-Exe]]

## References

- Official GitHub Repository: https://github.com/api0cradle/UltimateAppLockerByPassList
- Microsoft AppLocker Documentation: https://docs.microsoft.com/en-us/windows/security/threat-protection/windows-defender-application-control/applocker
- Related Research: Search for "AppLocker Bypass" on offensive security blogs.
