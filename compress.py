import subprocess

def compress_file(input_file, output_file, crf, codec, preset):

    command = [

        'ffmpeg',

        '-i', input_file,

        '-c:v', codec,

        '-crf', str(crf),

        '-preset', preset,

        '-c:a', 'copy',

        output_file

    ]

    try:

        subprocess.run(command, check=True)

        return True

    except subprocess.CalledProcessError:

        return False

