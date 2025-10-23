---
id: ae919fae-4042-46c3-bf5e-4be41a4809e7
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:08.937599+00:00'
updated_at: '2023-04-10T20:20:58.743576+00:00'
---

# Code Snippet ae919fae

**Language**: Powershell

```powershell
wget https://digi.ninja/files/bucket_finder_1.1.tar.bz2 -O bucket_finder_1.1.tar.bz2
./bucket_finder.rb my_words
./bucket_finder.rb --region ie my_words
    US Standard         = http://s3.amazonaws.com
    Ireland             = http://s3-eu-west-1.amazonaws.com
    Northern California = http://s3-us-west-1.amazonaws.com
    Singapore           = http://s3-ap-southeast-1.amazonaws.com
    Tokyo               = http://s3-ap-northeast-1.amazonaws.com

./bucket_finder.rb --download --region ie my_words
./bucket_finder.rb --log-file bucket.out my_words
```


