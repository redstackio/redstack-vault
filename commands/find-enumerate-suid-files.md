---
id: 70d037bc-c74b-4bc7-ab8f-bcd48baa351b
type: command
executor: bash
data: find $_DIRECTORY -perm -4000 -ls 2>/dev/null
output: >
  root@hackers:~# find /usr -perm -4000 -ls 2>/dev/null

  -rwsr-xr-x 1 root root 157192 Jan 12  2019 /usr/bin/sudo

  -rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp

  -rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su

  -rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount

  -rwsr-xr-- 1 root kismet 641616 May  7  2018 /usr/bin/kismet_capture

  -rwsr-xr-x 1 root root 23288 Jan 15  2019 /usr/bin/pkexec

  -rwsr-xr-x 1 root root 55400 Mar  6  2019 /usr/bin/bwrap

  -rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount

  -rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn

  -rwsr-xr-x 1 root root 154352 Mar 21 16:52 /usr/bin/ntfs-3g

  -rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd

  -rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd

  -rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh

  -rwsr-xr-x 1 root root 34896 Jan  7  2019 /usr/bin/fusermount

  -rwsr-xr-x 1 root root 436552 Apr  8 03:13 /usr/lib/openssh/ssh-keysign

  -rwsr-xr-x 1 root root 10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device

  -rwsr-sr-x 1 root root 14608 Oct 25  2018 /usr/lib/xorg/Xorg.wrap

  -rwsr-xr-- 1 root messagebus 51184 Dec  4  2018
  /usr/lib/dbus-1.0/dbus-daemon-launch-helper

  -r-sr-xr-x 1 root root 14320 Aug 21 10:23
  /usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper

  -r-sr-xr-x 1 root root 13628 Aug 21 10:23
  /usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper

  -rwsr-xr-x 1 root root 18712 Mar 18 19:19 /usr/lib/chromium/chrome-sandbox

  -rwsr-xr-x 1 root root 18888 Jan 15  2019
  /usr/lib/policykit-1/polkit-agent-helper-1

  -rwsr-xr-- 1 root dip 386792 Mar  9  2019 /usr/sbin/pppd

  -rwsr-xr-x 1 root root 1181320 Feb 20  2019 /usr/sbin/exim4
created_at: '2019-09-17T06:24:10.210583+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - Enumeration
  - Privilege Escalation
verified: true
validated: true
---

# find-enumerate-suid-files

## Command

```bash
find $_DIRECTORY -perm -4000 -ls 2>/dev/null
```

## Description

This command searches for files with the Set User ID (SUID) bit set in the specified directory and its subdirectories. SUID files allow execution with elevated privileges (typically root), which can be exploited for privilege escalation if misconfigured. The -ls option provides detailed listing, and 2>/dev/null suppresses permission denied errors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DIRECTORY | Starting directory for the search (e.g., / or /usr) | Yes |
| -perm -4000 | Matches files with SUID bit set (at least 4000 permissions) | Built-in |
| -ls | Lists matches in long format (like ls -l) | Built-in |
| 2>/dev/null | Redirects stderr to null to hide access errors | Built-in |

## Examples

### Basic Usage

Search for SUID files starting from the root directory:

```bash
find / -perm -4000 -ls 2>/dev/null
```

### Advanced Usage

Search only in /usr/bin for SUID executables:

```bash
find /usr/bin -perm -4000 -ls 2>/dev/null
```

## Expected Output

A list of SUID files with details including permissions, owner, size, and path. Example:

```
root@hackers:~# find /usr -perm -4000 -ls 2>/dev/null
-rwsr-xr-x 1 root root 157192 Jan 12  2019 /usr/bin/sudo
-rwsr-xr-x 1 root root 44440 Jul 27  2018 /usr/bin/newgrp
-rwsr-xr-x 1 root root 63568 Jan 10  2019 /usr/bin/su
-rwsr-xr-x 1 root root 34888 Jan 10  2019 /usr/bin/umount
-rwsr-xr-- 1 root kismet 641616 May  7  2018 /usr/bin/kismet_capture
-rwsr-xr-x 1 root root 23288 Jan 15  2019 /usr/bin/pkexec
-rwsr-xr-x 1 root root 55400 Mar  6  2019 /usr/bin/bwrap
-rwsr-xr-x 1 root root 51280 Jan 10  2019 /usr/bin/mount
-rwsr-xr-x 1 root root 54096 Jul 27  2018 /usr/bin/chfn
-rwsr-xr-x 1 root root 154352 Mar 21 16:52 /usr/bin/ntfs-3g
-rwsr-xr-x 1 root root 84016 Jul 27  2018 /usr/bin/gpasswd
-rwsr-xr-x 1 root root 63736 Jul 27  2018 /usr/bin/passwd
-rwsr-xr-x 1 root root 44528 Jul 27  2018 /usr/bin/chsh
-rwsr-xr-x 1 root root 34896 Jan  7  2019 /usr/bin/fusermount
-rwsr-xr-x 1 root root 436552 Apr  8 03:13 /usr/lib/openssh/ssh-keysign
-rwsr-xr-x 1 root root 10232 Mar 27  2017 /usr/lib/eject/dmcrypt-get-device
-rwsr-sr-x 1 root root 14608 Oct 25  2018 /usr/lib/xorg/Xorg.wrap
-rwsr-xr-- 1 root messagebus 51184 Dec  4  2018 /usr/lib/dbus-1.0/dbus-daemon-launch-helper
-r-sr-xr-x 1 root root 14320 Aug 21 10:23 /usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
-r-sr-xr-x 1 root root 13628 Aug 21 10:23 /usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
-rwsr-xr-x 1 root root 18712 Mar 18 19:19 /usr/lib/chromium/chrome-sandbox
-rwsr-xr-x 1 root root 18888 Jan 15  2019 /usr/lib/policykit-1/polkit-agent-helper-1
-rwsr-xr-- 1 root dip 386792 Mar  9  2019 /usr/sbin/pppd
-rwsr-xr-x 1 root root 1181320 Feb 20  2019 /usr/sbin/exim4
```

Success is indicated by listing files with 's' in the owner permissions (e.g., -rwsr-xr-x).

## Related

- [[tools/find]]
- [[Related Procedure for SUID Exploitation]]
