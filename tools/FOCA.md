---
id: e33b1acb-444d-49c1-94d3-e183c4cefc1f
name: FOCA
type: tool
verified: true
created_at: '2019-08-28T21:17:25.363089+00:00'
updated_at: '2024-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - reconnaissance
  - osint
  - metadata-extraction
  - fingerprinting
url: 'https://github.com/ElevenPaths/FOCA'
validated: true
---

# FOCA

**Status**: Unverified

## Overview

FOCA (Fingerprinting Organizations with Collected Archives) is a GUI-based tool designed for passive reconnaissance and organization fingerprinting. It automates the discovery of publicly available documents associated with a target organization, downloads them, and extracts valuable metadata to reveal internal information such as usernames, email addresses, software versions, and hidden relationships. Commonly used in red teaming and OSINT operations to map an organization's digital footprint without direct interaction.

## Description

FOCA excels in collecting documents from search engines (Google, Bing, DuckDuckGo) and alternative sources like Shodan, then analyzing them for metadata using integrated tools similar to ExifTool. It builds visual graphs of entities (people, servers, printers) discovered in the metadata, helping to identify potential entry points or weak configurations. Ideal for initial reconnaissance phases where understanding the target's structure is key, but it requires manual configuration for advanced searches and is Windows-centric.

## Features

- Feature 1: Multi-engine document search using custom Google dorks and other queries to find PDFs, DOCs, XLS, etc.
- Feature 2: Automated metadata extraction revealing authors, revision histories, embedded usernames, MAC addresses, and software details.
- Feature 3: Relationship mapping and graphing to visualize connections between extracted entities.
- Feature 4: Integration with external sources like Shodan for device fingerprinting and export options (CSV, XML, graphs).
- Feature 5: Deduplication and filtering of results to focus on high-value intelligence.

## Installation

### Requirements

- Windows 7 or later (primary platform; can run on Linux via Wine with limitations).
- .NET Framework 4.5 or higher.
- Internet access for searches.

### Install Commands

FOCA is distributed as a Windows executable; download and install manually from the official GitHub releases.

```powershell
# Download the latest release (manual step: visit GitHub and download FOCA.zip)
# Extract to a directory, e.g., C:\Tools\FOCA
# No installer; run FOCA.exe directly

# To add to PATH (optional, via PowerShell as admin):
$env:Path += ";C:\Tools\FOCA"
[Environment]::SetEnvironmentVariable("Path", $env:Path, [EnvironmentVariableTarget]::Machine)
```

For Kali Linux (experimental via Wine):

```bash
sudo apt update && sudo apt install wine
# Download FOCA.zip, unzip, and run with wine FOCA.exe
wine FOCA.exe
```

## Basic Usage

```powershell
# Launch FOCA (see related command)
& "C:\Tools\FOCA\FOCA.exe"
```

Once launched:
1. Create a new project and enter the target domain (e.g., target.com).
2. Configure search engines and dorks (e.g., filetype:pdf site:target.com).
3. Initiate search to download documents.
4. Run metadata extraction and review results in the graph view.

### Common Options

| Option | Description |
|--------|-------------|
| New Project | Starts a fresh fingerprinting session for a domain. |
| Search Engines | Select Google, Bing, etc., with proxy support for evasion. |
| Metadata Filters | Choose extraction types (e.g., only emails or versions). |
| Export | Save results as CSV, XML, or images of graphs. |

## Examples

### Example 1: Basic Usage

Launch FOCA and create a project for reconnaissance:

```powershell
& "C:\Tools\FOCA\FOCA.exe"
```
In GUI: File > New Project > Enter "example.com" > Search > Extract Metadata. Results show document list and entity graph.

### Example 2: Advanced Usage

Automate project creation and extraction:

```powershell
Start-Process "C:\Tools\FOCA\FOCA.exe" -ArgumentList "new-project example.com --extract-metadata"
```
Focus on specific file types (configure in GUI: PDF and DOC only) to harvest emails from author fields.

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Social Media]] Search Open Websites/Domains (document collection via search engines)
- [[Hardware]] Gather Victim Identity Information (metadata extraction for usernames/emails)
- [[Scan Databases]] Search Open Websites/Domains: Social Media (extended to public docs)

### Tactics

- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: High volume of searches from a single IP to Google/Bing with specific dorks (e.g., filetype:pdf site:domain.com); monitor via web proxy logs.
- Detection method 2: Unusual downloads of organization documents from public sources; track via CDN or search engine analytics.
- Detection method 3: Presence of FOCA executable or project files (.foca) on compromised Windows systems; scan for known hashes.
- Detection method 4: Network traffic to Shodan API if integrated; log API key usage.

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Maltego]] (advanced OSINT graphing)
- [[tools/theHarvester]] (email and subdomain enumeration)
- [[tools/ExifTool]] (standalone metadata extraction)

## References

- Official GitHub: https://github.com/ElevenPaths/FOCA
- Documentation: https://www.elevenpaths.com/labstools/foca/
- Related resources: OSINT Framework entry on document metadata analysis
