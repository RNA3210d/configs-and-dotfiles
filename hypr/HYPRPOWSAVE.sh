#!/usr/bin/env sh
HYPRPOWSAVE=$(hyprctl getoption animations:enabled | awk 'NR==1{print $2}')
if [ "$HYPRPOWSAVE" = 1 ] ; then
    hyprctl --batch "\
        keyword animations:enabled 0;\
        keyword decoration:shadow:enabled 0;\
        keyword decoration:blur:enabled 0;\
        keyword general:gaps_in 0;\
        keyword general:gaps_out 0;\
        keyword general:border_size 1;\
        keyword monitor eDP-1, 1920x1080@60, 0x0, 1.2;\
        keyword decoration:rounding 0"
    exit
fi
hyprctl reload
