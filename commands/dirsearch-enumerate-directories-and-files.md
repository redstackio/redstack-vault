---
id: f11cdc4d-aa86-4242-be58-87fca7c688b3
name: dirsearch-enumerate-directories-and-files
type: command
executor: bash
data: |
  python3 dirsearch.py -u $_TARGET_URL -e $_EXTENSIONS
output: null
created_at: '2020-07-24T17:11:43.591611+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - linux
  - web
tags:
  - reconnaissance
  - web-scanning
verified: true
validated: true
---

# dirsearch-enumerate-directories-and-files

## Command

```bash
python3 dirsearch.py -u $_TARGET_URL -e $_EXTENSIONS
```

## Description

This command invokes dirsearch to perform brute-force enumeration of directories and files on a target web server. It tests a built-in wordlist of common paths against the specified URL, appending the given extensions to check for specific file types. Use this during web reconnaissance to uncover hidden resources without manual guessing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target website (e.g., http://example.com or https://sub.domain.com) | Yes |
| $_EXTENSIONS | Comma-separated list of file extensions to test (e.g., php,html,js) or .* for all built-in extensions | Yes |
| -u | Specifies the target URL (short for --url) | Built-in |
| -e | Specifies extensions (short for --extensions) | Built-in |

## Examples

### Basic Usage

```bash
python3 dirsearch.py -u http://redstack.io -e .*
```

This scans the root of redstack.io for all common directories and files using dirsearch's default wordlist.

### Advanced Usage

```bash
python3 dirsearch.py -u https://target.com -e php,asp,aspx --wordlist=/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -o results.txt
```

This uses a custom wordlist, limits to specific extensions, and saves output to a file. Note: Additional flags like --wordlist and -o are optional extensions to the core command.

## Expected Output

The command produces real-time output showing tested paths and their HTTP responses. Successful discovery is indicated by non-404 codes:


[+] http://redstack.io/ (CODE:200|SIZE:2456) [Status: OK]
[+] http://redstack.io/admin (CODE:200|SIZE:0) [Status: OK]
[+] http://redstack.io/config.bak (CODE:403|SIZE:123) [Status: Forbidden]
[-] http://redstack.io/nonexistent (CODE:404|SIZE:0) [Status: Not Found]


At completion:


[09:45:23] Starting:
[09:45:23] Target: http://redstack.io
[09:45:23] Extensions: .*
...
[09:46:15] Finished:
[09:46:15] Requests: 5000
[09:46:15] Time: 52s


Review for 200, 301, or 403 responses to identify potential resources.

## Related

- [[procedures/Fuzz-Website-Directories-and-Files-with-Dirsearch]]
- [[tools/Dirsearch]]
