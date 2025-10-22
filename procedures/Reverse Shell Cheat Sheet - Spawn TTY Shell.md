---
id: b9e86d7a-02f5-4ed0-86d9-6516f8d6c0f0
name: Reverse Shell Cheat Sheet - Spawn TTY Shell
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:25.008476+00:00'
updated_at: '2023-04-10T20:25:31.223134+00:00'
tactics:
- '[[Lateral Movement|TA0008 - Lateral Movement]]'
techniques:
- '[[Shared Webroot|T1051 - Shared Webroot]]'
tags:
- '[[Reverse Shell Cheat Sheet]]'
- '[[Spawn TTY Shell]]'
commands:
- '[[Create a TCP listener on port 12345]]'
- '[[Installation]]'
- '[[Installing rlwrap]]'
- '[[Pressing CTRL + L]]'
- '[[rlwrap nc]]'
- '[[rlwrap -r -f . nc]]'
---

# Reverse Shell Cheat Sheet - Spawn TTY Shell

## Summary

The Spawn TTY Shell technique allows an attacker to spawn a new TTY shell from within an existing shell session. This can be useful when the current shell does not have the necessary privileges or capabilities. The new TTY shell will inherit the privileges and capabilities of the parent shell, allo

## Description

# Description

The Spawn TTY Shell technique allows an attacker to spawn a new TTY shell from within an existing shell session. This can be useful when the current shell does not have the necessary privileges or capabilities. The new TTY shell will inherit the privileges and capabilities of the parent shell, allowing an attacker to escalate their privileges or perform actions that were not possible in the original shell.

From a technical perspective, this technique works by spawning a new TTY shell using the 'python', 'perl', or 'ruby' interpreter. The interpreter is used to execute a one-liner command that creates a new TTY shell.

The business value of this technique is that it allows an attacker to gain access to sensitive information or systems that were previously unavailable to them.

## Requirements

1. Access to an existing shell session

## Defense

1. Implement strict access controls and permissions to limit the ability of attackers to gain access to shell sessions

1. Monitor for unusual or suspicious activity, such as the spawning of new TTY shells

1. Implement network segmentation and firewalls to limit the ability of attackers to move laterally within a network

## Objectives

1. Spawn a new TTY shell from within an existing shell session

1. Escalate privileges or perform actions that were not possible in the original shell

# Instructions

1. To listen for a shell, use the following command:

rlwrap nc -nlvp <PORT>

**Code**: [[rlwrap]]

> The 'nc' command stands for netcat and is used for creating TCP/UDP connections. The options used here are:

-l: listen mode
-v: verbose mode
-p <PORT>: specify the port to listen on

The 'rlwrap' command is used for line editing and history for any command. It is used here to provide a more user-friendly interface for the netcat command.

**Command** ([[Installing rlwrap]]):

```bash
sudo apt-get install rlwrap
```

2. To use this command, simply press the keys [CTRL] + [L] on your keyboard.

**Code**: [[[CTRL] + [L]]]

> This command is used to clear the terminal screen. It is a useful command when you want to clear the output of previous commands from the terminal and start with a clean slate. By pressing [CTRL] + [L], the terminal screen will be cleared and you will be able to see only the prompt at the top of the screen.

**Command** ([[Pressing CTRL + L]]):

```bash
[CTRL] + [L]
```

3. To establish a remote connection using rlwrap, run the following command:
rlwrap nc [ip_address] [port_number]

To use the current history file as a completion word list, run the following command:
rlwrap -r -f . nc [ip_address] [port_number]

**Code**: [[rlwrap nc 10.0.0.1 4242

rlwrap -r -f . nc 10.0.0.]]

> The 'rlwrap' command is used to provide a readline-style editing of keyboard input for any other command. In this case, it is used to wrap the 'nc' (netcat) command to establish a remote connection. The '-r' option puts all words seen on in- and output on the completion list. The '-f .' option specifies the current history file as a completion word list. The 'nc' command is used to establish a TCP/IP connection to the specified IP address and port number.

**Command** ([[rlwrap nc]]):

```bash
rlwrap nc 10.0.0.1 4242
```

**Command** ([[rlwrap -r -f . nc]]):

```bash
rlwrap -r -f . nc 10.0.0.1 4242
```

4. The `sh` command is used to execute shell scripts. However, it is important to use this command with caution as it can potentially break your system if not used properly. When using this command, make sure you have a clear understanding of what the script does and the potential consequences of running it. Additionally, be aware that OhMyZSH might break this command, so use a simple "," instead.

**Code**: [[sh]]

> The `sh` command takes a shell script as an argument and executes it. It can be used to run various commands and scripts, but it is important to ensure that the script being executed is safe and does not cause any harm to the system. When using this command, it is recommended to use it with caution and only execute scripts from trusted sources. Additionally, it is important to understand the arguments that the script takes and their potential consequences. Overall, the `sh` command can be a powerful tool, but it should be used responsibly and with care.

5. To reset your shell terminal and set environment variables, follow the instructions below:

**Code**: [[ctrl+z
echo $TERM && tput lines && tput cols

# fo]]

> 1. Press 'ctrl+z' to suspend the current process.
2. Type 'echo $TERM && tput lines && tput cols' to display the current terminal type and size.
3. If you are using bash, type 'stty raw -echo' and then 'fg' to put the shell in raw mode and bring it back to the foreground. If you are using zsh, type 'stty raw -echo; fg' instead.
4. Type 'reset' to reset the terminal.
5. Type 'export SHELL=bash' to set the default shell to bash.
6. Type 'export TERM=xterm-256color' to set the terminal type to xterm-256color.
7. Type 'stty rows <num> columns <cols>' to set the number of rows and columns for the terminal.

6. To establish a bidirectional data transfer between two endpoints using Socat, use the following command:

socat <endpoint 1> <endpoint 2>

**Code**: [[socat]]

> The 'socat' command is a versatile networking tool that can establish various types of connections between two endpoints. To transfer data bidirectionally, you can specify two endpoints as arguments. For example, to transfer data between a TCP server running on port 1234 and a UDP client running on port 4321, you can use the following command:

socat TCP4-LISTEN:1234,fork UDP4-SENDTO:127.0.0.1:4321

Here, 'TCP4-LISTEN:1234,fork' instructs Socat to listen for incoming TCP connections on port 1234 and fork a child process for each connection. 'UDP4-SENDTO:127.0.0.1:4321' instructs Socat to send data to the specified UDP endpoint. You can customize the endpoints and their types based on your requirements.

**Command** ([[Installation]]):

```bash
sudo apt-get install socat
```

7. Use this command to forward TCP traffic from a remote server to a local port. The command opens a TCP socket on port 12345 on the local machine and forwards all incoming traffic to the remote server. This can be useful for debugging network issues or for accessing remote services that are not directly accessible from the local machine.

**Code**: [[socat file:`tty`,raw,echo=0 tcp-listen:12345]]

> The command uses the 'socat' utility which is a versatile tool for forwarding data between two endpoints. The 'file:`tty`,raw,echo=0' argument sets up a raw terminal on the local machine that can be used to interact with the remote server. The 'tcp-listen:12345' argument opens a TCP socket on port 12345 on the local machine. Any incoming traffic on this port is forwarded to the remote server. The remote server can be specified as an IP address or a hostname followed by a port number.

**Command** ([[Create a TCP listener on port 12345]]):

```bash
socat file:`tty`,raw,echo=0 tcp-listen:12345
```

8. To spawn a TTY shell from an interpreter, use one of the following commands depending on the interpreter you are using:
- For Python 3: 
  - python3 -c 'import pty; pty.spawn("/bin/sh")'
  - python3 -c "__import__('pty').spawn('/bin/bash')"
  - python3 -c "__import__('subprocess').call(['/bin/bash'])"
- For Perl: 
  - perl -e 'exec "/bin/sh";'
  - perl: exec "/bin/sh";
  - perl -e 'print `/bin/bash`'
- For Ruby: 
  - ruby: exec "/bin/sh"
- For Lua: 
  - lua: os.execute('/bin/sh')

**Code**: [[/bin/sh -i
python3 -c 'import pty; pty.spawn("/bin]]

> This command allows the user to spawn a TTY shell from an interpreter. This can be useful in situations where a normal shell is not available or when trying to escalate privileges. The command works by executing a command that spawns a new shell with TTY support.

## MITRE ATT&CK Mapping

### Tactics

- [[Lateral Movement|TA0008 - Lateral Movement]]

### Techniques

- [[Shared Webroot|T1051 - Shared Webroot]]

## Commands Used

- [[Create a TCP listener on port 12345]]
- [[Installation]]
- [[Installing rlwrap]]
- [[Pressing CTRL + L]]
- [[rlwrap nc]]
- [[rlwrap -r -f . nc]]

## Tags

- [[Reverse Shell Cheat Sheet]]
- [[Spawn TTY Shell]]
