timeout 4
adb -s %1 wait-for-device logcat -v threadtime >%time::=.%_%1.txt  