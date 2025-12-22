---
id: 0fdcb1db-01df-49c9-9550-7fdd53990c21
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.584641+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - roadrecon
  - auth
validated: true
---

# roadrecon-auth-gather-gui-commands

## Code

```powershell
pipenv shell
roadrecon auth [-h] [-u USERNAME] [-p PASSWORD] [-t TENANT] [-c CLIENT] [--as-app] [--device-code] [--access-token ACCESS_TOKEN] [--refresh-token REFRESH_TOKEN] [-f TOKENFILE] [--tokens-stdout]
roadrecon gather [-h] [-d DATABASE] [-f TOKENFILE] [--tokens-stdin] [--mfa]
roadrecon auth -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>
roadrecon gather
roadrecon gui
```

## Description

This script demonstrates ROADRecon workflow: activating environment, authenticating, gathering AAD data, and launching GUI. It includes help syntax for auth and gather subcommands.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| USERNAME | Azure username | test@tenant.onmicrosoft.com |
| PASSWORD | Password | <PASSWORD> |
| TENANT | Tenant name | tenant |
| DATABASE | SQLite DB file | roadrecon.db |
| TOKENFILE | Path to tokens | tokens.json |

## Usage

Run in pipenv shell for ROADRecon setup. Auth first, then gather to populate DB, finally gui for visualization. Supports app auth or device code for MFA.

## Detection

- Azure AD logs for ROADRecon client ID or unusual token requests.
- File system monitoring for roadrecon.db or token files.
- Network to graph.microsoft.com with high query volume.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/ROADRecon]]
