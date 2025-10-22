---
id: 55071142-b9cb-4792-81ed-224a867fdedb
name: Eyewitness
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:08.655721+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# Eyewitness

**Command** ([[Get the most recent version]]):

```bash
git clone https://github.com/ChrisTruncer/EyeWitness.git

```

**Command** ([[Faster Scan]]):

```bash
./EyeWitness.py --web -f hosts.txt --timeout 5 --threads 10 -d /mnt/event/Recon/ew --results 1000 --no-prompt --user-agent IE --add-https-ports 443,8443 --add-http-ports 80,8080 --prepend-https

```

**Command** ([[Slow version via proxychains]]):

```bash
proxychains ./EyeWitness.py --web -f hosts.txt --timeout 10 --threads 2 -d /mnt/event/Recon/ew --no-dns --results 1000 --no-prompt --user-agent IE --add-https-ports 443,8443 --add-http-ports 80,8080 --prepend-https proxychains ./EyeWitness.py --web -x nmaphosts.xml --timeout 10 --threads 2 -d /mnt/event/Recon/ew2 --no-dns --results 1000 --no-prompt --user-agent IE --add-https-ports 443,8443 --add-http-ports 80,8080 --prepend-https

```
