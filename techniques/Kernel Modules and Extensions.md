---
id: 0bb27865-31a7-46a4-9578-0a02c1a3e4ea
name: Kernel Modules and Extensions
type: technique
mitre_id: T1215
mitre_url: null
created_at: '2019-08-28T21:17:35.984383+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Gopher SMTP Back Connect SSRF]]'
- '[[Kernel Exploitation - Useradd.exe Compilation]]'
- '[[Linux - Backdooring a VirtualBox Driver]]'
---

# Kernel Modules and Extensions

**MITRE ID**: T1215

## Description

Loadable Kernel Modules (or LKMs) are pieces of code that can be loaded and unloaded into the kernel upon demand. They extend the functionality of the kernel without the need to reboot the system. For example, one type of module is the device driver, which allows the kernel to access hardware connected to the system. [1] When used maliciously, Loadable Kernel Modules (LKMs) can be a type of kernel-mode Rootkit that run with the highest operating system privilege (Ring 0). [2] Adversaries can use loadable kernel modules to covertly persist on a system and evade defenses. Examples have been found in the wild and there are some open source projects. [3] [4] [5] [6]Common features of LKM based rootkits include: hiding itself, selective hiding of files, processes and network activity, as well as log tampering, providing authenticated backdoors and enabling root access to non-privileged users. [7]Kernel extensions, also called kext, are used for macOS to load functionality onto a system similar to LKMs for Linux. They are loaded and unloaded through kextload and kextunload commands. Several examples have been found where this can be used. [8] [9] Examples have been found in the wild. [10]

# Detection

LKMs are typically loaded into /lib/modules and have had the extension .ko ("kernel object") since version 2.6 of the Linux kernel. [14]

Many LKMs require Linux headers (specific to the target kernel) in order to compile properly. These are typically obtained through the operating systems package manager and installed like a normal package.

Adversaries will likely run these commands on the target system before loading a malicious module in order to ensure that it is properly compiled. [7]

On Ubuntu and Debian based systems this can be accomplished by running: apt-get install linux-headers-$(uname -r)

On RHEL and CentOS based systems this can be accomplished by running: yum install kernel-devel-$(uname -r)

Loading, unloading, and manipulating modules on Linux systems can be detected by monitoring for the following commands:modprobe insmod lsmod rmmod modinfo [15]

For macOS, monitor for execution of kextload commands and correlate with other unknown or suspicious activity.

# Mitigation

Common tools for detecting Linux rootkits include: rkhunter [11], chrootkit [12], although rootkits may be designed to evade certain detection tools.

LKMs and Kernel extensions require root level permissions to be installed. Limit access to the root account and prevent users from loading kernel modules and extensions through proper privilege separation and limiting Privilege Escalation opportunities.

Application whitelisting and software restriction tools, such as SELinux, can also aide in restricting kernel module loading. [13]

# Footnotes

[1] Pomerantz, O., Salzman, P. (2003, April 4). The  (Citation: Linux Kernel Module Programming Guide). Retrieved April 6, 2018.

[2] Pomerantz, O., Salzman, P. (2003, April 4). Modules vs Programs. Retrieved April 6, 2018.

[3] Case, A. (2012, October 10). Phalanx 2 Revealed: Using Volatility to Analyze an Advanced Linux Rootkit. Retrieved April 9, 2018.

[4] Kurtz, G. (2012, November 19). HTTP iframe Injecting Linux Rootkit. Retrieved December 21, 2017.

[5] Augusto, I. (2018, March 8). Reptile - LMK Linux rootkit. Retrieved April 9, 2018.

[6] Mello, V. (2018, March 8). Diamorphine - LMK rootkit for Linux Kernels 2.6.x/3.x/4.x (x86 and x86_64). Retrieved April 9, 2018.

[7] Chuvakin, A. (2003, February). An Overview of Rootkits. Retrieved April 6, 2018.

[8] Wardle, P. (2015, April). Malware Persistence on OS X Yosemite. Retrieved April 6, 2018.

[9] Wardle, P. (2017, September 8). High Sierra’s ‘Secure Kernel Extension Loading’ is Broken. Retrieved April 6, 2018.

[10] Mikhail, K. (2014, October 16). The Ventir Trojan: assemble your MacOS spy. Retrieved April 6, 2018.

[11] Rootkit Hunter Project. (2018, February 20). The Rootkit Hunter project. Retrieved April 9, 2018.

[12] Murilo, N., Steding-Jessen, K. (2017, August 23). Chkrootkit. Retrieved April 9, 2018.

[13] Vander Stoep, J. (2016, April 5). [v3] selinux: restrict kernel module loadinglogin  register. Retrieved April 9, 2018.

[14] Wikipedia. (2018, March 17). Loadable kernel module. Retrieved April 9, 2018.

[15] Henderson, B. (2006, September 24). How To Insert And Remove LKMs. Retrieved April 9, 2018.

## Defense

Common tools for detecting Linux rootkits include: rkhunter (Citation: SourceForge rkhunter), chrootkit (Citation: Chkrootkit Main), although rootkits may be designed to evade certain detection tools.

LKMs and Kernel extensions require root level permiss

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (3)

- [[Gopher SMTP Back Connect SSRF]]
- [[Kernel Exploitation - Useradd.exe Compilation]]
- [[Linux - Backdooring a VirtualBox Driver]]
