# ICQ Notes Bot
ICQ bot for saving your notes. Saves your notes to Yandex Disk  
Provide your access token in ICQ_ACCESS_TOKEN environment variable and whitelist of allowed users in ICQ_ALLOWED_USERIDS var. 
Yandex Disk access token should be provided in DISK_ACCESS_TOKEN var.  

_ICQ_ACCESS_TOKEN_ can be obtained via [Metabot](https://icq.im/70001)  
Instructions about _DISK_ACCESS_TOKEN_ can be found [here](https://yandex.ru/dev/disk/api/concepts/quickstart-docpage/)
Example:  
```
DISK_ACCESS_TOKEN='1111111_2_333333333333333333333' \
ICQ_ACCESS_TOKEN='111.2222222222.3333333333:444444444' \
ICQ_ALLOWED_USERIDS='1234567,8901234,56789012' \
./api.py
```

ICQ API documentation can be found [here](https://icq.com/botapi/)  
Yandex Disk API documentation can be found [here](https://yandex.ru/dev/disk/), Pyhton plugin documentation [here](https://yadisk.readthedocs.io/ru/latest/docs.html)  
