---
id: 8972e896-34eb-4e23-a460-ba067d3d39a5
name: Vulnerable-Curl-Executor-Script
type: code
language: python
verified: true
created_at: '2023-04-06T03:55:54.013910+00:00'
updated_at: '2023-04-06T03:55:54.027603+00:00'
platforms:
  - Linux
  - Unix
tags:
  - vulnerable
  - injection
  - python
validated: true
---

# Vulnerable-Curl-Executor-Script

## Code

```python
from shlex import quote,split
import sys
import subprocess

if __name__=="__main__":
    command = ['curl']
    command = command + split(sys.argv[1])
    print(command)
    r = subprocess.Popen(command)
```

## Description

This Python script is a vulnerable example that takes a user-supplied string argument, splits it into tokens using shlex.split(), appends them to a base 'curl' command, prints the resulting list, and executes it via subprocess.Popen(). Due to lack of validation, it allows command injection via shell metacharacters in the input string.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sys.argv[1] | The input string to parse and inject into the curl command | "https://example.com ; id" |

## Usage

Save as vulnerable_curl.py and execute with python vulnerable_curl.py "<malicious args>". Used in red team exercises to demonstrate argument injection in dynamic command construction. Deliver via file upload or API if targeting a web app.

## Detection

- Monitor Python processes spawning curl or subprocess with dynamic args.
- Log argv in application logs to detect metacharacters like ';', '&&'.
- Use EDR tools to alert on unexpected command chaining in Popen calls.
- Static analysis: Scan for shlex.split() followed by list append to subprocess without quoting.

## Related

- [[procedures/Command-Injection-via-Curl-Arguments]]
- [[commands/execute-vulnerable-curl-script]]
