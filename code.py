import csv
import sys
import statistics

def is_float(value):
    try:
        float(value)
        return True
    except:
        return False

def column_stats(file_path):
    with open(file_path, newline='') as f:
        reader = csv.DictReader(f)
        data = list(reader)

    if not data:
        return

    columns = data[0].keys()

    for col in columns:
        values = [row[col] for row in data if row[col] != ""]
        numeric_values = [float(v) for v in values if is_float(v)]

        print(f"\nColumn: {col}")
        print(f"Count: {len(values)}")

        if numeric_values:
            print(f"Sum: {sum(numeric_values)}")
            print(f"Mean: {statistics.mean(numeric_values)}")
            print(f"Median: {statistics.median(numeric_values)}")
            print(f"Min: {min(numeric_values)}")
            print(f"Max: {max(numeric_values)}")
            if len(numeric_values) > 1:
                print(f"Std Dev: {statistics.stdev(numeric_values)}")

if __name__ == "__main__":
    column_stats(sys.argv[1])
