# Test REPL Commands (using patches for input/output handling)

from unittest.mock import patch

from app.calculator_repl import COMMAND_TEXT, ERROR_TEXT, WARNING_TEXT, calculator_repl, NORMAL_TEXT, NUMBER1_TEXT, NUMBER2_TEXT, NUMBER3_TEXT


@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        calculator_repl()
        mock_save_history.assert_called_once()
        mock_print.assert_any_call("History saved successfully.")
        mock_print.assert_any_call(NORMAL_TEXT+"Goodbye!")

@patch('builtins.input', side_effect=['exit'])
@patch('builtins.print')
def test_calculator_repl_exit_history_failure(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        simulated_error_message = "Simulated disk full error during save."
        mock_save_history.side_effect = IOError(simulated_error_message)
        calculator_repl()
        mock_save_history.assert_called_once()
        mock_print.assert_any_call(WARNING_TEXT+ f"Warning: Could not save history: Simulated disk full error during save.")

@patch('builtins.input', side_effect=['clear', 'exit'])
@patch('builtins.print')
def test_calculator_repl_clear(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("History cleared")

@patch('builtins.input', side_effect=['history', 'exit'])
@patch('builtins.print')
def test_calculator_repl_no_history(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("No calculations in history")

@patch('builtins.input', side_effect=['undo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_no_undo(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Nothing to undo")

@patch('builtins.input', side_effect=['redo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_no_redo(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Nothing to redo")

@patch('builtins.input', side_effect=['multiply', '10', '5', 'undo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_undo(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Operation undone")

@patch('builtins.input', side_effect=['divide', '10', '5', 'undo', 'redo', 'exit'])
@patch('builtins.print')
def test_calculator_repl_redo(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Operation redone")

@patch('builtins.input', side_effect=['add', '2', '3', 'history', 'exit'])
@patch('builtins.print')
def test_calculator_repl_history(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("Calculation History:")

@patch('builtins.input', side_effect=['save', 'exit'])
@patch('builtins.print')
def test_calculator_repl_save(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("History saved successfully")

@patch('builtins.input', side_effect=['save', 'exit'])
@patch('builtins.print')
def test_calculator_repl_save_history_failure(mock_print, mock_input):
    with patch('app.calculator.Calculator.save_history') as mock_save_history:
        simulated_error_message = "Simulated disk full error during save."
        mock_save_history.side_effect = IOError(simulated_error_message)
        calculator_repl()
        #mock_save_history.assert_called_once()
        mock_print.assert_any_call(WARNING_TEXT+ f"Warning: Could not save history: Simulated disk full error during save.")


@patch('builtins.input', side_effect=['load', 'exit'])
@patch('builtins.print')
def test_calculator_repl_load(mock_print, mock_input):
    calculator_repl()
    mock_print.assert_any_call("History loaded successfully")


@patch('builtins.input', side_effect=['load', 'exit'])
@patch('builtins.print')
def test_calculator_repl_load_history_failure(mock_print, mock_input):
    with patch('app.calculator.Calculator.load_history') as mock_load_history:
        simulated_error_message = "Simulated disk full error during load."
        mock_load_history.side_effect = IOError(simulated_error_message)
        calculator_repl()
        #mock_load_history.assert_called_once()
        mock_print.assert_any_call(ERROR_TEXT+ "Error loading history: Simulated disk full error during load.")


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
    mock_print.assert_any_call(ERROR_TEXT+"Error: Invalid number format: two")

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
    mock_print.assert_any_call(ERROR_TEXT+"Unknown command"+NORMAL_TEXT+": 'and'.  Type '"+COMMAND_TEXT+"help"+NORMAL_TEXT+"' for available commands.")

@patch('builtins.input', side_effect=['subtract', '5', '5', 'exit'])
@patch('builtins.print')
def test_calculator_repl_interrupt(mock_print, mock_input):
    with patch('app.calculator.Calculator.perform_operation') as mock_perform_oper:
        mock_perform_oper.side_effect = KeyboardInterrupt()
        calculator_repl()
        #mock_perform_oper.assert_called_once()
        mock_print.assert_any_call("\nOperation cancelled")

