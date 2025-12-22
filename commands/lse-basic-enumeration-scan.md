---
id: 111ae502-6b1f-4390-9462-081070d30d29
name: lse-basic-enumeration-scan
type: command
executor: bash
data: ./lse.sh -l 1
output: null
created_at: '2019-09-17T06:34:44.725288+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - linux
verified: true
validated: true
---

# lse-basic-enumeration-scan

## Command

```bash
./lse.sh -l 1
```

## Description

Executes Linux Smart Enumeration at level 1 verbosity to perform a basic local system scan, gathering essential information on users, sudo, services, and potential vulnerabilities without requiring a password or deep checks. Use this for an initial high-level assessment during post-exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l 1` | Sets verbosity to basic level (quick overview, no password prompts) | Yes |
| `./lse.sh` | Path to the LSE script (ensure executable) | Yes |

## Examples

### Basic Usage

```bash
./lse.sh -l 1
```

### With Password for Enhanced Results (Level 2)

```bash
./lse.sh -l 2 -p "$_USER_PASSWORD"
```

## Expected Output

```
---
If you know the current user password, write it here for better results: 
---

        User: root
     User ID: 0
    Password: none
        Home: /root
        Path: /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
       umask: 0022

    Hostname: hackers
       Linux: 4.19.0-kali4-amd64
Distribution: Kali GNU/Linux Rolling
Architecture: x86_64

==================================================================( users )=====
[i] usr000 Current user groups............................................. yes!
[*] usr010 Is current user in an administrative group?..................... nope
[*] usr020 Are there other users in an administrative groups?.............. nope
[*] usr030 Other users with shell.......................................... yes!
[i] usr040 Environment information......................................... skip
[i] usr050 Groups for other users.......................................... skip
[i] usr060 Other users..................................................... skip
===================================================================( sudo )=====
[!] sud000 Can we sudo without a password?................................. yes!
---
uid=0(root) gid=0(root) groups=0(root)
---
[*] sud040 Can we read /etc/sudoers?....................................... yes!
[*] sud050 Do we know if any other users used sudo?........................ nope

.... CUT ....
```

Look for [!] indicators for critical findings like passwordless sudo, and [*] for potential issues like administrative users.

## Related

- [[Related Procedure: Linux Local Enumeration]]
- [[commands/lse-full-enumeration-scan]] (for level 3)
