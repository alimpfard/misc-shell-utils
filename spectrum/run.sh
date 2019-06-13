if [[ ! -e .execd ]]; then
    sudo modprobe snd_aloop
    DEFAULT_OUTPUT=$(pacmd list-sinks | grep -A1 "* index" | grep -oP "<\K[^ >]+")
    pactl load-module module-combine-sink \
        sink_name=record-n-play slaves=$DEFAULT_OUTPUT,alsa_output.platform-snd_aloop.0.analog-stereo \
        sink_properties=device.description="Record-and-play"
    touch .execd
fi

python clean.py | citron -e "File special: 'stdin', generateLines fmap: {:x Shell open: '~/spark' mode: 'w', write: x, close. ^''.}" | citron -e "File special: 'stdin', generateLines fmap: {:x Pen clear write: x. ^''.}"
