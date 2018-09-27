def get_total_request(data):
    count = len(data)
    return count


def get_method_type_count(data, method_type):
    value_list = []
    for vals in data:
        if vals.get("method_type") == method_type:
            value_list.append(vals)

    return len(value_list)


def get_average_response_time(count, data):
    total_duration = 0
    for vals in data:
        duration = int(vals.get("duration"))
        total_duration += duration

    return float(total_duration/count) if count != 0 else 0

def get_stat_response(data):
    response = dict()
    total_reqs = get_total_request(data)
    response.update({"Total_Requests": total_reqs})
    response.update({"Avg_Response_Time": get_average_response_time(total_reqs, data)})
    response.update({"Total_GET_Requests": get_method_type_count(data, "GET")})
    response.update({"Total_POST_Requests": get_method_type_count(data, "POST")})
    response.update({"Total_PUT_Requests": get_method_type_count(data, "PUT")})
    response.update({"Total_DELETE_Requests": get_method_type_count(data, "DELETE")})

    return response
