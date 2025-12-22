---
id: 9d3aca81-b851-4247-93d7-5e10b160cfdc
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.586245+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - microburst
  - domain
validated: true
---

# microburst-get-azure-domain-info

## Code

```powershell
PS C:> Import-Module .\MicroBurst.psm1
PS C:> Import-Module .\Get-AzureDomainInfo.ps1
PS C:> Get-AzureDomainInfo -folder MicroBurst -Verbose
```

## Description

Imports MicroBurst modules and gathers Azure domain information, including services and configs, with verbose output to a folder.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| -folder | Output directory | MicroBurst |
| -Verbose | Detailed logs | Enabled |

## Usage

Run after cloning MicroBurst. Collects domain trusts, weak configs, and post-ex data. Useful for hybrid environment recon.

## Detection

- PowerShell imports of MicroBurst.psm1.
- File writes to output folder with Azure data.
- API calls to domain services endpoints.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/MicroBurst]]
