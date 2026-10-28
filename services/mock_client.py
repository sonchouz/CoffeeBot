from models.schemas import Product, Promotion, Client


class MockOneCClient:

    async def get_new_products(self) -> list[Product]:
        return [
            Product(
                id=1,
                name="Раф ванильный",
                description="Кофе со сливками и ванилью",
                price=250,
            ),
            Product(
                id=2,
                name="Латте карамельный",
                description="Латте с карамельным сиропом",
                price=220,
            ),
        ]

    async def get_promotions(self) -> list[Promotion]:
        return [
            Promotion(
                id=1,
                title="Скидка на кофе",
                description="Скидка 10% на выбранные напитки",
                discount_percent=10,
            ),
            Promotion(
                id=2,
                title="Утреннее предложение",
                description="Скидка 15% на кофе до 11:00",
                discount_percent=15,
            ),
        ]

    async def get_client(
        self,
        telegram_id: int,
    ) -> Client | None:
        # Тестовый клиент для проверки интерфейса
        return Client(
            id=1,
            telegram_id=telegram_id,
            name="Тестовый клиент",
            bonus_balance=350,
        )