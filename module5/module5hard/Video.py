class Video:
    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False) -> None:
        self.title = title #(заголовок, строка)
        self.duration = duration #(продолжительность, секунды)
        self.time_now = time_now #(секунда остановки (изначально 0))
        self.adult_mode = adult_mode #(ограничение по возрасту, bool (False по умолчанию))

    def __contains__(self, title: str) -> bool:
        return title.lower() in self.title.lower()
    
    def __eq__(self, title: str) -> bool:
        return title == self.title
