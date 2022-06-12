


def main():

    jump_speed = 10
    burst_time = 1000
    # sleep_time = 1000

    x_pitch_um = 50
    y_pitch_um = 50

    line_number = 10


    output_path = f'./out_{x_pitch_um}um.TXT'
    output_file = open(output_path, "wt")

    output_file.write('rtListOpen(1);\n')
    output_file.write(f'rtSetJumpSpeed({jump_speed});\n')
    output_file.write('rtSetLaser(0);\n')

    pitch = x_pitch_um / 1000
    x = 0
    y = 0

    line_i = 0

    for i in range(line_number):
        x = 0

        for j in range(int(1/pitch)):
            jump_line = f'rtJumpTo({x},{y});\n'
            output_file.write(jump_line)
            # output_file.write(f'rtSleep')

            output_file.write(f'rtBurst({burst_time});\n')
            output_file.write('rtSetLaser(1);\n')
            output_file.write('rtSetLaser(0);\n')

            # output_file.write(f'rtSetLaser(0); {line_i}\n')

            x += pitch
            x = round(x, 4)

            line_i += 1

        y += y_pitch_um / 1000
        y = round(y, 4)

    output_file.write('rtJumpTo(0,0);\n')
    output_file.write('rtListClose();\n')
    output_file.close()






if __name__ == '__main__':

    main()
