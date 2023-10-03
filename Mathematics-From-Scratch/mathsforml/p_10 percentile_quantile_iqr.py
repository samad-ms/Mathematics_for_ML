# def calculate_percentile(data, percentile):
#     n = len(data)
#     sorted_data = sorted(data)
#     return sorted_data[int((percentile / 100) * n)]
#
# # Example usage
# data = [1,2,3,4,5,6,7,8,9,10]
# percentile_value = calculate_percentile(data, 95)
# print("Percentile Value:", percentile_value)

def calculate_median(data):
    n = len(data)
    sorted_data = sorted(data)
    if n % 2 == 0:
        median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
    else:
        median = sorted_data[(n - 1) // 2]
    return median

def calculate_first_quartile(data):
    n = len(data)
    lower_half = sorted(data)[:n // 2]
    return calculate_median(lower_half)

def calculate_third_quartile(data):
    n = len(data)
    upper_half = sorted(data)[n // 2:]
    return calculate_median(upper_half)

def calculate_iqr(data):
    q1 = calculate_first_quartile(data)
    q3 = calculate_third_quartile(data)
    iqr = q3 - q1
    return iqr

# Example usage
data = [12, 16, 17, 20, 22, 24, 25, 28, 30, 32]

iqr = calculate_iqr(data)

print("Interquartile Range (IQR):", iqr)
