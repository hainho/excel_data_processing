import pandas as pd
import openpyxl
from datetime import date
import datetime
from datetime import timedelta


df = pd.read_csv("src.csv")
wb = openpyxl.Workbook()
ws = wb.active

# jstart = 0
# for i in range(1000):
#     flag = True
#     for j in range(jstart, 1000):
#         if ((df.iloc[i, 1]) == df.iloc[j, 15]):
#             date_time_1 = datetime.datetime.strptime(
#                 df.iloc[i, 0], '%Y-%m-%d %H:%M')
#             date_time_2 = datetime.datetime.strptime(
#                 df.iloc[j, 25], '%Y-%m-%d %H:%M')
#             if (date_time_1 >= date_time_2):
#                 date_diff = date_time_1 - date_time_2
#             else:
#                 date_diff = date_time_2 - date_time_1
#             if date_diff <= timedelta(days=1):
#                 ws.append([df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7], df.iloc[i, 8], df.iloc[i, 9], df.iloc[i, 10], df.iloc[i, 11], df.iloc[i, 12],
#                           df.iloc[j, 14], df.iloc[j, 15], df.iloc[j, 16], df.iloc[j, 17], df.iloc[j, 18], df.iloc[j, 19], df.iloc[j, 20], df.iloc[j, 21], df.iloc[j, 22], df.iloc[j, 23], df.iloc[j, 24], df.iloc[j, 25], df.iloc[j, 26]])
#                 if flag == True:
#                     flag = False
#                     jstart = j
#             else:
#                 if date_time_1 < date_time_2:

#                     break
# wb.save("./test11.xlsx")

jstart = 0

time_lst_1 = []
time_lst_2 = []
start = 0
end = 10000
for i in range(start, end):
    time_lst_1.append(datetime.datetime.strptime(
        df.iloc[i, 0], '%Y-%m-%d %H:%M'))
for i in range(start, end):
    time_lst_2.append(datetime.datetime.strptime(
        df.iloc[i, 0], '%Y-%m-%d %H:%M'))
for i in range(0, end - start):
    j = jstart
    # if (time_lst_1[i] >= time_lst_2[j]):
    #     date_diff = time_lst_1[i] - time_lst_2[j]
    # else:
    #      date_diff = time_lst_2[j] - time_lst_1[i]

    date_diff = time_lst_1[i] - time_lst_2[j]
    while (date_diff > timedelta(days=1) and j < end - start):
        date_diff = time_lst_1[i] - time_lst_2[j]
        j += 1
    date_diff = time_lst_2[j] - time_lst_1[i]
    jstart = j
    while (date_diff <= timedelta(days=1) and j < end - start):
        if ((df.iloc[i, 1]) == df.iloc[j, 15]):
            ws.append([df.iloc[i, 0], df.iloc[i, 1], df.iloc[i, 2], df.iloc[i, 3], df.iloc[i, 4], df.iloc[i, 5], df.iloc[i, 6], df.iloc[i, 7], df.iloc[i, 8], df.iloc[i, 9], df.iloc[i, 10], df.iloc[i, 11], df.iloc[i, 12],
                      df.iloc[j, 14], df.iloc[j, 15], df.iloc[j, 16], df.iloc[j, 17], df.iloc[j, 18], df.iloc[j, 19], df.iloc[j, 20], df.iloc[j, 21], df.iloc[j, 22], df.iloc[j, 23], df.iloc[j, 24], df.iloc[j, 25], df.iloc[j, 26]])
        date_diff = time_lst_2[j] - time_lst_1[i]
        j += 1

wb.save("./test10000.xlsx")

# for i in range(500):
#     flag = True
#     print()
#     for j in range(jstart, 500):
#         if ((df.iloc[i, 1]) == df.iloc[j, 15]):
#             date_time_1 = datetime.datetime.strptime(
#                 df.iloc[i, 0], '%Y-%m-%d %H:%M')
#             date_time_2 = datetime.datetime.strptime(
#                 df.iloc[j, 25], '%Y-%m-%d %H:%M')
#             if (date_time_1 >= date_time_2):
#                 date_diff = date_time_1 - date_time_2
#             else:
#                 date_diff = date_time_2 - date_time_1
#             if date_diff <= timedelta(days=1):
#                 if flag == True:
#                     flag = False
#                     jstart = j
#                     print(date_time_1, date_time_2, j)
#             else:
#                 if date_time_1 < date_time_2:
#                     print(date_time_1, date_time_2, j)
#                     break
