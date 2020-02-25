import pytest
import lift.lift as lift

def test_call_lift():
    assert lift.call_lift(3, "down") == "ok"
