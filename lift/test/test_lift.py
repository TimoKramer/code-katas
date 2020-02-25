import pytest
import lift.lift as lift

test_lift = lift.Lift()

def test_deliver_to_floor():
    assert test_lift.current_floor == 0
    assert test_lift.current_direction is None
    assert test_lift.deliver_to_floor(3) == ("ok", 3)

def test_collect_at_floor():
    assert test_lift.collect_at_floor(3) == ("ok", 3)

def test_call_lift():
    assert test_lift.queue == []
    assert test_lift.call_lift(3, "down") == ("ok", 3)
    assert test_lift.queue == [3]

def test_send_lift():
    assert test_lift.send_lift(0) == ("ok", 3)
    assert test_lift.queue == [3, 0]
