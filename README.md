## Data Source

The dataset used in this project is from [Kaggle: Coffee Sales Dataset](https://www.kaggle.com/datasets/navjotkaushal/coffee-sales-dataset)  
License: [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/)  
Original author: Navjot Kaushal

---

## 1. Basic Analysis
### Preview (Screenshot)
![Data Head](images/head.png)
- 🔼 *It gives us a look into our 1st 5 row*
- `df.head()`

![Data info](images/info.png)
- 🔼 *shows all column, data types, missing values....*
- `df.info()`

![Describe](images/describe.png)
- 🔼 *It gives min,max,mean....*
- `df.describe()`

![Checking Missing values](images/isnull.png)
- 🔼 *Checks if we have any missing values*
- `df.isnull().sum()`
---

## 2. Common Q/A
### Preview (Screenshot)
![most popular coffee](images/popularcoffee.png)
- 🔼 *What kind of coffee makes most sales*
- `coffee_count`

![best sale time](images/mostmoneyday.png)
- 🔼 *What time of day makes most sales *
- `sales_by_time`

![prefered payment method](images/preferpayment.png)
- 🔼 *What kind of payment do customer prefer*
- `prefer_payment`

![busiest day of the week](images/busiestday.png)
- 🔼 *What day of week is the most busiest*
- `busiest_day`

![busiest month of the year](images/busiestyear.png)
- 🔼 *What month of year is most busiest*
- `busiest_year`
---

## 3. Visualization of Data Analysis
### Preview (Screenshot)
![most popular coffee plot](images/coffeebarplot.png)
- 🔼 *What kind of coffee makes most sales*
- `coffee_count`

![best sale time plot](images/peaksalesplot.png)
- 🔼 *What time of day makes most sales*
- `sales_by_time`

![busiest day of the week plot](images/busiestdayplot.png)
- 🔼 *What day of week is the most busiest*
- `busiest_day`

![busiest month of the year plot](images/busiestyearplot.png)
- 🔼 *What month of year is most busiest*
- `busiest_year`
---