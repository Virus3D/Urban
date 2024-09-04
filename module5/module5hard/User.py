class User:
    def __init__(self, nickname: str, password: str, age: int) -> None:
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        
    def __str__(self) -> str:
        return self.nickname