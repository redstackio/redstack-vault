---
id: 5ece34e3-610e-4fbb-9cde-5f783e1863ee
name: Linux Timestomping Evasion
type: procedure
verified: false
submitted: false
created_at: '2023-04-06T03:56:17.824412+00:00'
updated_at: '2023-04-10T20:34:10.419755+00:00'
tactics:
- '[[Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
- '[[Timestomp|T1099 - Timestomp]]'
tags:
- '[[Linux - Evasion]]'
- '[[Timestomping]]'
commands:
- '[[Change access and modification times using YYYYMMDDhhmm format]]'
- '[[Change time using Unix epoch timestamp]]'
- '[[Copy timestamp from one file to another]]'
- '[[Create empty file]]'
- '[[Create file.txt using touch command]]'
- '[[Get the file''s modification timestamp, modify the file, then restore the timestamp]]'
- '[[Set system time to 2022-10-31 23:59:59]]'
---

# Linux Timestomping Evasion

## Summary

The Linux Timestomping Evasion procedure involves manipulating the timestamps of files on a Linux system to evade detection by security tools. This technique is commonly used by attackers to hide their tracks and make it difficult for defenders to determine when a file was created or modified. Time

## Description

# Description

The Linux Timestomping Evasion procedure involves manipulating the timestamps of files on a Linux system to evade detection by security tools. This technique is commonly used by attackers to hide their tracks and make it difficult for defenders to determine when a file was created or modified. Timestomping involves changing the timestamps of a file to an earlier or later date than the actual date of creation or modification. This can be done using various tools and techniques, including the 'touch' command or manually modifying the timestamp values in the file system. By using this technique, an attacker can avoid detection by security tools that rely on timestamps to identify suspicious activity.

From a technical perspective, timestomping involves modifying the 'atime', 'mtime', and 'ctime' values of a file. These values represent the access time, modification time, and change time of a file, respectively. By modifying these values, an attacker can make it appear as though a file was created or modified at a different time than it actually was.

The business value of this procedure is that it allows attackers to remain undetected and continue their operations without being detected. This can result in the theft of sensitive data, the compromise of systems, and the disruption of business operations.

 

## Requirements

1. Access to a Linux system

1. Permission to modify file timestamps

1. Knowledge of timestomping techniques

 

## Defense

1. Implement file integrity monitoring to detect changes to file timestamps

1. Use security tools that can detect timestomping activity

1. Limit user privileges to prevent unauthorized access and modification of files

 

## Objectives

1. Evade detection by security tools

1. Hide tracks and make it difficult for defenders to determine when a file was created or modified

1. Avoid detection and continue operations

 

# Instructions

1. touch [file_name]

 



**Code**: [[touch]]



> The touch command is used to create a new file. When executed, it creates a file with the name specified in the command. If the file already exists, it updates the timestamp of the file. The [file_name] argument is the name of the file that you want to create or update. If the file name contains spaces, you must enclose it in quotes.



**Command** ([[Create empty file]]):

```bash
touch file.txt
```



2. Use the touch command to modify the access and modification times of a file. There are several ways to do this, including specifying the time using YYYYMMDDhhmm format, Unix epoch timestamp, or copying the timestamp from another file. Additionally, you can use the stat command to get the modification timestamp of a file, modify the file, and then restore the original timestamp using touch.

 



**Code**: [[# Changes the access (-a) and modification (-m) ti]]



> The touch command is used to modify the access and modification times of a file. The -a option changes the access time, and the -m option changes the modification time. You can specify the time using the -t option followed by the YYYYMMDDhhmm format or the -d option followed by a Unix epoch timestamp. The -r option can be used to copy the timestamp from another file.

In the example provided, the touch command is used to modify the timestamps of the file "example". The first command changes the timestamps to October 31, 2022 at 11:59 PM. The second command changes the timestamps to the Unix epoch timestamp 1667275140. The third command copies the timestamps from the file "other_file" to "example". The fourth command uses the stat command to get the modification timestamp of "example", modifies the file by adding the text "backdoor", and then restores the original modification timestamp using touch.



**Command** ([[Change access and modification times using YYYYMMDDhhmm format]]):

```bash
touch -a -m -t 202210312359 "example"
```





**Command** ([[Change time using Unix epoch timestamp]]):

```bash
touch -a -m -d @1667275140 "example"
```





**Command** ([[Copy timestamp from one file to another]]):

```bash
touch -a -m -r "other_file" "example"
```





**Command** ([[Get the file's modification timestamp, modify the file, then restore the timestamp]]):

```bash
MODIFIED_TS=$(stat --format="%Y" "example")
echo "backdoor" >> "example"
touch -a -m -d @$MODIFIED_TS "example"
```



3. The touch command is used to create a new file in the current working directory. If the file already exists, the command will update the timestamp of the file without changing its content.

 



**Code**: [[touch]]



> The touch command takes one or more arguments, which are the names of the files to be created or updated. If the file does not exist, the command will create a new file with the given name. If the file already exists, the command will update the timestamp of the file without changing its content. The touch command is often used to create empty files or to update the timestamp of a file to the current time.



**Command** ([[Create file.txt using touch command]]):

```bash
touch file.txt
```



4. To execute this command, the attacker must have root privileges. The command changes the system time to October 31, 2022 at 11:59:59 PM, creates a new file named 'example', and changes the access and modification times of the file to match the modified system time. The original system time is then restored.

 



**Code**: [[ORIG_TIME=$(date)
date -s "2022-10-31 23:59:59"
to]]



> The attacker can use this technique to manipulate files on the system without being detected. By setting the system time to a date in the past, they can create or modify a file and make it appear as if it was created or modified at an earlier time. This can be useful for hiding their tracks or making it appear as if someone else was responsible for the file. However, this technique requires root privileges and can be detected if system logs are checked for changes in the system time.



**Command** ([[Set system time to 2022-10-31 23:59:59]]):

```bash
ORIG_TIME=$(date)
date -s "2022-10-31 23:59:59"
touch -a -m "example"
date -s "${ORIG_TIME}"
```



## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion|TA0005 - Defense Evasion]]

### Techniques

- [[Timestomp|T1099 - Timestomp]]

## Commands Used

- [[Change access and modification times using YYYYMMDDhhmm format]]
- [[Change time using Unix epoch timestamp]]
- [[Copy timestamp from one file to another]]
- [[Create empty file]]
- [[Create file.txt using touch command]]
- [[Get the file's modification timestamp, modify the file, then restore the timestamp]]
- [[Set system time to 2022-10-31 23:59:59]]

## Tags

- [[Linux - Evasion]]
- [[Timestomping]]


