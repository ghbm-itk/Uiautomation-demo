import os
from typing import Literal

import uiautomation as auto
from uiautomation import GroupControl, WindowControl


def main():
    os.system("calc.exe")

    calculator = auto.WindowControl(Name="Lommeregner", searchDepth=1)
    number_pad = calculator.GroupControl(AutomationId="NumberPad", searchDepth=4)
    operator_pad = calculator.GroupControl(AutomationId="StandardOperators")

    calculate("34-45*2", number_pad, operator_pad)
    print(get_result(calculator))


def calculate(equation: str, number_pad, operator_pad):
    for c in equation:
        if c.isdigit():
            click_number(number_pad, int(c))
        elif c in ("+", "-", "/", "*", "="):
            if c == '+':
                click_function_button(operator_pad, "plus")
            elif c == '-':
                click_function_button(operator_pad, "minus")
            elif c == '/':
                click_function_button(operator_pad, "divide")
            elif c == '*':
                click_function_button(operator_pad, "multiply")

    click_function_button(operator_pad, "equal")


def click_number(number_pad: GroupControl, number: int):
    automation_id = f"num{number}Button"
    number_pad.ButtonControl(AutomationId=automation_id).GetInvokePattern().Invoke(waitTime=0)


def click_function_button(operator_pad: GroupControl, button: Literal["divide", "multiply", "minus", "plus", "equal"]):
    automation_id = f"{button}Button"
    operator_pad.ButtonControl(AutomationId=automation_id).GetInvokePattern().Invoke(waitTime=0)


def get_result(calculator: WindowControl) -> str:
    return calculator.TextControl(AutomationId="CalculatorResults", searchDepth=5).PaneControl(AutomationId="TextContainer").Name


if __name__ == '__main__':
    main()
