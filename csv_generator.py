import csv
import math



def main():
    factor = 2000
    divisor = '\t'
    with open('wave.txt', 'w', newline='') as csvfile_w:
        sinwriter = csv.writer(csvfile_w, delimiter='d', quotechar='q', quoting=csv.QUOTE_NONE, escapechar='e')
        for i in range(factor+1):
            value_x = 0.5*math.sin(math.pi*i/(factor/1))
            value_y = 0*math.sin(math.pi*i/(factor/1))
            value_z = 0.5*math.sin(math.pi*i/(factor/1))
            value_u = 2*math.sin(math.pi*i/(factor/1))
            value_v = 0*math.sin(math.pi*i/(factor/2))
            value_w = 0.5*math.sin(math.pi*i/(factor/8))
            
            value_string = truncate(value_x)
            value_string = value_string + divisor + truncate(value_y)
            value_string = value_string + divisor + truncate(value_z)
            value_string = value_string + divisor + truncate(value_u)
            value_string = value_string + divisor + truncate(value_v)
            value_string = value_string + divisor + truncate(value_w)
            sinwriter.writerow([value_string])

    print('wave.txt created!')

def truncate(number):
    truncated_number = "{:.3f}".format(number)
    return truncated_number

if __name__ == '__main__':
    # PILogger.setLevel(DEBUG)
    main()
