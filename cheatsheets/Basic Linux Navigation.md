---
id: 4b433ca6-f059-4f3a-abab-a4f2f9436f29
name: Basic Linux Navigation
type: cheatsheet
verified: true
created_at: '2020-03-10T03:42:56.253292+00:00'
updated_at: '2023-05-30T20:12:35.420379+00:00'
---

# Basic Linux Navigation

**Status**: ✓ Verified

# Description

Simple commands for getting around the Linux filesystem.



## ls - List Directory Contents





**Command** ([[List All Files and Folders]]):

```bash
ls -alh $_PATH
```



- -a - list all files and folders including hidden content


- -l - list results in long listing format (includes permissions, size, etc)


- -h - list bytes in human readable sizes



## cat - Concatenate file(s)





**Command** ([[Print a Files Contents]]):

```bash
cat $_FILE
```









**Command** ([[Concatenate Two Files into a New File]]):

```bash
cat $_FILE1 $_FILE2 > $_OUTPUT
```





## cd - Change Working Directory





**Command** ([[Change Directory to Last Dir]]):

```bash
cd -
```





## file - Determine File Type





**Command** ([[Determine File Type]]):

```bash
file $_FILE
```





## cp - Copy File





**Command** ([[Copy Folder Recursively]]):

```bash
cp -r $_FOLDER $_DESTINATION
```





## mv - Move a File or Folder





**Command** ([[Move a Directory]]):

```bash
mv $_FOLDER $_DESTINATION
```





## rm - Delete a File or Folder





**Command** ([[Delete a File]]):

```bash
rm $_FILE
```









**Command** ([[Delete a Folder and All Contents]]):

```bash
rm -rf $_FOLDER
```



- -r - delete recursively

- -f - force deletion

## strings - Print Printable Strings





**Command** ([[Print Human Readable Strings in a File]]):

```bash
strings $_FILE
```








