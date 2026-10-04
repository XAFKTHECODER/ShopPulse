import unittest

import pandas as pd

from main import calculate_metrics, clean_data, create_data


class ShopPulseTests(unittest.TestCase):
    def test_clean_data_calculates_gross_net_sales_and_month(self):
        frame = pd.DataFrame(
            {
                "Date": pd.to_datetime(["2026-01-10", "2026-02-05"]),
                "Category": ["Electronics", "Books"],
                "Quantity": [2, 1],
                "UnitPrice": [10.0, 20.0],
                "Discount": [0.10, 0.0],
            }
        )

        cleaned = clean_data(frame)

        self.assertEqual(cleaned["GrossSales"].tolist(), [20.0, 20.0])
        self.assertEqual(cleaned["NetSales"].tolist(), [18.0, 20.0])
        self.assertEqual(cleaned["Month"].astype(str).tolist(), ["2026-01", "2026-02"])

    def test_calculate_metrics_groups_sales_and_returns_totals(self):
        frame = pd.DataFrame(
            {
                "Category": ["Electronics", "Books", "Electronics"],
                "Month": pd.PeriodIndex(["2026-01", "2026-02", "2026-01"], freq="M"),
                "NetSales": [18.0, 20.0, 2.0],
            }
        )

        by_category, by_month, total_revenue, average_sale = calculate_metrics(frame)

        self.assertEqual(by_category.to_dict(), {"Books": 20.0, "Electronics": 20.0})
        self.assertEqual(
            {str(month): value for month, value in by_month.items()},
            {"2026-01": 20.0, "2026-02": 20.0},
        )
        self.assertEqual(total_revenue, 40.0)
        self.assertAlmostEqual(average_sale, 40.0 / 3)

    def test_create_data_returns_expected_transaction_shape(self):
        frame = create_data()

        self.assertEqual(len(frame), 1000)
        self.assertEqual(
            frame.columns.tolist(),
            ["Transaction_id", "Date", "Category", "Quantity", "UnitPrice", "Discount", "PaymentMethod"],
        )


if __name__ == "__main__":
    unittest.main()
