from abc import ABC, abstractmethod


class Shakl(ABC):
    """Barcha shakllar uchun abstrakt asos."""

    @abstractmethod
    def yuza(self) -> float:
        """Shaklning yuzasi."""
        ...

    @abstractmethod
    def perimetr(self) -> float:
        """Shaklning perimetri."""
        ...

    @classmethod
    def fabrika(cls, turi: str, *args):
        """Turi bo'yicha shakl yaratadi."""
        # Quyida to'ldiramiz — circular import muammosini hal qilish uchun
        from tortburchak import Tortburchak, Kvadrat

        turi = turi.lower()
        if turi == "kvadrat":
            return Kvadrat(*args)
        if turi == "tortburchak":
            return Tortburchak(*args)
        raise ValueError(f"Noma'lum shakl turi: {turi}")

    def __str__(self):
        return f"{self.__class__.__name__}(yuza={self.yuza():.2f})"