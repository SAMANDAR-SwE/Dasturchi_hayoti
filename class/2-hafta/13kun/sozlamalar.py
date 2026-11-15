class Sozlamalar:
    _nusxa = None

    def __new__(cls, *args, **kwargs):
        if cls._nusxa is None:
            cls._nusxa = super().__new__(cls)
        return cls._nusxa

    def __init__(self, til: str = "uz", valyuta: str = "so'm"):
        # __init__ har safar chaqiriladi — faqat birinchi marta sozlaymiz
        if not hasattr(self, "_tayyor"):
            self.til = til
            self.valyuta = valyuta
            self._tayyor = True

    def __repr__(self):
        return f"Sozlamalar(til={self.til!r}, valyuta={self.valyuta!r})"