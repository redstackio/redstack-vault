---
type: procedure
verified: true
submitted: false
tactics:
  - '[[tactics/Credential-Access]]'
techniques:
  - '[[techniques/Steal-or-Forge-Kerberos-Tickets]]'
sub_techniques:
  - '[[sub-techniques/Kerberoasting]]'
  - '[[sub-techniques/AS-REP-Roasting]]'
tags:
  - '[[tags/Active-Directory-Attacks]]'
  - '[[tags/Kerberos]]'
  - '[[tags/Keytab]]'
  - '[[tags/CCACHE]]'
commands:
  - '[[commands/git-clone-keytabparser]]'
  - '[[commands/python-keytabparser-parse-keytab]]'
  - '[[commands/kinit-generate-tgt-from-keytab]]'
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Extract-and-Reuse-Kerberos-Tickets-from-Keytab

## Summary

This procedure demonstrates how to extract Kerberos credentials from a keytab file and use them to generate a Credential Cache (CCACHE) file containing a Ticket Granting Ticket (TGT). This allows reuse of service account credentials for authentication to Active Directory resources without needing the plaintext password, enabling lateral movement or access to restricted services.

## Description

In Active Directory environments, keytab files store long-term Kerberos keys for service accounts, often used by applications for authentication. If an attacker obtains a keytab (e.g., via file access on a compromised host or misconfiguration), they can parse it to identify usable credentials and then initialize a Kerberos session to obtain reusable tickets. This technique leverages tools like KeytabParser for inspection and standard Kerberos utilities like kinit to create a CCACHE file. The resulting CCACHE can be loaded into tools like Mimikatz, Rubeus, or Impacket for further attacks such as service ticket requests (Kerberoasting) or pass-the-ticket. This is particularly effective in Linux/Unix hosts running services like SSH or in cross-platform AD setups. Prerequisites include having the keytab file and Kerberos client tools installed. Success enables persistent authentication without alerting password-based logins.

## Requirements

1. Access to a keytab file (e.g., /etc/krb5.keytab) containing service account credentials.
2. Kerberos client tools installed (e.g., krb5-user package on Linux, providing kinit and klist).
3. Python 3 environment for running KeytabParser.
4. Network access to the domain controller for ticket requests.
5. Knowledge of the service principal name (SPN) and realm from the keytab.

## Defense

- Restrict access to keytab files using file permissions (e.g., 600 ownership by service account) and monitor for unauthorized reads via file auditing.
- Implement least-privilege for service accounts and regularly rotate keytab contents.
- Enable Kerberos logging on domain controllers to detect anomalous ticket requests from service accounts.
- Use monitoring tools like Sysmon or EDR to alert on keytab access or execution of parsing tools like KeytabParser.
- Enforce ticket signing and encryption policies to limit replay attacks.

## Objectives

1. Parse the keytab to identify extractable Kerberos keys and principals.
2. Generate a CCACHE file with a valid TGT for the service account.
3. Enable reuse of the TGT for authentication to AD resources, facilitating lateral movement.

## Instructions

### Step 1: Clone KeytabParser Repository

**Context**: KeytabParser is a Python tool for inspecting and extracting details from keytab files, including encryption types and principal names, which helps identify the correct principal for TGT generation.

**Command** ([[commands/git-clone-keytabparser]]):
```bash
git clone https://github.com/its-a-feature/KeytabParser
```

> This clones the repository to your current directory. Navigate into the cloned directory if needed for execution. Expected output includes download progress and confirmation of the clone.

### Step 2: Parse the Keytab File

**Context**: Running KeytabParser on the keytab reveals the contained keys, principals, and potential weaknesses (e.g., RC4 encryption), allowing selection of the appropriate principal for the next step.

**Command** ([[commands/python-keytabparser-parse-keytab]]):
```bash
python KeytabParser.py $_KEYTAB_PATH
```

> Replace $_KEYTAB_PATH with the path to your keytab (e.g., /etc/krb5.keytab). This step outputs a detailed parse of the keytab contents. If the principal or realm is unknown, note it from this output for use in Step 3.

### Step 3: Generate CCACHE with TGT from Keytab

**Context**: Using the identified principal, initialize a Kerberos session with kinit to obtain a TGT and store it in the default CCACHE file (usually /tmp/krb5cc_<uid>). This creates the reusable ticket for further authentication.

**Command** ([[commands/kinit-generate-tgt-from-keytab]]):
```bash
kinit -kt $_KEYTAB_PATH $_PRINCIPAL@$_REALM
```

> Replace $_KEYTAB_PATH with the keytab path, $_PRINCIPAL with the service principal (e.g., host/server.example.com), and $_REALM with the AD realm (e.g., EXAMPLE.COM). This authenticates silently using the keytab and caches the TGT. Verify with `klist` to see the ticket.
