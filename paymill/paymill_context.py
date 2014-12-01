# coding=utf-8
__author__ = 'yalnazov'
import paymill.utils.http_client
import paymill.services.client_service
import paymill.services.offer_service
import paymill.services.payment_service
import paymill.services.preauthorization_service
import paymill.services.refund_service
import paymill.services.subscription_service
import paymill.services.transaction_service
import paymill.services.webhook_service


class PaymillContext(object):

    """Entry point for PAYMILL API.
       Use the getter methods in order to access the required PAYMILL service.
    """

    def __init__(self, api_key):
        """
        :param str api_key: your PAYMILL private key
        :rtype : PaymillContext
        """
        self.api_url = 'https://api.paymill.com/v2.1'
        self.api_key = api_key
        self.http_client = paymill.utils.http_client.HTTPClient(self.api_url, api_key, "")
        self.client_service = paymill.services.client_service.ClientService(self.http_client)
        self.offer_service = paymill.services.offer_service.OfferService(self.http_client)
        self.payment_service = paymill.services.payment_service.PaymentService(self.http_client)
        self.preauthorization_service = paymill.services.preauthorization_service.PreauthorizationService(self.http_client)
        self.refund_service = paymill.services.refund_service.RefundService(self.http_client)
        self.subscription_service = paymill.services.subscription_service.SubscriptionService(self.http_client)
        self.transaction_service = paymill.services.transaction_service.TransactionService(self.http_client)
        self.webhook_service = paymill.services.webhook_service.WebhookService(self.http_client)

    """Getter methods for each PAYMILL service."""

    def get_client_service(self):
        return self.client_service

    def get_offer_service(self):
        return self.offer_service

    def get_payment_service(self):
        return self.payment_service

    def get_preauthorization_service(self):
        return self.preauthorization_service

    def get_refund_service(self):
        return self.refund_service

    def get_subscription_service(self):
        return self.subscription_service

    def get_transaction_service(self):
        return self.transaction_service

    def get_webhook_service(self):
        return self.webhook_service