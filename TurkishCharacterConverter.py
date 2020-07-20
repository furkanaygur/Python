message = "ç Ç ğ Ğ ı İ ö Ö ş Ş ü Ü"
message = message.replace('ç','c')\
    .replace('Ç','C')\
    .replace('ğ','g')\
    .replace('Ğ','G')\
    .replace('ı','i')\
    .replace('İ','I')\
    .replace('ö','o')\
    .replace('Ö','O')\
    .replace('ş','s')\
    .replace('Ş','S')\
    .replace('ü','u')\
    .replace('Ü','U')
print(message)