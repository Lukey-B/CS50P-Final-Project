from project import ROR,formatted_dollar,get_input
import pytest
from unittest.mock import patch
from project import RetirementCalculator

def test_ROR():
    assert(ROR("low")) == .04
    assert(ROR("medium")) == .07
    assert(ROR("high")) == .09

def test_formatted_dollar():
    assert(formatted_dollar(1000)) == "$1,000"
    assert(formatted_dollar(10000)) == "$10,000"
    assert(formatted_dollar(100000)) == "$100,000"
    assert(formatted_dollar(1000000)) == "$1,000,000"

#please note I have a tutor who helped me implement the with patch line and mock testing in conjuction with my own research
def test_get_input():
     with patch("builtins.input", return_value= "30"):
         output = int(get_input("how old are you? ",lambda x: x.isnumeric() and int(x) >= 0, "Please enter a valid age"))
         assert output == 30


def test_getinputnegative():
     with patch("builtins.input", return_value = "-10"):
            with pytest.raises(SystemExit):
                int(get_input("how old are you? ",lambda x: x.isnumeric() and int(x) >= 0, "Please enter a valid age"))

def test_get_input_nonnumeric():
     with patch("builtins.input", return_value= "dog"):
         with pytest.raises(SystemExit):
            int(get_input("how old are you? ",lambda x: x.isnumeric() and int(x) >= 0, "Please enter a valid age"))

