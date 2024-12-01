class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.time = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2
        self.time += 1

    def walk(self):
        self.distance += self.speed
        self.time += 1

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name

    def __hash__(self):
        return hash(self.name)  # Использование имени для хэширования


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[participant] = (participant.time, participant.distance)
                    self.participants.remove(participant)

        # Сортируем по времени (по расстоянию в случае равенства)
        sorted_finishers = sorted(finishers.items(), key=lambda item: (item[1][0], -item[1][1]))
        # Возвращаем отсортированные результаты с местами
        return {place + 1: runner for place, (runner, _) in enumerate(sorted_finishers)}
