#string challenge
line = "X-DSPAM-Confidence:0.8475"
#challenge is to 1) extract everything after the colon, and 2)convert that value to a floating point number
line_2 = line.find(":")
line_3 = line[line_2+1:(len(line))] #holy shit this worked...I didn't think it would
answer = float(line_3)
print(answer)
print(type(answer))
