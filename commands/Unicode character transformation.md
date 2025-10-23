---
id: 8830769f-a690-4e56-b589-9ccc0452df66
name: Unicode character transformation
type: command
executor: bash
data: 'Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN (encoded as %EF%BC%9C) was
  transformed into U+003C LESS­THAN SIGN (<)


  Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was transformed
  into U+0022 QUOTATION MARK (\")


  Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was transformed
  into U+0027 APOSTROPHE (\'')


  E.g : http://www.example.net/something%CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/

  %EF%BC%9E becomes >

  %EF%BC%9C becomes <'
output: null
created_at: '2023-04-06T03:56:43.000803+00:00'
updated_at: '2023-04-10T20:21:30.233009+00:00'
---

# Unicode character transformation

```bash
Unicode character U+FF1C FULLWIDTH LESS­THAN SIGN (encoded as %EF%BC%9C) was transformed into U+003C LESS­THAN SIGN (<)

Unicode character U+02BA MODIFIER LETTER DOUBLE PRIME (encoded as %CA%BA) was transformed into U+0022 QUOTATION MARK (\")

Unicode character U+02B9 MODIFIER LETTER PRIME (encoded as %CA%B9) was transformed into U+0027 APOSTROPHE (\')

E.g : http://www.example.net/something%CA%BA%EF%BC%9E%EF%BC%9Csvg%20onload=alert%28/XSS/%29%EF%BC%9E/
%EF%BC%9E becomes >
%EF%BC%9C becomes <
```


