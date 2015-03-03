subscription_service = paymill_context.get_subscription_service();
subscription_without_offer = subscription_service.create_with_amount(
    payment_id='pay_3af44644dd6d25c820a9',
    amount=4200,
    currency='EUR',
    interval='2 DAYS,MONDAY'
);
