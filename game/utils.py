from datetime import datetime
from dateutil import *
from dateutil.relativedelta import *


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
    time_detail_list = compare_time(data)
    avg_duration_last_hour = float(time_detail_list[0]/time_detail_list[2]) if time_detail_list[2] != 0 else 0
    avg_duration_last_min = float(time_detail_list[1]/time_detail_list[3]) if time_detail_list[3] != 0 else 0
    hour_req_list = time_detail_list[4]
    min_req_list = time_detail_list[5]


    response.update({"Total_Requests": total_reqs})
    response.update({"Avg_Response_Time": get_average_response_time(total_reqs, data)})
    response.update({"Total_GET_Requests": get_method_type_count(data, "GET")})
    response.update({"Total_POST_Requests": get_method_type_count(data, "POST")})
    response.update({"Total_PUT_Requests": get_method_type_count(data, "PUT")})
    response.update({"Total_DELETE_Requests": get_method_type_count(data, "DELETE")})

    response.update({"Total_Requests_Last_Hour": avg_duration_last_hour})
    response.update({"Avg_Response_Time_Last_Hour": get_average_response_time(len(hour_req_list), hour_req_list)})
    response.update({"Total_GET_Requests_Last_Hour": get_method_type_count(hour_req_list, "GET")})
    response.update({"Total_POST_Requests_Last_Hour": get_method_type_count(hour_req_list, "POST")})
    response.update({"Total_PUT_Requests_Last_Hour": get_method_type_count(hour_req_list, "PUT")})
    response.update({"Total_DELETE_Requests_Last_Hour": get_method_type_count(hour_req_list, "DELETE")})

    response.update({"Total_Requests_Last_Min": avg_duration_last_min})
    response.update({"Avg_Response_Time_Last_Min": get_average_response_time(len(min_req_list), min_req_list)})
    response.update({"Total_GET_Requests_Last_Min": get_method_type_count(min_req_list, "GET")})
    response.update({"Total_POST_Requests_Last_Min": get_method_type_count(min_req_list, "POST")})
    response.update({"Total_PUT_Requests_Last_Min": get_method_type_count(min_req_list, "PUT")})
    response.update({"Total_DELETE_Requests_Last_Min": get_method_type_count(min_req_list, "DELETE")})

    return response


def compare_time_hour(input):
    now = datetime.now()
    hour = now - relativedelta(hours=+1)
    datetime_object = parser.parse(input, ignoretz=True)

    if hour < datetime_object and now > datetime_object:
        return True
    else:
        return False


def compare_time_minutes(input):
    now = datetime.now()
    minute = now - relativedelta(minutes=+1)
    datetime_object = parser.parse(input, ignoretz=True)
    if minute < datetime_object and now > datetime_object:
        return True
    else:
        return False


def compare_time(data):
    last_hour_count = 0
    last_min_count = 0
    duration_hour = 0
    duration_min = 0
    hour_req_list = list()
    min_req_list = list()
    for val in data:
        time = val.get("time")
        if time:
            if compare_time_hour(time):
                last_hour_count += 1
                duration_hour += int(val.get("duration"))
                hour_req_list.append(val)
            if compare_time_minutes(time):
                last_min_count += 1
                duration_min += int(val.get("duration"))
                min_req_list.append(val)

    return [last_hour_count, last_min_count, duration_hour, duration_min, hour_req_list, min_req_list]

