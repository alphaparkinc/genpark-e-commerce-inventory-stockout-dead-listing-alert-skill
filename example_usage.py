from client import ECommerceInventoryStockoutDeadListingAlertClient

def main():
    client = ECommerceInventoryStockoutDeadListingAlertClient()
    inv = [{"channel": "Amazon FBA", "qty": 450}, {"channel": "Shopify Warehouse", "qty": 200}]
    res = client.evaluate_inventory_health(inv, 50.0)
    print(f"Days of Supply Remaining: {res['days_of_supply_remaining']} days")
    print(f"Reorder Recommendation: {res['reorder_recommendation']}")

if __name__ == "__main__":
    main()
