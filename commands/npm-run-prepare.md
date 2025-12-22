---
id: new-uuid-for-npm-run-prepare
name: npm-run-prepare
type: command
executor: bash
data: npm run prepare
output: null
created_at: '2023-04-06T03:56:41.112637+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - rce
  - npm
verified: true
validated: true
---

# npm-run-prepare

## Command

```bash
npm run prepare
```

## Description

This command explicitly runs the 'prepare' script defined in a package.json file, which is useful for triggering lifecycle hooks in NPM packages during testing or exploitation scenarios. In the context of malicious configurations, it executes embedded shell commands without needing a full install.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `run` | NPM subcommand to execute scripts | Yes |
| `prepare` | The specific script name to run | Yes |

## Examples

### Basic Usage

```bash
npm run prepare
```

Run in the directory containing package.json to execute the prepare hook.

### Advanced Usage

```bash
npm run prepare --silent
```

Suppresses output for stealthier execution.

## Expected Output

If the prepare script succeeds (e.g., touches a file), NPM outputs:

```
> @ prepare
> /bin/touch /tmp/pwned.txt


up to date, audited 1 package in 0.5s
```

No errors if the command runs successfully; check for side effects like file creation.

## Related

- [[procedures/Upload-Malicious-Package-Manager-Configurations-for-RCE]]
- [[codes/NPM-Package-JSON-Prepare-Script]]
