from src.inventory import get_all_products

def check_low_stock():
    """
    Functional Module 3: Reporting/Analytics.
    Checks if any product is below its threshold.
    """
    products = get_all_products()
    alerts = []
    for p in products:
        if p.quantity <= p.threshold:
            alerts.append(f"[ALERT] '{p.name}' is low! (Qty: {p.quantity})")
    return alerts