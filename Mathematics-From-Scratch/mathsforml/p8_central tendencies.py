x = [1, 2, 3, 4, 5]

mean=sum(x)/len(x)

sortedlist=sorted(x)
l=len(x)
if len(x)%2==0:
  median=(x[l//2-1]+x[l//2])/2
else:
  median=x[l//2]


max_count=0
for c in range(len(x)):
  cur_count=x.count(c)
  if max_count<cur_count:
    mode=c
  max_count=max(max_count,cur_count)
  if max_count<=1:
    mode=None

print(mean)
print(median)
print(mode)

#
#
#
# # Sample list of numbers
# data = [1, 2, 3, 4, 4, 5, 5, 6, 6, 7]
#
# # Calculate the mean
# mean = sum(data) / len(data)
# print("Mean:", mean)
#
# # Calculate the median
# sorted_data = sorted(data)
# n = len(sorted_data)
# if n % 2 == 0:
#     median = (sorted_data[n // 2 - 1] + sorted_data[n // 2]) / 2
# else:
#     median = sorted_data[n // 2]
# print("Median:", median)
#
# # Calculate the mode
# freq_dict = {}
# for num in data:
#     if num in freq_dict:
#         freq_dict[num] += 1
#     else:
#         freq_dict[num] = 1
#
# mode = [key for key, value in freq_dict.items() if value == max(freq_dict.values())]
# if len(mode) == len(data):
#     print("There is no unique mode in the data.")
# else:
#     print("Mode:", mode)
