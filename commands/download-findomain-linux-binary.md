---
id: 93c75e2f-9995-43c8-972f-234c2cc61f0a
name: download-findomain-linux-binary
type: command
executor: bash
data: >-
  wget
  https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
output: null
created_at: '2023-04-06T03:56:25.541931+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - download
  - installation
verified: true
validated: true
---

# download-findomain-linux-binary

## Command

```bash
wget https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
```

## Description

This command downloads the latest Linux binary release of Findomain from GitHub, used as the first step in setting up the tool for subdomain enumeration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | Direct link to the binary release | Built-in |

## Examples

### Basic Usage

```bash
wget https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
```

### With Output Directory

```bash
wget -P /opt/tools/ https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
```

## Expected Output

HTTP download progress:

--2023-10-01 12:00:00--  https://github.com/Edu4rdSHL/findomain/releases/latest/download/findomain-linux
Resolving github.com (github.com)... 140.82.121.3
Connecting to github.com (github.com)|140.82.121.3|:443... connected.
HTTP request sent, awaiting response... 302 Found
Location: https://github.com/Edu4rdSHL/findomain/releases/download/8.0.0/findomain-linux [following]
--2023-10-01 12:00:00--  https://github.com/Edu4rdSHL/findomain/releases/download/8.0.0/findomain-linux
Resolving github.com (github.com)... 140.82.121.3
... [progress bar]
Length: 12345678 (12M) [application/octet-stream]
Saving to: 'findomain-linux'

findomain-linux  100%[===================>]  11.78M  1.23MB/s    in 9.6s     

2023-10-01 12:00:10 (1.23 MB/s) - 'findomain-linux' saved [12345678/12345678]

## Related

- [[procedures/Subdomain-Enumeration-with-Findomain]]
- [[commands/make-findomain-linux-executable]]
