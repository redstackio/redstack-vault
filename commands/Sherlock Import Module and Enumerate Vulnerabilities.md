---
id: 6afe9cbd-693c-4c34-b66a-fe0ff066772b
name: Sherlock Import Module and Enumerate Vulnerabilities
type: command
executor: powershell
data: Find-AllVulns
output: 'PS C:\> Find-AllVulns

  Title      : User Mode to Ring (KiTrap0D)

  MSBulletin : MS10-015

  CVEID      : 2010-0232

  Link       : https://www.exploit-db.com/exploits/11199/

  VulnStatus : Not supported on 64-bit systems

  Title      : Task Scheduler .XML

  MSBulletin : MS10-092

  CVEID      : 2010-3338, 2010-3888

  Link       : https://www.exploit-db.com/exploits/19930/

  VulnStatus : Not Vulnerable

  Title      : NTUserMessageCall Win32k Kernel Pool Overflow

  MSBulletin : MS13-053

  CVEID      : 2013-1300

  Link       : https://www.exploit-db.com/exploits/33213/

  VulnStatus : Not supported on 64-bit systems

  Title      : TrackPopupMenuEx Win32k NULL Page

  MSBulletin : MS13-081

  CVEID      : 2013-3881

  Link       : https://www.exploit-db.com/exploits/31576/

  VulnStatus : Not supported on 64-bit systems

  Title      : TrackPopupMenu Win32k Null Pointer Dereference

  MSBulletin : MS14-058

  CVEID      : 2014-4113

  Link       : https://www.exploit-db.com/exploits/35101/

  VulnStatus : Not Vulnerable

  Title      : ClientCopyImage Win32k

  MSBulletin : MS15-051

  CVEID      : 2015-1701, 2015-2433

  Link       : https://www.exploit-db.com/exploits/37367/

  VulnStatus : Not Vulnerable

  Title      : Font Driver Buffer Overflow

  MSBulletin : MS15-078

  CVEID      : 2015-2426, 2015-2433

  Link       : https://www.exploit-db.com/exploits/38222/

  VulnStatus : Not Vulnerable

  Title      : ''mrxdav.sys'' WebDAV

  MSBulletin : MS16-016

  CVEID      : 2016-0051

  Link       : https://www.exploit-db.com/exploits/40085/

  VulnStatus : Not supported on 64-bit systems

  Title      : Secondary Logon Handle

  MSBulletin : MS16-032

  CVEID      : 2016-0099

  Link       : https://www.exploit-db.com/exploits/39719/

  VulnStatus : Not Vulnerable

  Title      : Windows Kernel-Mode Drivers EoP

  MSBulletin : MS16-034

  CVEID      : 2016-0093/94/95/96

  Link       : https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-034?

  VulnStatus : Not Vulnerable

  Title      : Win32k Elevation of Privilege

  MSBulletin : MS16-135

  CVEID      : 2016-7255

  Link       : https://github.com/FuzzySecurity/PSKernel-Primitives/tree/master/Sample-Exploits/MS16-135

  VulnStatus : Not Vulnerable

  Title      : Nessus Agent 6.6.2 - 6.10.3

  MSBulletin : N/A

  CVEID      : 2017-7199

  Link       : https://aspe1337.blogspot.co.uk/2017/04/writeup-of-cve-2017-7199.html

  VulnStatus : Not Vulnerable'
created_at: '2020-01-24T21:45:44.862325+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Sherlock Import Module and Enumerate Vulnerabilities

```powershell
Find-AllVulns
```

## Expected Output

```
PS C:\> Find-AllVulns

Title      : User Mode to Ring (KiTrap0D)
MSBulletin : MS10-015
CVEID      : 2010-0232
Link       : https://www.exploit-db.com/exploits/11199/
VulnStatus : Not supported on 64-bit systems

Title      : Task Scheduler .XML
MSBulletin : MS10-092
CVEID      : 2010-3338, 2010-3888
Link       : https://www.exploit-db.com/exploits/19930/
VulnStatus : Not Vulnerable

Title      : NTUserMessageCall Win32k Kernel Pool Overflow
MSBulletin : MS13-053
CVEID      : 2013-1300
Link       : https://www.exploit-db.com/exploits/33213/
VulnStatus : Not supported on 64-bit systems

Title      : TrackPopupMenuEx Win32k NULL Page
MSBulletin : MS13-081
CVEID      : 2013-3881
Link       : https://www.exploit-db.com/exploits/31576/
VulnStatus : Not supported on 64-bit systems

Title      : TrackPopupMenu Win32k Null Pointer Dereference
MSBulletin : MS14-058
CVEID      : 2014-4113
Link       : https://www.exploit-db.com/exploits/35101/
VulnStatus : Not Vulnerable

Title      : ClientCopyImage Win32k
MSBulletin : MS15-051
CVEID      : 2015-1701, 2015-2433
Link       : https://www.exploit-db.com/exploits/37367/
VulnStatus : Not Vulnerable

Title      : Font Driver Buffer Overflow
MSBulletin : MS15-078
CVEID      : 2015-2426, 2015-2433
Link       : https://www.exploit-db.com/exploits/38222/
VulnStatus : Not Vulnerable

Title      : 'mrxdav.sys' WebDAV
MSBulletin : MS16-016
CVEID      : 2016-0051
Link       : https://www.exploit-db.com/exploits/40085/
VulnStatus : Not supported on 64-bit systems

Title      : Secondary Logon Handle
MSBulletin : MS16-032
CVEID      : 2016-0099
Link       : https://www.exploit-db.com/exploits/39719/
VulnStatus : Not Vulnerable

Title      : Windows Kernel-Mode Drivers EoP
MSBulletin : MS16-034
CVEID      : 2016-0093/94/95/96
Link       : https://github.com/SecWiki/windows-kernel-exploits/tree/master/MS16-034?
VulnStatus : Not Vulnerable

Title      : Win32k Elevation of Privilege
MSBulletin : MS16-135
CVEID      : 2016-7255
Link       : https://github.com/FuzzySecurity/PSKernel-Primitives/tree/master/Sample-Exploits/MS16-135
VulnStatus : Not Vulnerable

Title      : Nessus Agent 6.6.2 - 6.10.3
MSBulletin : N/A
CVEID      : 2017-7199
Link       : https://aspe1337.blogspot.co.uk/2017/04/writeup-of-cve-2017-7199.html
VulnStatus : Not Vulnerable
```
