---
id: 21f2ad61-4f6c-4290-9e7b-918a0238a207
name: Basic Linux Disk and File Search
type: cheatsheet
verified: true
created_at: '2020-03-10T06:28:38.846343+00:00'
updated_at: '2023-05-30T20:13:04.412293+00:00'
---

# Basic Linux Disk and File Search

**Status**: ✓ Verified

# Description

Simple commands for looking around.

## grep - Find text in a File

**Command** ([[Search for Text in a File (Case Insensitive)]]):

```bash
grep -i $_STRING $_FILE
```

**Command** ([[Recursive Search for Text in All Files]]):

```bash
grep -R $_STRING $_PATH/*
```

**Command** ([[Recursive Search for Text in Files with Regex]]):

```bash
grep -RE $_REGEX $_PATH
```

- Examples of regex patterns and concepts can be found here: [https://cs.lmu.edu/~ray/notes/regex/](https://cs.lmu.edu/~ray/notes/regex/)

## find - Find Files and Folders

**Command** ([[Find Files by Name]]):

```bash
find / -name $_STRING
```

- -name - specifies a string in the filename to match. Accepts wildcards with "*" 

**Command** ([[Search for Files Modified Within 60 Minutes]]):

```bash
find / -ctime -60
```

- ctime - refers to last changed time. 

- -60 - sets the ctime range to the past 60 mins

**Command** ([[Find Files by Name and Execute a Command]]):

```bash
find $_PATH -name $_STRING -exec $_COMMAND {} \;
```

- -exec - execute a program on the results of the search. The command is executed on the contents of the braces,  and "\;" is necessary to indicate the end of the command,
