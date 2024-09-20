from django.test import TestCase

# Create your tests here.
from django.test import TestCase, Client
import time

class TimeBehaviorTest(TestCase):
    def test_message_response_time(self):
        client = Client()
        response_times = []
        total_requests = 100  # Test with 100 requests

        for _ in range(total_requests):
            start_time = time.time()
            response = client.post('/your-chat-endpoint/', {'message': 'Test message'})
            end_time = time.time()

            response_times.append((end_time - start_time) * 1000)  # Convert to milliseconds

        # Sort times to get the 95th percentile
        response_times.sort()
        percentile_95_time = response_times[int(0.95 * len(response_times)) - 1]

        # Assert that the 95th percentile time is under 200ms
        self.assertTrue(percentile_95_time < 200, f"95% of the requests took less than 200ms, but the 95th percentile was {percentile_95_time}ms")
