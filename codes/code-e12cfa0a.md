---
id: e12cfa0a-be98-41bf-9b19-f55f39246129
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:56:21.931090+00:00'
updated_at: '2023-04-10T20:25:06.989302+00:00'
---

# Code Snippet e12cfa0a

**Language**: Bash

```bash
sudo nmap -sSV -p- 192.168.0.1 -oA OUTPUTFILE -T4
sudo nmap -sSV -oA OUTPUTFILE -T4 -iL INPUTFILE.csv

• -sSV: Sends a TCP SYN packet and determines any service on open ports
• -p-: Scans all 65,535 ports
• 192.168.0.1: IP address to scan
• -oA OUTPUTFILE: Outputs the findings in its three major formats at once using the filename "OUTPUTFILE"
• -iL INPUTFILE: Uses the provided file as inputs
• -T4: Sets timing template to aggressive

Instructions: Run the command with sudo privileges to scan for open ports on the target IP address. Use the -oA flag to save the output in all major formats. Use the -iL flag to specify a list of targets to scan from a file.
```


