# Task 1: Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
unique_ids = set(customer_ids) # Converting a list to a set removes duplicates
print(sorted(unique_ids)) # Since sets are unordered, I sorted before printing for easier readability