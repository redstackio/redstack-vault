---
id: 22099ef5-ae7a-4bb6-9cd4-362425183031
name: Discover subdomains with Aquatone
type: command
executor: bash
data: 'aquatone-discover --domain example.com

  aquatone-discover --domain example.com --threads 25

  aquatone-discover --domain example.com --sleep 5 --jitter 30

  aquatone-discover --set-key shodan o1hyw8pv59vSVjrZU3Qaz6ZQqgM91ihQ'
output: null
created_at: '2023-04-06T03:56:25.578136+00:00'
updated_at: '2023-04-10T20:25:37.047769+00:00'
---

# Discover subdomains with Aquatone

```bash
aquatone-discover --domain example.com
aquatone-discover --domain example.com --threads 25
aquatone-discover --domain example.com --sleep 5 --jitter 30
aquatone-discover --set-key shodan o1hyw8pv59vSVjrZU3Qaz6ZQqgM91ihQ
```
