import json
import csv
from datetime import datetime, timedelta

# Datos JSON
json_data = {
  "producto_sugerir": {
    "id": 4,
    "name": "Cheese Burger",
    "default_code": False,
    "list_price": 13.0,
    "standard_price": 11.7,
    "categ_id": "Saleable",
    "barcode": False,
    "type": "consu",
    "uom": "Unidades",
    "active": True,
    "description": ""
  },
  "ventas_filtradas": [
    {
      "order_id": 1,
      "cliente": "UserA",
      "fecha": "2025-01-01",
      "total_orden": 41.65,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 5,
      "price_unit": 8.33,
      "subtotal": 41.65
    },
    {
      "order_id": 2,
      "cliente": "UserA",
      "fecha": "2025-01-02",
      "total_orden": 95.25,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 19.05,
      "subtotal": 95.25
    },
    {
      "order_id": 3,
      "cliente": "UserA",
      "fecha": "2025-01-03",
      "total_orden": 54.48,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 13.62,
      "subtotal": 54.48
    },
    {
      "order_id": 4,
      "cliente": "UserA",
      "fecha": "2025-01-04",
      "total_orden": 75.35,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 15.07,
      "subtotal": 75.35
    },
    {
      "order_id": 5,
      "cliente": "UserA",
      "fecha": "2025-01-05",
      "total_orden": 36.52,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 18.26,
      "subtotal": 36.52
    },
    {
      "order_id": 6,
      "cliente": "UserC",
      "fecha": "2025-01-06",
      "total_orden": 32.97,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 10.99,
      "subtotal": 32.97
    },
    {
      "order_id": 7,
      "cliente": "UserC",
      "fecha": "2025-01-07",
      "total_orden": 36.16,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 9.04,
      "subtotal": 36.16
    },
    {
      "order_id": 8,
      "cliente": "UserD",
      "fecha": "2025-01-08",
      "total_orden": 55.5,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 18.5,
      "subtotal": 55.5
    },
    {
      "order_id": 9,
      "cliente": "UserB",
      "fecha": "2025-01-09",
      "total_orden": 67.05,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 13.41,
      "subtotal": 67.05
    },
    {
      "order_id": 10,
      "cliente": "UserD",
      "fecha": "2025-01-10",
      "total_orden": 79.25,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 15.85,
      "subtotal": 79.25
    },
    {
      "order_id": 11,
      "cliente": "UserB",
      "fecha": "2025-01-11",
      "total_orden": 8.77,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 1,
      "price_unit": 8.77,
      "subtotal": 8.77
    },
    {
      "order_id": 12,
      "cliente": "UserE",
      "fecha": "2025-01-12",
      "total_orden": 38.55,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 12.85,
      "subtotal": 38.55
    },
    {
      "order_id": 13,
      "cliente": "UserB",
      "fecha": "2025-01-13",
      "total_orden": 92.5,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 18.5,
      "subtotal": 92.5
    },
    {
      "order_id": 14,
      "cliente": "UserA",
      "fecha": "2025-01-14",
      "total_orden": 15.17,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 15.17,
      "subtotal": 15.17
    },
    {
      "order_id": 15,
      "cliente": "UserC",
      "fecha": "2025-01-15",
      "total_orden": 57.24,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 19.08,
      "subtotal": 57.24
    },
    {
      "order_id": 16,
      "cliente": "UserD",
      "fecha": "2025-01-16",
      "total_orden": 49.59,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 16.53,
      "subtotal": 49.59
    },
    {
      "order_id": 17,
      "cliente": "UserB",
      "fecha": "2025-01-17",
      "total_orden": 45.93,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 15.31,
      "subtotal": 45.93
    },
    {
      "order_id": 18,
      "cliente": "UserC",
      "fecha": "2025-01-18",
      "total_orden": 15.99,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 1,
      "price_unit": 15.99,
      "subtotal": 15.99
    },
    {
      "order_id": 19,
      "cliente": "UserB",
      "fecha": "2025-01-19",
      "total_orden": 26.28,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 13.14,
      "subtotal": 26.28
    },
    {
      "order_id": 20,
      "cliente": "UserC",
      "fecha": "2025-01-20",
      "total_orden": 62.2,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 15.55,
      "subtotal": 62.2
    },
    {
      "order_id": 21,
      "cliente": "UserC",
      "fecha": "2025-01-21",
      "total_orden": 8.16,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 8.16,
      "subtotal": 8.16
    },
    {
      "order_id": 22,
      "cliente": "UserC",
      "fecha": "2025-01-22",
      "total_orden": 23.3,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 11.65,
      "subtotal": 23.3
    },
    {
      "order_id": 23,
      "cliente": "UserE",
      "fecha": "2025-01-23",
      "total_orden": 67.1,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 13.42,
      "subtotal": 67.1
    },
    {
      "order_id": 24,
      "cliente": "UserD",
      "fecha": "2025-01-24",
      "total_orden": 19.44,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 1,
      "price_unit": 19.44,
      "subtotal": 19.44
    },
    {
      "order_id": 25,
      "cliente": "UserE",
      "fecha": "2025-01-25",
      "total_orden": 19.45,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 1,
      "price_unit": 19.45,
      "subtotal": 19.45
    },
    {
      "order_id": 26,
      "cliente": "UserD",
      "fecha": "2025-01-26",
      "total_orden": 73.65,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 5,
      "price_unit": 14.73,
      "subtotal": 73.65
    },
    {
      "order_id": 27,
      "cliente": "UserB",
      "fecha": "2025-01-27",
      "total_orden": 22.58,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 11.29,
      "subtotal": 22.58
    },
    {
      "order_id": 28,
      "cliente": "UserB",
      "fecha": "2025-01-28",
      "total_orden": 39.2,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 2,
      "price_unit": 19.6,
      "subtotal": 39.2
    },
    {
      "order_id": 29,
      "cliente": "UserD",
      "fecha": "2025-01-29",
      "total_orden": 31.28,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 15.64,
      "subtotal": 31.28
    },
    {
      "order_id": 30,
      "cliente": "UserC",
      "fecha": "2025-01-30",
      "total_orden": 85.1,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 17.02,
      "subtotal": 85.1
    },
    {
      "order_id": 31,
      "cliente": "UserD",
      "fecha": "2025-01-31",
      "total_orden": 48.0,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 9.6,
      "subtotal": 48.0
    },
    {
      "order_id": 32,
      "cliente": "UserE",
      "fecha": "2025-02-01",
      "total_orden": 55.2,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 18.4,
      "subtotal": 55.2
    },
    {
      "order_id": 33,
      "cliente": "UserD",
      "fecha": "2025-02-02",
      "total_orden": 33.06,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 16.53,
      "subtotal": 33.06
    },
    {
      "order_id": 34,
      "cliente": "UserD",
      "fecha": "2025-02-03",
      "total_orden": 51.52,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 12.88,
      "subtotal": 51.52
    },
    {
      "order_id": 35,
      "cliente": "UserA",
      "fecha": "2025-02-04",
      "total_orden": 63.0,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 4,
      "price_unit": 15.75,
      "subtotal": 63.0
    },
    {
      "order_id": 36,
      "cliente": "UserE",
      "fecha": "2025-02-05",
      "total_orden": 43.72,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 10.93,
      "subtotal": 43.72
    },
    {
      "order_id": 37,
      "cliente": "UserE",
      "fecha": "2025-02-06",
      "total_orden": 30.3,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 3,
      "price_unit": 10.1,
      "subtotal": 30.3
    },
    {
      "order_id": 38,
      "cliente": "UserC",
      "fecha": "2025-02-07",
      "total_orden": 20.32,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 10.16,
      "subtotal": 20.32
    },
    {
      "order_id": 39,
      "cliente": "UserC",
      "fecha": "2025-02-08",
      "total_orden": 76.04,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 19.01,
      "subtotal": 76.04
    },
    {
      "order_id": 40,
      "cliente": "UserB",
      "fecha": "2025-02-09",
      "total_orden": 46.2,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 15.4,
      "subtotal": 46.2
    },
    {
      "order_id": 41,
      "cliente": "UserC",
      "fecha": "2025-02-10",
      "total_orden": 26.36,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 13.18,
      "subtotal": 26.36
    },
    {
      "order_id": 42,
      "cliente": "UserE",
      "fecha": "2025-02-11",
      "total_orden": 39.58,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 19.79,
      "subtotal": 39.58
    },
    {
      "order_id": 43,
      "cliente": "UserB",
      "fecha": "2025-02-12",
      "total_orden": 70.7,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 5,
      "price_unit": 14.14,
      "subtotal": 70.7
    },
    {
      "order_id": 44,
      "cliente": "UserB",
      "fecha": "2025-02-13",
      "total_orden": 90.5,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 5,
      "price_unit": 18.1,
      "subtotal": 90.5
    },
    {
      "order_id": 45,
      "cliente": "UserA",
      "fecha": "2025-02-14",
      "total_orden": 53.25,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 17.75,
      "subtotal": 53.25
    },
    {
      "order_id": 46,
      "cliente": "UserC",
      "fecha": "2025-02-15",
      "total_orden": 30.98,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 15.49,
      "subtotal": 30.98
    },
    {
      "order_id": 47,
      "cliente": "UserA",
      "fecha": "2025-02-16",
      "total_orden": 70.0,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 14.0,
      "subtotal": 70.0
    },
    {
      "order_id": 48,
      "cliente": "UserB",
      "fecha": "2025-02-17",
      "total_orden": 31.59,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 10.53,
      "subtotal": 31.59
    },
    {
      "order_id": 49,
      "cliente": "UserD",
      "fecha": "2025-02-18",
      "total_orden": 13.07,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 1,
      "price_unit": 13.07,
      "subtotal": 13.07
    },
    {
      "order_id": 50,
      "cliente": "UserD",
      "fecha": "2025-02-19",
      "total_orden": 89.4,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 17.88,
      "subtotal": 89.4
    },
    {
      "order_id": 51,
      "cliente": "UserE",
      "fecha": "2025-02-20",
      "total_orden": 68.05,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 13.61,
      "subtotal": 68.05
    },
    {
      "order_id": 52,
      "cliente": "UserD",
      "fecha": "2025-02-21",
      "total_orden": 35.16,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 17.58,
      "subtotal": 35.16
    },
    {
      "order_id": 53,
      "cliente": "UserB",
      "fecha": "2025-02-22",
      "total_orden": 31.56,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 10.52,
      "subtotal": 31.56
    },
    {
      "order_id": 54,
      "cliente": "UserD",
      "fecha": "2025-02-23",
      "total_orden": 36.5,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 18.25,
      "subtotal": 36.5
    },
    {
      "order_id": 55,
      "cliente": "UserD",
      "fecha": "2025-02-24",
      "total_orden": 15.59,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 1,
      "price_unit": 15.59,
      "subtotal": 15.59
    },
    {
      "order_id": 56,
      "cliente": "UserA",
      "fecha": "2025-02-25",
      "total_orden": 34.98,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 11.66,
      "subtotal": 34.98
    },
    {
      "order_id": 57,
      "cliente": "UserC",
      "fecha": "2025-02-26",
      "total_orden": 36.33,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 12.11,
      "subtotal": 36.33
    },
    {
      "order_id": 58,
      "cliente": "UserC",
      "fecha": "2025-02-27",
      "total_orden": 16.4,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 16.4,
      "subtotal": 16.4
    },
    {
      "order_id": 59,
      "cliente": "UserE",
      "fecha": "2025-02-28",
      "total_orden": 14.07,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 1,
      "price_unit": 14.07,
      "subtotal": 14.07
    },
    {
      "order_id": 60,
      "cliente": "UserC",
      "fecha": "2025-03-01",
      "total_orden": 29.68,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 14.84,
      "subtotal": 29.68
    },
    {
      "order_id": 61,
      "cliente": "UserB",
      "fecha": "2025-03-02",
      "total_orden": 18.45,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 1,
      "price_unit": 18.45,
      "subtotal": 18.45
    },
    {
      "order_id": 62,
      "cliente": "UserC",
      "fecha": "2025-03-03",
      "total_orden": 9.4,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 1,
      "price_unit": 9.4,
      "subtotal": 9.4
    },
    {
      "order_id": 63,
      "cliente": "UserB",
      "fecha": "2025-03-04",
      "total_orden": 27.81,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 9.27,
      "subtotal": 27.81
    },
    {
      "order_id": 64,
      "cliente": "UserE",
      "fecha": "2025-03-05",
      "total_orden": 54.32,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 13.58,
      "subtotal": 54.32
    },
    {
      "order_id": 65,
      "cliente": "UserB",
      "fecha": "2025-03-06",
      "total_orden": 33.6,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 8.4,
      "subtotal": 33.6
    },
    {
      "order_id": 66,
      "cliente": "UserE",
      "fecha": "2025-03-07",
      "total_orden": 71.44,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 4,
      "price_unit": 17.86,
      "subtotal": 71.44
    },
    {
      "order_id": 67,
      "cliente": "UserC",
      "fecha": "2025-03-08",
      "total_orden": 40.8,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 5,
      "price_unit": 8.16,
      "subtotal": 40.8
    },
    {
      "order_id": 68,
      "cliente": "UserB",
      "fecha": "2025-03-09",
      "total_orden": 35.61,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 3,
      "price_unit": 11.87,
      "subtotal": 35.61
    },
    {
      "order_id": 69,
      "cliente": "UserC",
      "fecha": "2025-03-10",
      "total_orden": 27.26,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 13.63,
      "subtotal": 27.26
    },
    {
      "order_id": 70,
      "cliente": "UserE",
      "fecha": "2025-03-11",
      "total_orden": 46.92,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 15.64,
      "subtotal": 46.92
    },
    {
      "order_id": 71,
      "cliente": "UserE",
      "fecha": "2025-03-12",
      "total_orden": 16.58,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 8.29,
      "subtotal": 16.58
    },
    {
      "order_id": 72,
      "cliente": "UserA",
      "fecha": "2025-03-13",
      "total_orden": 17.44,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 8.72,
      "subtotal": 17.44
    },
    {
      "order_id": 73,
      "cliente": "UserE",
      "fecha": "2025-03-14",
      "total_orden": 46.45,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 9.29,
      "subtotal": 46.45
    },
    {
      "order_id": 74,
      "cliente": "UserD",
      "fecha": "2025-03-15",
      "total_orden": 49.83,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 16.61,
      "subtotal": 49.83
    },
    {
      "order_id": 75,
      "cliente": "UserA",
      "fecha": "2025-03-16",
      "total_orden": 77.76,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 19.44,
      "subtotal": 77.76
    },
    {
      "order_id": 76,
      "cliente": "UserB",
      "fecha": "2025-03-17",
      "total_orden": 33.84,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 11.28,
      "subtotal": 33.84
    },
    {
      "order_id": 77,
      "cliente": "UserA",
      "fecha": "2025-03-18",
      "total_orden": 36.22,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 2,
      "price_unit": 18.11,
      "subtotal": 36.22
    },
    {
      "order_id": 78,
      "cliente": "UserD",
      "fecha": "2025-03-19",
      "total_orden": 40.56,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 10.14,
      "subtotal": 40.56
    },
    {
      "order_id": 79,
      "cliente": "UserC",
      "fecha": "2025-03-20",
      "total_orden": 19.96,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 19.96,
      "subtotal": 19.96
    },
    {
      "order_id": 80,
      "cliente": "UserD",
      "fecha": "2025-03-21",
      "total_orden": 95.65,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 19.13,
      "subtotal": 95.65
    },
    {
      "order_id": 81,
      "cliente": "UserA",
      "fecha": "2025-03-22",
      "total_orden": 29.34,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 14.67,
      "subtotal": 29.34
    },
    {
      "order_id": 82,
      "cliente": "UserC",
      "fecha": "2025-03-23",
      "total_orden": 17.03,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 1,
      "price_unit": 17.03,
      "subtotal": 17.03
    },
    {
      "order_id": 83,
      "cliente": "UserE",
      "fecha": "2025-03-24",
      "total_orden": 18.14,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 9.07,
      "subtotal": 18.14
    },
    {
      "order_id": 84,
      "cliente": "UserD",
      "fecha": "2025-03-25",
      "total_orden": 27.03,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 9.01,
      "subtotal": 27.03
    },
    {
      "order_id": 85,
      "cliente": "UserB",
      "fecha": "2025-03-26",
      "total_orden": 45.48,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 15.16,
      "subtotal": 45.48
    },
    {
      "order_id": 86,
      "cliente": "UserE",
      "fecha": "2025-03-27",
      "total_orden": 26.94,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 8.98,
      "subtotal": 26.94
    },
    {
      "order_id": 87,
      "cliente": "UserE",
      "fecha": "2025-03-28",
      "total_orden": 8.4,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 8.4,
      "subtotal": 8.4
    },
    {
      "order_id": 88,
      "cliente": "UserE",
      "fecha": "2025-03-29",
      "total_orden": 35.78,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 2,
      "price_unit": 17.89,
      "subtotal": 35.78
    },
    {
      "order_id": 89,
      "cliente": "UserC",
      "fecha": "2025-03-30",
      "total_orden": 37.52,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 9.38,
      "subtotal": 37.52
    },
    {
      "order_id": 90,
      "cliente": "UserD",
      "fecha": "2025-03-31",
      "total_orden": 55.84,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 13.96,
      "subtotal": 55.84
    },
    {
      "order_id": 91,
      "cliente": "UserE",
      "fecha": "2025-04-01",
      "total_orden": 27.8,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 13.9,
      "subtotal": 27.8
    },
    {
      "order_id": 92,
      "cliente": "UserE",
      "fecha": "2025-04-02",
      "total_orden": 34.54,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 17.27,
      "subtotal": 34.54
    },
    {
      "order_id": 93,
      "cliente": "UserB",
      "fecha": "2025-04-03",
      "total_orden": 44.8,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 4,
      "price_unit": 11.2,
      "subtotal": 44.8
    },
    {
      "order_id": 94,
      "cliente": "UserD",
      "fecha": "2025-04-04",
      "total_orden": 79.48,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 19.87,
      "subtotal": 79.48
    },
    {
      "order_id": 95,
      "cliente": "UserD",
      "fecha": "2025-04-05",
      "total_orden": 50.4,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 12.6,
      "subtotal": 50.4
    },
    {
      "order_id": 96,
      "cliente": "UserC",
      "fecha": "2025-04-06",
      "total_orden": 17.01,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 1,
      "price_unit": 17.01,
      "subtotal": 17.01
    },
    {
      "order_id": 97,
      "cliente": "UserC",
      "fecha": "2025-04-07",
      "total_orden": 8.53,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 8.53,
      "subtotal": 8.53
    },
    {
      "order_id": 98,
      "cliente": "UserE",
      "fecha": "2025-04-08",
      "total_orden": 77.68,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 19.42,
      "subtotal": 77.68
    },
    {
      "order_id": 99,
      "cliente": "UserD",
      "fecha": "2025-04-09",
      "total_orden": 47.8,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 11.95,
      "subtotal": 47.8
    },
    {
      "order_id": 100,
      "cliente": "UserD",
      "fecha": "2025-04-10",
      "total_orden": 34.32,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 11.44,
      "subtotal": 34.32
    },
    {
      "order_id": 101,
      "cliente": "UserC",
      "fecha": "2025-04-11",
      "total_orden": 14.99,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 1,
      "price_unit": 14.99,
      "subtotal": 14.99
    },
    {
      "order_id": 102,
      "cliente": "UserA",
      "fecha": "2025-04-12",
      "total_orden": 49.71,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 3,
      "price_unit": 16.57,
      "subtotal": 49.71
    },
    {
      "order_id": 103,
      "cliente": "UserC",
      "fecha": "2025-04-13",
      "total_orden": 34.04,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 17.02,
      "subtotal": 34.04
    },
    {
      "order_id": 104,
      "cliente": "UserB",
      "fecha": "2025-04-14",
      "total_orden": 76.0,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 15.2,
      "subtotal": 76.0
    },
    {
      "order_id": 105,
      "cliente": "UserB",
      "fecha": "2025-04-15",
      "total_orden": 41.91,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 13.97,
      "subtotal": 41.91
    },
    {
      "order_id": 106,
      "cliente": "UserC",
      "fecha": "2025-04-16",
      "total_orden": 66.48,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 16.62,
      "subtotal": 66.48
    },
    {
      "order_id": 107,
      "cliente": "UserE",
      "fecha": "2025-04-17",
      "total_orden": 54.15,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 10.83,
      "subtotal": 54.15
    },
    {
      "order_id": 108,
      "cliente": "UserC",
      "fecha": "2025-04-18",
      "total_orden": 54.2,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 13.55,
      "subtotal": 54.2
    },
    {
      "order_id": 109,
      "cliente": "UserA",
      "fecha": "2025-04-19",
      "total_orden": 28.12,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 14.06,
      "subtotal": 28.12
    },
    {
      "order_id": 110,
      "cliente": "UserC",
      "fecha": "2025-04-20",
      "total_orden": 82.8,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 16.56,
      "subtotal": 82.8
    },
    {
      "order_id": 111,
      "cliente": "UserB",
      "fecha": "2025-04-21",
      "total_orden": 22.26,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 11.13,
      "subtotal": 22.26
    },
    {
      "order_id": 112,
      "cliente": "UserD",
      "fecha": "2025-04-22",
      "total_orden": 32.1,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 16.05,
      "subtotal": 32.1
    },
    {
      "order_id": 113,
      "cliente": "UserC",
      "fecha": "2025-04-23",
      "total_orden": 13.62,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 1,
      "price_unit": 13.62,
      "subtotal": 13.62
    },
    {
      "order_id": 114,
      "cliente": "UserD",
      "fecha": "2025-04-24",
      "total_orden": 56.1,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 18.7,
      "subtotal": 56.1
    },
    {
      "order_id": 115,
      "cliente": "UserD",
      "fecha": "2025-04-25",
      "total_orden": 25.68,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 12.84,
      "subtotal": 25.68
    },
    {
      "order_id": 116,
      "cliente": "UserA",
      "fecha": "2025-04-26",
      "total_orden": 54.24,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 18.08,
      "subtotal": 54.24
    },
    {
      "order_id": 117,
      "cliente": "UserB",
      "fecha": "2025-04-27",
      "total_orden": 83.0,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 16.6,
      "subtotal": 83.0
    },
    {
      "order_id": 118,
      "cliente": "UserE",
      "fecha": "2025-04-28",
      "total_orden": 63.92,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 15.98,
      "subtotal": 63.92
    },
    {
      "order_id": 119,
      "cliente": "UserD",
      "fecha": "2025-04-29",
      "total_orden": 52.36,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 13.09,
      "subtotal": 52.36
    },
    {
      "order_id": 120,
      "cliente": "UserD",
      "fecha": "2025-04-30",
      "total_orden": 22.1,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 11.05,
      "subtotal": 22.1
    },
    {
      "order_id": 121,
      "cliente": "UserA",
      "fecha": "2025-05-01",
      "total_orden": 35.7,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 17.85,
      "subtotal": 35.7
    },
    {
      "order_id": 122,
      "cliente": "UserC",
      "fecha": "2025-05-02",
      "total_orden": 38.88,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 2,
      "price_unit": 19.44,
      "subtotal": 38.88
    },
    {
      "order_id": 123,
      "cliente": "UserA",
      "fecha": "2025-05-03",
      "total_orden": 14.71,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 1,
      "price_unit": 14.71,
      "subtotal": 14.71
    },
    {
      "order_id": 124,
      "cliente": "UserA",
      "fecha": "2025-05-04",
      "total_orden": 79.4,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 19.85,
      "subtotal": 79.4
    },
    {
      "order_id": 125,
      "cliente": "UserA",
      "fecha": "2025-05-05",
      "total_orden": 50.7,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 5,
      "price_unit": 10.14,
      "subtotal": 50.7
    },
    {
      "order_id": 126,
      "cliente": "UserC",
      "fecha": "2025-05-06",
      "total_orden": 90.6,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 18.12,
      "subtotal": 90.6
    },
    {
      "order_id": 127,
      "cliente": "UserA",
      "fecha": "2025-05-07",
      "total_orden": 16.64,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 8.32,
      "subtotal": 16.64
    },
    {
      "order_id": 128,
      "cliente": "UserD",
      "fecha": "2025-05-08",
      "total_orden": 10.83,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 1,
      "price_unit": 10.83,
      "subtotal": 10.83
    },
    {
      "order_id": 129,
      "cliente": "UserB",
      "fecha": "2025-05-09",
      "total_orden": 10.49,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 1,
      "price_unit": 10.49,
      "subtotal": 10.49
    },
    {
      "order_id": 130,
      "cliente": "UserA",
      "fecha": "2025-05-10",
      "total_orden": 33.46,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 16.73,
      "subtotal": 33.46
    },
    {
      "order_id": 131,
      "cliente": "UserE",
      "fecha": "2025-05-11",
      "total_orden": 71.75,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 14.35,
      "subtotal": 71.75
    },
    {
      "order_id": 132,
      "cliente": "UserC",
      "fecha": "2025-05-12",
      "total_orden": 70.3,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 14.06,
      "subtotal": 70.3
    },
    {
      "order_id": 133,
      "cliente": "UserA",
      "fecha": "2025-05-13",
      "total_orden": 37.23,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 12.41,
      "subtotal": 37.23
    },
    {
      "order_id": 134,
      "cliente": "UserD",
      "fecha": "2025-05-14",
      "total_orden": 33.76,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 16.88,
      "subtotal": 33.76
    },
    {
      "order_id": 135,
      "cliente": "UserC",
      "fecha": "2025-05-15",
      "total_orden": 91.85,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 5,
      "price_unit": 18.37,
      "subtotal": 91.85
    },
    {
      "order_id": 136,
      "cliente": "UserD",
      "fecha": "2025-05-16",
      "total_orden": 50.49,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 16.83,
      "subtotal": 50.49
    },
    {
      "order_id": 137,
      "cliente": "UserD",
      "fecha": "2025-05-17",
      "total_orden": 12.6,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 1,
      "price_unit": 12.6,
      "subtotal": 12.6
    },
    {
      "order_id": 138,
      "cliente": "UserC",
      "fecha": "2025-05-18",
      "total_orden": 34.44,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 8.61,
      "subtotal": 34.44
    },
    {
      "order_id": 139,
      "cliente": "UserB",
      "fecha": "2025-05-19",
      "total_orden": 76.55,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 15.31,
      "subtotal": 76.55
    },
    {
      "order_id": 140,
      "cliente": "UserD",
      "fecha": "2025-05-20",
      "total_orden": 33.57,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 11.19,
      "subtotal": 33.57
    },
    {
      "order_id": 141,
      "cliente": "UserB",
      "fecha": "2025-05-21",
      "total_orden": 28.83,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 9.61,
      "subtotal": 28.83
    },
    {
      "order_id": 142,
      "cliente": "UserB",
      "fecha": "2025-05-22",
      "total_orden": 86.2,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 5,
      "price_unit": 17.24,
      "subtotal": 86.2
    },
    {
      "order_id": 143,
      "cliente": "UserE",
      "fecha": "2025-05-23",
      "total_orden": 44.6,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 5,
      "price_unit": 8.92,
      "subtotal": 44.6
    },
    {
      "order_id": 144,
      "cliente": "UserE",
      "fecha": "2025-05-24",
      "total_orden": 41.64,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 13.88,
      "subtotal": 41.64
    },
    {
      "order_id": 145,
      "cliente": "UserA",
      "fecha": "2025-05-25",
      "total_orden": 31.42,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 2,
      "price_unit": 15.71,
      "subtotal": 31.42
    },
    {
      "order_id": 146,
      "cliente": "UserC",
      "fecha": "2025-05-26",
      "total_orden": 78.68,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 19.67,
      "subtotal": 78.68
    },
    {
      "order_id": 147,
      "cliente": "UserD",
      "fecha": "2025-05-27",
      "total_orden": 10.32,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 1,
      "price_unit": 10.32,
      "subtotal": 10.32
    },
    {
      "order_id": 148,
      "cliente": "UserC",
      "fecha": "2025-05-28",
      "total_orden": 40.48,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 10.12,
      "subtotal": 40.48
    },
    {
      "order_id": 149,
      "cliente": "UserC",
      "fecha": "2025-05-29",
      "total_orden": 43.32,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 14.44,
      "subtotal": 43.32
    },
    {
      "order_id": 150,
      "cliente": "UserB",
      "fecha": "2025-05-30",
      "total_orden": 61.76,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 15.44,
      "subtotal": 61.76
    },
    {
      "order_id": 151,
      "cliente": "UserB",
      "fecha": "2025-05-31",
      "total_orden": 38.46,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 2,
      "price_unit": 19.23,
      "subtotal": 38.46
    },
    {
      "order_id": 152,
      "cliente": "UserB",
      "fecha": "2025-06-01",
      "total_orden": 36.06,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 18.03,
      "subtotal": 36.06
    },
    {
      "order_id": 153,
      "cliente": "UserB",
      "fecha": "2025-06-02",
      "total_orden": 39.08,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 9.77,
      "subtotal": 39.08
    },
    {
      "order_id": 154,
      "cliente": "UserB",
      "fecha": "2025-06-03",
      "total_orden": 18.44,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 9.22,
      "subtotal": 18.44
    },
    {
      "order_id": 155,
      "cliente": "UserC",
      "fecha": "2025-06-04",
      "total_orden": 64.64,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 16.16,
      "subtotal": 64.64
    },
    {
      "order_id": 156,
      "cliente": "UserD",
      "fecha": "2025-06-05",
      "total_orden": 30.18,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 10.06,
      "subtotal": 30.18
    },
    {
      "order_id": 157,
      "cliente": "UserB",
      "fecha": "2025-06-06",
      "total_orden": 23.26,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 11.63,
      "subtotal": 23.26
    },
    {
      "order_id": 158,
      "cliente": "UserE",
      "fecha": "2025-06-07",
      "total_orden": 32.19,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 10.73,
      "subtotal": 32.19
    },
    {
      "order_id": 159,
      "cliente": "UserB",
      "fecha": "2025-06-08",
      "total_orden": 42.66,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 14.22,
      "subtotal": 42.66
    },
    {
      "order_id": 160,
      "cliente": "UserB",
      "fecha": "2025-06-09",
      "total_orden": 29.28,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 2,
      "price_unit": 14.64,
      "subtotal": 29.28
    },
    {
      "order_id": 161,
      "cliente": "UserE",
      "fecha": "2025-06-10",
      "total_orden": 64.28,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 16.07,
      "subtotal": 64.28
    },
    {
      "order_id": 162,
      "cliente": "UserD",
      "fecha": "2025-06-11",
      "total_orden": 53.88,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 4,
      "price_unit": 13.47,
      "subtotal": 53.88
    },
    {
      "order_id": 163,
      "cliente": "UserC",
      "fecha": "2025-06-12",
      "total_orden": 71.24,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 17.81,
      "subtotal": 71.24
    },
    {
      "order_id": 164,
      "cliente": "UserA",
      "fecha": "2025-06-13",
      "total_orden": 25.3,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 2,
      "price_unit": 12.65,
      "subtotal": 25.3
    },
    {
      "order_id": 165,
      "cliente": "UserD",
      "fecha": "2025-06-14",
      "total_orden": 53.3,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 10.66,
      "subtotal": 53.3
    },
    {
      "order_id": 166,
      "cliente": "UserC",
      "fecha": "2025-06-15",
      "total_orden": 43.77,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 14.59,
      "subtotal": 43.77
    },
    {
      "order_id": 167,
      "cliente": "UserE",
      "fecha": "2025-06-16",
      "total_orden": 33.16,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 16.58,
      "subtotal": 33.16
    },
    {
      "order_id": 168,
      "cliente": "UserA",
      "fecha": "2025-06-17",
      "total_orden": 75.36,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 18.84,
      "subtotal": 75.36
    },
    {
      "order_id": 169,
      "cliente": "UserB",
      "fecha": "2025-06-18",
      "total_orden": 33.66,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 11.22,
      "subtotal": 33.66
    },
    {
      "order_id": 170,
      "cliente": "UserC",
      "fecha": "2025-06-19",
      "total_orden": 44.25,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 8.85,
      "subtotal": 44.25
    },
    {
      "order_id": 171,
      "cliente": "UserE",
      "fecha": "2025-06-20",
      "total_orden": 45.72,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 11.43,
      "subtotal": 45.72
    },
    {
      "order_id": 172,
      "cliente": "UserA",
      "fecha": "2025-06-21",
      "total_orden": 47.85,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 5,
      "price_unit": 9.57,
      "subtotal": 47.85
    },
    {
      "order_id": 173,
      "cliente": "UserB",
      "fecha": "2025-06-22",
      "total_orden": 71.48,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 17.87,
      "subtotal": 71.48
    },
    {
      "order_id": 174,
      "cliente": "UserA",
      "fecha": "2025-06-23",
      "total_orden": 39.36,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 9.84,
      "subtotal": 39.36
    },
    {
      "order_id": 175,
      "cliente": "UserE",
      "fecha": "2025-06-24",
      "total_orden": 71.56,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 4,
      "price_unit": 17.89,
      "subtotal": 71.56
    },
    {
      "order_id": 176,
      "cliente": "UserB",
      "fecha": "2025-06-25",
      "total_orden": 57.35,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 5,
      "price_unit": 11.47,
      "subtotal": 57.35
    },
    {
      "order_id": 177,
      "cliente": "UserA",
      "fecha": "2025-06-26",
      "total_orden": 26.82,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 8.94,
      "subtotal": 26.82
    },
    {
      "order_id": 178,
      "cliente": "UserB",
      "fecha": "2025-06-27",
      "total_orden": 75.24,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 4,
      "price_unit": 18.81,
      "subtotal": 75.24
    },
    {
      "order_id": 179,
      "cliente": "UserB",
      "fecha": "2025-06-28",
      "total_orden": 38.7,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 12.9,
      "subtotal": 38.7
    },
    {
      "order_id": 180,
      "cliente": "UserA",
      "fecha": "2025-06-29",
      "total_orden": 25.77,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 8.59,
      "subtotal": 25.77
    },
    {
      "order_id": 181,
      "cliente": "UserD",
      "fecha": "2025-06-30",
      "total_orden": 50.67,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 3,
      "price_unit": 16.89,
      "subtotal": 50.67
    },
    {
      "order_id": 182,
      "cliente": "UserA",
      "fecha": "2025-07-01",
      "total_orden": 33.8,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 4,
      "price_unit": 8.45,
      "subtotal": 33.8
    },
    {
      "order_id": 183,
      "cliente": "UserE",
      "fecha": "2025-07-02",
      "total_orden": 35.1,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 3,
      "price_unit": 11.7,
      "subtotal": 35.1
    },
    {
      "order_id": 184,
      "cliente": "UserC",
      "fecha": "2025-07-03",
      "total_orden": 44.97,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 14.99,
      "subtotal": 44.97
    },
    {
      "order_id": 185,
      "cliente": "UserB",
      "fecha": "2025-07-04",
      "total_orden": 75.6,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 18.9,
      "subtotal": 75.6
    },
    {
      "order_id": 186,
      "cliente": "UserC",
      "fecha": "2025-07-05",
      "total_orden": 54.18,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 3,
      "price_unit": 18.06,
      "subtotal": 54.18
    },
    {
      "order_id": 187,
      "cliente": "UserD",
      "fecha": "2025-07-06",
      "total_orden": 16.57,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 1,
      "price_unit": 16.57,
      "subtotal": 16.57
    },
    {
      "order_id": 188,
      "cliente": "UserB",
      "fecha": "2025-07-07",
      "total_orden": 40.38,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 3,
      "price_unit": 13.46,
      "subtotal": 40.38
    },
    {
      "order_id": 189,
      "cliente": "UserD",
      "fecha": "2025-07-08",
      "total_orden": 50.7,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 3,
      "price_unit": 16.9,
      "subtotal": 50.7
    },
    {
      "order_id": 190,
      "cliente": "UserB",
      "fecha": "2025-07-09",
      "total_orden": 56.28,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 4,
      "price_unit": 14.07,
      "subtotal": 56.28
    },
    {
      "order_id": 191,
      "cliente": "UserB",
      "fecha": "2025-07-10",
      "total_orden": 16.48,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 2,
      "price_unit": 8.24,
      "subtotal": 16.48
    },
    {
      "order_id": 192,
      "cliente": "UserA",
      "fecha": "2025-07-11",
      "total_orden": 68.1,
      "producto_id": 5,
      "producto_name": "Double Burger",
      "qty": 5,
      "price_unit": 13.62,
      "subtotal": 68.1
    },
    {
      "order_id": 193,
      "cliente": "UserA",
      "fecha": "2025-07-12",
      "total_orden": 89.65,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 17.93,
      "subtotal": 89.65
    },
    {
      "order_id": 194,
      "cliente": "UserD",
      "fecha": "2025-07-13",
      "total_orden": 43.35,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 14.45,
      "subtotal": 43.35
    },
    {
      "order_id": 195,
      "cliente": "UserC",
      "fecha": "2025-07-14",
      "total_orden": 54.35,
      "producto_id": 3,
      "producto_name": "Veggie Burger",
      "qty": 5,
      "price_unit": 10.87,
      "subtotal": 54.35
    },
    {
      "order_id": 196,
      "cliente": "UserD",
      "fecha": "2025-07-15",
      "total_orden": 57.45,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 3,
      "price_unit": 19.15,
      "subtotal": 57.45
    },
    {
      "order_id": 197,
      "cliente": "UserB",
      "fecha": "2025-07-16",
      "total_orden": 15.95,
      "producto_id": 2,
      "producto_name": "Chicken Burger",
      "qty": 1,
      "price_unit": 15.95,
      "subtotal": 15.95
    },
    {
      "order_id": 198,
      "cliente": "UserA",
      "fecha": "2025-07-17",
      "total_orden": 35.34,
      "producto_id": 1,
      "producto_name": "Bacon Burger",
      "qty": 3,
      "price_unit": 11.78,
      "subtotal": 35.34
    },
    {
      "order_id": 199,
      "cliente": "UserA",
      "fecha": "2025-07-18",
      "total_orden": 25.84,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 12.92,
      "subtotal": 25.84
    },
    {
      "order_id": 200,
      "cliente": "UserA",
      "fecha": "2025-07-19",
      "total_orden": 38.28,
      "producto_id": 4,
      "producto_name": "Fish Burger",
      "qty": 2,
      "price_unit": 19.14,
      "subtotal": 38.28
    }
  ]
}

# Mapeo de usuarios a nombres completos Y Partner IDs
user_mapping = {
    "UserA": {"name": "Juan Pérez López", "partner_id": 109},
    "UserB": {"name": "María García Rodríguez", "partner_id": 110},
    "UserC": {"name": "Carlos Hernández Silva", "partner_id": 111},
    "UserD": {"name": "Ana Martínez Díaz", "partner_id": 112},
    "UserE": {"name": "Roberto Sánchez Cruz", "partner_id": 113}
}

# Vendedores (rotación)
vendedores = ["Vendedor 1", "Vendedor 2", "Vendedor 3"]

# Términos de pago (rotación)
payment_terms = ["15 Days", "30 Days", "Immediate Payment", "45 Days"]

# Función para calcular fecha de entrega (7 días después)
def calcular_fecha_entrega(fecha_orden):
    fecha_dt = datetime.strptime(fecha_orden, "%Y-%m-%d")
    fecha_entrega = fecha_dt + timedelta(days=7)
    return fecha_entrega.strftime("%Y-%m-%d")

# Archivo de salida
output_file = "ordenes_odoo_final.csv"

# Columnas para Odoo con Partner ID
columnas_odoo = [
    'Order Reference',
    'Partner ID',  # ID numérico del partner
    'Customer Name', 
    'Order Date',
    'Expected Delivery',
    'Salesperson',
    'Payment Terms',
    'Status',
    'Warehouse',
    'Source Location',
    'Destination Location',
    'Product',
    'Quantity',
    'Unit Price',
    'Subtotal',
    'Tax Amount',
    'Total Amount'
]

print("🔄 Generando archivo CSV para Odoo con Partner IDs...")
print("="*60)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=columnas_odoo)
    writer.writeheader()
    
    # Procesar todas las ventas del JSON
    for idx, venta in enumerate(json_data["ventas_filtradas"], start=1):
        # Obtener info del usuario
        user_info = user_mapping.get(venta['cliente'], {"name": venta['cliente'], "partner_id": 99})
        
        # Calcular impuestos (16%)
        tax_amount = round(venta["subtotal"] * 0.16, 2)
        total_amount = round(venta["subtotal"] + tax_amount, 2)
        
        # Crear registro completo
        row = {
            'Order Reference': f"SO{str(venta['order_id']).zfill(3)}",
            'Partner ID': user_info['partner_id'],  # ID numérico del cliente
            'Customer Name': user_info['name'],
            'Order Date': venta['fecha'],
            'Expected Delivery': calcular_fecha_entrega(venta['fecha']),
            'Salesperson': vendedores[idx % len(vendedores)],
            'Payment Terms': payment_terms[idx % len(payment_terms)],
            'Status': 'sale',
            'Warehouse': 'WH',
            'Source Location': 'WH/Stock',
            'Destination Location': 'Partners/Customers',
            'Product': venta['producto_name'],
            'Quantity': venta['qty'],
            'Unit Price': f"{venta['price_unit']:.2f}",
            'Subtotal': f"{venta['subtotal']:.2f}",
            'Tax Amount': f"{tax_amount:.2f}",
            'Total Amount': f"{total_amount:.2f}"
        }
        
        writer.writerow(row)

print(f"\n✅ Archivo generado exitosamente: {output_file}")
print(f"📊 Total de órdenes procesadas: {len(json_data['ventas_filtradas'])}")
print("\n📋 Mapeo de Partner IDs:")
print("-" * 60)
for user, info in user_mapping.items():
    print(f"   {user:8} → Partner ID: {info['partner_id']} | {info['name']}")

print("\n⚠️  IMPORTANTE - Antes de importar en Odoo:")
print("-" * 60)
print("1. ✓ Verifica que los Partner IDs (3-7) existan en Odoo")
print("2. ✓ Asegúrate que el almacén 'WH' esté configurado")
print("3. ✓ Confirma que la ubicación 'WH/Stock' existe")
print("4. ✓ Los productos deben existir con los nombres exactos")
print("5. ✓ Si los Partner IDs son diferentes, ajusta el mapeo")
print("="*60)