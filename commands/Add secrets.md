---
id: f9606cde-728e-429a-83e3-b3d721886d93
name: Add secrets
type: command
executor: bash
data: '# Add secrets

  PS > . C:\Tools\Add-AzADAppSecret.ps1

  PS > Add-AzADAppSecret -GraphToken $graphtoken -Verbose

  '
output: null
created_at: '2023-05-24T20:21:06.336735+00:00'
updated_at: '2023-05-24T20:21:06.612131+00:00'
---

# Add secrets

```bash
# Add secrets
PS > . C:\Tools\Add-AzADAppSecret.ps1
PS > Add-AzADAppSecret -GraphToken $graphtoken -Verbose

```
