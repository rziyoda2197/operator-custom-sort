from operator import attrgetter

class Talaba:
    def __init__(self, ism, baho):
        self.ism = ism
        self.baho = baho

talabalar = [
    Talaba("Ali", 90),
    Talaba("Vali", 80),
    Talaba("Hasan", 95),
    Talaba("Husan", 85),
]

# Baho bo'yicha saralash
talabalar.sort(key=attrgetter('baho'), reverse=True)

# Natija chiqarish
for talaba in talabalar:
    print(f"{talaba.ism}: {talaba.baho}")
```

Kodni ishlatish uchun quyidagilarni amalga oshiring:

1. `Talaba` klassini yaratib, `ism` va `baho` atributlarini kiritib, ularni ro'yxatga qo'shing.
2. `sort` metodidan foydalanib, `key` parametriga `attrgetter('baho')` ni yuboring. Bu ro'yxatni baho bo'yicha saralayadi.
3. `reverse=True` parametriga `sort` metodidan foydalanib, ro'yxatni teskari tartibda saralayadi.
4. Natija chiqarish uchun `for` tsikliga talabalar ro'yxatidan foydalaning.
