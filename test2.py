from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()

screen.setup(width=500, height=400)

user_bet = screen.textinput(
    title="make your bet", prompt="Which turtle will win the race? Enter a colour: ")


y_positions = [-70, -40, -10, 20, 50, 80]
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

all_turtles = []

for i in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[i])
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True


while is_race_on:


    for turtle in all_turtles:


        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print("You've won!")
                is_race_on = False
                break
            else:
                print(f"the winning color is: {winning_color}")
                print("You've lost please try again!")
                is_race_on = False
                break


        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()



from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.types import StructType, StructField, IntegerType, StringType

spark = SparkSession.builder.appName("DataQuality").getOrCreate()

# Create DataFrame
data = [
    {"user_id": 1, "name": "Alice", "email": "alice@gmail.com", "age": 25},
    {"user_id": 1, "name": "Alice", "email": "alice@gmail.com", "age": 25},  # Duplicate
    {"user_id": 2, "name": "Bob", "email": None, "age": 30},  # Missing email
    {"user_id": 3, "name": "Charlie", "email": "charlie@gmail.com", "age": None},  # Missing age
    {"user_id": 4, "name": "David", "email": "david@gmail.com", "age": 150},  # Invalid age
]

df = spark.createDataFrame(data)

# Step 1: Remove exact duplicates
df_no_dupes = df.dropDuplicates()

# Step 2: Identify data quality issues
# Create a column that flags issues
df_with_issues = df_no_dupes.withColumn(
    "quality_issue",
    F.when(F.col("email").isNull() | F.col("age").isNull(), "Missing value") \
     .when((F.col("age") > 120) | (F.col("age") < 0), "Invalid age") \
     .otherwise("None")
)

# Step 3: Split into clean and issues
clean_data = df_with_issues.filter(F.col("quality_issue") == "None") \
    .drop("quality_issue")

data_quality_issues = df_with_issues.filter(F.col("quality_issue") != "None") \
    .select("user_id", "name", "email", "age", "quality_issue")

# Show results
print("=== CLEAN DATA ===")
clean_data.show()

print("\n=== DATA QUALITY ISSUES ===")
data_quality_issues.show()

from pyspark.sql import SparkSession
from pyspark.sql import functions as F
from pyspark.sql.window import Window

# Initialize Spark
spark = SparkSession.builder.appName("EmployeeRanking").getOrCreate()

# Create DataFrame
data = [
    {"emp_id": 1, "name": "Alice", "dept": "Sales", "salary": 50000, "bonus": 5000},
    {"emp_id": 2, "name": "Bob", "dept": "IT", "salary": 60000, "bonus": 8000},
    {"emp_id": 3, "name": "Charlie", "dept": "Sales", "salary": 55000, "bonus": 6000},
    {"emp_id": 4, "name": "David", "dept": "IT", "salary": 65000, "bonus": 9000},
    {"emp_id": 5, "name": "Eve", "dept": "Sales", "salary": 52000, "bonus": 5500}
]

df = spark.createDataFrame(data)

# Step 1: Define window for ranking within each department
dept_window = Window.partitionBy("dept").orderBy(F.desc("salary"))

# Step 2: Add rank column
ranked_df = df.withColumn("rank_in_dept", F.row_number().over(dept_window))

# Step 3: Calculate total department salary budget
dept_budget_window = Window.partitionBy("dept")
budget_df = ranked_df.withColumn(
    "total_dept_budget", 
    F.sum("salary").over(dept_budget_window)
)

# Step 4: Filter for rank #1 or #2
final_df = budget_df.filter(F.col("rank_in_dept") <= 2) \
    .select("emp_id", "name", "dept", "salary", "rank_in_dept", "total_dept_budget") \
    .orderBy("dept", "rank_in_dept")

final_df.show()
