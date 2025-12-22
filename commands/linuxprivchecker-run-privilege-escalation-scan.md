---
id: 74027deb-aee5-4eed-9d25-879abbe42b19
name: linuxprivchecker-run-privilege-escalation-scan
type: command
executor: bash
data: python linuxprivchecker.py
output: >
  root@hackers:~/git/linuxprivchecker# python linuxprivchecker.py 

  =================================================================================================

  LINUX PRIVILEGE ESCALATION CHECKER

  =================================================================================================


  [*] GETTING BASIC SYSTEM INFO...


  [+] Kernel
      Linux version 4.19.0-kali4-amd64 (devel@kali.org) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP Debian 4.19.28-2kali1 (2019-03-18)

  [+] Hostname
      hackers

  [+] Operating System
      Kali GNU/Linux Rolling \n \l

  .... CUT ....
created_at: '2019-09-17T06:34:44.714301+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - Enumeration
  - Privilege Escalation
verified: true
validated: true
---

# linuxprivchecker-run-privilege-escalation-scan

## Command

```bash
python linuxprivchecker.py
```

## Description

This command executes the linuxprivchecker.py script on a Linux target to perform a comprehensive privilege escalation enumeration. It checks for misconfigurations, writable files, SUID binaries, cron jobs, and potential kernel exploits without requiring any arguments. Use this during post-exploitation to identify escalation paths locally.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The script accepts no parameters; it runs all checks by default | N/A |

## Examples

### Basic Usage

Run the full scan on the target:

```bash
python linuxprivchecker.py
```

### Advanced Usage

Redirect output for offline analysis:

```bash
python linuxprivchecker.py > /tmp/priv_esc_report.txt 2>&1
```

## Expected Output

The script outputs a detailed report starting with system info and proceeding through various checks. Successful execution produces sections like kernel details, hostname, and enumerations of potential vectors. Example excerpt:

```
root@hackers:~/git/linuxprivchecker# python linuxprivchecker.py 
=================================================================================================
LINUX PRIVILEGE ESCALATION CHECKER
=================================================================================================

[*] GETTING BASIC SYSTEM INFO...

[+] Kernel
    Linux version 4.19.0-kali4-amd64 (devel@kali.org) (gcc version 8.3.0 (Debian 8.3.0-2)) #1 SMP Debian 4.19.28-2kali1 (2019-03-18)

[+] Hostname
    hackers

[+] Operating System
    Kali GNU/Linux Rolling \n \l

.... CUT ....
```

Look for [+] indicators of findings (e.g., writable files) and [!] for potential exploits.

## Related

- [[Related Procedure: Linux Privilege Escalation Enumeration]]
- [[tools/linuxprivchecker]]
