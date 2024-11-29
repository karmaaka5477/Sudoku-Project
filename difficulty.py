from enum import Enum


class DifficultyLevel(Enum):
    EASY = 30
    MEDIUM = 40
    HARD = 50


class Difficulty:
    difficulty = DifficultyLevel.EASY

    @classmethod
    def set_difficulty(cls, difficulty: DifficultyLevel):
        cls.difficulty = difficulty

    @classmethod
    def get_difficulty(cls):
        return cls.difficulty
