---
id: 6d2433c6-98ae-4f42-b5cb-c30741edaa00
name: Slow version via proxychains
type: command
executor: bash
data: 'proxychains ./EyeWitness.py --web -f hosts.txt --timeout 10 --threads 2 -d
  /mnt/event/Recon/ew --no-dns --results 1000 --no-prompt --user-agent IE --add-https-ports
  443,8443 --add-http-ports 80,8080 --prepend-https proxychains ./EyeWitness.py --web
  -x nmaphosts.xml --timeout 10 --threads 2 -d /mnt/event/Recon/ew2 --no-dns --results
  1000 --no-prompt --user-agent IE --add-https-ports 443,8443 --add-http-ports 80,8080
  --prepend-https

  '
output: null
created_at: '2020-07-14T18:21:08.435140+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Slow version via proxychains

```bash
proxychains ./EyeWitness.py --web -f hosts.txt --timeout 10 --threads 2 -d /mnt/event/Recon/ew --no-dns --results 1000 --no-prompt --user-agent IE --add-https-ports 443,8443 --add-http-ports 80,8080 --prepend-https proxychains ./EyeWitness.py --web -x nmaphosts.xml --timeout 10 --threads 2 -d /mnt/event/Recon/ew2 --no-dns --results 1000 --no-prompt --user-agent IE --add-https-ports 443,8443 --add-http-ports 80,8080 --prepend-https

```
