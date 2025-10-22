---
id: 0284a483-4291-4684-b53d-8f8bff005dc6
name: Systemd Service
type: technique
mitre_id: T1501
mitre_url: null
created_at: '2019-08-28T21:17:45.331357+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Persistence|TA0003 - Persistence]]'
procedures:
- '[[Create a Systemd Service]]'
---

# Systemd Service

**MITRE ID**: T1501

## Description

Systemd services can be used to establish persistence on a Linux system. The systemd service manager is commonly used for managing background daemon processes (also known as services) and other system resources.[1][2] Systemd is the default initialization (init) system on many Linux distributions starting with Debian 8, Ubuntu 15.04, CentOS 7, RHEL 7, Fedora 15, and replaces legacy init systems including SysVinit and Upstart while remaining backwards compatible with the aforementioned init systems.Systemd utilizes configuration files known as service units to control how services boot and under what conditions. By default, these unit files are stored in the /etc/systemd/system and /usr/lib/systemd/system directories and have the file extension .service. Each service unit file may contain numerous directives that can execute system commands. ExecStart, ExecStartPre, and ExecStartPost directives cover execution of commands when a services is started manually by 'systemctl' or on system start if the service is set to automatically start. ExecReload directive covers when a service restarts. ExecStop and ExecStopPost directives cover when a service is stopped or manually by 'systemctl'.Adversaries have used systemd functionality to establish persistent access to victim systems by creating and/or modifying service unit files that cause systemd to execute malicious commands at recurring intervals, such as at system boot.[3][4][5][6]While adversaries typically require root privileges to create/modify service unit files in the /etc/systemd/system and /usr/lib/systemd/system directories, low privilege users can create/modify service unit files in directories such as ~/.config/systemd/user/ to achieve user-level persistence.[7]

# Detection

Systemd service unit files may be detected by auditing file creation and modification events within the /etc/systemd/system, /usr/lib/systemd/system/, and /home//.config/systemd/user/ directories, as well as associated symbolic links. Suspicious processes or scripts spawned in this manner will have a parent process of ‘systemd’, a parent process ID of 1, and will usually execute as the ‘root’ user.

Suspicious systemd services can also be identified by comparing results against a trusted system baseline. Malicious systemd services may be detected by using the systemctl utility to examine system wide services: systemctl list-units -–type=service –all. Analyze the contents of .service files present on the file system and ensure that they refer to legitimate, expected executables.

Auditing the execution and command-line arguments of the 'systemctl' utility, as well related utilities such as /usr/sbin/service may reveal malicious systemd service execution.

# Mitigation

The creation and modification of systemd service unit files is generally reserved for administrators such as the Linux root user and other users with superuser privileges. Limit user access to system utilities such as systemctl to only users who have a legitimate need. Restrict read/write access to systemd unit files to only select privileged users who have a legitimate need to manage system services. Additionally, the installation of software commonly adds and changes systemd service unit files. Restrict software installation to trusted repositories only and be cautious of orphaned software packages. Utilize malicious code protection and application whitelisting to mitigate the ability of malware to create or modify systemd services. 

# Footnotes

[1] Linux man-pages. (2014, January). systemd(1) - Linux manual page. Retrieved April 23, 2019.

[2] Freedesktop.org. (2018, September 29). systemd System and Service Manager. Retrieved April 23, 2019.

[3] Anomali Labs. (2019, March 15). Rocke Evolves Its Arsenal With a New Malware Family Written in Golang. Retrieved April 24, 2019.

[4] Catalin Cimpanu. (2018, July 10). ~x file downloaded in public Arch package compromise. Retrieved April 23, 2019.

[5] Catalin Cimpanu. (2018, July 10). Malware Found in Arch Linux AUR Package Repository. Retrieved April 23, 2019.

[6] Eli Schwartz. (2018, June 8). acroread package compromised. Retrieved April 23, 2019.

[7] Rapid7. (2016, June 22). Service Persistence. Retrieved April 23, 2019.

[8] Nicolas Verdier. (n.d.). Retrieved January 29, 2018.

## Defense

The creation and modification of systemd service unit files is generally reserved for administrators such as the Linux root user and other users with superuser privileges. Limit user access to system utilities such as systemctl to only users who have a le

## Tactics

- [[Persistence|TA0003 - Persistence]]

## Related Procedures (1)

- [[Create a Systemd Service]]
