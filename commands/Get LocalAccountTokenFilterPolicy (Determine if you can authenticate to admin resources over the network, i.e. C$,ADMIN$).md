---
id: 1801cfcf-4e03-4b98-9adc-b786be39d4eb
name: Get LocalAccountTokenFilterPolicy (Determine if you can authenticate to admin
  resources over the network, i.e. C$,ADMIN$)
type: command
executor: bash
data: 'Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\
  |Select LocalAccountTokenFilterPolicy |fl

  '
output: null
created_at: '2020-07-14T18:21:10.826116+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get LocalAccountTokenFilterPolicy (Determine if you can authenticate to admin resources over the network, i.e. C$,ADMIN$)

```bash
Get-ItemProperty HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System\ |Select LocalAccountTokenFilterPolicy |fl

```


