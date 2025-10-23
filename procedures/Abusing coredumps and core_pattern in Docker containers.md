---
id: d3972e53-1595-4a1d-82e4-aab73d844200
name: Abusing coredumps and core_pattern in Docker containers
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.162938+00:00'
updated_at: '2023-04-10T20:33:47.309840+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Impact|TA0040 - Impact]]'
techniques:
- '[[Inhibit System Recovery|T1490 - Inhibit System Recovery]]'
- '[[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]'
sub_techniques:
- '[[Create Cloud Instance|T1578.002 - Create Cloud Instance]]'
tags:
- '[[Abusing coredumps and core_pattern]]'
- '[[Container - Docker Pentest]]'
- '[[Exploit privileged container abusing the Linux cgroup v1]]'
commands:
- '[[Check Mount Point]]'
- '[[Update Core Dump Location]]'
---

# Abusing coredumps and core_pattern in Docker containers

## Summary

Abusing coredumps and core_pattern is a technique that can be used to escalate privileges in Docker containers. By setting the core_pattern to a writable file in a privileged container, an attacker can generate a coredump of a faulty program that will be written to the specified file. This can be u

## Description

# Description

Abusing coredumps and core_pattern is a technique that can be used to escalate privileges in Docker containers. By setting the core_pattern to a writable file in a privileged container, an attacker can generate a coredump of a faulty program that will be written to the specified file. This can be used to write arbitrary data to a file with elevated permissions, allowing for further exploitation of the system. From a technical perspective, this attack relies on the fact that the core_pattern file is writable by the container user, which is often the case in privileged containers. From a business standpoint, this attack can lead to a complete compromise of the system, resulting in data theft or loss, as well as financial damages and reputational harm.

 

## Requirements

1. Access to a privileged Docker container

1. Ability to modify the core_pattern file

 

## Defense

1. Ensure that the core_pattern file is not writable by the container user

1. Limit the use of privileged containers to only necessary cases

1. Monitor for any changes to the core_pattern file

 

## Objectives

1. Escalate privileges in a Docker container

1. Write arbitrary data to a file with elevated permissions

 

# Instructions

1. To identify the mounting point of a file system, use the `mount` command followed by `head -n 1` to display the first line of the output. The output will include the type of file system and the location where it is mounted.

 



**Code**: [[$ mount | head -n 1
overlay on / type overlay (rw,]]



> The `mount` command is used to mount file systems and display information about mounted file systems. The `head` command is used to display the first line of the output. In this case, we are looking for the first line of the output to identify the type of file system and the location where it is mounted.



**Command** ([[Check Mount Point]]):

```bash
$ mount | head -n 1
overlay on / type overlay (rw,relatime,lowerdir=/var/lib/docker/overlay2/l/YLH6C6EQMMG7DA2AL5DUANDHYJ:/var/lib/docker/overlay2/l/HP7XLDFT4ERSCYVHJ2WMZBG2YT,upperdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff,workdir=/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/work)
```



2. This command sets the core pattern for Docker. The core pattern specifies the program to be executed when a coredump occurs. In this case, the program is set to /var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff/poc.

 



**Code**: [[echo "|/var/lib/docker/overlay2/c51a87501842b28701]]



> The '> /proc/sys/kernel/core_pattern' part of the command redirects the output of the echo command to the /proc/sys/kernel/core_pattern file, which sets the core pattern for the system.



**Command** ([[Update Core Dump Location]]):

```bash
echo "|/var/lib/docker/overlay2/c51a87501842b287018d22e9d09d7d8dc4ede83a867f36ca199434d5ea5ac8f5/diff/poc" > /proc/sys/kernel/core_pattern
```



3. To generate a coredump with a faulty program, you can use the following command:
`gcc -o crash crash.c && ./crash`
This command compiles the `crash.c` file and executes the resulting `crash` binary. The program is designed to write to a buffer beyond its allocated size, causing a segmentation fault and generating a coredump.

 



**Code**: [[int main(void) {
    char buf[1];
    for (int i =]]



> The `gcc` command is used to compile the `crash.c` file and generate an executable binary named `crash`. The `&&` operator is used to chain the two commands together, so that the `crash` binary is executed immediately after it is compiled. The program itself is designed to write to a buffer beyond its allocated size, causing a segmentation fault and generating a coredump. This can be useful for debugging purposes, as it allows you to inspect the state of the program at the time of the crash.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Impact|TA0040 - Impact]]

### Techniques

- [[Inhibit System Recovery|T1490 - Inhibit System Recovery]]
- [[Modify Cloud Compute Infrastructure|T1578 - Modify Cloud Compute Infrastructure]]

### Sub-Techniques

- [[Create Cloud Instance|T1578.002 - Create Cloud Instance]]

## Commands Used

- [[Check Mount Point]]
- [[Update Core Dump Location]]

## Tags

- [[Abusing coredumps and core_pattern]]
- [[Container - Docker Pentest]]
- [[Exploit privileged container abusing the Linux cgroup v1]]


