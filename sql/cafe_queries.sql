SELECT
	"Item",
	SUM("Total Spent") AS total_revenue
FROM cafe_sales
GROUP BY "Item"
ORDER BY total_revenue DESC;


WITH highest_item AS (
	SELECT 
		"Item",
		"Location",
		"Payment Method",
		DENSE_RANK() OVER(
			PARTITION BY "Payment Method"
			ORDER BY "Total Spent" DESC
		) AS payment_method_ranking
	FROM cafe_sales
)
SELECT *
FROM highest_item
WHERE payment_method_ranking = 1;


SELECT
	"Item",
	"Total Spent"
FROM cafe_sales 
WHERE "Total Spent" > (
	SELECT
		AVG("Total Spent")
	FROM cafe_sales cs
)
ORDER BY "Total Spent" DESC;



SELECT
	"Item",
	TO_CHAR("Transaction Date"::date, 'Mon') as "Month",
	"Total Spent",
	LAG("Total Spent") OVER(
		ORDER BY "Transaction Date"::date 
	) AS Previous_Sales,
	"Total Spent" -LAG("Total Spent") OVER(ORDER BY "Transaction Date"::date) AS Business_Growth
FROM cafe_sales;
		




















