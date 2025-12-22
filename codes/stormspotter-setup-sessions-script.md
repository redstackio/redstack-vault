---
id: dc5bfe03-7921-407e-8655-1ecb9219a1c4
type: code
language: powershell
verified: true
created_at: '2023-04-06T03:56:14.584978+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - stormspotter
  - setup
validated: true
---

# stormspotter-setup-sessions-script

## Code

```powershell
# session 1 - backend
- Activate virtual environment: `pipenv shell`
- Start the backend server: `python ssbackend.pyz`

# session 2 - frontend
- Navigate to the frontend directory: `cd C:\Tools\stormspotter\frontend\dist\spa\`
- Start the frontend server: `quasar.cmd serve -p 9091 --history`

# session 3 - collector
- Activate virtual environment: `pipenv shell`
- Login to Azure: `az login -u test@<TENANT NAME>.onmicrosoft.com -p <PASSWORD>`
- Start the collector: `python C:\Tools\stormspotter\stormcollector\sscollector.pyz cli`

# Web access on http://localhost:9091
- Username: `neo4j`
- Password: `BloodHound`
- Server: `bolt://localhost:7687`
```

## Description

Multi-session setup script for Azure StormSpotter: backend (Neo4j), frontend (Quasar UI), and collector (data ingestion via az CLI).

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <TENANT NAME> | Azure tenant | contoso |
| <PASSWORD> | Login password | MyPassword |
| C:\Tools\... | Installation paths | Adjust as needed |

## Usage

Execute in three terminal sessions as noted. Access UI at localhost:9091 with neo4j/BloodHound. Used for graphing Azure attack paths.

## Detection

- Local Neo4j process (bolt:7687) or Quasar dev server (9091).
- Az CLI logins from recon tools.
- Outbound to azure.com management APIs.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/Azure-StormSpotter]]
