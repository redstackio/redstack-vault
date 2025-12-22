---
id: 3a2efba6-a759-42a6-90fd-7af4a432e626
name: python-run-bzr-dumper
type: command
executor: bash
data: 'python3 dumper.py -u "http://127.0.0.1:5000/" -o source'
output: null
created_at: '2023-04-06T03:56:00.354679+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - python
  - bzr-dumper
  - extract
verified: true
validated: true
---

# python-run-bzr-dumper

## Command

```bash
python3 dumper.py -u "$_TARGET_URL" -o $_OUTPUT_DIR
```

## Description

This command executes the bzr_dumper Python script to extract contents from an insecure Bazaar repository by sending HTTP GET requests to fetch repository files and metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u $_TARGET_URL | The HTTP URL of the target Bazaar repository (e.g., http://target.com/bzr/) | Yes |
| -o $_OUTPUT_DIR | The local directory to save the extracted source code | Yes |
| python3 | Python 3 interpreter | Yes |
| dumper.py | The bzr_dumper script file | Yes |

## Examples

### Basic Usage

```bash
python3 dumper.py -u "http://target.example.com/bzr-repo/" -o extracted-source
```

### Advanced Usage

Run with a verbose flag if supported by the script (check script for options):

```bash
python3 dumper.py -u "http://target.example.com/bzr-repo/" -o extracted-source
```

## Expected Output

Created a standalone tree (format: 2a)
[!] Target : http://target.example.com/bzr-repo/
[+] Start.
[+] GET repository/pack-names
[+] GET README
[+] GET checkout/dirstate
[+] GET branch/branch.conf
[+] GET branch/format
[+] GET branch/last-revision
[+] GET b'154411f0f33adc3ff8cfb3d34209cbd1'
[*] Finish

## Related

- [[procedures/Extract-Source-Code-from-Insecure-Bazaar-Repository]]
