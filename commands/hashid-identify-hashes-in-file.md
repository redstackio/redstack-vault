---
id: 05683ded-3de2-4776-9973-d83e6dcdae6a
name: hashid-identify-hashes-in-file
type: command
executor: bash
data: hashid $_FILENAME
output: >-
  root@kali:~# hashid hash.txt 

  --File 'hash.txt'--

  Analyzing
  '$6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57dZfYPhac6mPQAFdjow1NMY0OLOYkJFLJC5rIja7FsIneWJz0'

  [+] SHA-512 Crypt 

  --End of file 'hash.txt'--
created_at: '2019-09-24T22:00:40.485941+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - cryptography
  - hash-identification
verified: true
validated: true
---

# hashid-identify-hashes-in-file

## Command

```bash
hashid $_FILENAME
```

## Description

This command uses hashid to analyze a file containing one or more hash strings and identify their types based on regular expression patterns. It is useful for determining the hashing algorithm used in password dumps or captured credentials to select the appropriate cracking tool and mode.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_FILENAME | Path to the file containing hash(es) to analyze | Yes |

## Examples

### Basic Usage

```bash
hashid hash.txt
```

This scans the file 'hash.txt' and outputs the identified hash type(s).

### Advanced Usage

```bash
hashid -m hash.txt
```

Includes corresponding hashcat modes in the output for direct use in cracking tools.

## Expected Output

```
root@kali:~# hashid hash.txt 
--File 'hash.txt'--
Analyzing '$6$fN8i1AxB$0Z9xZy3X/NzJVWjyS1YhPpz7uy5vHsXA1Yxh57dZfYPhac6mPQAFdjow1NMY0OLOYkJFLJC5rIja7FsIneWJz0'
[+] SHA-512 Crypt 
--End of file 'hash.txt'--
```

The output lists each analyzed hash and the detected type(s), such as SHA-512 Crypt in this example.

## Related

- [[tools/hashid]]
- [[procedures/Identify-and-Crack-Hashes]]
