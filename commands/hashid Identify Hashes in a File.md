---
id: 05683ded-3de2-4776-9973-d83e6dcdae6a
name: hashid Identify Hashes in a File
type: command
executor: bash
data: hashid $_FILENAME
output: "root@kali:~# hashid hash.txt \n--File 'hash.txt'--\nAnalyzing '$6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57dZfYPhac6mPQAFdjow1NMY0OLOYkJFLJC5rIja7FsIneWJz0'\n\
  [+] SHA-512 Crypt \n--End of file 'hash.txt'--"
created_at: '2019-09-24T22:00:40.485941+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# hashid Identify Hashes in a File

```bash
hashid $_FILENAME
```

## Expected Output

```
root@kali:~# hashid hash.txt 
--File 'hash.txt'--
Analyzing '$6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57dZfYPhac6mPQAFdjow1NMY0OLOYkJFLJC5rIja7FsIneWJz0'
[+] SHA-512 Crypt 
--End of file 'hash.txt'--
```
