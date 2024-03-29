import os
import io
from PIL import Image
from PIL.ExifTags import TAGS
import calendar
import datetime as dt

def get_exif_info(jpg_file):
    im = Image.open(jpg_file)
    try:
        exif = im._getexif()
    except AttributeError:
        return {}
    dic_ = {}
    for id, value in exif.items():
        dic_[TAGS.get(id)] = value
    try:
        when_list = dic_['DateTimeOriginal'].split(' ')
        day_list = when_list[0].split(':')
        time_list = when_list[1]
        date = dt.date(int(day_list[0]), int(day_list[1]), int(day_list[2]))
        day_index = date.weekday()  # => 1
        day = calendar.day_name[day_index] #曜日
        time = time_list #時間
        return day,time
    except:
       raise Exception("error")
   

def get_file_created_at(file_binary):
    path = "media/temp.jpg"
    with open(path, mode="wb") as f:
        f.write(file_binary)
    return dt.datetime.fromtimestamp(os.stat(path).st_ctime)