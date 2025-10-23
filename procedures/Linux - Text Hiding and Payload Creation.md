---
id: 13f59ced-51e6-4054-8f70-7a6a0e3ada17
name: Linux - Text Hiding and Payload Creation
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.756151+00:00'
updated_at: '2023-04-10T20:34:10.808024+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
- '[[Execution|TA0002 - Execution]]'
techniques:
- '[[Hide Artifacts|T1564 - Hide Artifacts]]'
- '[[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]'
- '[[Scripting|T1064 - Scripting]]'
sub_techniques:
- '[[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]'
tags:
- '[[Hiding Text]]'
- '[[Linux - Evasion]]'
commands:
- '[[Create a new file]]'
- '[[Display File Contents]]'
- '[[Exit nano]]'
- '[[Open a file in Vim]]'
- '[[Open an existing file]]'
- '[[Preview first lines of data]]'
- '[[Save changes to file]]'
- '[[View last lines of a file]]'
---

# Linux - Text Hiding and Payload Creation

## Summary

The Linux operating system offers a variety of commands and editors that can be used to hide text and create payloads to evade detection. This technique can be used by attackers to hide malicious code, configuration files, or other sensitive information. By using tools like Vim, Nano, or Emacs, att

## Description

# Description

The Linux operating system offers a variety of commands and editors that can be used to hide text and create payloads to evade detection. This technique can be used by attackers to hide malicious code, configuration files, or other sensitive information. By using tools like Vim, Nano, or Emacs, attackers can create hidden files and directories that can be used to store payloads or other sensitive information. Additionally, by using Bash scripts with sneaky payload commands, attackers can obfuscate their malicious activities and evade detection by security tools.

From a technical standpoint, hiding text and creating payloads involves using various Linux commands and editors to create and manipulate files. These files can be hidden by adding a dot (.) at the beginning of the file name, which makes them invisible to normal directory listings. Additionally, Bash scripts can be used to run commands in a way that makes them difficult to detect by security tools.

From a business perspective, this technique can be used by attackers to evade detection and maintain persistence on a compromised system. By hiding their activities and payloads, attackers can continue to operate undetected and steal sensitive information or disrupt business operations.

 

## Requirements

1. Access to a Linux operating system

1. Knowledge of Linux commands and editors

1. Ability to create and run Bash scripts

 

## Defense

1. Implement strict file permissions and access controls to prevent unauthorized access to sensitive files and directories

1. Regularly monitor system logs and file integrity to detect any suspicious activity or changes

1. Use security tools that are capable of detecting obfuscated files and suspicious command-line activity

 

## Objectives

1. Hide sensitive information and payloads on a compromised system

1. Evade detection by security tools

1. Maintain persistence on a compromised system

 

# Instructions

1. cat [file]

 



**Code**: [[cat]]



> The 'cat' command is used to concatenate and display the contents of one or more files to the terminal. The 'file' argument specifies the path to the file whose contents will be printed. Multiple files can be specified and they will be printed in the order they are listed. If no file is specified, 'cat' will read from standard input (stdin) until it reaches the end of the input (EOF) signal (Ctrl-D).



**Command** ([[Display File Contents]]):

```bash
file.txt
```



2. head [OPTION]... [FILE]...

 



**Code**: [[head]]



> Print the first 10 lines of each FILE to standard output. With more than one FILE, precede each with a header giving the file name. Possible options:
-n, --lines=[-]K: print the first K lines instead of the first 10; with the leading '-', print all but the last K lines of each file. 
-c, --bytes=[-]K: print the first K bytes instead of the first 10 lines; with the leading '-', print all but the last K bytes of each file. 
-q, --quiet, --silent: never print headers giving file names. 
-v, --verbose: always print headers giving file names. 
-z, --zero-terminated: line delimiter is NUL, not newline.



**Command** ([[Preview first lines of data]]):

```bash
head data
```



3. The tail command displays the last part of a file. By default, it displays the last 10 lines of a file.

 



**Code**: [[tail]]



> The tail command can be used to display the last n lines of a file by specifying the number of lines using the -n option. For example, 'tail -n 20 filename' will display the last 20 lines of the file. The tail command can also be used to continuously display new lines added to a file using the -f option. For example, 'tail -f filename' will display the last 10 lines of the file and continue to display any new lines added to the file in real-time.



**Command** ([[View last lines of a file]]):

```bash
tail data.txt
```



4. To edit a file with Vim, run the following command:

 



**Code**: [[vim]]



> The 'vim' command is used to open the Vim text editor. Once inside Vim, you can edit the file by typing in text, using various commands, and saving changes. If the file does not exist, Vim will create a new file with the given name. If the file already exists, Vim will open it for editing. To save changes and exit Vim, type ':wq' and press enter. To exit Vim without saving changes, type ':q!' and press enter.



**Command** ([[Open a file in Vim]]):

```bash
vim filename.txt
```



5. Nano is a text editor for Unix-like computing systems or operating environments using a command line interface.

 



**Code**: [[nano]]



> The nano command is used to create, edit and save text files. It provides a user-friendly interface with easy-to-use shortcuts for editing text. The command takes the name of the file to be edited as an argument. Once the file is open, you can use the keyboard to make changes to the text. Some of the most commonly used shortcuts include Ctrl + O to save the file, Ctrl + X to exit nano, and Ctrl + W to search for a specific word or phrase within the text. Nano is a lightweight and easy-to-use text editor that is ideal for simple text editing tasks.



**Command** ([[Create a new file]]):

```bash
nano newfile.txt
```





**Command** ([[Open an existing file]]):

```bash
nano existingfile.txt
```





**Command** ([[Save changes to file]]):

```bash
Press Ctrl+O
```





**Command** ([[Exit nano]]):

```bash
Press Ctrl+X
```



6. Here are some useful Emacs commands:

 



**Code**: [[emacs]]



> 1. C-x C-f: Open a file
2. C-x C-s: Save the current buffer
3. C-x C-c: Quit Emacs
4. C-g: Cancel the current command
5. C-x 1: Delete all other windows
6. C-x 2: Split the window horizontally
7. C-x 3: Split the window vertically
8. C-x o: Move to the other window
9. C-x b: Switch to a different buffer
10. C-x k: Kill the current buffer

7. To create a Bash script with a sneaky payload command, run the following commands:

 



**Code**: [[echo "sneaky-payload-command" > script.sh
echo "# ]]



> This command will create a Bash script named 'script.sh' and add a 'sneaky-payload-command' to it. The script will also clear the terminal and add a comment to indicate that it was generated from '/etc/issue.conf' by 'configure'. When the script is printed, only the last line will be visible.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]
- [[Execution|TA0002 - Execution]]

### Techniques

- [[Hide Artifacts|T1564 - Hide Artifacts]]
- [[Obfuscated Files or Information|T1027 - Obfuscated Files or Information]]
- [[Scripting|T1064 - Scripting]]

### Sub-Techniques

- [[Hidden Files and Directories|T1564.001 - Hidden Files and Directories]]

## Commands Used

- [[Create a new file]]
- [[Display File Contents]]
- [[Exit nano]]
- [[Open a file in Vim]]
- [[Open an existing file]]
- [[Preview first lines of data]]
- [[Save changes to file]]
- [[View last lines of a file]]

## Tags

- [[Hiding Text]]
- [[Linux - Evasion]]


