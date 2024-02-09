import subprocess
import os


def split_audio(file_name, path_to_save):
    """split a music track into specified sub-tracks by calling ffmpeg from the shell"""

    # create a template of the ffmpeg call in advance
    cmd_string = 'ffmpeg -y -i {tr} -acodec copy -ss {st} -to {en} {nm}.wav'

    timings = [25, 20, 15, 10]  # timings to split input file with  
    start_pos = 0
    out_name_num = 11

    for t in timings:
        # create command string for a given track
        name = path_to_save + 'target' + str(out_name_num)
        command = cmd_string.format(tr=file_name, st=start_pos, en=start_pos+t, nm=name)
        start_pos += t
        out_name_num += 1

        # use subprocess to execute the command in the shell
        subprocess.call(command, shell=True)

    # delete prerecorded voice of target
    if os.path.exists("target.wav"):
        os.remove("target.wav")
    else:
        print("The file does not exist")

    return None


# split_audio('target.wav', 'raw_data_wav/')
