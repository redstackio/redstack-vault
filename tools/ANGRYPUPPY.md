---
id: d984bc55-21c1-4b8f-b514-ce71c880296f
type: tool
verified: true
created_at: '2019-08-28T21:17:25.624312+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
tags:
  - cobaltstrike
  - bloodhound
  - ad-attack
  - automation
  - post-exploitation
url: >-
  https://github.com/BloodHoundAD/SharpHound/pull/1 (related) or Cobalt Strike
  community resources
validated: true
---

# ANGRYPUPPY

**Status**: Unverified

## Overview

ANGRYPUPPY is an Aggressor script for Cobalt Strike designed to automate attack paths discovered through BloodHound analysis in Active Directory environments. It enables red teams to efficiently traverse complex AD graphs by automating sequences of lateral movement, privilege escalation, and credential access techniques, reducing manual effort in targeting high-value assets like Domain Admins.

Common use cases include red team engagements where BloodHound data has identified shortest paths to domain dominance, allowing scripted execution of chains like Kerberoasting to DCSync.

## Description

ANGRYPUPPY integrates BloodHound's graph-based attack path findings directly into Cobalt Strike beacons. Once loaded, it provides custom beacon commands (e.g., 'puppy') that parse imported BloodHound JSON data and execute tailored attack sequences. This includes automatic tool downloads, credential spraying, and movement across sessions without operator intervention for each hop.

Key capabilities:
- Import and query BloodHound data within CS.
- Automate multi-hop paths (e.g., user -> machine -> admin).
- Support for common AD techniques: overpass-the-hash, token impersonation, etc.
- Logging and visualization of executed paths.

It is particularly useful in large AD environments where manual path following is time-consuming.

## Features

- **Path Automation**: Executes BloodHound-recommended paths as beacon tasks.
- **Dynamic Tooling**: Downloads and runs required binaries (e.g., Rubeus for Kerberoasting) on-the-fly.
- **Session Chaining**: Moves laterally across compromised hosts automatically.
- **Error Handling**: Retries failed steps and reports back to operator.
- **Customization**: Configurable via script variables for specific environments.

## Installation

### Requirements

- Cobalt Strike 4.0+ with Aggressor scripting enabled.
- BloodHound data (JSON exports) available for import.
- Network access to download additional tools if needed.
- Windows/Linux host for CS team server.

### Install Commands

1. Download the ANGRYPUPPY script (angrypuppy.cna) from trusted sources (e.g., Cobalt Strike community or GitHub forks).

2. Place the script in your Cobalt Strike scripts directory:

```bash
# On Linux team server
mkdir -p /opt/cobaltstrike/scripts
cp angrypuppy.cna /opt/cobaltstrike/scripts/

# On Windows
# Copy to C:\Cobalt Strike\scripts\
```

3. Restart the Cobalt Strike client or team server to load scripts automatically. Alternatively, load manually via console.

## Basic Usage

```aggressor
tool-load angrypuppy
# Or manually: script-load /path/to/angrypuppy.cna
```

Once loaded, import BloodHound data into CS (via alias or file upload), then use beacon commands like 'puppy shortestpath targetuser'.

### Common Options

| Option | Description |
|--------|-------------|
| `-h, --help` | Show ANGRYPUPPY-specific help in aggressor console |
| `-v, --verbose` | Enable detailed logging of path execution |
| `--data-path` | Specify path to BloodHound JSON data |

## Examples

### Example 1: Basic Usage

Load and execute a simple path:

```aggressor
script-load angrypuppy.cna
```

In beacon console:

```beacon
puppy shortest DOMAIN\Administrator
```

### Example 2: Advanced Usage

Execute with custom data:

```beacon
puppy kerberoast --data /shared/bloodhound.json DOMAIN\svc_account
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Use Alternate Authentication Material]] Use Alternate Authentication Material
- [[Steal or Forge Kerberos Tickets]] Steal or Forge Kerberos Tickets
- [[Valid Accounts]] Valid Accounts
- [[Remote Services]] Remote Services

### Tactics

- [[Lateral Movement]] Lateral Movement
- [[Privilege Escalation]] Privilege Escalation
- [[Persistence]] Persistence

## Detection

Indicators and methods for detecting this tool's usage:

- Unusual Aggressor script loads in CS logs.
- Beacon tasks with 'puppy' or automation patterns.
- Rapid lateral movement across AD objects matching BloodHound paths.
- Network traffic for tool downloads (e.g., Rubeus.exe).
- EDR alerts on chained credential access (Kerberoast + DCSync).

Monitor CS client logs for script imports and beacon command patterns.

## Related Procedures

- [[procedures/Import-BloodHound-Data-to-Cobalt-Strike]]
- [[procedures/Automate-Lateral-Movement-in-AD]]

## Related Tools

- [[tools/Cobalt-Strike]]
- [[tools/BloodHound]]
- [[tools/SharpHound]]

## References

- Cobalt Strike Aggressor Script documentation: https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/aggressor_script.htm
- BloodHound GitHub: https://github.com/BloodHoundAD/BloodHound
- Original ANGRYPUPPY discussion: Search Cobalt Strike forums or @harmj0y Twitter archives
