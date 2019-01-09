# (*)		(*)		(*)		(*)		(*)		(*)		(*)		(*)
# (*)														(*)
# (*)			SohrLiker By Finskiy    					(*)
# (*)	Возможности продукта:								(*)
# (*)	Автоматический пролайк всех сохр. 					(*)
# (*)	Статистика 											(*)
# (*)	       												(*)
# (*)														(*)
# (*)														(*)
# (*)														(*)
# (*)	+)Инициализация VkApi								(*)
# (*)	+)Передача ID аккаунта								(*)
# (*)	+)Получение всех сохраненных фото аккаунта - п.2	(*)
# (*)	+)Проверка - лайкнуто ли фото						(*)
# (*)	+)Если лайкнуто, то пропуск							(*)
# (*)	+)Просчет лайкнутых									(*)
# (*)	-)Отправка отчета									(*)
# (*)														(*)
# (*)		(*)		(*)		(*)		(*)		(*)		(*)		(*)


import vk
import time
from colorama import Fore, Back, Style

###################################################################################
mID = ""  # ОБЯЗАТЕЛЬНО УКАЗАТЬ СВОЙ ID В ВК!
access_token = ""  # ОБЯЗАТЕЛЬНО УКАЗАТЬ СВОЙ ТОКЕН! КАК ЕГО ПОЛУЧИТЬ ЧИТАТЬ В Readme
###################################################################################
session = vk.Session(access_token=access_token)
api = vk.API(session)


# https://oauth.vk.com/authorize?client_id=6812123&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos,wall,offline&response_type=token&v=5.92&state=123456


class Sohrliker():
    print(
        Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")")
    print(
        Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "                                                     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")")
    print(
        Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + Fore.WHITE + "                 SohrLiker By Finskiy                " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")")
    print(
        Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "                                                     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")")
    print(
        Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")" + "     " + Fore.RED + "(" + Fore.GREEN + "*" + Fore.RED + ")")

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

    ID = getUserId(ID)

    def GetPhotosList(ID):
        an = api.users.get(user_ids=ID, v=5.92)
        al = an[0]["last_name"]
        af = an[0]["first_name"]
        ID = int(ID)
        photos = api.photos.get(owner_id=ID, album_id='saved', rev=1, count='1000', v=5.92)
        cnt = str(photos['count'])
        print(af + " " + al)
        print("Кол-во сохраненок - " + cnt)

        return photos

    def Action(ID, p, offset, mID):
        Max = p['count']
        Counter = offset
        # CaptchaLim = int(Counter) + 48
        Liked = 0
        Counter = int(Counter)
        # print(Counter)
        # print(CaptchaLim)
        try:
            while Counter < Max:

                # if Counter == CaptchaLim:
                #     CaptchaLim = int(CaptchaLim) + 48
                #     time.sleep(120)
                # Попытка обойти каптчу

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
