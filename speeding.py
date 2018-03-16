
speed_limit = float(input("Enter the speed limit:"))
measured_speed = float(input("Enter the measured speed:"))

diff_speed = abs(measured_speed - speed_limit)
if diff_speed == 0:
    print("speed was legal")
else :
    print("speed is illegal")


if speed_limit>=90 and measured_speed>90 :
    fine=(diff_speed*5)+50+200

else:
    fine = (diff_speed * 5) + 50
print("fine is :$",fine)