# Test memento to_dict and from_dict methods

from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.calculator_memento import CalculatorMemento
from app.operations import OperationFactory


def test_memento_to_from_dic():
    # Create a calculator
    config = CalculatorConfig()
    calc = Calculator(config)

    # Make sure it's empty
    calc.clear_history()
    assert len(calc.history) == 0

    # Add an operation to the history and confirm there is one item.
    operation = OperationFactory.create_operation('add')
    calc.set_operation(operation)
    result = calc.perform_operation(2, 3)
    assert len(calc.history) == 1

    # Create a Memento from the one history item
    mem = CalculatorMemento(calc.history.copy())

    # Convert back and forth then compare the history before and after.
    data = mem.to_dict()
    back = CalculatorMemento.from_dict(data)
    assert back.history == calc.history