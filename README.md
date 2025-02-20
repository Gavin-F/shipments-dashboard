# shipments-dasboard

## Run locally
##### Setup DB
`docker-compose up -d db`
##### Let the DB spin up, wait 30s, then run backend
`docker-compose up -d backend`
##### Run frontend
`docker-compose up -d frontend`

- http://localhost:5173/ React App



## Logistics API

<details>
 <summary><code>GET</code><code>/shipments/{shipment_id}</code></summary>

##### Summary: get shipment by id

Get Shipment

##### Parameters

| Name | Located in | Required | Schema |
| ---- | ---------- | -------- | ---- |
| shipment_id | path | Yes | string |

##### Responses

```json
{
  "shipment_id": "string",
  "origin": "string",
  "destination": "string",
  "weight": 0,
  "cost": 0,
  "delivery_time": 0,
  "log_id": "string"
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
| 404 | Not Found |

</details>

<details>
 <summary><code>GET</code><code>/shipments/analysis/route-summary</code></summary>

##### Summary: get key metrics for a route

Get Route Summary

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| origin | query | origin city | Yes | string |
| destination | query | destination city | Yes | string |

##### Responses

```json
{
  "origin": "string",
  "destination": "string",
  "average_delivery_time": 0,
  "total_cost": 0,
  "num_deliveries": 0
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
| 404 | Not Found |

</details>
<details>
 <summary><code>GET</code><code>/shipments/analysis/top-expensive-routes</code></summary>
  
##### Summary: get most expensive routes

Get Top Expensive Routes

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| limit | query | Number of routes | No | integer |

##### Responses

```json
{
  "data": [
    {
      "origin": "string",
      "destination": "string",
      "total_cost": 0,
      "num_deliveries": 0
    }
  ]
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

</details>
<details>
 <summary><code>GET</code><code>/vehicles/{vehicle_id}</code></summary>

##### Summary: get vehicle by id

Get Vehicle

##### Parameters

| Name | Located in  | Required | Schema |
| ---- | ----------  | -------- | ---- |
| vehicle_id | path | Yes | string |

##### Responses

```json
{
  "vehicle_id": "string",
  "name": "string",
  "total_mileage": 0
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
| 404 | Not Found |

</details>
<details>
 <summary><code>GET</code><code>/vehicles/analysis/efficiency</code></summary>

##### Summary: get vehicles and metrics

Vehicle Efficiency

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| limit | query | Number of vehicles | No | integer |
| offset | query | page offset value | No | integer |

##### Responses

```json
{
  "data": [
    {
      "vehicle_id": "string",
      "total_mileage": 0,
      "total_fuel_used": 0,
      "fuel_efficiency": 0
    }
  ]
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

</details>
<details>
 <summary><code>GET</code><code>/vehicle-logs/{log_id}</code></summary>

##### Summary: get vehicle log by id

Get Vehicle Log

##### Parameters

| Name | Located in  | Required | Schema |
| ---- | ----------  | -------- | ---- |
| log_id | path  | Yes | string |

##### Responses

```json
{
  "log_id": "string",
  "vehicle_id": "string",
  "trip_date": "2025-02-20",
  "mileage": 0,
  "fuel_used": 0
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
| 404 | Not Found |

</details>
<details>
 <summary><code>GET</code><code>/analysis/daily-summary</code></summary>

##### Summary: get daily summary metrics

Daily Summary

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| summary_date | query | Date in YYYY-MM-DD format | Yes | date |

##### Responses

```json
{
  "date": "2025-02-20",
  "num_shipments": 0,
  "total_vehicles_used": 0,
  "total_mileage": 0,
  "total_fuel_used": 0
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |
| 404 | Not Found |

</details>
<details>
 <summary><code>GET</code><code>/analysis/timeseries</code></summary>

##### Summary: get daily summary metrics time series

Get Summary Timeseries

##### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ---- |
| range | query | Number of days to retrieve (7 or 30) | No | integer |

##### Responses

```json
{
  "data": [
    {
      "date": "2025-02-20",
      "num_shipments": 0,
      "total_vehicles_used": 0,
      "total_fuel_used": 0,
      "total_mileage": 0
    }
  ]
}
```

| Code | Description |
| ---- | ----------- |
| 200 | Successful Response |
| 422 | Validation Error |

</details>

## Other Notes

<details>
 <summary>Compromises Made</summary>
 
#### Due to the time constraints I had and the nature of a take-home assignment, various compromises were made during development:

- opted for raw SQL queries vs setting up schema migrations
- opted for manual testing vs setting up a testing suite with unit and integration tests
- opted for simpler, more standard REST endpoints
- opted for synchronous database operations
- very basic FE

</details>

<details>
 <summary>Potential Future Optimizations/Expansions</summary>

- Database connection pooling
- Caching expensive queries with Redis
- Caching API responses
- Async db queries
- API authentication
- Admin Page

</details>

