# A while loop keeps running a block of code as long as its condition is True. It checks the condition before every iteration.

# Basic while loop — counts from 1 to 5 
# =========================================

count = 1

while count <= 5:
    print(f"Count: {count}")
    count += 1   # same as: count = count + 1


# Output:
# Count: 1
# Count: 2
# Count: 3
# Count: 4
# Count: 5


# =========================================
# While loop with accumulator
# Sum all numbers from 1 to 10
# =========================================

n = 1
total = 0

while n <= 10:
    total += n
    n += 1

print(f"Sum 1–10: {total}")

# Output:
# Sum 1–10: 55


# =========================================
# Process items from a list using while
# =========================================

queue = ["file_1.csv", "file_2.csv", "file_3.csv"]

while queue:   # runs while list is NOT empty

    file = queue.pop(0)   # remove first item

    print(f"Processing: {file}")


# Output:
# Processing: file_1.csv
# Processing: file_2.csv
# Processing: file_3.csv


# =========================================
# BREAK — Exit loop immediately
# =========================================

attempts = 0
max_attempts = 5

while attempts < max_attempts:

    attempts += 1

    print(f"Attempt {attempts}: connecting to database...")

    # simulate successful connection
    if attempts == 3:
        print("✅ Connected!")

        break   # exit loop immediately


print(f"Done after {attempts} attempt(s)")


# Output:
# Attempt 1: connecting to database...
# Attempt 2: connecting to database...
# Attempt 3: connecting to database...
# ✅ Connected!
# Done after 3 attempt(s)



# =========================================
# CONTINUE — Skip current iteration
# =========================================

n = 0

print("\nOdd numbers only:")

while n < 10:

    n += 1

    # if number is even
    if n % 2 == 0:
        continue   # skip remaining code below

    # only odd numbers reach here
    print(n)


# Output:
# 1
# 3
# 5
# 7
# 9



# =========================================
# ELSE with WHILE
# Runs only if loop finishes naturally
# =========================================

i = 0

while i < 3:

    print(f"i = {i}")

    i += 1

else:
    print("Loop finished naturally")


# Output:
# i = 0
# i = 1
# i = 2
# Loop finished naturally

'''
break vs continue — quick mental model
break
— "I'm done, exit the loop completely right now"
continue
— "Skip this one item, carry on with the next"
else
— "What to do after the loop finishes without breaking"


🔶 Data Engineering link: Pattern 2 (batch processing) is exactly how Spark processes data in micro-batches during streaming. Each batch is a chunk of records — Spark reads, processes, commits offset, reads next batch. The offset variable is literally what Kafka uses to track which messages have been consumed.
'''

# =========================================
# PATTERN 1 — Retry with Backoff
# API / DB / S3 Connection Retry
# =========================================

max_retries = 3
attempt = 0
connected = False

while attempt < max_retries and not connected:

    attempt += 1

    print(f"Attempt {attempt}: connecting to S3...")

    # simulate success on attempt 2
    if attempt == 2:
        connected = True
        print("✅ S3 connection established")


# executed after loop ends
if not connected:
    print("❌ Max retries reached — pipeline failed")


# =========================================
# PATTERN 2 — Batch Processing
# Process records in chunks
# =========================================

all_records = list(range(1, 21))   # [1..20]

batch_size = 5
offset = 0
batch_num = 0

print("\n--- Batch Processing ---")

while offset < len(all_records):

    # slice records
    batch = all_records[offset : offset + batch_size]

    batch_num += 1

    print(f"Batch {batch_num}: {batch}")

    # move to next batch
    offset += batch_size


# Output:
# Batch 1: [1, 2, 3, 4, 5]
# Batch 2: [6, 7, 8, 9, 10]
# Batch 3: [11, 12, 13, 14, 15]
# Batch 4: [16, 17, 18, 19, 20]



# =========================================
# PATTERN 3 — Skip Nulls, Process Valid Rows
# =========================================

rows = ["Ravi", None, "Priya", None, "Ankit"]

idx = 0
processed = 0
skipped = 0

print("\n--- Null Skip ---")

while idx < len(rows):

    row = rows[idx]

    idx += 1

    # skip null values
    if row is None:
        skipped += 1
        continue

    # process valid rows
    print(f"✅ Processing: {row}")

    processed += 1


print(f"\nProcessed: {processed}")
print(f"Skipped: {skipped}")

'''
An infinite loop runs forever because its condition never becomes False. It is the most dangerous mistake with while loops — it hangs your program or crashes your pipeline.
'''

# =========================================
# ❌ INFINITE LOOP EXAMPLES
# DO NOT RUN THESE
# =========================================


# -----------------------------------------
# Mistake 1:
# Forgot to update the counter
# -----------------------------------------

count = 1

while count <= 5:

    print(count)

    # count += 1   ← MISSING!


# Problem:
# count always stays 1

# Flow:
# count = 1
# 1 <= 5 → True
# print(1)
# count still 1
# again True
# again print(1)
# forever...



# -----------------------------------------
# Mistake 2:
# Condition can never become False
# -----------------------------------------

x = 10

while x > 0:

    print(x)

    x += 1


# Problem:
# x becomes:
# 10 → 11 → 12 → 13 ...

# Condition:
# x > 0

# always True forever



# =========================================
# ✅ SAFE PATTERN
# Infinite loop with exit conditions
# =========================================

count = 0

MAX_LOOPS = 1000   # safety valve

while True:

    count += 1

    print(f"Tick {count}")

    # normal exit condition
    if count >= 5:

        print("Done")

        break


    # emergency safety exit
    if count >= MAX_LOOPS:

        print("Safety limit hit!")

        break