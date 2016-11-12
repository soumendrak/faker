# coding=utf-8
from __future__ import unicode_literals
from .. import Provider as PersonProvider


class Provider(PersonProvider):
    formats = (
        '{{first_name_male}} {{last_name}}',
        '{{first_name_female}} {{last_name}}',
        '{{prefix_male}} {{first_name_male}} {{last_name}}',
        '{{prefix_female}} {{first_name_female}} {{last_name}}',
    )

    # got from
    # http://uk.wikipedia.org/wiki/%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D1%96_%D1%96%D0%BC%D0%B5%D0%BD%D0%B0
    first_names_male = [
        'Аарон', 'Августин', 'Аврелій', 'Адам', 'Азар', 'Алевтин', 'Альберт', 'Амвросій', 'Андрій', 'Антон', 'Аркадій',
        'Арсен', 'Артем', 'Орхип', 'Богдан', 'Богодар', 'Богуслав', 'Болеслав', 'Борис', 'Борислав', 'Вадим',
        'Валентин', 'Валерій', 'Варфоломій', 'Василь', 'Венедикт', 'Веніямин', 'Віктор', 'Віталій', 'Владислав',
        'Володимир', 'В\'ячеслав', 'Гаврило', 'Геннадій', 'Георгій', 'Герман ', 'Гордій', 'Григорій', 'Гліб', 'Данило',
        'Давид', 'Дан', 'Демид', 'Дем\'ян', 'Дмитро', 'Захар', 'Зиновій', 'Зорян', 'Іван', 'Ігнат', 'Ігор', 'Ілля',
        'Едуард', 'Євген', 'Єлисей', 'Єфрем', 'Йосип', 'Климент',
        'Костянтин', 'Левко', 'Лесь', 'Леон', 'Леонід', 'Леонтій', 'Леопольд', 'Лук\'ян', 'Кирило', 'Макар', 'Максим',
        'Марко', 'Мартин', 'Микита', 'Миколай', 'Мирон', 'Мирослав', 'Михайло', 'Назар', 'Нестор', 'Олег', 'Олекса',
        'Олександр', 'Олесь', 'Омелян', 'Онисим', 'Опанас', 'Орест', 'Остап', 'Охрім', 'Петро', 'Павло', 'Панас',
        'Пантелеймон', 'Пармен', 'Пилип', 'Прохір', 'Роман', 'Ростислав', 'Руслан', 'Святослав', 'Семен', 'Сергій',
        'Симон', 'Соломон', 'Спас', 'Станіслав', 'Степан', 'Стефан', 'Тарас', 'Теодор', 'Тимофій', 'Трохим',
        'Устим', 'Федір', 'Феофан', 'Франц', 'Хома', 'Юстим', 'Юхим', 'Яків', 'Ярема', 'Ярослав',
    ]

    first_names_female = [
        'Ада', 'Аліна', 'Алла', 'Альбіна', 'Амалія', 'Анастасія', 'Аніта', 'Анжела', 'Ганна', 'Богуслава', 'Богданна',
        'Валентина', 'Варвара', 'Василина', 'Вікторія', 'Віолетта', 'Віра', 'Володимира', 'Галина', 'Данна', 'Дарина',
        'Едита', 'Єва', 'Єлисавета', 'Емілія', 'Еріка', 'Ірина', 'Ірена', 'Златослава', 'Камілла', 'Клавдія', 'Лариса',
        'Ліза', 'Лілія', 'Людмила', 'Любов', 'Марія', 'Марина', 'Марта', 'Мар\'яна', 'Маруся', 'Михайлина', 'Мілена',
        'Надія', 'Наталія', 'Пріска', 'Розалія', 'Святослава', 'Сніжана', 'Соломія', 'Софія', 'Одарка', 'Оксана',
        'Оксенія', 'Олена', 'Ольга', 'Орина', 'Орися', 'Роксолана', 'Світлана', 'Тереза', 'Тетяна', 'Юстина',
        'Христина', 'Ярина', 'Ярослава',
    ]

    first_names = first_names_male + first_names_female

    # Ukrainian last names are taken from
    # http://uk.wikipedia.org/wiki/%D0%9A%D0%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D1%96%D1%8F:%D0%A3%D0%BA%D1%80%D0%B0%D1%97%D0%BD%D1%81%D1%8C%D0%BA%D1%96_%D0%BF%D1%80%D1%96%D0%B7%D0%B2%D0%B8%D1%89%D0%B0
    last_names = [
        # А
        'Абрагамовський', 'Абраменко', 'Абрамчук', 'Авдєєнко', 'Аверченко', 'Авраменко', 'Аврамчук', 'Адаменко',
        'Адамчук', 'Ажажа', 'Акименко', 'Акуленко', 'Александренко', 'Алексеєнко', 'Алексійчук', 'Алексюк',
        'Андрейко', 'Андрієвич', 'Андрієнко', 'Андріїшин', 'Андрійович', 'Андрійчук', 'Андрощук', 'Андрусенко',
        'Аронець', 'Арсенич', 'Артеменко', 'Артим', 'Артимишин', 'Артимович', 'Артюх', 'Артюшенко', 'Архимович',
        'Архипенко', 'Асаула', 'Атаманчук', 'Атаманюк', 'Атрощенко',
        # Б
        'Баб\'юк', 'Баб\'як', 'Бабак', 'Бабариченко', 'Бабенко', 'Бабич', 'Бабиченко', 'Бабій', 'Бабійчук', 'Бабко',
        'Базавлученко', 'Базилевич', 'Базилевський', 'Байда', 'Байдак', 'Байрак', 'Баклан', 'Бакуменко', 'Балабан',
        'Бандера', 'Бандура', 'Бандурка', 'Барабаш', 'Баран', 'Баранець', 'Бараник', 'Баранник',
        'Батіг', 'Батуринець', 'Батюк', 'Башполченко', 'Баштан', 'Бгиденко', 'Бебешко', 'Бевз',
        'Бевзенко', 'Безбородьки', 'Безбородько', 'Бездітко',
        # В
        'Вакарчук', 'Вакуленко', 'Валенко', 'Ванченко', 'Василашко', 'Василевич', 'Василенко', 'Василечко',
        'Ватаманюк', 'Вахній', 'Ващенко', 'Ващенко-Захарченко', 'Ващук', 'Вдовенко', 'Вдовиченко',
        'Величко', 'Венгринович', 'Вергун', 'Верес', 'Верменич', 'Вернигора', 'Вернидуб', 'Вертипорох', 'Верховинець',
        'Верхола', 'Височан', 'Вишиваний', 'Вишняк', 'Вівчаренко', 'Вітер', 'Вітрук', 'Власенко', 'Власюк',
        'Влох', 'Воблий', 'Вовк',
        # Г
        'Габелко', 'Гавриленко', 'Гаврилець', 'Гаврилишин', 'Гаврилів', 'Гаврилюк', 'Гавриш', 'Гавришкевич',
        'Гаврюшенко', 'Гаєвський', 'Гайворонський', 'Гайда', 'Гайдабура', 'Гайдай', 'Гайдамака', 'Гайденко',
        'Гоголь', 'Гоголь-Яновський', 'Годунок', 'Голик', 'Голобородько', 'Гресь', 'Гречаник', 'Гречко',
        'Гриценко', 'Гузенко', 'Гузій', 'Гузь', 'Гук', 'Гунько', 'Гупало', 'Гуцуляк',
        # Ґ
        'Ґалаґан', 'Ґереґа', 'Ґерета', 'Ґерус', 'Ґжицький', 'Ґоляш',
        # Д
        'Давиденко', 'Давимука', 'Даниленко', 'Данилюк', 'Данильчук', 'Данченко', 'Данчук', 'Данькевич', 'Даньків',
        'Данько', 'Дараган', 'Дахно', 'Даценко', 'Дацюк', 'Дашенко', 'Дашкевич', 'Девдюк', 'Дейнека', 'Дейнеко',
        'Дейсун', 'Дем\'яненко', 'Дем\'янчук', 'Дем\'янюк', 'Демиденко', 'Дергач', 'Дерев\'янко',
        'Дерегус', 'Деркач', 'Деряжний', 'Джунь', 'Джус', 'Дроб\'язко', 'Дробаха', 'Дрозд', 'Дрозденко',
        'Дубас', 'Дубенко', 'Дубина', 'Дзиндра', 'Дзюба', 'Доценко', 'Дуплій', 'Дурдинець', 'Дутка',
        # Е
        'Ейбоженко',
        #
        'Євдокименко', 'Євтушенко', 'Євтушок','Ємельяненко', 'Ємець', 'Єременко', 'Єресько', 'Єрмоленко',
        'Єрошенко', 'Єрченко', 'Єрьоменко', 'Єсипенко', 'Єфименко', 'Єщенко',
        # Ж
        'Жадан', 'Жайворон', 'Жаліло', 'Жарко', 'Жук', 'Журавель', 'Журба', 'Жученко',
        # З
        'Забара', 'Забарний', 'Забашта', 'Забіла', 'Заєць', 'Заїка', 'Зайченко', 'Закусило', 'Запорожець', 'Заруба',
        'Зарудний', 'Засенко', 'Засуха', 'Засядько', 'Затовканюк', 'Затула', 'Захаренко', 'Захарченко', 'Зінкевич',
        'Зінченко', 'Зінчук', 'Зубко',
        # І
        'Іваненко', 'Іваничук', 'Іванченко', 'Івасюк', 'Іващенко', 'Ільєнко', 'Ільченко', 'Ірванець', 'Ісаєвич',
        'Ісаєнко', 'Іщак', 'Іщенко',
        # Ї
        'Їжак', 'Їжакевич',
        # К
        'Кабалюк', 'Кабаненко', 'Каденюк', 'Калениченко', 'Кальченко', 'Канівець', 'Карась', 'Кармалюк', 'Карпа',
        'Карпенко', 'Кащенко', 'Кибкало', 'Килимник', 'Кириленко', 'Коваленко', 'Ковалюк',
        'Ковпак', 'Козак', 'Козаченко', 'Колесниченко', 'Колісниченко', 'Колодуб', 'Комар', 'Конопленко', 'Конопля',
        'Копитко', 'Корбут', 'Корж', 'Короленко', 'Корпанюк', 'Корсун',
        # Л
        'Лаба', 'Лавренко', 'Лагода', 'Лазаренко', 'Левченко', 'Лемешко', 'Лесик', 'Лисенко', 'Литвин', 'Литвиненко',
        'Лубенець', 'Лукаш', 'Лупій', 'Луценко', 'Ляшко',
        # М
        'Мазепа', 'Мазур', 'Макаренко', 'Макогон', 'Малик', 'Малишко', 'Мамчур', 'Масляк', 'Масоха', 'Матвієнко',
        'Матяш', 'Медведенко', 'Микитюк', 'Михайличенко', 'Михайлюк', 'Михалюк', 'Мірошниченко', 'Міщенко', 'Москаль',
        # Н
        'Назаренко', 'Наливайко', 'Негода', 'Непорожній', 'Нестайко', 'Нестеренко', 'Ніколюк', 'Носаченко', 'Носенко',
        # О
        'Оберемко', 'Овсієнко', 'Овчаренко', 'Олійник', 'Оліфіренко', 'Онищенко', 'Оніщук', 'Онуфрієнко', 'Опанасенко',
        'Орлик', 'Оробець', 'Остапчук', 'Охримович', 'Охріменко',
        # П
        'П\'ятаченко', 'Павленко', 'Павлик', 'Павличенко', 'Палій', 'Панчук', 'Парасюк', 'Пелех', 'Перебийніс',
        'Перепелиця', 'Петлюра', 'Петренко', 'Петрик', 'Пилипенко', 'Піддубний', 'Полтавець', 'Приймак', 'Примаченко',
        'Притула', 'Приходько', 'Прокопович', 'Проценко', 'Пустовіт', 'Пушкар',
        # Р
        'Радченко', 'Рак', 'Ребрик', 'Рева', 'Редько', 'Романенко', 'Романець', 'Романчук', 'Рубан', 'Рубець', 'Рудик',
        'Рудько', 'Рябець', 'Рябовіл', 'Рябошапка', 'Рябченко',
        # С
        'Савенко', 'Сагаль', 'Саєнко', 'Салій', 'Самойленко', 'Сацюк', 'Саченко', 'Свириденко', 'Свистун', 'Семенченко',
        'Симоненко', 'Сиротенко', 'Сич', 'Сімашкевич', 'Сірко', 'Сіробаба', 'Сірченко', 'Скиба', 'Скирда', 'Скопенко',
        'Скорик', 'Скоробогатько', 'Смик', 'Слюсар', 'Сомко', 'Стельмах', 'Стець', 'Стус', 'Супруненко',
        # Т
        'Талан', 'Таран', 'Тарасенко', 'Твердохліб', 'Теличенко', 'Теліженко', 'Терещенко', 'Терещук', 'Тесленко',
        'Тесля', 'Тимченко', 'Тимчук', 'Титаренко', 'Тихий', 'Тичина', 'Ткач', 'Ткаченко', 'Товстоліс', 'Товстуха',
        'Токар', 'Тригуб', 'Туркало', 'Тягнибок',
        # У
        'Удовенко', 'Удовиченко', 'Уманець', 'Усик', 'Устенко',
        # Ф
        'Фаренюк', 'Фартушняк', 'Фастенко', 'Фесенко', 'Філіпенко', 'Фоменко', 'Франко', 'Франчук', 'Фурс',
        # Х
        'Харченко', 'Хмара', 'Хоменко', 'Хомик', 'Хорішко', 'Христенко', 'Христич', 'Худоб\'як', 'Худяк',
        # Ц
        'Царенко', 'Цибуленко', 'Цимбал', 'Цимбалюк', 'Цісик', 'Цушко', 'Цюпа', 'Цюцюра',
        # Ч
        'Чабан', 'Чайка', 'Чаленко', 'Чалий', 'Чарниш', 'Чекалюк', 'Червоненко', 'Чередник', 'Черінько', 'Черненко',
        'Чміль', 'Чорновіл', 'Чубай', 'Чуйко', 'Чумак', 'Чумаченко', 'Чуприна',
        # Ш
        'Шаблій', 'Шамрай', 'Шаповал', 'Шахрай', 'Швайка', 'Швачка', 'Швачко', 'Шведченко', 'Шеремета', 'Шевченко',
        'Шелест', 'Шеремет', 'Шило', 'Шинкаренко', 'Шиян', 'Шморгун', 'Шовкопляс', 'Штепа', 'Штокало', 'Шутько',
        'Шухевич',
        # Щ
        'Щербак', 'Щербань', 'Щириця', 'Щорс',
        # Ю
        'Юрченко', 'Юрчишин', 'Юрчук', 'Юхименко', 'Ющенко',
        # Я
        'Якименко', 'Якимчук', 'Яковенко', 'Ярема', 'Яременко', 'Яремків', 'Яремко', 'Яремчук', 'Ярош', 'Яценко',
        'Яценюк', 'Ященко', 'Ящук',
        ]

    prefixes_male = ('пан',)
    prefixes_female = ('пані',)
