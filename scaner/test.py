


def main():

    output_path = './out_20um.TXT'
    output_file = open(output_path, "wt")
    sleep_time = 1000
    jump_speed = 3000
    burst_time = 10

    pitch_um = 20
    line_number = 4


    output_file.write('rtListOpen(1);\n')
    output_file.write(f'rtSetJumpSpeed({jump_speed});\n')
    output_file.write('rtSetLaser(0);\n')

    pitch = pitch_um / 1000
    x = 0
    y = 0


    for i in range(line_number):
        x = 0

        for j in range(int(1/pitch)):
            jump_line = f'rtJumpTo({x},{y});\n'
            output_file.write(jump_line)

            output_file.write(f'rtBurst({burst_time});\n')
            output_file.write('rtSetLaser(1);\n')
            output_file.write('rtSetLaser(0);\n')

            x += pitch
            x = round(x, 4)

        y += 40 / 1000

    output_file.write('rtJumpTo(0,0);\n')
    output_file.write('rtListClose();\n')
    output_file.close()






if __name__ == '__main__':

    main()
