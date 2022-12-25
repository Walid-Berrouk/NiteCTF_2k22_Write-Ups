# Travel

## Write-Up

When checking metadata of the `owl.jpg` image, we can find the following link :

```
exiftool owl.jpg
```

```
...
Exif Byte Order                 : Big-endian (Motorola, MM)
Artist                          : bit.ly/mytodooolist
XP Author                       : bit.ly/mytodooolist
Padding                         : (Binary data 2060 bytes, use -b option to extract)
Profile CMM Type                : Linotronic
...
```

The link leads us to a clipboard in google (Check TODO1.png). After checking the file locally, it gave us no information, but when creating a copy in our google drive `https://jamboard.google.com/d/1ZmtjSttAs7372FuuqsIT3v9d9l_VBKJjPRju-3k02cU/viewer?f=0` and move clips away, we can find a link to a webiste : 

```
https://tr4v3l1.netlify.app/
```

You find the `ZmxhZy50eHQ=` as comment, and when decode it, we get the following : 

```
└─$ echo "ZmxhZy50eHQ=" | base64 -d
flag.txt   
```

After requesting the `flag.txt`, you get a txt file but with bin data in it with no useful information.

After exploring the website more, we also find this comment : 


```html
<!--  <p> <b>Go Back in time and get the previous month's menu!!!</b></p>  -->
```

And since we can't check previous version of netlify, but we can check if there is a public repository in github of it, and indeed there is one in the name of `https://github.com/tr4v3l1/tr4v3l1`

And after checking the commits, we can see that the flag has been added, then deleted before last commit, we can find it in the `flag.txt` file of previous commits.


## Flag

nitectf{y0u_w3nt_b4ck_1n_t1m3}
