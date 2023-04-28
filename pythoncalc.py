def accumulated_amount(principal: float, rate: float, n: int, time: int) -> float:
    """Calculate the accumulated amount using the given formula.

    principal = the initial amount
    rate = the interest rate as a decimal
    n = the number of times that interest is compounded per time period
    time = the number of time periods
    """
    amount = principal * (1 + rate / n) ** (n * time)
    return amount

print("",accumulated_amount(1234))
 


