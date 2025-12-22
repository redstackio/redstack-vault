---
id: 4651aae9-f5e6-476b-b9c6-ca5a368b6b1b
name: spawn-tty-using-interpreters
type: code
language: bash
verified: true
created_at: '2023-04-06T03:56:24.983731+00:00'
updated_at: '2023-04-10T20:25:31.246275+00:00'
platforms:
  - Linux
  - Unix
tags:
  - tty
  - spawn
  - interpreter
  - post-exploitation
validated: true
---

# spawn-tty-using-interpreters

## Code

```bash
/bin/sh -i
python3 -c 'import pty; pty.spawn("/bin/sh")'
python3 -c "__import__('pty').spawn('/bin/bash')"
python3 -c "__import__('subprocess').call(['/bin/bash'])
perl -e 'exec "/bin/sh";'
perl: exec "/bin/sh";
perl -e 'print `/bin/bash`'
ruby: exec "/bin/sh"
lu: os.execute('/bin/sh')
```

## Description

Collection of one-liner commands to spawn a TTY-backed shell using common interpreters when a basic shell lacks interactivity. Prioritizes Python for PTY spawning, with fallbacks to Perl, Ruby, and Lua for broader compatibility.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| /bin/sh | Target shell path | /bin/bash (alternative) |

## Usage

In a non-TTY reverse shell, execute one-liner based on available interpreter (check with `which python3`). Follow with `export TERM=screen` for colors. Useful after initial RCE for stable access.

## Detection

- EDR alerts on interpreter executions spawning shells (e.g., python exec /bin/sh).
- Sysmon logs for process creation with parent as nc/python and child as bash.
- Network forensics showing shell commands over unusual interpreter processes.

## Related

- [[procedures/Spawn-TTY-Shell-from-Existing-Session]]
