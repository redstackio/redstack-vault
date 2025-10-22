---
id: dee905ef-53a8-4150-bbf7-78a16c869d7c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:25.577997+00:00'
updated_at: '2023-04-10T20:25:37.045240+00:00'
---

# Code Snippet dee905ef

**Language**: Powershell

```powershell
gem install aquatone

Discover subdomains : results in ~/aquatone/example.com/hosts.txt
aquatone-discover --domain example.com
aquatone-discover --domain example.com --threads 25
aquatone-discover --domain example.com --sleep 5 --jitter 30
aquatone-discover --set-key shodan o1hyw8pv59vSVjrZU3Qaz6ZQqgM91ihQ

Active scans : results in ~/aquatone/example.com/urls.txt
aquatone-scan --domain example.com
aquatone-scan --domain example.com --ports 80,443,3000,8080
aquatone-scan --domain example.com --ports large
aquatone-scan --domain example.com --threads 25

Final results
aquatone-gather --domain example.com
```
