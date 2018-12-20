from unittest.mock import Mock

from molange.event_manager import event_manager


class TestEventBus:
    def setup_method(self):
        event_manager._reset()

    def test_call_subscriber_when_event(self):
        subscriber_mock, event_mock = self._subscribe_to_event('randomevent')

        event_manager.trigger(event_mock)

        subscriber_mock.run.assert_called_once_with(event_mock)

    def test_call_correct_subscriber(self):
        subscriber_mock1, event_mock1 = self._subscribe_to_event('randomevent-1')
        subscriber_mock2, event_mock2 = self._subscribe_to_event('randomevent-2')

        event_manager.trigger(event_mock1)

        subscriber_mock2.run.assert_not_called()

    def _subscribe_to_event(self, event_name):
        event_mock = Mock()
        event_mock.name = event_name

        subscriber_mock = Mock()
        subscriber_mock.subscribe_to = [event_mock]
        event_manager.subscribe(subscriber_mock)

        return subscriber_mock, event_mock
