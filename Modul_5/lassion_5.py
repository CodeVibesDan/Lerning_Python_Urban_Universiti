import time

class User:
    """
    Атрибуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    def __init__(self, nickname, password, age):
        self.nickname = nickname # список объектов USer
        self.password =  hash(password)
        self.age = age # возраст, число

    def __str__(self):
        return f"{self.nickname} ({self.age} лет)"



class Video:
    """
    Атрибуты: title(заголовок, строка),
    duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)),
    adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    def __init__(self, title, duration, adult_mode = False):
        self.title = title # Заголовок
        self.duration = duration # продолжительность
        self.time_now = 0 # секунда остановки
        self.adult_mode = adult_mode # ограничение по возрасту 18+

    def __str__(self):
        return self.title


class UrTube:
    """
     Атрибуты: users(список объектов User),
     videos(список объектов Video),
     current_user(текущий пользователь, User)
    """
    def __init__(self):
        self.users = [] # список пользователей name
        self.videos = [] # список видео title
        self.current_user = None # текущий пользователь (по умолчанию)

    def log_in(self, nickname, password):
        """
        Метод log_in, который принимает на вход аргументы:
        nickname, password и пытается найти пользователя
        в users с такими же логином и паролем. Если такой пользователь существует,
        то current_user меняется на найденного. Помните, что password передаётся в виде строки,
        а сравнивается по хэшу.
        """
        for user in self.users:
            if user.nickname == nickname and user.password == password:
                self.current_user = user
                return True
        return False


    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента:
        nickname, password, age, и добавляет пользователя в список,
        если пользователя не существует (с таким же nickname). Если существует,
        выводит на экран: "Пользователь {nickname} уже существует".
        После регистрации, вход выполняется автоматически.
        """
        if self.log_in(nickname, password):
            print(f"Пользователь {nickname} уже существует")
        else:
            self.users.append(User(nickname, password, age))
            self.current_user = self.users[-1]
            print(f"Пользователь {str(self.users[-1])} успешно зарегистрирован.")


    def loh_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        self.current_user = None
        print("Вы вышли из аккаунта")

    def add(self, *videos):
        """
        Метод add, который принимает неограниченное кол-во
        объектов класса Video и все добавляет в videos, если с таким же
        названием видео ещё не существует. В противном случае ничего не происходит.
        """
        for video in videos:
            if str(video) not in self.videos:
                self.videos.append(video)

    def get_videos(self,  search_term):
        """
        Метод get_videos, который принимает поисковое слово и возвращает список
        названий всех видео, содержащих поисковое слово. Следует учесть, что слово 'UrbaN'
        присутствует в строке 'Urban the best' (не учитывать регистр).

            Для метода watch_video так же учитывайте следующие особенности:
        Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube.
        В противном случае выводить в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к есть
        ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        """
        result = []
        for video in self.videos:
            if search_term.lower() in video.title.lower():
                result.append(str(video))
        return result

    def watch_video(self, title):
        """Метод watch_video, который принимает название фильма, если не находит
        точного совпадения(вплоть до пробела), то ничего не воспроизводится,
        если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        """
        if self.current_user is None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    return
                for second in range(video.time_now + 1, video.duration + 1):
                    print(second, end=" ", flush=True)
                    time.sleep(1)
                print("Конец видео")
                video.time_now = 0
                return
        print("Видео не найдено")


# Код для проверки:
ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))
#
# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)
# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
