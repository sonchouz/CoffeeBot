from dataclasses import dataclass


@dataclass
class Product:
    id: int
    name: str
    description: str
    price: float


@dataclass
class Promotion:
    id: int
    title: str
    description: str
    discount_percent: int


@dataclass
class Client:
    id: int
    telegram_id: int
    name: str
    bonus_balance: int