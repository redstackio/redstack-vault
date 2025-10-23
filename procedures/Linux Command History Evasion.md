---
id: a7e8187c-4d55-4a13-a753-f099bdd50ac2
name: Linux Command History Evasion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.677770+00:00'
updated_at: '2023-04-10T20:34:12.027865+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Indicator Removal on Host|T1070 - Indicator Removal on Host]]'
sub_techniques:
- '[[Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]]'
- '[[File Deletion|T1070.004 - File Deletion]]'
tags:
- '[[Command History]]'
- '[[Linux - Evasion]]'
commands:
- '[[Clear history]]'
- '[[Delete history entry]]'
- '[[Disable Bash history]]'
- '[[Ignore duplicate and specific commands in history]]'
- '[[Ignore specific commands from being saved in history]]'
- '[[my-sneaky-command]]'
- '[[Remove a command from the list]]'
- '[[Remove most recently logged command]]'
- '[[Set HISTSIZE]]'
- '[[View Bash History]]'
- '[[View History File Location]]'
- '[[Viewing Command History]]'
---

# Linux Command History Evasion

## Summary

Linux Command History Evasion is a set of techniques used to prevent or hide the command history of a Linux system. This can be used by attackers to evade detection by security tools that rely on command history to identify malicious activity. By removing or hiding command history, attackers can pr

## Description

# Description

Linux Command History Evasion is a set of techniques used to prevent or hide the command history of a Linux system. This can be used by attackers to evade detection by security tools that rely on command history to identify malicious activity. By removing or hiding command history, attackers can prevent investigators from tracing their actions and identifying the tools and techniques they used.

From a technical perspective, this involves manipulating the shell's command history file or configuration to prevent the logging of commands. This can be done using a variety of techniques, such as disabling logging, clearing the command history, or excluding specific commands from being logged. These techniques can be used individually or in combination to achieve the desired level of evasion.

The business value of Linux Command History Evasion is that it allows attackers to operate undetected on a compromised system, potentially stealing sensitive data or using the system for further attacks.

 

## Requirements

1. Access to a Linux system with shell access

1. Knowledge of Linux shell commands and configuration

1. Privileged access to manipulate system settings (in some cases)

 

## Defense

1. Monitor command history for suspicious activity

1. Implement logging and auditing of command history

1. Restrict access to sensitive systems and data

 

## Objectives

1. Prevent detection by security tools that rely on command history

1. Hide the attacker's actions from investigators

1. Maintain access to a compromised system

 

# Instructions

1. To view the command history, simply type `history` in the shell and press enter.

 



**Code**: [[history]]



> The `history` command will display a list of the most recent commands executed in the shell. Each command is preceded by a number, which can be used to recall that command using the `!` operator. For example, to execute the 3rd command in the history, you can type `!3` and press enter. You can also use the `history` command with optional arguments to customize the output, such as showing a specific number of commands or filtering by a specific string.



**Command** ([[Viewing Command History]]):

```bash
history
```



2. To view the location of the history file, use the following command: echo $HISTFILE

 



**Code**: [[$HISTFILE]]



> This will display the location of the history file which stores a list of previously executed commands in the terminal. The history file can be manually inspected by navigating to the directory where it is located and opening it with a text editor.



**Command** ([[View History File Location]]):

```bash
$HISTFILE
```



3. history | less

 



**Code**: [[~/.bash_history]]



> This command will display the entire bash history in the terminal. The output can be scrolled using the arrow keys. Press 'q' to exit the viewer.



**Command** ([[View Bash History]]):

```bash
~/.bash_history
```



4. To disable Bash history logging, use the following commands:

 



**Code**: [[# Prevent writing to the history file at all
unset]]



> The `unset HISTFILE` command prevents Bash from writing to the history file, while the `export HISTSIZE=0` command prevents this session's command history from being saved in memory. Together, these commands effectively disable Bash history logging.



**Command** ([[Disable Bash history]]):

```bash
unset HISTFILE
export HISTSIZE=0
```



5. The HISTIGNORE command is used to ignore specific commands from being added to the history list. This command takes a pattern as an argument and any command that matches that pattern will not be added to the history list.

 



**Code**: [[HISTIGNORE]]



> The argument for the HISTIGNORE command is a pattern that can be used to match against commands entered in the terminal. The pattern can be a regular expression or a simple string. For example, if you want to ignore any command that starts with 'ls', you can use the pattern 'ls*'. This will ignore commands like 'ls', 'ls -l', 'ls -a', etc. You can also use multiple patterns by separating them with a colon. For example, 'ls*:cd*' will ignore any command that starts with 'ls' or 'cd'.



**Command** ([[Ignore duplicate and specific commands in history]]):

```bash
export HISTIGNORE="&:ls:ll:cd:exit"

```



6. To exclude HISTFILE from command history, add the following line to your .bashrc file:

HISTIGNORE=$HISTIGNORE:HISTFILE

This will prevent any commands entered that include HISTFILE from being saved in the command history.

 



**Code**: [[HISTFILE]]



> The HISTFILE variable in Bash stores the path to the file where the command history is saved. By default, all commands entered in the terminal are saved to this file. However, there may be certain commands that you do not want saved in the history, such as those that contain sensitive information. By adding HISTFILE to the HISTIGNORE variable, any commands entered that include HISTFILE will be excluded from the command history.

7. export HISTSIZE=<value>

 



**Code**: [[HISTSIZE]]



> This command is used to set the size of the command history. The <value> argument specifies the number of commands that can be stored in the history. Once the history reaches the specified size, the oldest commands will be removed from the history.



**Command** ([[Set HISTSIZE]]):

```bash
HISTSIZE=1000
```



8. The HISTIGNORE command is used to prevent certain commands from being saved to the history list.

 



**Code**: [[HISTIGNORE]]



> This command takes a list of patterns as arguments. Any command matching one of the patterns will not be saved to the history list. This is useful for ignoring repetitive or sensitive commands, such as those that involve passwords or other sensitive information.



**Command** ([[Ignore specific commands from being saved in history]]):

```bash
HISTIGNORE=$HISTIGNORE:"ls -l"
```





**Command** ([[Remove a command from the list]]):

```bash
HISTIGNORE=${HISTIGNORE%%:"ls -l"*}
```



9. To execute this command, type 'my-sneaky-command' in the terminal.

 



**Code**: [[# Note the leading space character:
 my-sneaky-com]]



> This command is used to perform a sneaky action, possibly without being detected. It is recommended to use this command with caution and only for ethical purposes. The leading space character is added to prevent the command from being stored in the command history.



**Command** ([[my-sneaky-command]]):

```bash
# Note the leading space character:
 my-sneaky-command
```



10. To remove a specific command from the history, use the following syntax: history -d [index], where [index] is the index number of the command in the history list.

 



**Code**: [[history -d]]



> This command is useful when you accidentally enter a sensitive command in the terminal and you don't want it to show up in the history. By using this command, you can delete specific commands from the history list, preventing them from being accidentally executed in the future.



**Command** ([[Delete history entry]]):

```bash
history -d
```



11. Use this command to remove the most recent command from your bash history. This can be useful if you accidentally typed a sensitive command or if you want to keep your history clean.

 



**Code**: [[# Removes the most recently logged command.
# Note]]



> The `history -d` command is used to delete a specific entry from your bash history. In this case, we are deleting two entries at once: the most recent command and the command that was used to delete it (`history -d -1`). This is necessary because if we only delete the most recent command, the `history -d` command itself will be logged as the most recent command. The `&&` operator is used to execute the two `history -d` commands in sequence.



**Command** ([[Remove most recently logged command]]):

```bash
history -d -2 && history -d -1
```



12. To clear the command history, use the following command:

 



**Code**: [[# Clears the in-memory history and writes the empt]]



> The 'history -c' command clears the in-memory history of commands executed in the current session, while the 'history -w' command writes the empty history to disk. This will effectively erase all previous commands executed in the current session and prevent them from being viewed using the 'history' command. This command can be useful for maintaining privacy or security by preventing others from viewing your command history.



**Command** ([[Clear history]]):

```bash
history -c && history -w
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Indicator Removal on Host|T1070 - Indicator Removal on Host]]

### Sub-Techniques

- [[Clear Windows Event Logs|T1070.001 - Clear Windows Event Logs]]
- [[File Deletion|T1070.004 - File Deletion]]

## Commands Used

- [[Clear history]]
- [[Delete history entry]]
- [[Disable Bash history]]
- [[Ignore duplicate and specific commands in history]]
- [[Ignore specific commands from being saved in history]]
- [[my-sneaky-command]]
- [[Remove a command from the list]]
- [[Remove most recently logged command]]
- [[Set HISTSIZE]]
- [[View Bash History]]
- [[View History File Location]]
- [[Viewing Command History]]

## Tags

- [[Command History]]
- [[Linux - Evasion]]


