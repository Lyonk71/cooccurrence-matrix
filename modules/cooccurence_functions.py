def cooccurence_matrix_step_1(cluster_id:list, npi_field:list):
    '''Converts a cluster id & npi into a dictonary of sets'''

    if len(cluster_id)==len(npi_field):
        pass
    else:
        raise ValueError('cluster id must be same length as npi field')

    record_count = len(cluster_id)
    dict_of_sets = {}

    for i in range(record_count):
        if cluster_id[i] == cluster_id[i-1]:
            pass
        elif cluster_id[i] != cluster_id[i-1]:
            temp_set = set()

        temp_set.add(npi_field[i])
        dict_of_sets[cluster_id[i]] = temp_set

    return dict_of_sets


def cooccurence_matrix_step_2(cluster_a, npi_a, cluster_b, npi_b):
    '''generate matrix'''
    dict_a = cooccurence_matrix_step_1(cluster_a, npi_a)
    dict_b = cooccurence_matrix_step_1(cluster_b, npi_b)
    temp_dict={}
    for i in dict_a:
        for j in dict_b:
            temp_dict.update({(i, j): len(dict_a[i].intersection(dict_b[j]))})

    return temp_dict
