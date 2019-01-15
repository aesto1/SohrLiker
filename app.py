# ver 0.11beta | first stable | with captcha limit

import vk
import sys
import time
import math
from colorama import Fore, Back, Style
from vk.exceptions import VkAPIError

###################################################################################
mID = "****"  # ОБЯЗАТЕЛЬНО УКАЗАТЬ СВОЙ ID В ВК!
access_token = "****"  # ОБЯЗАТЕЛЬНО УКАЗАТЬ СВОЙ ТОКЕН! КАК ЕГО ПОЛУЧИТЬ ЧИТАТЬ В Readme
###################################################################################
session = vk.Session(access_token=access_token)
api = vk.API(session)


class Sohrliker():
    print(Fore.GREEN + """   _____ ____  __  ______  __    ______ __ __________ 
  / ___// __ \/ / / / __ \/ /   /  _/ //_// ____/ __ 
  \__ \/ / / / /_/ / /_/ / /    / // ,<  / __/ / /_/ /
 ___/ / /_/ / __  / _, _/ /____/ // /| |/ /___/ _, _/ 
/____/\____/_/ /_/_/ |_/_____/___/_/ |_/_____/_/ |_|  
                                                      
             ____   _____         __                  
            / __ \ <  / /_  ___  / /_____ _           
           / / / / / / __ \/ _ \/ __/ __ `/           
          / /_/ / / / /_/ /  __/ /_/ /_/ /            
          \____(_)_/_.___/\___/\__/\__,_/             
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
                    print(pid, '- Уже лайкнул')
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
