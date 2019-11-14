#
from modules.cooccurence_functions import cooccurence_matrix_step_1
from modules.cooccurence_functions import cooccurence_matrix_step_2

#
cluster_id_a = [1, 1, 1, 1, 1, 1, 2, 2, 2, 2]
npi_a = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5]
cluster_id_b = ['a', 'a', 'a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'b']
npi_b = [1, 2, 3, 4, 5, 6, 2, 3, 4, 5, 6]

#
z = cooccurence_matrix_step_2(cluster_id_a, npi_a, cluster_id_b, npi_b)
print(z)

#
