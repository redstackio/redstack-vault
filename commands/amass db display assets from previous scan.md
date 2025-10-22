---
id: c3434943-464e-44f5-bbe1-b1c188a7b5bd
name: amass db display assets from previous scan
type: command
executor: bash
data: amass db -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -enum $_LIST_NUMBER -show
output: "root@kali ~# amass db -dir owasp.org/ -d owasp.org -enum 2 -show\nlists.owasp.org\n\
  ocms.owasp.org\nowasp.org\nwiki.owasp.org\ndev.owasp.org\ngapps.owasp.org\nvideos.owasp.org\n\
  austin.owasp.org\nwww2.owasp.org\ncontact.owasp.org\nname-virt-host.owasp.org\n\
  www.owasp.org\ncheatsheetseries.owasp.org\ngroups.owasp.org\ncalendar.owasp.org\n\
  sl.owasp.org\nmail.owasp.org\nkerala.owasp.org\n\nOWASP Amass v3.7.2           \
  \                     https://github.com/OWASP/Amass\n--------------------------------------------------------------------------------\n\
  18 names discovered - cert: 10, api: 8\n--------------------------------------------------------------------------------\n\
  ASN: 13335 - CLOUDFLARENET, US\n\t2606:4700:10::/44 \t54   Subdomain Name(s)\n\t\
  172.67.0.0/20     \t18   Subdomain Name(s)\n\t104.22.16.0/20    \t36   Subdomain\
  \ Name(s)\n"
created_at: '2020-06-29T18:05:44.400386+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass db display assets from previous scan

```bash
amass db -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -enum $_LIST_NUMBER -show
```

## Expected Output

```
root@kali ~# amass db -dir owasp.org/ -d owasp.org -enum 2 -show
lists.owasp.org
ocms.owasp.org
owasp.org
wiki.owasp.org
dev.owasp.org
gapps.owasp.org
videos.owasp.org
austin.owasp.org
www2.owasp.org
contact.owasp.org
name-virt-host.owasp.org
www.owasp.org
cheatsheetseries.owasp.org
groups.owasp.org
calendar.owasp.org
sl.owasp.org
mail.owasp.org
kerala.owasp.org

OWASP Amass v3.7.2                                https://github.com/OWASP/Amass
--------------------------------------------------------------------------------
18 names discovered - cert: 10, api: 8
--------------------------------------------------------------------------------
ASN: 13335 - CLOUDFLARENET, US
	2606:4700:10::/44 	54   Subdomain Name(s)
	172.67.0.0/20     	18   Subdomain Name(s)
	104.22.16.0/20    	36   Subdomain Name(s)

```
