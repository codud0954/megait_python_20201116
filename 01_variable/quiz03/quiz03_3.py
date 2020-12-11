inputSec = int(input("초: "))
minutes = inputSec // 60
seconds = inputSec % 60

print("%d분 %d초" % (minutes, seconds))

# 다른 방법
print("%d분 %d초" % divmod(inputSec, 60))
