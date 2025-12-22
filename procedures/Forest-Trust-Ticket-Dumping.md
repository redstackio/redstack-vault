---
id: 2f9d6500-e41a-427b-b0ae-1282a6d6563e
name: Forest-Trust-Ticket-Dumping
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:07.296686+00:00'
updated_at: '2023-04-10T20:26:22.966685+00:00'
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
  - '[[tactics/Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
  - '[[techniques/Domain Trust Discovery|T1482 - Domain Trust Discovery]]'
  - '[[techniques/Pass the Ticket|T1097 - Pass the Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Dumping trust passwords (trust keys)]]'
  - '[[tags/Forest to Forest Compromise - Trust Ticket]]'
commands:
  - '[[commands/mimikatz-lsadump-trust-extract]]'
  - '[[commands/windows-reg-query-trust-account-hash]]'
platforms:
  - Windows
tools:
  - '[[tools/Mimikatz]]'
validated: true
---

# Forest-Trust-Ticket-Dumping

## Summary

Forest Trust Ticket Dumping is a post-exploitation technique in Active Directory environments that allows attackers with access to a domain controller to extract trust account hashes. These hashes can then be used to forge Kerberos tickets for accessing resources in a trusted forest, enabling lateral movement across forest boundaries without valid credentials in the target forest.

## Description

In multi-forest Active Directory setups, trust relationships are established to allow resource sharing between forests. Each trust is represented by a special machine account (e.g., TRUST_NAME$) whose password hash is stored on domain controllers. By compromising a domain controller in one forest and using tools like Mimikatz, an attacker can dump these trust hashes from the LSASS process or registry. The extracted hashes (typically NTLM) can be used in pass-the-hash attacks or to request trust tickets via tools like Rubeus or custom scripts. This technique is effective in environments with forest trusts and is commonly used after initial domain compromise to expand the attack surface to interconnected forests. It requires high privileges, such as Domain Admin or equivalent, and targets Windows Server domain controllers running Active Directory.

## Requirements

1. Compromised access to a domain controller in the source forest with Domain Admin privileges or DCSync rights.
2. Mimikatz tool installed or transferred to the target system.
3. Local administrator privileges on the domain controller to inject into LSASS.
4. Knowledge of the target forest trust name (e.g., via enumeration of trusts using nltest or PowerView).

## Defense

- Implement strong password policies and regularly rotate trust account passwords, considering inter-forest trusts high-risk.
- Monitor for suspicious activity on domain controllers, such as anomalous LSASS access, Mimikatz process signatures, or unusual Kerberos ticket requests involving trust accounts.
- Use network segmentation to isolate domain controllers and limit lateral movement between forests; consider disabling unnecessary trusts.
- Enable advanced auditing for privilege use and process creation on DCs; deploy tools like Microsoft Defender for Identity to detect trust enumeration and dumping attempts.

## Objectives

1. Extract trust account hashes from a compromised domain controller to impersonate the trust relationship.
2. Forge Kerberos tickets using the hashes for authentication to the trusted forest.
3. Achieve lateral movement and access sensitive resources in the target forest.

## Instructions

### Step 1: Verify Trust Enumeration and Prerequisites

**Context**: Before dumping, confirm the existence of forest trusts to identify the target trust account. This step ensures you have the necessary context and privileges, preventing errors during extraction.

Use domain enumeration tools (e.g., PowerView or nltest) to list trusts. For example, run `nltest /domain_trusts` from an elevated command prompt to verify the trust name.

**Expected Output**: A list of trusted domains/forests, such as "TRUST_NAME (Forest Trust)".

If no trusts are present, this procedure is not applicable; proceed only if inter-forest trusts exist.

### Step 2: Launch Mimikatz with Elevated Privileges

**Context**: Mimikatz requires SeDebugPrivilege to access LSASS. This step initializes the tool securely on the compromised domain controller.

Transfer and execute Mimikatz.exe as an administrator. Open an elevated command prompt and navigate to the Mimikatz directory.

**Command** ([[commands/mimikatz-lsadump-trust-extract]]):

Run Mimikatz and elevate:

```cmd
mimikatz.exe "privilege::debug" "exit"
```

> This grants debug privileges. Expected output: "Privilege '20' OK". If failed, ensure DA privileges and retry.

### Step 3: Extract Trust Account Hashes Using LSADump

**Context**: The core extraction step targets the trust keys stored in LSASS. The /patch option retrieves AES and RC4 keys for the trust accounts, enabling ticket generation.

Within the Mimikatz prompt, execute the LSADump module.

**Command** ([[commands/mimikatz-lsadump-trust-extract]]):

```cmd
lsadump::trust /patch
```

> This queries all trust accounts and outputs their hashes (NTLM, AES128/256 keys). Expected output: A table-like list showing trust names, realms, and keys, e.g., "* Trust: TRUST_NAME$ / NTLM: aad3b435b51404eeaad3b435b51404ee:5e4c...". Save this output for offline cracking or direct use in pass-the-ticket.

### Step 4: Alternative Extraction via Registry Query

**Context**: If Mimikatz is unavailable or LSASS access is restricted, query the SAM registry for trust-related aliases. This is less reliable for full hashes but can reveal trust account references for further enumeration.

From an elevated command prompt, search the registry.

**Command** ([[commands/windows-reg-query-trust-account-hash]]):

```cmd
reg query HKLM\SAM\SAM\Domains\Account\Aliases /s | findstr /i trust
```

> This searches for trust-related entries. Expected output: Registry paths containing 'trust' strings, potentially leading to SID or hash references. Cross-reference with trust names from Step 1; this method may require additional tools like secretsdump for full extraction if hashes are partial.

### Step 5: Validate and Use Extracted Hashes

**Context**: Verify the hashes and prepare for ticket generation. This confirms success and sets up for lateral movement.

Review the output from Step 3 for valid NTLM hashes (should be 32 hex characters). Use tools like Rubeus to request a trust ticket: `Rubeus.exe asktgt /user:TRUST_NAME$ /rc4:HASH /getcredentials`. Expected output: A .kirbi ticket file if successful.

If hashes are weak, crack offline with Hashcat using a wordlist of domain names.

**Success Indicators**:
- Trust hashes extracted without errors.
- Ability to generate valid Kerberos tickets using the hashes.
- No alerts from EDR on LSASS access.
