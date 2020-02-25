import pytest
import lift.lift as lift

test_lift = lift.Lift()

def test_departing_to_floor():
    assert test_lift.current_floor == 0
    assert test_lift.current_direction is None
    assert test_lift.departing_to_floor(3) == ("ok", 0)
    assert test_lift.current_direction is "up"

def test_arriving_at_floor():
    test_lift.queue = [1,2,1,2,1,2,3,3,3]
    assert test_lift.current_direction is "up"
    assert test_lift.arriving_at_floor(3) == ("ok", 3)
    assert test_lift.queue == [1,2,1,2,1,2]
    assert test_lift.current_direction is None
    assert test_lift.arriving_at_floor(3) == ("ok", 3)

def test_call_lift():
    assert test_lift.queue == [1,2,1,2,1,2]
    assert test_lift.call_lift(3, "down") == ("ok", 3)
    assert test_lift.queue == [1,2,1,2,1,2,3]

def test_send_lift():
    assert test_lift.send_lift(0) == ("ok", 3)
    assert test_lift.queue == [1,2,1,2,1,2,3,0]
