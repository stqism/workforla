def format_currency(n):
    """Format an integer or float as a USD currency string."""
    if isinstance(n, int):
        return '${:,.0f}'.format(n)
    elif isinstance(n, float):
        return '${:,.2f}'.format(n)
    raise TypeError('Expected int or float')
