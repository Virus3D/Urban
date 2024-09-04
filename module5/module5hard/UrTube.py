from User import User
from Video import Video
import time

class UrTube:
    users = [] #(список объектов User) 
    videos = [] #(список объектов Video)
    current_user = None #(текущий пользователь, User)

    def log_in(self, nickname: str, password: str) -> None:
        for user in self.users:
            if user.nickname == nickname and user.password == hash(password):
                self.current_user = user

    def register(self, nickname: str, password: str, age:int) -> None:
        for user in self.users:
            if user.nickname == nickname:
                print(f"Пользователь {nickname} уже существует")
                return
        self.users.append(user := User(nickname, password, age))
        self.current_user = user

    def log_out(self) -> None:
        self.current_user = None

    def add(self, *videos: Video) -> None:
        for new_video in videos:
            found = False
            for video in self.videos:
                if new_video.title == video.title:
                    found = True
            if not found:
                self.videos.append(new_video)

    def get_videos(self, string: str) -> list:
        list_video = []
        for video in self.videos:
            if string in video:
                list_video.append(video.title)
        return list_video

    def watch_video(self, title: str) -> None:
        if self.current_user == None:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        
        found = False
        for video in self.videos:
            if title == video:
                found = video
        if found == False:
            return

        if video.adult_mode and self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return

        for video.time_now in range(1, video.duration + 1):
            time.sleep(1)
            print(video.time_now, end = ' ', flush=True)

        time.sleep(1)
        video.time_now = 0
        print("Конец видео")
        time.sleep(1)
        
