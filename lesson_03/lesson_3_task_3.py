from address import Address
from mailing import Mailing

sender = Address("101000", "Москва", "Арбат", "32", "1")
recipient = Address("445000", "Тольятти", "Кудашева", "108", "45")

mail = Mailing(
    from_address=sender,
    to_address=recipient,
    cost=100,
    track="MSK123"
)

print(
    f"Отправление {mail.track} из {mail.from_address.index}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.index}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)
