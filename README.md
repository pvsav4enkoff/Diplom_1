Программа учета регламентных работ и ремонта.

Данная программа предназначена для учета работ проходящих на площадках предприятий. Бригада ремонта и ТО получает задание и работает над его выполнением.

Технологии.
Python 3.9
Представление :
asgiref==3.8.1
Django==5.1.3
sqlparse==0.5.2
tzdata==2024.2

Чтобы проект работал нужно:
Установить Django: pip install django
![2024-12-19_18-51-25](https://github.com/user-attachments/assets/022b7ad7-3653-4ce1-bc98-60495474e5d2)
Импортировать openpyxl и datetime
pip install openpyxl
pip install datetime
Приложение запускается командой:
python manage.py runserver
![2024-12-19_18-59-03](https://github.com/user-attachments/assets/5de6a580-8769-43ef-9337-f521dc2d7163)
нажмите на  http://127.0.0.1:8000/ 
откроется приложение
![2024-12-19_19-03-21](https://github.com/user-attachments/assets/ff5982f6-434b-4517-8f36-c34b3721366f)
Первы пункт меню "Сотрудники"
![2024-12-19_19-06-02](https://github.com/user-attachments/assets/9c503b1d-ffa4-4120-a3c0-81aed664fecd)
У списка сотрудников есть кнопка добавить ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/6935b455-113c-43ee-9ba4-b5eb45f75976)
 нажав её вы перехродите в форму добавления
 ![2024-12-19_19-18-36](https://github.com/user-attachments/assets/4615e317-8eb0-4791-8ed0-98764d598bc5)
 при правильнро заполненной форме выйдет сообщение
![2024-12-19_19-23-29](https://github.com/user-attachments/assets/9a28388a-8192-42c9-9b55-bca64f49fcf6)
при нажатии вернуться возщвращаемся к списку
![2024-12-19_19-25-40](https://github.com/user-attachments/assets/b0e1cf87-123a-4639-ba45-f9b20cdc7423)
сотрудника можно отредактировать нажам на ![2024-12-19_19-27-08](https://github.com/user-attachments/assets/23db12b9-c1cf-4506-8f29-ad188ac84d4a)
![2024-12-19_19-40-15](https://github.com/user-attachments/assets/69563a8c-aafe-4a85-81e3-4d905d3e7177)
при изменении нажать "Сохранить"
Выйдя в главное меню нажмите "Площадки" это перечень производственных площадок на которых требуется ремонт.
![2024-12-19_19-49-00](https://github.com/user-attachments/assets/56fa0780-dd2b-4278-9aae-e0269637d65f)
нажав на кнопку ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/644bb6ec-af57-46f8-9871-b56a4be68fce) можно добавить площадку 
![2024-12-19_19-58-42](https://github.com/user-attachments/assets/39ef94d9-fbc3-442c-8cea-c0d395d1e281)
при успешном вводе выйдет сообщение
![image](https://github.com/user-attachments/assets/f98f22b7-4156-41f0-9985-833190667834)
"Вернуться" возвращяемся к списку
![2024-12-19_20-03-03](https://github.com/user-attachments/assets/6f7c36a0-1c15-42ef-ad28-56dc4c5d6902)
В главном меню нажимаем "Участки" и выходим к списку ремонтов и их исполнителей
![2024-12-19_20-07-21](https://github.com/user-attachments/assets/22f4cee0-5740-4da5-9962-dfffa823a2b4)
по кнопке ![2024-12-19_19-08-26](https://github.com/user-attachments/assets/13022891-e3f0-462e-b24a-1c24d5f703a4)
  можно добавить новый ремонт













Доступ администратора:
логин: admin
пароль: 123
