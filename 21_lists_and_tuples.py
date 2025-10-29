# Tuples
def convert_seconds(seconds):
    hours= seconds//3600
    minutes= (seconds-hours*3600)//60
    remaining_seconds= seconds-hours*3600-minutes*60
    return hours,minutes,remaining_seconds
result= convert_seconds(1000)
hours,minutes,remaining_seconds=result
print(type(result))
print(result)
print(hours,minutes,remaining_seconds)