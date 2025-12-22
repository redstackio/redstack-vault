---
id: 9d862c4b-ecdb-4bd9-8506-df7bd525c730
name: Crack-NTLM-Hashes-with-Hashcat
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:04.102377+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
techniques:
  - '[[techniques/Brute Force|T1110 - Brute Force]]'
sub_techniques:
  - '[[sub-techniques/Password Cracking|T1110.002 - Password Cracking]]'
  - '[[sub-techniques/Password Guessing|T1110.001 - Password Guessing]]'
tags:
  - '[[tags/Active Directory Attacks]]'
  - '[[tags/Crack NTLM hashes with hashcat]]'
  - '[[tags/Dumping AD Domain Credentials]]'
commands:
  - '[[commands/git-clone-iphelix-pack]]'
  - '[[commands/statsgen-generate-stats-from-potfile]]'
  - '[[commands/maskgen-generate-custom-mask]]'
  - '[[commands/hashcat-crack-ntlm-dictionary-attack]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Hashcat]]'
validated: true
---

# Crack-NTLM-Hashes-with-Hashcat

## Summary

This procedure outlines how to crack NTLM password hashes obtained from a Windows environment using Hashcat. It covers generating custom masks based on previous cracks from a potfile and performing dictionary-based attacks to recover plaintext passwords, enabling further access to user accounts and potential privilege escalation.

## Description

NTLM hashes are a legacy authentication mechanism in Windows environments used to store and transmit password credentials. Attackers often obtain these hashes by dumping them from memory (e.g., using Mimikatz on a domain controller) or from files like SAM hives. Once acquired, Hashcat can be used to perform offline cracking via dictionary attacks, rule-based mutations, or custom masks derived from patterns in previously cracked passwords. This technique is effective against weak or common passwords and is commonly applied in Active Directory compromise scenarios to expand lateral movement. The procedure assumes the attacker has the hashes in a file and access to a cracking rig with GPU acceleration for efficiency.

## Requirements

1. NTLM hashes in a file (e.g., from Mimikatz output or ntds.dit extraction).
2. Hashcat installed on a system with GPU support (NVIDIA/AMD recommended for speed).
3. A wordlist/dictionary file (e.g., rockyou.txt) and optional rules file (e.g., best64.rule).
4. Access to a .potfile from previous Hashcat sessions for mask generation.
5. Python 2 installed for mask generation scripts.
6. Git installed to clone required repositories.

## Defense

- Implement strong password policies enforcing length, complexity, and regular rotation to resist cracking.
- Monitor for credential dumping tools like Mimikatz via process monitoring and EDR solutions.
- Enable Windows protected users group and restrict NTLM usage where possible (e.g., via Group Policy).
- Use account lockout policies and multi-factor authentication (MFA) to limit impact of cracked credentials.
- Detect offline cracking attempts by monitoring for unusual GPU/CPU usage on internal systems.

## Objectives

1. Generate a custom cracking mask based on patterns from previously cracked passwords.
2. Perform a dictionary attack on NTLM hashes using Hashcat to recover plaintext passwords.
3. Validate cracked credentials for use in further attacks, such as lateral movement in Active Directory.

## Instructions

### Step 1: Clone Mask Generation Tools

**Context**: The iphelix/pack repository provides Python scripts for generating optimized masks from Hashcat potfiles, which capture patterns from previously cracked passwords to improve future attacks.

**Command** ([[commands/git-clone-iphelix-pack]]):
```bash
git clone https://github.com/iphelix/pack
```

> This clones the repository containing statsgen.py and maskgen.py. Run this once in a working directory. Expected output includes download progress and confirmation of cloned files. If already cloned, skip this step.

### Step 2: Generate Statistics from Potfile

**Context**: statsgen.py analyzes the Hashcat .potfile (which stores cracked hash:password pairs) to identify common character patterns, lengths, and structures for mask creation.

**Command** ([[commands/statsgen-generate-stats-from-potfile]]):
```bash
cd pack
python2 statsgen.py ../hashcat.potfile -o hashcat.mask
```

> Navigate to the cloned pack directory and run statsgen.py, pointing to your .potfile and output mask file. This step creates a base mask file from historical cracks. Expected output: A hashcat.mask file generated without errors, containing statistical patterns.

### Step 3: Generate Custom Mask

**Context**: maskgen.py uses the statistics to produce an optimized .hcmask file tailored for a target runtime (e.g., 1 hour), prioritizing likely patterns for efficient cracking.

**Command** ([[commands/maskgen-generate-custom-mask]]):
```bash
python2 maskgen.py hashcat.mask --targettime 3600 --optindex -q -o hashcat_1H.hcmask
```

> Run maskgen.py with the stats file, specifying 3600 seconds (1 hour) target time, optimization index for best candidates first, quiet mode (-q), and output file. This produces a mask file for use in Hashcat. Expected output: hashcat_1H.hcmask file created, with console output showing generated masks (suppressed by -q).

### Step 4: Crack Hashes with Dictionary Attack

**Context**: Use Hashcat to perform a straight dictionary attack on NTLM hashes, optionally applying rules for mutations and optimizing for performance. This step recovers passwords if they match the wordlist or rules.

**Command** ([[commands/hashcat-crack-ntlm-dictionary-attack]]):
```bash
hashcat -m 1000 -w 4 -O -a 0 -o cracked.pot hashes.txt wordlist.txt -r rules/best64.rule --opencl-device-types 1,2
```

> Execute Hashcat with NTLM mode (-m 1000), insane workload (-w 4), optimizations (-O), dictionary attack (-a 0), output to potfile, input hash file, wordlist, rules, and GPU device types. Replace placeholders with actual paths. This runs until completion or interruption. Expected output: Progress updates, speed metrics, and recovered passwords displayed (e.g., 'user:password' if cracked), saved to cracked.pot.
