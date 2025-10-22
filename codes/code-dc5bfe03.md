---
id: dc5bfe03-7921-407e-8655-1ecb9219a1c4
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:14.584978+00:00'
updated_at: '2023-04-10T20:19:39.811529+00:00'
---

# Code Snippet dc5bfe03

**Language**: Powershell

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
