---
id: 811ccd9d-31df-460a-82be-c7efac1a1d30
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:25.499275+00:00'
updated_at: '2023-04-10T20:25:39.526230+00:00'
---

# Code Snippet 811ccd9d

**Language**: Powershell

```powershell
go get github.com/subfinder/subfinder
./Subfinder/subfinder --set-config PassivetotalUsername='USERNAME',PassivetotalKey='KEY'
./Subfinder/subfinder --set-config RiddlerEmail="EMAIL",RiddlerPassword="PASSWORD"
./Subfinder/subfinder --set-config CensysUsername="USERNAME",CensysSecret="SECRET"
./Subfinder/subfinder --set-config SecurityTrailsKey='KEY'
./Subfinder/subfinder -d example.com -o /tmp/results_subfinder.txt
```


