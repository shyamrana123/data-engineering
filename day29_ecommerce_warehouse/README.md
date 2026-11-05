\# Day 29 — E-commerce Data Warehouse Project



\## Project Overview



Built an end-to-end e-commerce data pipeline using Python, pandas, PostgreSQL and SQL. The project extracts data from CSV files, transforms and validates it, loads it into staging tables, and builds a dimensional data warehouse using a star schema.



\## Technologies



\- Python

\- pandas

\- PostgreSQL

\- Psycopg 3

\- SQL

\- Git



\## Project Structure



day29\_ecommerce\_warehouse/

│

├── data/

│   ├── customers.csv

│   ├── products.csv

│   └── orders.csv

│

├── scripts/

│   ├── extract\_transform.py

│   └── load\_to\_postgres.py

│

├── sql/

│   └── create\_staging\_tables.sql

│

└── README.md



Pipeline:



1\. Extract customer, product and order data from CSV files.

2\. Transform orders by joining customer and product information.

3\. Calculate sales amounts using quantity × unit price.

4\. Validate missing values and duplicate order items.

5\. Load the transformed data into PostgreSQL staging tables.

6\. Populate customer, product and date dimensions.

7\. Load sales transactions into the fact table using dimension surrogate keys.

8\. Run analytical queries to validate the warehouse.



\## Data Warehouse Design



The warehouse is stored in the PostgreSQL schema `day29\_dw`.



| Table | Purpose |



| dim\_customers | Customer attributes |

| dim\_products | Product attributes and unit prices |

| dim\_date | Calendar information |

| fact\_sales | Order-item transactions and sales measures |



The fact table grain is one row per order item. It connects to the three dimensions through foreign keys.



\## Data Validation



| Validation | Result |

|---|---:|

| Customers loaded | 10 |

| Products loaded | 8 |

| Distinct order dates | 10 |

| Sales order items | 12 |

| Total quantity | 17 |

| Total revenue | €3,770.00 |

| Matched customers | 12 |

| Matched products | 12 |

| Matched dates | 12 |

| Missing values in transformed data | 0 |

| Duplicate order items | 0 |



\## Analytical Queries



The warehouse supports analysis by:



\- Customer country — Portugal generated the highest revenue (€1,395).

\- Product category — Electronics generated €3,120.

\- Month — October 2026 generated €3,770.



\## Key Concepts Practised



\- ETL pipeline design

\- Data extraction and transformation

\- Data quality validation

\- PostgreSQL staging tables

\- Dimensional modelling

\- Star schema

\- Fact and dimension tables

\- Surrogate keys

\- Primary and foreign keys

\- SQL joins and aggregations

\- Analytical reporting



\## Project Outcome



Successfully built and validated an end-to-end e-commerce data warehouse pipeline, from raw CSV files to analytical SQL queries. The Day 29 warehouse is isolated in its own PostgreSQL schema, preserving the earlier learning projects.

