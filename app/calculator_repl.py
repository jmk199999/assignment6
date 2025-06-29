########################
# Calculator REPL       #
########################

from decimal import Decimal
import logging

from colorama import Fore, init, Style, Back
from app.calculator import Calculator
from app.exceptions import OperationError, ValidationError
from app.operations import OperationFactory
from app.history import AutoSaveObserver, LoggingObserver

NORMAL_TEXT = Style.NORMAL + Fore.WHITE + Back.RESET
COMMAND_TEXT = Style.BRIGHT + Fore.YELLOW + Back.RESET
CMDLINE_TEXT = Style.BRIGHT + Fore.WHITE + Back.BLUE
NUMBER1_TEXT = Style.NORMAL + Fore.LIGHTBLUE_EX + Back.RESET
NUMBER2_TEXT = Style.NORMAL + Fore.LIGHTGREEN_EX + Back.RESET
NUMBER3_TEXT = Style.NORMAL + Fore.LIGHTCYAN_EX + Back.RESET
ERROR_TEXT = Style.NORMAL + Fore.LIGHTRED_EX + Back.RESET
WARNING_TEXT = Style.NORMAL + Fore.LIGHTYELLOW_EX + Back.RESET

def calculator_repl():
    """
    Command-line interface for the calculator.

    Implements a Read-Eval-Print Loop (REPL) that continuously prompts the user
    for commands, processes arithmetic operations, and manages calculation history.
    """
    try:

        # Initialize Colorama
        init()

        # Initialize the Calculator instance
        calc = Calculator()

        # Register observers for logging and auto-saving history
        calc.add_observer(LoggingObserver())
#        print(f"Auto-save: {calc.config.auto_save}")
#        if calc.config.auto_save:
#            calc.add_observer(AutoSaveObserver(calc))
        calc.add_observer(AutoSaveObserver(calc))

        print(NORMAL_TEXT+ "Calculator started.  Type '" + COMMAND_TEXT + "help" + NORMAL_TEXT + "' for commands.")

        while True:
            try:
                # Prompt the user for a command
                command = input("\n"+CMDLINE_TEXT + "Enter command:" + COMMAND_TEXT+" ").lower().strip()
                print(NORMAL_TEXT)

                if command == 'help':
                    # Display available commands
                    print("Available commands:")
                    print("  Operation commands: Will prompt for "+NUMBER1_TEXT+"first number"+ NORMAL_TEXT+" then "+NUMBER2_TEXT+"second number"+ NORMAL_TEXT+" and return the "+NUMBER3_TEXT+"result")
                    print("    "+COMMAND_TEXT+"add       " + NORMAL_TEXT + " - Adds second number to first number                     "+NUMBER1_TEXT+"2.5"+NORMAL_TEXT+" + "+NUMBER2_TEXT+"1.3"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"3.8"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"subtract  " + NORMAL_TEXT + " - Subtracts second number from first number              "+NUMBER1_TEXT+"5.7"+NORMAL_TEXT+" - "+NUMBER2_TEXT+"3.2"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"2.5"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"multiply  " + NORMAL_TEXT + " - Multiplys first number by the second number            "+NUMBER1_TEXT+"2.5"+NORMAL_TEXT+" * "+NUMBER2_TEXT+"4.1"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"10.25"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"divide    " + NORMAL_TEXT + " - Divides first number by the second number              "+NUMBER1_TEXT+"10.5"+NORMAL_TEXT+" / "+NUMBER2_TEXT+"-2"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"-5.25"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"power     " + NORMAL_TEXT + " - Raises first number to power of second number          "+NUMBER1_TEXT+"2.5"+NORMAL_TEXT+" ^ "+NUMBER2_TEXT+"3"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"15.625"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"root      " + NORMAL_TEXT + " - Get second number's root of first number               ROOT("+NUMBER1_TEXT+"56.25"+NORMAL_TEXT+" , "+NUMBER2_TEXT+"2"+NORMAL_TEXT+") = "+NUMBER3_TEXT+"7.5"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"modulus   " + NORMAL_TEXT + " - Remainder of dividing first number by second number    "+NUMBER1_TEXT+"17"+NORMAL_TEXT+" % "+NUMBER2_TEXT+"5"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"2"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"int_divide" + NORMAL_TEXT + " - Integer of dividing first number by second number      "+NUMBER1_TEXT+"17"+NORMAL_TEXT+" // "+NUMBER2_TEXT+"5"+NORMAL_TEXT+" = "+NUMBER3_TEXT+"3"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"percent   " + NORMAL_TEXT + " - Percentage of first number of second number            PERC("+NUMBER1_TEXT+"45"+NORMAL_TEXT+" , "+NUMBER2_TEXT+"900"+NORMAL_TEXT+") = "+NUMBER3_TEXT+"5"+NORMAL_TEXT)
                    print("    "+COMMAND_TEXT+"abs_diff  " + NORMAL_TEXT + " - Subtracts smaller number from larger number            ABS("+NUMBER1_TEXT+"3.2"+NORMAL_TEXT+" - "+NUMBER2_TEXT+"5.7"+NORMAL_TEXT+") = "+NUMBER3_TEXT+"2.5"+NORMAL_TEXT)
                    print("\n  Additional commands:")
                    print("    "+COMMAND_TEXT+"history   " + NORMAL_TEXT + " - Show calculation history")
                    print("    "+COMMAND_TEXT+"clear     " + NORMAL_TEXT + " - Clear calculation history")
#                    print("    "+COMMAND_TEXT+"undo      " + NORMAL_TEXT + " - Undo the last calculation")
#                    print("    "+COMMAND_TEXT+"redo      " + NORMAL_TEXT + " - Redo the last undone calculation")
                    print("    "+COMMAND_TEXT+"save      " + NORMAL_TEXT + " - Save calculation history to file")
                    print("    "+COMMAND_TEXT+"load      " + NORMAL_TEXT + " - Load calculation history from file")
                    print("    "+COMMAND_TEXT+"help      " + NORMAL_TEXT + " - Displays this help information")
                    print("    "+COMMAND_TEXT+"exit      " + NORMAL_TEXT + " - Exit the calculator")
                    continue

                if command == 'exit':
                    # Attempt to save history before exiting
                    try:
                        calc.save_history()
                        print("History saved successfully.")
                    except Exception as e:
                        print(WARNING_TEXT+ f"Warning: Could not save history: {e}")
                    print(NORMAL_TEXT+"Goodbye!")
                    break

                if command == 'history':
                    # Display calculation history
                    history = calc.show_history()
                    if not history:
                        print("No calculations in history")
                    else:
                        print("Calculation History:")
                        for i, entry in enumerate(history, 1):
                            print(f"{i}. {entry}")
                    continue

                if command == 'clear':
                    # Clear calculation history
                    calc.clear_history()
                    print("History cleared")
                    continue

                if command == 'save':
                    # Save calculation history to file
                    try:
                        calc.save_history()
                        print("History saved successfully")
                    except Exception as e:
                        print(ERROR_TEXT+ f"Error saving history: {e}")
                    continue

                if command == 'load':
                    # Load calculation history from file
                    try:
                        calc.load_history()
                        print("History loaded successfully")
                    except Exception as e:
                        print(ERROR_TEXT+ f"Error loading history: {e}")
                    continue

                if command in ['add', 'subtract', 'multiply', 'divide', 'power', 'root', 'modulus', 'int_divide', 'percent', 'abs_diff']:
                    # Perform the specified arithmetic operation
                    try:
                        print(NORMAL_TEXT+"Enter numbers (or '"+COMMAND_TEXT+"cancel"+NORMAL_TEXT+"' to abort):")
                        a = input(NORMAL_TEXT+"First number: "+NUMBER1_TEXT)
                        if a.lower() == 'cancel':
                            print(NORMAL_TEXT+"Operation cancelled")
                            continue
                        b = input(NORMAL_TEXT+"Second number: "+NUMBER2_TEXT)
                        if b.lower() == 'cancel':
                            print(NORMAL_TEXT+"Operation cancelled")
                            continue

                        # Create the appropriate operation instance using the Factory pattern
                        operation = OperationFactory.create_operation(command)
                        calc.set_operation(operation)

                        # Perform the calculation
                        result = calc.perform_operation(a, b)

                        # Normalize the result if it's a Decimal
                        if isinstance(result, Decimal):
                            result = result.normalize()
                        
                        str_result = format_value(result, calc.config.precision)
                        print(NORMAL_TEXT+"Result: "+NUMBER3_TEXT+str_result+NORMAL_TEXT)
                    except (ValidationError, OperationError) as e:
                        # Handle known exceptions related to validation or operation errors
                        print(ERROR_TEXT+ f"Error: {e}")
                    except Exception as e:
                        # Handle any unexpected exceptions
                        print(f"Unexpected error: {e}")
                    continue

                # Handle unknown commands
                print(ERROR_TEXT+"Unknown command"+NORMAL_TEXT+": '"+command+"'.  Type '"+COMMAND_TEXT+"help"+NORMAL_TEXT+"' for available commands.")

            except KeyboardInterrupt:
                # Handle Ctrl+C interruption gracefully
                print("\nOperation cancelled")
                continue
            except EOFError: # pragma: no cover
                # Handle end-of-file (e.g., Ctrl+D) gracefully
                print("\nInput terminated. Exiting...")
                break
            except Exception as e: # pragma: no cover
                # Handle any other unexpected exceptions
                print(f"Error: {e}")
                continue

    except Exception as e: # pragma: no cover
        # Handle fatal errors during initialization
        print(f"Fatal error: {e}")
        logging.error(f"Fatal error in calculator REPL: {e}")
        raise


def format_value(value: Decimal, precision: int = 10) -> str:
    """
    Format the calculation result with specified precision.

    This method formats the result to a fixed number of decimal places,
    removing any trailing zeros for a cleaner presentation.

    Args:
        precision (int, optional): Number of decimal places to show. Defaults to 10.

    Returns:
        str: Formatted string representation of the result.
    """
    try:
        # Remove trailing zeros and format to specified precision
        str_res = str(value.quantize(Decimal('0.'+ '0' * precision)))
        return str_res.rstrip('0').rstrip('.')
    except Exception:  # pragma: no cover
        return str(value)
