class Calculator:
    """Простой калькулятор с делением и обработкой ошибок."""

    @staticmethod
    def add(a: float, b: float) -> float:
        """Сложение."""
        return a + b

    @staticmethod
    def subtract(a: float, b: float) -> float:
        """Вычитание."""
        return a - b

    @staticmethod
    def multiply(a: float, b: float) -> float:
        """Умножение."""
        return a * b

    @staticmethod
    def divide(a: float, b: float) -> float:
        """Деление. При делении на 0 возвращает None."""
        if b == 0:
            return None
        return a / b

    @staticmethod
    def power(a: float, b: int) -> float:
        """Возведение в степень. Работает только с целыми показателями."""
        if not isinstance(b, int):
            raise TypeError("Степень должна быть целым числом")
        return a**b
