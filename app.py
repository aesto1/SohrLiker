# ver 0.11beta | first release          | with captcha limit
# ver 0.2      | with saving settings   | captcha bypass every 48likes for 200sec (shit) <<--

import vk
import sys
import time
import math
import os
from colorama import Fore, Back, Style
from vk.exceptions import VkAPIError

try:
    import configparser
except ImportError:
    import ConfigParser as configparser

config = configparser.ConfigParser()
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
path = os.path.join(BASE_DIR, "config.ini")



def createConfig(path, a, b):
    config = configparser.ConfigParser()
    config.add_section("Config")
    config.set("Config", "access_token", a)
    config.set("Config", "mID", b)
    
    with open(path, "w") as config_file:
        config.write(config_file)

if not os.path.exists(path):
    os.system('start https://vk.cc/8VlNxj')
    a = input('Введите access_token\n')
    os.system('start http://regvk.com/id/')
    b = input('Введите ВАШ численный vkID\n')
    createConfig(path, a, b)

###################################################################################
config.read(path)
mID = config.get("Config", "mID")
access_token = config.get("Config", "access_token")
###################################################################################
session = vk.Session(access_token=access_token)
api = vk.API(session)

class Sohrliker():
    print(Fore.GREEN + """
███████╗ ██████╗ ██╗  ██╗██████╗ ██╗     ██╗██╗  ██╗███████╗██████╗ 
██╔════╝██╔═══██╗██║  ██║██╔══██╗██║     ██║██║ ██╔╝██╔════╝██╔══██╗
███████╗██║   ██║███████║██████╔╝██║     ██║█████╔╝ █████╗  ██████╔╝
╚════██║██║   ██║██╔══██║██╔══██╗██║     ██║██╔═██╗ ██╔══╝  ██╔══██╗
███████║╚██████╔╝██║  ██║██║  ██║███████╗██║██║  ██╗███████╗██║  ██║
╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝
                       ██████╗    ██████╗                           
                      ██╔═████╗   ╚════██╗                          
                      ██║██╔██║    █████╔╝                          
                      ████╔╝██║   ██╔═══╝                           
                      ╚██████╔╝██╗███████╗                          
                       ╚═════╝ ╚═╝╚══════╝                          
                                                                    
 """)
    print(Fore.BLUE + 'Введите ID')
    ID = input()
    print(Fore.GREEN + 'Введите Offset')
    offset = input()
    if offset == "":
        offset = 0

    def getUserId(link):  # Преобразование vkid из id1, vk.com/durov в 1
        id = link
        if 'vk.com/' in link:  # проверяем эту ссылку
            id = link.split('/')[-1]  # если да, то получаем его последнюю часть
        if not id.replace('id', '').isdigit():  # если в нем после отсечения 'id' сами цифры - это и есть id
            id = api.utils.resolveScreenName(screen_name=id, v=5.8)[
                'object_id']  # если нет, получаем id с помощью метода API
        else:
            id = id.replace('id', '')
        return int(id)
    try:
        ID = getUserId(ID)
    except Exception:
        print("Ошибка! Проверьте правильность access_token и mID")
        sys.exit()


    def GetPhotosList(ID):
        an = api.users.get(user_ids=ID, v=5.92)
        al = an[0]["last_name"]
        af = an[0]["first_name"]
        ID = int(ID)
        photos = api.photos.get(owner_id=ID, album_id='saved', rev=1, count='1000', v=5.92)
        cnt = str(photos['count'])
        print(af + " " + al)
        print("Кол-во сохраненок - " + cnt)
        print("Ожидается 'прогонов' " + str(math.ceil(int(cnt)/50)))

        return photos

    def Action(ID, p, offset, mID):
        Max = p['count']
        Counter = offset
        CaptchaLim = int(Counter) + 49
        Liked = 0
        Counter = int(Counter)
        # print(Counter)
        # print(CaptchaLim)
        try:
            while Counter <= Max:

                if Counter == CaptchaLim:
                     CaptchaLim = int(CaptchaLim) + 48
                     print(Fore.RED + "Пауза 200 секунд")
                     print(Fore.GREEN)
                     time.sleep(200)


                time.sleep(0.5)  # обход лимита на запросы :)
                pid = p["items"][Counter]["id"]
                a = api.likes.isLiked(user_id=mID, type='photo', owner_id=ID, item_id=pid, v=5.92)
                if a['liked'] == 0:
                    api.likes.add(type="photo", owner_id=ID, item_id=pid, v=5.92)
                    print(pid, '- Лайкнул')
                    Counter = Counter + 1
                    Liked = Liked + 1
                if a['liked'] == 1:
                    print(pid, '- Пропуск')
                    Counter = Counter + 1
        except IndexError:
            print("Работа завершена!")

        except Exception as e:
            print("Captcha!!! Try again later with offset - ", Fore.RED, Counter)

        except KeyboardInterrupt:
            print("Программа остановлена вручную (ctrl+c)")


        return Liked

    li = GetPhotosList(ID)

    finaly = Action(ID, li, offset, mID)

    print(Fore.WHITE, 'Успешно пролайкано -', Fore.GREEN, finaly)


if __name__ == '__main__':
    Sohrliker()