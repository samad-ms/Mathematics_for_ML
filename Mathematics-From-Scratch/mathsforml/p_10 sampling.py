import random
# def simple_random_sample(s_size,data):
#     return random.sample(data,s_size)
# data=[1,2,3,4,5,6,7,8,9,523,5234,42,4]
# print(simple_random_sample(3,data))

# def systematic_sampling(data, sample_size):
#     step = len(data) // sample_size
#     start_index = random.randint(0, step - 1)
#     print(start_index)
#     systematic_sample = [data[i] for i in range(start_index, len(data), step)]
#     return systematic_sample

# def stratified_sampling(data, strata, sample_size):
#     samples = []
#     for group, size in strata.items():
#         stratum_data = random.sample(data[group], size)
#         samples.extend(stratum_data)
#     return samples
#
# data = {
#     'stratum1': [1, 2, 3],
#     'stratum2': [4, 5, 6],
#     'stratum3': [7, 8, 9]
# }
# strata = {'stratum1': 1, 'stratum2': 2, 'stratum3': 2}
# sample_size = 5
# stratified_sample = stratified_sampling(data, strata, sample_size)
# print(stratified_sample)

# def cluster_sampling(data, clusters, sample_size):
#     selected_clusters = random.sample(clusters, sample_size)
#     cluster_samples = [data[cluster] for cluster in selected_clusters]
#     return cluster_samples
#
# data = {
#     'cluster1': [1, 2, 3],
#     'cluster2': [4, 5, 6],
#     'cluster3': [7, 8, 9]
# }
# clusters = list(data.keys())
# sample_size = 2
# cluster_sample = cluster_sampling(data, clusters, sample_size)
# print(cluster_sample)
