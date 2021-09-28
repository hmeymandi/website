from jalali_date import datetime2jalali,date2jalali
from django.utils import datetime

def persian_number():
        time2str=datetime2jalali
        number={
            '0':'۰',
            '1':'۱',
            '2':'۲',
            '3':'۳',
            '4':'۴',
            '5':'۵',
            '6':'۶',
            '7':'۷',
            '8':'۸',
            '9':'۹',
       }
        for i,j in number.items():
            time2str=time2str.replace(i,j)

        print(time2str)
        return time2str
