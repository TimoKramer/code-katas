import pytest
import lift.lift as lift


def test_get_current_floor():
    test_lift = lift.Lift(2)
    assert test_lift.get_current_floor() == 2

def test_deliver_to_floor():
    test_lift = lift.Lift(2)
    assert test_lift.deliver_to_floor(3) == ("ok", 2)

def test_call_lift():
    test_lift = lift.Lift(2)
    assert test_lift.call_lift(3, "down") == ("ok", 2)


