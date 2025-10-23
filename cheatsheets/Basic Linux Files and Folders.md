---
id: 5e16f192-1bf6-4c0e-b279-a0e0ab39e281
name: Basic Linux Files and Folders
type: cheatsheet
verified: true
created_at: '2020-03-10T01:23:34.540544+00:00'
updated_at: '2023-05-30T20:07:49.231257+00:00'
---

# Basic Linux Files and Folders

**Status**: ✓ Verified

# Description

A simple high-level view of files and folders found on popular Linux distributions, and why they matter to red teams. 



## Root Filesystem

- **/**bin - essential commands **for** all users (cp, mv, ls, ...)

- /boot - boot loaders that prepare and run the OS

- /dev - device files such hard drives (**in** VMs, generally labeled sda, sdb,...) and pseudo devices **(**null, urandom, tcp, etc**)**

- **/**etc - system and application configuration files. May include passwords and other sensitive information

- **/**home - user directories, may contain sensitive information

- **/**lib - libraries **for** binaries stored **in** **/**bin and **/**sbin

- **/**media - **mount** point **for** removable media (DVD, CD-ROm, etc)

- /mnt - temporary mount point for file systems

- /opt - optional software packages are often installed to /opt

- /proc - virtual file system containing system and process information. Useful for enumeration with minimal tools

- /root - generally only readable by the root user

- /run - contains run-time data which describes the system's running state (daemons, logged **in** users, etc)

- **/**sbin - system binaries **for** all users (fsck, ifconfig, getcap)

- /srv - site-specific directory for server data such as FTP, alternate web data folder, etc

- /sys - virtual file system which covers devices, drivers, kernel modules, etc. Similar to /proc but organized

- /usr - non-essential programs and user binaries, documentation and libraries

- /var - files that continually change. Eg logs (/var/log), temp files (/var/mail/, web apps (/var/www)

More details: [https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf](https://refspecs.linuxfoundation.org/FHS_3.0/fhs-3.0.pdf)



## Important Files and Folders

- **/**home - enumerate files and folders **for** sensitive information

- /dev  - see system devices and interact with them if possible

- /etc  - enumerate all configuration files found, especially those for services currently running

- /etc/passwd - lists all users configured to sign into the local system

- /etc/shadow - similar to passwd but contains user password hashes. *Should* only be accessible by root

- /etc/group - lists all groups

- /etc/apache2/ - contains web server configuration files

- /etc/httpd/ - contains web server configuration files

- /etc/nginx - contains web server configuration files

- /etc/sudoers - configures sudo permissions

- /etc/hosts - handles static assignments between IP addresses and hostnames

- /etc/resolv.conf - handles DNS server settings. Can be manually edited but does not necessarily persist after reboot

- /opt - programs installed without package managers are often placed here

- /usr/bin - enumerate for vulnerable applications

- /usr/local/bin - enumerate for vulnerable applications

- /var/backups - contains backups of /etc/passwd and /etc/shadow files

- /var/www/ - generally contains web server data

- /var/spool or /var/mail - contains mail data including unread messages




