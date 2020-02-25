import pytest
import lift.lift as lift

test_lift = lift.Lift(2, None)

def test_get_current_floor():
    assert test_lift.get_current_floor() == 2

def test_deliver_to_floor():
    assert test_lift.deliver_to_floor(3) == ("ok", 3)

def test_collect_at_floor():
    assert test_lift.collect_at_floor(3) == ("ok", 3)

def test_call_lift():
    assert test_lift.call_lift(3, "down") == ("ok", 3)


