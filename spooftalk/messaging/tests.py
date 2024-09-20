
# Create your tests here.
import asyncio
from messaging.consumers import MessengerConsumer
from django.test import TransactionTestCase
from channels.testing import WebsocketCommunicator
from django.test import TestCase, Client
import time


class TimeBehaviorTest(TestCase):
    def test_message_response_time(self):
        client = Client()
        response_times = []
        total_requests = 100

        for _ in range(total_requests):
            start_time = time.time()
            response = client.get(
                '/messages/count/')
            end_time = time.time()

            response_times.append((end_time - start_time) * 1000)

        response_times.sort()
        percentile_95_time = response_times[int(
            0.95 * len(response_times)) - 1]
        print(percentile_95_time)

        self.assertTrue(percentile_95_time < 200,
                        f"95% of the requests took less than 200ms, but the 95th percentile was {percentile_95_time}ms")


class TimeBehaviorTest2(TransactionTestCase):
    async def test_message_response_time(self):
        communicator = WebsocketCommunicator(
            MessengerConsumer.as_asgi(), "/ws/messaging/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)
        response_times = []
        total_requests = 100

        for _ in range(total_requests):
            message = {'message': 'Test message'}
            start_time = time.time()
            await communicator.send_json_to(message)
            response = await communicator.receive_json_from()
            end_time = time.time()
            print(response)

            response_times.append((end_time - start_time) * 1000)

        await communicator.disconnect()

        response_times.sort()
        percentile_95_time = response_times[int(
            0.95 * len(response_times)) - 1]
        print(percentile_95_time)

        self.assertTrue(percentile_95_time < 200,
                        f"95% of the requests took less than 200ms, but the 95th percentile was {percentile_95_time}ms")


class RecoverabilityTest(TransactionTestCase):
    async def test_server_recoverability(self):
        communicator = WebsocketCommunicator(
            MessengerConsumer.as_asgi(), "/ws/messaging/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        await communicator.send_json_to({'message': 'Message before server down'})
        response = await communicator.receive_json_from()
        print(response)
        self.assertEqual(response['message'], 'Message before server down')

        await communicator.disconnect()

        await asyncio.sleep(1)

        communicator = WebsocketCommunicator(
            MessengerConsumer.as_asgi(), "/ws/messaging/")
        connected, _ = await communicator.connect()
        self.assertTrue(connected)

        await communicator.send_json_to({'message': 'Message after server up'})
        response = await communicator.receive_json_from()
        print(response)
        self.assertEqual(response['message'], 'Message after server up')

        await communicator.disconnect()
