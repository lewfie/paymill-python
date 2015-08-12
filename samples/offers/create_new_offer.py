offer_service = paymill_context.get_offer_service()
offer = offer_service.create(
    amount=4200,
    currency='EUR',
    interval='1 WEEK',
    'Nerd Special',
    0
)
