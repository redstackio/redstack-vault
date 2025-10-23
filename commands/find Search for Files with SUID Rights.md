---
id: 70d037bc-c74b-4bc7-ab8f-bcd48baa351b
name: find Search for Files with SUID Rights
type: command
executor: bash
data: find $_DIRECTORY -perm -4000 -ls 2>/dev/null
output: 'root@hackers:~# find /usr -perm -4000 -ls 2>/dev/null

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

  '
created_at: '2019-09-17T06:24:10.210583+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# find Search for Files with SUID Rights

```bash
find $_DIRECTORY -perm -4000 -ls 2>/dev/null
```

## Expected Output

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


