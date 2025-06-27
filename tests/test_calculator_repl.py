# Test REPL Commands (using patches for input/output handling)

from unittest.mock import patch

from app.calculator_repl import calculator_repl, NORMAL_TEXT, NUMBER1_TEXT, NUMBER2_TEXT, NUMBER3_TEXT


@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit(mock_print, mock_input):
        calculator_repl()
        mock_print.assert_any_call(NORMAL_TEXT+"Goodbye!")


@patch('builtins.input', side_effect=['help', 'exit'])
@patch('builtins.print')
def test_calculator_repl_help(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Available commands:")


@patch('builtins.input', side_effect=['add', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_addition(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "5"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['subtract', '10', '5', 'exit'])
@patch('builtins.print')
def test_calculator_repl_subtraction(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "5"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['multiply', '2', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_multiplication(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "6"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['divide', '10', '4', 'exit'])
@patch('builtins.print')
def test_calculator_repl_division(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "2.5"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['power', '10', '4', 'exit'])
@patch('builtins.print')
def test_calculator_repl_power(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "10000"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['root', '8', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_root(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "2"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['modulus', '8', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_modulus(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "2"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['int_divide', '8', '3', 'exit'])
@patch('builtins.print')
def test_calculator_repl_int_divide(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "2"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['percent', '2', '10', 'exit'])
@patch('builtins.print')
def test_calculator_repl_percent(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "20"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['abs_diff', '3', '8', 'exit'])
@patch('builtins.print')
def test_calculator_repl_abs_diff(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+ "5"+NORMAL_TEXT)


@patch('builtins.input', side_effect=['add', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_cancel_first_number(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Operation cancelled")

@patch('builtins.input', side_effect=['add', '5', 'cancel', 'exit'])
@patch('builtins.print')
def test_calculator_repl_cancel_second_number(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call(NORMAL_TEXT+"Operation cancelled")

@patch('builtins.input', side_effect=['add', '5', 'two', 'exit'])
@patch('builtins.print')
def test_calculator_repl_validation_error(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Error: Invalid number format: two")

@patch('builtins.input', side_effect=['subtract', '5', '5', 'exit'])
@patch('builtins.print')
def test_calculator_repl_unexpected_error(mock_print, mock_input):
    with patch('app.calculator.Calculator.perform_operation') as mock_perform_oper:
        simulated_error_message = "Simulated disk full error during load."
        mock_perform_oper.side_effect = IOError(simulated_error_message)
        calculator_repl()
        #mock_perform_oper.assert_called_once()
        mock_print.assert_any_call("Unexpected error: Simulated disk full error during load.")

@patch('builtins.input', side_effect=['and', 'exit'])
@patch('builtins.print')
def test_calculator_repl_unknown_command(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Unknown command: 'and'. Type 'help' for available commands.")

@patch('builtins.input', side_effect=['subtract', '5', '5', 'exit'])
@patch('builtins.print')
def test_calculator_repl_interrupt(mock_print, mock_input):
    with patch('app.calculator.Calculator.perform_operation') as mock_perform_oper:
        mock_perform_oper.side_effect = KeyboardInterrupt()
        calculator_repl()
        #mock_perform_oper.assert_called_once()
        mock_print.assert_any_call("\nOperation cancelled")

