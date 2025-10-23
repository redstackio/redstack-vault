---
id: 4766fd8f-cc5c-42b0-b094-53b653a0dc7e
name: Active scans with Aquatone
type: command
executor: bash
data: 'aquatone-scan --domain example.com

  aquatone-scan --domain example.com --ports 80,443,3000,8080

  aquatone-scan --domain example.com --ports large

  aquatone-scan --domain example.com --threads 25'
output: null
created_at: '2023-04-06T03:56:25.578182+00:00'
updated_at: '2023-04-10T20:25:37.047769+00:00'
---

# Active scans with Aquatone

```bash
aquatone-scan --domain example.com
aquatone-scan --domain example.com --ports 80,443,3000,8080
aquatone-scan --domain example.com --ports large
aquatone-scan --domain example.com --threads 25
```


