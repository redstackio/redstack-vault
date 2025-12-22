---
type: procedure
tactics:
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Unsecured Credentials|T1552 - Unsecured Credentials]]'
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - >-
    [[sub-techniques/SSH Authorized Keys File|T1552.007 - SSH Authorized Keys
    File]]
tags:
  - '[[tags/Linux - Privilege Escalation]]'
  - '[[tags/SSH Key]]'
  - '[[tags/SSH Key Predictable PRNG]]'
commands:
  - '[[commands/grep-search-predictable-ssh-key-string]]'
platforms:
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Linux-SSH-Key-Predictable-PRNG-Privilege-Escalation

## Summary

This procedure exploits vulnerabilities in the predictable Pseudo Random Number Generator (PRNG) used during SSH key generation on vulnerable Linux systems, such as those affected by historical issues like the Debian OpenSSL weakness. By searching for a known weak key identifier string in authorized_keys files across user home directories, an attacker with initial low-privilege shell access can identify weak public keys. These can then be used to predict or brute-force corresponding private keys, enabling unauthorized SSH access to higher-privilege accounts for privilege escalation.

## Description

The predictable PRNG flaw leads to SSH keys with low entropy, making private keys recoverable if the public key and generation details are known. This procedure assumes initial foothold access (e.g., via a user account) on a Linux target. The attacker searches for files containing a specific weak string (derived from known vulnerable key comments) in ~/.ssh/authorized_keys. Upon discovery, the weak public key is extracted, and offline tools (like custom scripts or known exploits for the PRNG) are used to derive the private key. With the private key, the attacker can SSH into the target as the privileged user, achieving escalation. This technique is realistic in legacy or unpatched environments and maps to accessing valid accounts via unsecured credentials stored in SSH authorized keys files.

## Requirements

1. Initial low-privilege shell access to the target Linux system (e.g., via compromised user account).
2. Read access to user home directories and .ssh folders (may require enumeration of permissions).
3. Knowledge of the weak PRNG string identifier (e.g., from vulnerability research like Debian SSH weak keys).
4. Offline access to tools for private key prediction (e.g., custom PRNG recovery scripts; not covered in this procedure but referenced externally).
5. SSH client on the attacker's machine to test derived keys.

## Defense

- Ensure SSH key generation uses high-entropy PRNG (e.g., update OpenSSL and use /dev/urandom).
- Regularly audit and rotate SSH keys, removing weak or known vulnerable ones using tools like ssh-keygen -y for verification.
- Restrict .ssh/authorized_keys permissions to 600 and owned by the user (no world-readable).
- Enable SSH logging (e.g., via syslog) and monitor for anomalous key usage or failed authentications.
- Use certificate-based authentication or restrict SSH to key-based only with multi-factor where possible.

## Objectives

1. Identify weak SSH public keys in authorized_keys files using PRNG fingerprint strings.
2. Derive private keys from discovered weak public keys to impersonate privileged users.
3. Achieve privilege escalation by SSH-ing into higher-privilege accounts on the target.
4. Maintain persistence via the escalated SSH access for further operations.

## Instructions

### Step 1: Enumerate User Directories for SSH Access

**Context**: Begin by identifying potential user home directories where authorized_keys files may reside, focusing on those readable from your current privilege level. This step ensures efficient targeting and avoids unnecessary searches.

Use basic Linux commands to list home directories:

```bash
ls /home
```

> This lists users like /home/user1, /home/admin. Expected output: A list of directories. If no read access, note permission denied errors and target writable or readable ones.

Decision point: If running as root or high priv, skip to Step 2; otherwise, check permissions with `ls -la /home/*/`. Proceed only to readable .ssh folders.

### Step 2: Search for Predictable PRNG Weak Key String

**Context**: Use the grep command to recursively search for the known weak PRNG string in authorized_keys files. This string is a fingerprint from vulnerable key generation processes (e.g., 'AAAA487rt384ufrgh432087fhy02nv84u7fg839247fg8743gf087b3849yb98304yb9v834ybf'). Success here identifies files with weak keys.

**Command** ([[commands/grep-search-predictable-ssh-key-string]]):

```bash
grep -lr 'AAAA487rt384ufrgh432087fhy02nv84u7fg839247fg8743gf087b3849yb98304yb9v834ybf' /home/*/.ssh/authorized_keys 2>/dev/null
```

> The -l flag lists only filenames, -r recurses into directories, and 2>/dev/null suppresses errors. Expected output: Paths to files like /home/admin/.ssh/authorized_keys if containing the string. If no output, no weak keys found—abort or expand search to /root/.ssh if accessible.

### Step 3: Extract and Analyze Weak Public Key

**Context**: Once a file is identified, extract the public key line containing the weak string. This key will be used offline to predict the private key based on the PRNG flaw.

Copy the file content:

```bash
cat /home/admin/.ssh/authorized_keys | grep 'AAAA487rt384ufrgh432087fhy02nv84u7fg839247fg8743gf087b3849yb98304yb9v834ybf'
```

> Expected output: The full public key line, e.g., ssh-rsa AAAAB3NzaC1yc2E... comment:AAAA487rt.... Save this to a local file (e.g., weak_pub.key) for offline processing.

Decision point: Verify the key type (e.g., DSA/RSA) matches known vulnerable formats (often DSA 1024-bit from old Debian).

### Step 4: Predict Private Key Offline

**Context**: Transfer the public key to your attacker machine and use PRNG recovery tools (e.g., custom scripts exploiting the Debian weak key generator) to derive the private key. This step requires external research/tools not executed on-target.

On attacker machine (example using hypothetical tool):

```bash
# Example: Use a PRNG recovery script (research-specific to vuln)
python prng_ssh_key_recover.py weak_pub.key > predicted_priv.key
```

> Expected output: A PEM-formatted private key file. Test validity with `ssh-keygen -y -f predicted_priv.key` to regenerate public key and match.

### Step 5: Escalate via SSH with Predicted Key

**Context**: Use the predicted private key to SSH into the target as the privileged user, achieving escalation. Ensure SSH daemon allows key auth.

From attacker machine:

```bash
ssh -i predicted_priv.key admin@target_ip
```

> Expected output: Successful shell prompt as 'admin' without password. If fails, recheck key derivation or permissions.

Decision point: If escalation to root needed, repeat process targeting /root/.ssh/authorized_keys or chain with other priv esc techniques.
