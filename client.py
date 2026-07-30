class ECommerceInventoryStockoutDeadListingAlertClient:
    def evaluate_inventory_health(self, channel_inventory: list, sales_velocity_daily: float = 45.0) -> dict:
        total_units = sum(item.get("qty", 0) for item in channel_inventory)
        dos = round(total_units / max(sales_velocity_daily, 1.0), 1)
        return {
            "days_of_supply_remaining": dos,
            "reorder_recommendation": {
                "units_to_order": 1500 if dos < 30 else 0,
                "urgency": "HIGH_STOCKOUT_RISK" if dos < 14 else "NORMAL"
            },
            "suppressed_listings": []
        }
