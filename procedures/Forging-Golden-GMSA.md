---
id: 3be2e98f-e501-423b-8719-eca4c50a72f4
name: Forging-Golden-GMSA
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.628923+00:00'
updated_at: '2023-04-10T20:25:56.688767+00:00'
tactics:
  - '[[Privilege Escalation]]'
techniques:
  - '[[Steal or Forge Kerberos Tickets]]'
  - '[[Golden Ticket]]'
sub_techniques: []
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Forging Golden GMSA]]'
  - active-directory
  - gmsa
  - kerberos
  - privilege-escalation
commands:
  - '[[commands/golden-gmsa-enumerate-all-gmsas]]'
  - '[[commands/golden-gmsa-query-specific-gmsa]]'
  - '[[commands/golden-gmsa-dump-all-kds-root-keys]]'
  - '[[commands/golden-gmsa-dump-specific-kds-root-key]]'
  - '[[commands/golden-gmsa-compute-password-privileged-access]]'
  - '[[commands/golden-gmsa-compute-password-ldap-access]]'
  - '[[commands/golden-gmsa-compute-password-offline-mode]]'
platforms:
  - Windows
tools:
  - '[[tools/GoldenGMSA]]'
validated: true
---

# Forging-Golden-GMSA

## Summary

Forging a Golden GMSA is an advanced Active Directory attack technique that allows attackers to create forged Group Managed Service Account (GMSA) credentials, enabling authentication to domain services and potential privilege escalation. By computing GMSA passwords using Key Distribution Service (KDS) root keys, attackers can impersonate service accounts without direct access to the domain controller in some modes.

## Description

In an Active Directory environment, Group Managed Service Accounts (GMSAs) are used for automated password management for services. Attackers with sufficient access can enumerate GMSAs, extract KDS root keys, and compute passwords for these accounts using tools like GoldenGMSA.exe. This forged credential can then be used for lateral movement, persistence, or accessing restricted resources. The technique supports multiple modes: privileged domain access (full computation on-domain), LDAP access (using fetched keys), and offline (using pre-dumped keys and password IDs). This is particularly effective in environments with misconfigured GMSAs or weak KDS key protection, leading to domain compromise.

## Requirements

1. Domain-joined Windows system with network access to Active Directory.
2. Appropriate privileges: Domain Admin or equivalent for privileged mode; LDAP read access for key dumping; offline dumps for no-access scenarios.
3. GoldenGMSA.exe tool installed.
4. Knowledge of target GMSA SID or GUID for specific operations.

## Defense

- Limit creation and modification of GMSAs to trusted administrators.
- Implement least privilege for LDAP queries to restrict KDS key access.
- Monitor for anomalous GMSA usage, password computations, or tool executions via EDR.
- Use protected users groups and disable RC4 encryption to harden Kerberos.
- Regularly audit KDS root keys and rotate them if compromise is suspected.

## Objectives

1. Escalate privileges by forging GMSA credentials for service impersonation.
2. Gain unauthorized access to domain resources and sensitive systems.
3. Achieve persistence through valid-looking service account authentication.

## Instructions

### Step 1: Enumerate All GMSAs

**Context**: Begin by discovering all available Group Managed Service Accounts in the domain to identify potential targets for forging. This step requires LDAP read access and provides SIDs for further operations.

**Command** ([[commands/golden-gmsa-enumerate-all-gmsas]]):
```bash
GoldenGMSA.exe gmsainfo
```

> This command queries the domain for all GMSAs and lists their details, including SIDs. Use this to select a high-value GMSA, such as one tied to critical services.

### Step 2: Query Specific GMSA

**Context**: If a specific GMSA is known (e.g., from prior enumeration or reconnaissance), query its details using the SID to confirm attributes before proceeding to key dumping or password computation.

**Command** ([[commands/golden-gmsa-query-specific-gmsa]]):
```bash
GoldenGMSA.exe gmsainfo --sid $_GMSA_SID
```

> Replace $_GMSA_SID with the target SID (e.g., S-1-5-21-1437000690-1664695696-1586295871-1112). Expected output includes GMSA name, SID, and managed password ID if accessible.

### Step 3: Dump All KDS Root Keys

**Context**: Extract all Key Distribution Service root keys from the domain, which are required for computing GMSA passwords. This step needs LDAP access to the domain controller.

**Command** ([[commands/golden-gmsa-dump-all-kds-root-keys]]):
```bash
GoldenGMSA.exe kdsinfo
```

> This lists all available KDS root keys with their GUIDs and Base64-encoded blobs. Save the output for use in password computation steps.

### Step 4: Dump Specific KDS Root Key

**Context**: For targeted operations, dump a specific KDS root key using its GUID, reducing noise and focusing on the key associated with the target GMSA.

**Command** ([[commands/golden-gmsa-dump-specific-kds-root-key]]):
```bash
GoldenGMSA.exe kdsinfo --guid $_KDS_GUID
```

> Replace $_KDS_GUID with the key's GUID (e.g., 46e5b8b9-ca57-01e6-e8b9-fbb267e4adeb). Output is the Base64-encoded key blob for offline or LDAP use.

### Step 5: Compute GMSA Password with Privileged Access

**Context**: If the attacker has privileged domain access (e.g., Domain Admin), compute the GMSA password directly using the SID. This mode fetches keys automatically.

**Command** ([[commands/golden-gmsa-compute-password-privileged-access]]):
```bash
GoldenGMSA.exe compute --sid $_GMSA_SID
```

> Replace $_GMSA_SID with the target. Expected output is the computed password or hash, usable for authentication.

### Step 6: Compute GMSA Password with LDAP Access

**Context**: With LDAP read access but no privileges, provide the KDS key manually to compute the password. This is useful for mid-level compromises.

**Command** ([[commands/golden-gmsa-compute-password-ldap-access]]):
```bash
GoldenGMSA.exe compute --sid $_GMSA_SID --kdskey $_KDS_KEY
```

> Replace $_GMSA_SID and $_KDS_KEY (Base64 blob, e.g., AQAAALm45UZXyuYB[...]G2/M=). Output: Computed password for the GMSA.

### Step 7: Compute GMSA Password in Offline Mode

**Context**: For fully offline forging, use pre-dumped KDS key and the GMSA's managed password ID (from msDS-ManagedPasswordId attribute) to compute without any domain access.

**Command** ([[commands/golden-gmsa-compute-password-offline-mode]]):
```bash
GoldenGMSA.exe compute --sid $_GMSA_SID --kdskey $_KDS_KEY --pwdid $_PWD_ID
```

> Replace placeholders: $_GMSA_SID, $_KDS_KEY (Base64), $_PWD_ID (Base64 from LDAP dump, e.g., AQAAA[..]AAA). This yields the plaintext password offline.
