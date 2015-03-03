subscription_service = paymill_context.get_subscription_service();
subscription_with_offer_and_different_values = subscription_service.create_with_offer_id(
    payment_id='pay_3af44644dd6d25c820a9',
    offer_id='offer_bb33ea77b942f570997b',
    name='Subscription with values',
    period_of_validity='4 WEEKS',
    start_at=1409647372
);
