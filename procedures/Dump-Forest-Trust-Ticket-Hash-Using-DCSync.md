---
id: 7c1f090d-5489-4810-b2e9-c18ec271dd1d
name: Dump-Forest-Trust-Ticket-Hash-Using-DCSync
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.270608+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Credential Dumping|T1003 - Credential Dumping]]'
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Forest to Forest Compromise - Trust Ticket]]'
commands:
  - '[[commands/mimikatz-lsadump-dcsync-trust-account]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# Dump-Forest-Trust-Ticket-Hash-Using-DCSync

## Summary

This procedure uses Mimikatz's DCSync functionality to replicate and dump the NTLM hash of the inter-forest trust account from a target domain controller. The trust account hash enables forging Kerberos tickets for cross-forest authentication, allowing lateral movement between Active Directory forests without native credentials.

## Description

In multi-forest Active Directory environments, trusts between forests rely on special computer accounts (e.g., 'currentdomain\targetdomain$') that hold cryptographic keys for authentication. Attackers with Domain Admin privileges on one forest can abuse the replication protocol (DCSync) to extract the trust account's NTLM hash from the target forest's domain controller. This hash can then be used with tools like Rubeus or Pass-the-Hash techniques to impersonate the trust account and access resources in the target forest. This technique is particularly effective in trusted forest scenarios where direct credential theft is challenging, but requires high privileges and domain controller access. It targets environments with forest trusts configured for resource sharing.

## Requirements

1. Domain Admin or equivalent privileges in the attacker's forest with replication rights to the target domain controller.
2. Network access to the target domain controller (RPC/DCE port 135, SMB 445).
3. Mimikatz tool installed or available on the attacker's system.
4. Knowledge of the target domain name and a reachable domain controller IP.

## Defense

- Restrict replication rights to highly privileged accounts only and monitor for DCSync abuse via Event ID 4662 (sensitive object access) on domain controllers.
- Implement Protected Users group for trust accounts and enable multi-forest security boundaries.
- Use network segmentation to limit cross-forest DC access and deploy tools like Microsoft Defender for Identity to detect anomalous replication.
- Regularly audit forest trust configurations and disable unnecessary trusts.

## Objectives

1. Identify and target the inter-forest trust account for hash extraction.
2. Perform DCSync replication to dump the NTLM hash of the trust account.
3. Use the extracted hash to forge authentication tickets for the target forest.

## Instructions

### Step 1: Identify the Trust Account

**Context**: Determine the name of the trust account, which follows the format 'attacker_domain\target_domain$' where 'attacker_domain' is your current forest and 'target_domain' is the target forest's root domain. This step ensures you're targeting the correct account for hash dumping.

If not already known, query the current domain's trust information using native tools or PowerView to confirm the trust relationship.

**Success Indicators**:
- Trust account name confirmed (e.g., 'currentdomain\targetdomain$').
- No errors in trust enumeration.

### Step 2: Execute DCSync to Dump Trust Hash

**Context**: Use Mimikatz to impersonate a domain controller and replicate the trust account's hash from the target domain controller. This abuses the Active Directory replication protocol to extract credentials without direct LSASS access on the target.

**Command** ([[commands/mimikatz-lsadump-dcsync-trust-account]]):

Run Mimikatz with the lsadump::dcsync module, specifying the trust account username, target domain, and DC IP.

```cmd
mimikatz.exe "lsadump::dcsync /user:currentdomain\targetdomain$ /domain:targetdomain.com /dc:targetdc_ip"
```

> This command initiates replication for the specified user (trust account) from the target domain. Replace 'currentdomain\targetdomain$' with the actual trust account name, 'targetdomain.com' with the target domain FQDN, and 'targetdc_ip' with the target DC's IP address. The output will include the NTLM hash in the form of 'lm:empty:::::ntlm_hash'.

**Expected Output**:

Sample output showing successful hash dump:

```
[request]  : from \TARGETDC$ -> \TARGETDC$
* User : krbtgt (S-1-5-21-xxx-xxx-xxx-502)
...
** SAM ACCOUNT ** : currentdomain\targetdomain$
  SID : S-1-5-21-xxx-xxx-xxx-1108
  User : targetdomain$
  LM   : empty
  NTLM : aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
  ...
[status]  : OK !
```

**Success Indicators**:
- NTLM hash extracted without errors.
- No access denied or replication failure messages.

### Step 3: Verify and Export Hash

**Context**: Save the extracted NTLM hash for use in subsequent forging steps, such as with Rubeus for ticket generation. Verify the hash format is usable (48-character hex string).

Copy the NTLM hash from the output and store it securely (e.g., in a file like trust_hash.txt). Test the hash offline if possible using tools like hashcat to ensure integrity, though trust hashes are often complex.

**Expected Output**: Hash saved in a format ready for Pass-the-Hash or ticket forging (e.g., 'targetdomain$::aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::').

**Success Indicators**:
- Hash exported without corruption.
- Ready for use in cross-forest authentication tools.
