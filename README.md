# SohrLiker
Автоматизированный пролайк сохранненных фотографий

# Установка 
### Установка Python 3.7.0
  Скачать - [Python](https://www.python.org/ftp/python/3.7.0/python-3.7.0-amd64.exe)   
  Установить. Добавить Python в Path.

### Установка VK и Colorama
   **Вводить в консоли (win+r -> cmd)**
   ```
   pip install vk
   ```
   ```
   pip install colorama
   ```



# Настройка
### Получение access_token
  Перейди по ссылке - [vk.com](https://oauth.vk.com/authorize?client_id=6812123&display=page&redirect_uri=https://oauth.vk.com/blank.html&scope=photos,wall,offline&response_type=token&v=5.92&state=123456)  
  Далее подтвердить получение доступа.  
  Скопировать access_token из адресной строки от знака = до знака &  
  Например 
  ```
  https://oauth.vk.com/blank.html#access_token=954ce7e03ce9342ae63b6b9bb523c0a660fd57qwe42577b06b955905b45ae303c20e5828ff751137eddf&expires_in=0
  ```
  Я скопирую  
  ```
  954ce7e03ce9342ae63b6b9bb523c0a660fd57qwe42577b06b955905b45ae303c20e5828ff751137eddf
  ```
  **Вставить его в app.py в переменную access_token**

### Получение vkID
  Перейди по ссылке [ссылка](http://regvk.com/id/)   
  Вставить ссылку на свою страницу в поле
  Нажать "Определить ID"
  Скопировать ***ID пользователя***   
  **Вставить его в переменную *mID***
  
  # Утилита готова к работе!
  
  
